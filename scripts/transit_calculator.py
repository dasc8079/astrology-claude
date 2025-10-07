#!/usr/bin/env python3
"""
Transit Calculator
Unified transit report data generator combining all timing techniques.

Calculates:
- Current timing context (profections, ZR L1, ZR L2, Firdaria, Solar Return, Progressed Moon)
- Transits by date (planetary positions and aspects to natal)
- Eclipses in date range
- Tiered importance filtering (CRITICAL, IMPORTANT, NOTABLE)
- Bonification/Maltreatment quality scoring
- Convergence detection (when multiple techniques align)

Output: JSON file with all transit report data

Usage:
    # Explicit dates
    python transit_calculator.py --profile darren --start-date 2025-01-15 --end-date 2025-07-15

    # Duration from today
    python transit_calculator.py --profile darren --duration 180

    # Duration from custom start
    python transit_calculator.py --profile darren --start-date 2025-01-15 --duration 180

    # Use profile default
    python transit_calculator.py --profile darren
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from profile_loader import load_profile, list_profiles
from profections_calculator import calculate_profection_with_natal
from zodiacal_releasing import calculate_zr_from_lot, find_current_period
from firdaria_calculator import calculate_major_periods, calculate_sub_periods, find_active_periods
from solar_returns import calculate_solar_return_chart, find_sr_to_natal_aspects
from secondary_progressions import calculate_progressed_positions, find_progressed_aspects_to_natal
from transits import calculate_transiting_positions, find_transit_aspects_to_natal

# Default orbs by planet speed
DEFAULT_ORBS = {
    'Moon': 1.0,          # Fast mover, tight orb
    'Sun': 1.5,           # Medium speed
    'Mercury': 1.5,       # Medium speed
    'Venus': 1.5,         # Medium speed
    'Mars': 1.5,          # Medium speed
    'Jupiter': 2.0,       # Slow mover, wider orb
    'Saturn': 2.0,        # Slow mover, wider orb
    'Uranus': 2.0,        # Very slow
    'Neptune': 2.0,       # Very slow
    'Pluto': 2.0,         # Very slow
}


def parse_date_range(
    args: argparse.Namespace,
    profile_settings: Dict[str, Any]
) -> Tuple[str, str]:
    """
    Parse date range from command line arguments or profile defaults.

    Priority:
    1. Explicit start + end dates
    2. Start date + duration
    3. Duration from today
    4. Profile default duration

    Returns:
        Tuple of (start_date_str, end_date_str) in YYYY-MM-DD format
    """
    if args.start_date and args.end_date:
        # Explicit dates - highest priority
        return (args.start_date, args.end_date)

    if args.start_date and args.duration:
        # Start date + duration
        start = datetime.strptime(args.start_date, '%Y-%m-%d')
        end = start + timedelta(days=args.duration)
        return (args.start_date, end.strftime('%Y-%m-%d'))

    if args.duration:
        # Duration from today
        start = datetime.today()
        end = start + timedelta(days=args.duration)
        return (start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))

    # Fall back to profile default
    duration = int(profile_settings.get('transit_default_duration', 180))
    start = datetime.today()
    end = start + timedelta(days=duration)
    return (start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))


def get_orb_for_transit(
    transiting_planet: str,
    profile_settings: Dict[str, Any]
) -> float:
    """
    Get appropriate orb for transiting planet.

    Uses profile settings if available, otherwise defaults.
    """
    if transiting_planet == 'Moon':
        return float(profile_settings.get('transit_moon_orb', DEFAULT_ORBS['Moon']))
    elif transiting_planet in ['Saturn', 'Jupiter']:
        return float(profile_settings.get('transit_outer_planet_orb', DEFAULT_ORBS[transiting_planet]))
    else:
        return float(profile_settings.get('transit_default_orb', DEFAULT_ORBS.get(transiting_planet, 2.0)))


def calculate_transit_quality_score(
    transiting_planet: str,
    natal_planet: Dict[str, Any],
    aspect_type: str,
    natal_chart: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Calculate basic quality score for a transit (-10 to +10).

    Factors:
    1. Planet nature (benefic/malefic of sect) [+3/-3]
    2. Natal planet dignity [+2/0/-2]
    3. Aspect type (trine/sextile vs square/opposition) [+2/0/-2]

    Returns:
        {
            'score': int,  # -10 to +10
            'quality': str,  # 'benefic', 'malefic', or 'neutral'
            'factors': {...}  # Breakdown of scoring factors
        }
    """
    score = 0
    factors = {}

    # Get chart sect
    sect = natal_chart.get('sect', 'day')

    # 1. Sect benefic/malefic (+3/-3)
    benefics = ['Venus', 'Jupiter']
    malefics = ['Mars', 'Saturn']

    if sect == 'day':
        benefic_of_sect = 'Jupiter'
        malefic_of_sect = 'Saturn'
    else:  # night chart
        benefic_of_sect = 'Venus'
        malefic_of_sect = 'Mars'

    if transiting_planet == benefic_of_sect:
        score += 3
        factors['sect_nature'] = 'benefic of sect'
    elif transiting_planet == malefic_of_sect:
        score -= 3
        factors['sect_nature'] = 'malefic of sect'
    elif transiting_planet in benefics:
        score += 2
        factors['sect_nature'] = 'benefic (not of sect)'
    elif transiting_planet in malefics:
        score -= 2
        factors['sect_nature'] = 'malefic (not of sect)'
    else:
        factors['sect_nature'] = 'neutral (luminary or Mercury)'

    # 2. Natal planet dignity (+2/0/-2)
    natal_dignities = natal_planet.get('dignities', {}).get('essential', {})

    if natal_dignities.get('domicile') or natal_dignities.get('exaltation'):
        score += 2
        factors['natal_dignity'] = 'domicile or exaltation'
    elif natal_dignities.get('detriment') or natal_dignities.get('fall'):
        score -= 2
        factors['natal_dignity'] = 'detriment or fall'
    else:
        factors['natal_dignity'] = 'neutral'

    # 3. Aspect type (+2/0/-2)
    if aspect_type in ['trine', 'sextile']:
        score += 2
        factors['aspect_type'] = f'{aspect_type} (harmonious)'
    elif aspect_type in ['square', 'opposition']:
        score -= 2
        factors['aspect_type'] = f'{aspect_type} (challenging)'
    elif aspect_type == 'conjunction':
        factors['aspect_type'] = 'conjunction (depends on planet nature)'
    else:
        factors['aspect_type'] = aspect_type

    # Determine overall quality
    if score > 0:
        quality = 'benefic'
    elif score < 0:
        quality = 'malefic'
    else:
        quality = 'neutral'

    return {
        'score': score,
        'quality': quality,
        'factors': factors
    }


