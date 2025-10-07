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
    profection_data = timing_context.get('profection', {}).get('profection', {})
    lord_of_year = profection_data.get('lord_of_year')
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


def calculate_transit_duration(
    transiting_planet: str,
    natal_longitude: float,
    aspect_type: str,
    snapshot_date: str,
    orb: float,
    include_modern: bool = True,
    max_scan_days: int = 180
) -> Dict[str, Any]:
    """
    Calculate full duration arc of a transit (applying → exact → separating).

    Scans day-by-day around snapshot date to find:
    - When transit first enters orb (applying_date)
    - When transit becomes exact (exact_dates - list, may be multiple if retrograde)
    - When transit leaves orb (separating_date)
    - Total duration in days
    - Whether transit involves retrograde loop

    Args:
        transiting_planet: Name of transiting planet
        natal_longitude: Longitude of natal planet
        aspect_type: Type of aspect (conjunction, sextile, square, trine, opposition)
        snapshot_date: Date when transit was detected
        orb: Orb in degrees
        include_modern: Include modern planets
        max_scan_days: Maximum days to scan forward/backward

    Returns:
        {
            'applying_date': str,
            'exact_dates': [str, ...],
            'separating_date': str,
            'duration_days': int,
            'has_retrograde_loop': bool,
            'stations': [{'date': str, 'motion': 'retrograde'/'direct'}, ...]
        }
    """
    from transits import calculate_transiting_positions, find_transit_aspects_to_natal
    from datetime import datetime, timedelta

    # Calculate target aspect longitude
    aspect_degrees = {
        'conjunction': 0,
        'sextile': 60,
        'square': 90,
        'trine': 120,
        'opposition': 180
    }
    aspect_deg = aspect_degrees.get(aspect_type, 0)
    target_longitude = (natal_longitude + aspect_deg) % 360

    snapshot_dt = datetime.strptime(snapshot_date, '%Y-%m-%d')

    # Helper function to calculate orb for a given date
    def get_orb_for_date(date_dt):
        try:
            trans_data = calculate_transiting_positions(
                date_dt.strftime('%Y-%m-%d'),
                include_modern=include_modern
            )
            trans_planet = next(
                (p for p in trans_data['planets'] if p['name'] == transiting_planet),
                None
            )
            if not trans_planet:
                return None

            # Calculate orb to target aspect longitude
            trans_long = trans_planet['longitude']
            orb_calc = abs(trans_long - target_longitude)
            if orb_calc > 180:
                orb_calc = 360 - orb_calc

            speed = trans_planet['speed']
            return {'orb': orb_calc, 'speed': speed, 'longitude': trans_long}
        except:
            return None

    # Scan backward to find applying date (when first enters orb)
    applying_date = None
    current_dt = snapshot_dt
    for i in range(max_scan_days):
        current_dt = snapshot_dt - timedelta(days=i)
        result = get_orb_for_date(current_dt)
        if result is None:
            break
        if result['orb'] > orb:
            # Just exited orb going backward, so previous day was applying date
            applying_date = (current_dt + timedelta(days=1)).strftime('%Y-%m-%d')
            break

    if not applying_date:
        # Didn't find entry - transit may have started before scan window
        applying_date = (snapshot_dt - timedelta(days=max_scan_days)).strftime('%Y-%m-%d')

    # Scan forward to find exact dates and separating date
    exact_dates = []
    separating_date = None
    stations = []
    has_retrograde_loop = False

    current_dt = snapshot_dt
    prev_orb = None
    prev_speed = None

    for i in range(max_scan_days):
        current_dt = snapshot_dt + timedelta(days=i)
        result = get_orb_for_date(current_dt)
        if result is None:
            break

        current_orb = result['orb']
        current_speed = result['speed']

        # Detect stations (retrograde/direct changes)
        if prev_speed is not None:
            if prev_speed > 0 and current_speed < 0:
                stations.append({'date': current_dt.strftime('%Y-%m-%d'), 'motion': 'retrograde'})
                has_retrograde_loop = True
            elif prev_speed < 0 and current_speed > 0:
                stations.append({'date': current_dt.strftime('%Y-%m-%d'), 'motion': 'direct'})
                has_retrograde_loop = True

        # Detect exact dates (orb crosses through minimum, allowing 0.3° threshold)
        if prev_orb is not None:
            if current_orb < 0.3 and current_orb <= prev_orb:
                # Approaching exact
                if current_dt.strftime('%Y-%m-%d') not in exact_dates:
                    exact_dates.append(current_dt.strftime('%Y-%m-%d'))
            elif prev_orb < 0.3 and current_orb > prev_orb:
                # Just passed exact
                if (current_dt - timedelta(days=1)).strftime('%Y-%m-%d') not in exact_dates:
                    exact_dates.append((current_dt - timedelta(days=1)).strftime('%Y-%m-%d'))

        # Detect separating date (when exits orb)
        if current_orb > orb:
            separating_date = current_dt.strftime('%Y-%m-%d')
            break

        prev_orb = current_orb
        prev_speed = current_speed

    if not separating_date:
        # Transit still in orb at end of scan window
        separating_date = (snapshot_dt + timedelta(days=max_scan_days)).strftime('%Y-%m-%d')

    # Calculate total duration
    apply_dt = datetime.strptime(applying_date, '%Y-%m-%d')
    separate_dt = datetime.strptime(separating_date, '%Y-%m-%d')
    duration_days = (separate_dt - apply_dt).days

    return {
        'applying_date': applying_date,
        'exact_dates': exact_dates if exact_dates else [snapshot_date],  # Default to snapshot if no exact found
        'separating_date': separating_date,
        'duration_days': duration_days,
        'has_retrograde_loop': has_retrograde_loop,
        'stations': stations
    }


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

                    # Calculate duration for CRITICAL and IMPORTANT transits only (optimization)
                    if aspect['tier'] in ['critical', 'important']:
                        try:
                            duration_data = calculate_transit_duration(
                                transiting_planet=trans_name,
                                natal_longitude=natal_planet['longitude'],
                                aspect_type=asp['aspect_type'],
                                snapshot_date=date_str,
                                orb=asp['orb'],
                                include_modern=include_modern,
                                max_scan_days=180
                            )
                            aspect['duration'] = duration_data
                        except Exception as e:
                            print(f"Warning: Could not calculate duration for {trans_name} {asp['aspect_type']} {natal_name}: {e}")
                            aspect['duration'] = None
                    else:
                        aspect['duration'] = None

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

    # Peak/Low Period Detection and Auspicious/Challenging Day Analysis
    print("Analyzing daily quality scores for peak/low periods...")

    # Calculate daily quality scores by summing all active transits for each day
    daily_scores = {}
    current_scan_dt = start_dt
    while current_scan_dt <= end_dt:
        date_key = current_scan_dt.strftime('%Y-%m-%d')
        day_score = 0
        day_transits = []

        # Find all transits active on this day
        for transit in all_transits:
            if transit.get('duration'):
                applying = transit['duration']['applying_date']
                separating = transit['duration']['separating_date']

                # Check if this day is within the transit's duration
                try:
                    apply_dt = datetime.strptime(applying, '%Y-%m-%d')
                    separate_dt = datetime.strptime(separating, '%Y-%m-%d')

                    if apply_dt <= current_scan_dt <= separate_dt:
                        transit_score = transit['quality_score']['score']
                        day_score += transit_score
                        day_transits.append({
                            'transiting': transit['transiting_planet'],
                            'natal': transit['natal_planet'],
                            'aspect': transit['aspect_type'],
                            'score': transit_score
                        })
                except:
                    pass

        daily_scores[date_key] = {
            'score': day_score,
            'transits': day_transits
        }

        current_scan_dt += timedelta(days=1)

    # Sort days by score to find most auspicious/challenging
    sorted_days = sorted(daily_scores.items(), key=lambda x: x[1]['score'], reverse=True)

    # THE most auspicious day (single highest score)
    most_auspicious_day = None
    if sorted_days and sorted_days[0][1]['score'] > 0:
        most_auspicious_day = {
            'date': sorted_days[0][0],
            'score': sorted_days[0][1]['score'],
            'transits': sorted_days[0][1]['transits']
        }

    # Top 10-20 auspicious days (threshold > +10 or top 20, whichever is fewer)
    auspicious_days = []
    for date, data in sorted_days:
        if data['score'] > 10 or (len(auspicious_days) < 20 and data['score'] > 5):
            auspicious_days.append({
                'date': date,
                'score': data['score'],
                'transits': data['transits']
            })
        if len(auspicious_days) >= 20:
            break

    # THE most challenging day (single lowest score)
    most_challenging_day = None
    if sorted_days and sorted_days[-1][1]['score'] < 0:
        most_challenging_day = {
            'date': sorted_days[-1][0],
            'score': sorted_days[-1][1]['score'],
            'transits': sorted_days[-1][1]['transits']
        }

    # Top 10-20 challenging days (threshold < -10 or bottom 20, whichever is fewer)
    challenging_days = []
    for date, data in reversed(sorted_days):
        if data['score'] < -10 or (len(challenging_days) < 20 and data['score'] < -5):
            challenging_days.append({
                'date': date,
                'score': data['score'],
                'transits': data['transits']
            })
        if len(challenging_days) >= 20:
            break

    # Detect peak periods (consecutive days with total score > +12)
    peak_periods = []
    current_peak = None
    for date_key in sorted(daily_scores.keys()):
        score = daily_scores[date_key]['score']

        if score > 12:
            if current_peak is None:
                current_peak = {
                    'start_date': date_key,
                    'end_date': date_key,
                    'total_score': score,
                    'peak_score': score,
                    'days': [date_key]
                }
            else:
                current_peak['end_date'] = date_key
                current_peak['total_score'] += score
                current_peak['peak_score'] = max(current_peak['peak_score'], score)
                current_peak['days'].append(date_key)
        else:
            if current_peak is not None:
                peak_periods.append(current_peak)
                current_peak = None

    # Add final peak if exists
    if current_peak is not None:
        peak_periods.append(current_peak)

    # Detect low periods (consecutive days with total score < -12)
    low_periods = []
    current_low = None
    for date_key in sorted(daily_scores.keys()):
        score = daily_scores[date_key]['score']

        if score < -12:
            if current_low is None:
                current_low = {
                    'start_date': date_key,
                    'end_date': date_key,
                    'total_score': score,
                    'low_score': score,
                    'days': [date_key]
                }
            else:
                current_low['end_date'] = date_key
                current_low['total_score'] += score
                current_low['low_score'] = min(current_low['low_score'], score)
                current_low['days'].append(date_key)
        else:
            if current_low is not None:
                low_periods.append(current_low)
                current_low = None

    # Add final low if exists
    if current_low is not None:
        low_periods.append(current_low)

    print(f"Found {len(peak_periods)} peak periods and {len(low_periods)} low periods")
    if most_auspicious_day:
        print(f"Most auspicious day: {most_auspicious_day['date']} (score: {most_auspicious_day['score']:+d})")
    if most_challenging_day:
        print(f"Most challenging day: {most_challenging_day['date']} (score: {most_challenging_day['score']:+d})")

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
        'peak_periods': peak_periods,
        'low_periods': low_periods,
        'most_auspicious_day': most_auspicious_day,
        'auspicious_days': auspicious_days,
        'most_challenging_day': most_challenging_day,
        'challenging_days': challenging_days,
        'daily_scores': daily_scores,
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