def tier_transit(
    transit: Dict[str, Any],
    timing_context: Dict[str, Any],
    natal_chart: Dict[str, Any]
) -> str:
    """
    Assign importance tier to transit aspect.

    CRITICAL tier:
    - Transits to Lord of Year (profection)
    - Transits to natal Ascendant ruler
    - Transits to sect light (Sun day chart, Moon night chart)
    - Exact transits (orb < 1°) to angular house rulers (1, 4, 7, 10)

    IMPORTANT tier:
    - Transits to planets in profected house
    - Transits to ZR L1 lord
    - Transits to Firdaria major period lord
    - Transits with orb < 2° to any natal planet

    NOTABLE tier:
    - Transits with orb 2-3° to natal planets
    - Other transits

    Returns:
        'critical', 'important', or 'notable'
    """
    natal_planet_name = transit.get('natal_planet')
    orb = transit.get('orb', 5.0)

    # Get timing lords
    lord_of_year = timing_context.get('profection', {}).get('lord_of_year')
    ascendant_ruler = natal_chart.get('chart_ruler')
    sect = natal_chart.get('sect', 'day')
    sect_light = 'Sun' if sect == 'day' else 'Moon'

    # ZR and Firdaria lords
    zr_fortune_lord = timing_context.get('zr_fortune_l1', {}).get('ruler')
    zr_spirit_lord = timing_context.get('zr_spirit_l1', {}).get('ruler')
    firdaria_major_lord = timing_context.get('firdaria', {}).get('major_period_lord')

    # Angular house rulers (houses 1, 4, 7, 10)
    # For now, simplified - just check if planet rules angular houses

    # CRITICAL tier
    if natal_planet_name == lord_of_year:
        return 'critical'
    if natal_planet_name == ascendant_ruler:
        return 'critical'
    if natal_planet_name == sect_light:
        return 'critical'
    if orb < 1.0:  # Exact transit
        return 'critical'

    # IMPORTANT tier
    if natal_planet_name in [zr_fortune_lord, zr_spirit_lord, firdaria_major_lord]:
        return 'important'
    if orb < 2.0:
        return 'important'

    # NOTABLE tier (everything else)
    return 'notable'


def calculate_transit_report_data(
    profile_name: str,
    start_date: str,
    end_date: str,
    orb: Optional[float] = None,
    include_modern: bool = True
) -> Dict[str, Any]:
    """
    Calculate comprehensive transit report data.

    Args:
        profile_name: Profile identifier
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        orb: Custom orb override (optional)
        include_modern: Include Uranus, Neptune, Pluto

    Returns:
        Complete transit report data structure
    """
    # Load profile
    profile = load_profile(profile_name)
    if not profile:
        raise ValueError(f"Profile '{profile_name}' not found")

    # Get birth data
    birth_data = profile.get_birth_data()
    if not birth_data:
        raise ValueError(f"Profile '{profile_name}' missing birth data")

    # Get chart framework
    framework = profile.get_chart_framework()
    if not framework:
        raise ValueError(f"Profile '{profile_name}' missing chart framework")

    # Get profile settings (from framework metadata if available)
    settings = framework.get('metadata', {}).get('settings', {})

    # Calculate date range info
    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    days = (end_dt - start_dt).days

    # Get birth date for age calculation
    birth_date_str = birth_data.get('date')
    if not birth_date_str:
        raise ValueError(f"Profile '{profile_name}' missing birth date")

    birth_dt = datetime.strptime(birth_date_str, '%Y-%m-%d')
    current_age = int((start_dt - birth_dt).days / 365.25)

    # Get natal chart data
    natal_planets = profile.get_planets()
    natal_chart = {
        'sect': framework.get('sect', 'day'),
        'chart_ruler': framework.get('chart_ruler'),
        'planets': natal_planets
    }

    # Calculate current timing context (stays constant for this date range)
    print(f"Calculating timing context for age {current_age}...")

    # Profections
    profection = calculate_profection_with_natal(
        profile_name=profile_name,
        age=current_age
    )

    # ZR Fortune L1 and L2
    try:
        zr_fortune_data = calculate_zr_from_lot(profile_name, 'fortune', max_age=current_age + 20)
        zr_fortune_l1_periods = zr_fortune_data.get('l1_periods', [])
        zr_fortune_l2_periods = zr_fortune_data.get('l2_periods', [])

        # Find current L1 period
        current_zr_fortune_l1 = find_current_period(zr_fortune_l1_periods, current_age)
        if current_zr_fortune_l1:
            zr_fortune_l1 = {
                'period_sign': current_zr_fortune_l1['sign'],
                'ruler': current_zr_fortune_l1['ruler'],
                'start_age': current_zr_fortune_l1['start_age'],
                'end_age': current_zr_fortune_l1['end_age'],
                'duration': current_zr_fortune_l1['duration']
            }
        else:
            zr_fortune_l1 = None

        # Find current L2 period
        current_zr_fortune_l2 = find_current_period(zr_fortune_l2_periods, current_age)
        if current_zr_fortune_l2:
            zr_fortune_l2 = {
                'period_sign': current_zr_fortune_l2['sign'],
                'ruler': current_zr_fortune_l2['ruler'],
                'start_age': current_zr_fortune_l2['start_age'],
                'end_age': current_zr_fortune_l2['end_age'],
                'duration': current_zr_fortune_l2['duration'],
                'is_peak': current_zr_fortune_l2.get('is_peak', False)
            }
        else:
            zr_fortune_l2 = None
    except Exception as e:
        print(f"Warning: Could not calculate ZR Fortune: {e}")
        zr_fortune_l1 = None
        zr_fortune_l2 = None

    # ZR Spirit L1 and L2
    try:
        zr_spirit_data = calculate_zr_from_lot(profile_name, 'spirit', max_age=current_age + 20)
        zr_spirit_l1_periods = zr_spirit_data.get('l1_periods', [])
        zr_spirit_l2_periods = zr_spirit_data.get('l2_periods', [])

        # Find current L1 period
        current_zr_spirit_l1 = find_current_period(zr_spirit_l1_periods, current_age)
        if current_zr_spirit_l1:
            zr_spirit_l1 = {
                'period_sign': current_zr_spirit_l1['sign'],
                'ruler': current_zr_spirit_l1['ruler'],
                'start_age': current_zr_spirit_l1['start_age'],
                'end_age': current_zr_spirit_l1['end_age'],
                'duration': current_zr_spirit_l1['duration']
            }
        else:
            zr_spirit_l1 = None

        # Find current L2 period
        current_zr_spirit_l2 = find_current_period(zr_spirit_l2_periods, current_age)
        if current_zr_spirit_l2:
            zr_spirit_l2 = {
                'period_sign': current_zr_spirit_l2['sign'],
                'ruler': current_zr_spirit_l2['ruler'],
                'start_age': current_zr_spirit_l2['start_age'],
                'end_age': current_zr_spirit_l2['end_age'],
                'duration': current_zr_spirit_l2['duration'],
                'is_peak': current_zr_spirit_l2.get('is_peak', False)
            }
        else:
            zr_spirit_l2 = None
    except Exception as e:
        print(f"Warning: Could not calculate ZR Spirit: {e}")
        zr_spirit_l1 = None
        zr_spirit_l2 = None

    # Firdaria
    try:
        firdaria_data = find_active_periods(current_age, natal_chart['sect'])
        firdaria = {
            'major_period_lord': firdaria_data.get('major_period', {}).get('lord'),
            'major_start_age': firdaria_data.get('major_period', {}).get('start_age'),
            'major_end_age': firdaria_data.get('major_period', {}).get('end_age'),
            'sub_period_lord': firdaria_data.get('sub_period', {}).get('lord'),
            'sub_start_age': firdaria_data.get('sub_period', {}).get('start_age'),
            'sub_end_age': firdaria_data.get('sub_period', {}).get('end_age')
        }
    except Exception as e:
        print(f"Warning: Could not calculate Firdaria: {e}")
        firdaria = None

    # Solar Return - TODO: Fix SwissEph file issue
    # Skipping for now - not critical for MVP
    solar_return = None
    print("Solar Return calculation skipped (TODO: fix SwissEph file path)")

    # Progressed Moon - TODO: Fix type error in calculate_progressed_positions
    # Skipping for now - not critical for MVP
    progressed_moon = None
    print("Progressed Moon calculation skipped (TODO: fix date handling)")

    timing_context = {
        'profection': profection,
        'zr_fortune_l1': zr_fortune_l1,
        'zr_fortune_l2': zr_fortune_l2,
        'zr_spirit_l1': zr_spirit_l1,
        'zr_spirit_l2': zr_spirit_l2,
        'firdaria': firdaria,
        'solar_return': solar_return,
        'progressed_moon': progressed_moon
    }

    # Iterate through date range calculating transits
    print(f"Calculating transits from {start_date} to {end_date} ({days} days)...")

    all_transits = []

    # For MVP, calculate transits weekly (not daily) to keep data manageable
    current_date = start_dt
    week_count = 0
    while current_date <= end_dt:
        date_str = current_date.strftime('%Y-%m-%d')
        week_count += 1

        # Calculate transiting positions for this date
        try:
            transiting_data = calculate_transiting_positions(date_str, include_modern=include_modern)

            # Get default orb (use settings or default to 2.0)
            default_orb = orb if orb else float(settings.get('transit_default_orb', 2.0))

            # Find aspects between transiting and natal planets
            aspect_list = find_transit_aspects_to_natal(
                transits=transiting_data,
                profile_name=profile_name,
                orb=default_orb
            )

            # Process each aspect found
            for asp in aspect_list:
                trans_name = asp['transiting_planet']
                natal_name = asp['natal_planet']

                # Find the transiting planet data
                trans_planet = next(
                    (p for p in transiting_data['planets'] if p['name'] == trans_name),
                    None
                )

                # Find the natal planet data
                natal_planet = next(
                    (p for p in natal_chart['planets'] if p['name'] == natal_name),
                    None
                )

                if trans_planet and natal_planet:
                    # Build aspect data
                    aspect = {
                        'date': date_str,
                        'transiting_planet': trans_name,
                        'transiting_sign': trans_planet['sign'],
                        'transiting_degree': trans_planet['degree'],
                        'natal_planet': natal_name,
                        'natal_sign': natal_planet['sign'],
                        'natal_degree': natal_planet['degree'],
                        'aspect_type': asp['aspect_type'],
                        'orb': asp['orb'],
                        'exact': asp.get('exact', False),
                        'applying': asp.get('applying', False),
                        'quality_score': calculate_transit_quality_score(
                            trans_name,
                            natal_planet,
                            asp['aspect_type'],
                            natal_chart
                        )
                    }

                    # Assign tier
                    aspect['tier'] = tier_transit(aspect, timing_context, natal_chart)

                    all_transits.append(aspect)

        except Exception as e:
            print(f"Warning: Could not calculate transits for {date_str}: {e}")

        # Advance by 7 days (weekly snapshots)
        current_date += timedelta(days=7)

    print(f"Calculated {week_count} weeks of transits")

    # Separate by tier
    transits_by_tier = {
        'critical': [t for t in all_transits if t['tier'] == 'critical'],
        'important': [t for t in all_transits if t['tier'] == 'important'],
        'notable': [t for t in all_transits if t['tier'] == 'notable']
    }

    # Eclipse detection
    # TODO: Implement eclipse detection using Swiss Ephemeris
    # For now, placeholder - would use swe.sol_eclipse_when() and swe.lun_eclipse_when()
    eclipses = []
    print("Eclipse detection not yet implemented (TODO)")

    # Convergence detection
    # TODO: Implement convergence detection similar to life arc system
    # Flag when multiple techniques align (e.g., Lord of Year transit + Firdaria lord + ZR lord)
    convergences = []
    print("Convergence detection not yet implemented (TODO)")

    # Build final data structure
    report_data = {
        'profile': profile_name,
        'date_range': {
            'start': start_date,
            'end': end_date,
            'days': days
        },
        'current_age': current_age,
        'natal_chart': natal_chart,
        'current_timing': timing_context,
        'transits_by_tier': transits_by_tier,
        'all_transits': all_transits,
        'eclipses': eclipses,
        'convergences': convergences,
        'metadata': {
            'generated': datetime.now().isoformat(),
            'orb_defaults': DEFAULT_ORBS,
            'include_modern': include_modern
        }
    }

    return report_data


def get_unique_filename(base_path: Path) -> Path:
    """
    Get unique filename by appending _2, _3, etc. if file exists.
    """
    if not base_path.exists():
        return base_path

    counter = 2
    while True:
        new_path = base_path.parent / f"{base_path.stem}_{counter}{base_path.suffix}"
        if not new_path.exists():
            return new_path
        counter += 1


def save_transit_data(
    report_data: Dict[str, Any],
    profile_name: str,
    start_date: str,
    end_date: str
) -> Path:
    """
    Save transit report data to JSON file with auto-numbering.
    """
    # Create output directory
    output_dir = Path(__file__).parent.parent / 'profiles' / profile_name / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename
    filename = f"transit_data_{profile_name}_{start_date}_to_{end_date}.json"
    base_path = output_dir / filename

    # Get unique filename (auto-number if exists)
    output_path = get_unique_filename(base_path)

    # Save JSON
    with open(output_path, 'w') as f:
        json.dump(report_data, f, indent=2)

    print(f"\n✅ Transit data saved: {output_path}")
    print(f"   {len(report_data['all_transits'])} total transits")
    print(f"   {len(report_data['transits_by_tier']['critical'])} CRITICAL")
    print(f"   {len(report_data['transits_by_tier']['important'])} IMPORTANT")
    print(f"   {len(report_data['transits_by_tier']['notable'])} NOTABLE")

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Calculate transit report data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--start-date', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='End date (YYYY-MM-DD)')
    parser.add_argument('--duration', type=int, help='Duration in days from start (or today if no start)')
    parser.add_argument('--orb', type=float, help='Custom orb override')
    parser.add_argument('--include-modern', type=bool, default=True, help='Include modern planets')
    parser.add_argument('--list-profiles', action='store_true', help='List available profiles')

    args = parser.parse_args()

    if args.list_profiles:
        profiles = list_profiles()
        print("\nAvailable profiles:")
        for p in profiles:
            print(f"  - {p}")
        return

    # Load profile to get settings
    profile = load_profile(args.profile)
    if not profile:
        print(f"❌ Profile '{args.profile}' not found")
        return 1

    # Get settings from framework
    framework = profile.get_chart_framework()
    settings = framework.get('metadata', {}).get('settings', {}) if framework else {}

    # Parse date range
    start_date, end_date = parse_date_range(args, settings)

    print(f"\n📊 Transit Calculator")
    print(f"Profile: {args.profile}")
    print(f"Date Range: {start_date} to {end_date}")
    print(f"Duration: {(datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days} days\n")

    # Calculate transit report data
    report_data = calculate_transit_report_data(
        profile_name=args.profile,
        start_date=start_date,
        end_date=end_date,
        orb=args.orb,
        include_modern=args.include_modern
    )

    # Save to file
    output_path = save_transit_data(report_data, args.profile, start_date, end_date)

    return 0


if __name__ == '__main__':
    sys.exit(main())
