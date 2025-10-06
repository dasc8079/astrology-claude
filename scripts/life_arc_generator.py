#!/usr/bin/env python3
"""
Life Arc Generator
Unified timeline combining all timing techniques.

Creates comprehensive life arc report showing:
- Annual profections (yearly house activation)
- Zodiacal releasing from Fortune (body/livelihood)
- Zodiacal releasing from Spirit (mind/career)
- Secondary progressions (inner development)
- Solar returns (annual forecast)
- Current transits (real-time triggers)
- Major transitions and peak periods
- Integrated narrative view

Usage:
    python life_arc_generator.py --profile darren --start-age 0 --end-age 40
    python life_arc_generator.py --profile darren --current-age 35
    python life_arc_generator.py --profile darren --age-range 30-50 --format summary
    python life_arc_generator.py --profile darren --current-age 36 --include-progressions --include-sr
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from profile_loader import load_profile, list_profiles
from profections_calculator import calculate_profection_with_natal
from zodiacal_releasing import calculate_zr_from_lot, find_current_period
from secondary_progressions import calculate_progressed_positions, find_progressed_aspects_to_natal
from solar_returns import calculate_solar_return_chart, find_sr_to_natal_aspects
from transits import calculate_transiting_positions, find_transit_aspects_to_natal, find_transits_in_natal_houses


def generate_life_arc_timeline(
    profile_name: str,
    start_age: int = 0,
    end_age: int = 100,
    include_fortune: bool = True,
    include_spirit: bool = True,
    include_progressions: bool = False,
    include_solar_returns: bool = False,
    current_date: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate complete life arc timeline combining all techniques.

    Args:
        profile_name: Profile to analyze
        start_age: Starting age
        end_age: Ending age
        include_fortune: Include ZR from Fortune
        include_spirit: Include ZR from Spirit
        include_progressions: Include secondary progressions
        include_solar_returns: Include solar return charts
        current_date: Date for current transits (YYYY-MM-DD or None)

    Returns:
        Dictionary with unified timeline data
    """
    # Load profile
    profile = load_profile(profile_name)
    birth_data = profile.get_birth_data()

    # Calculate profections for entire range
    profections = []
    for age in range(start_age, end_age + 1):
        prof = calculate_profection_with_natal(profile_name, age)
        profections.append(prof)

    # Calculate ZR from Fortune and Spirit
    zr_fortune = None
    zr_spirit = None

    if include_fortune:
        zr_fortune = calculate_zr_from_lot(profile_name, 'fortune', max_age=end_age + 10)

    if include_spirit:
        zr_spirit = calculate_zr_from_lot(profile_name, 'spirit', max_age=end_age + 10)

    # Calculate progressions (if requested)
    progressions = None
    if include_progressions:
        progressions = {}
        for age in range(start_age, end_age + 1):
            prog = calculate_progressed_positions(profile_name, float(age))
            prog_aspects = find_progressed_aspects_to_natal(profile_name, float(age), orb=3.0)
            progressions[age] = {
                'positions': prog,
                'aspects': prog_aspects
            }

    # Calculate solar returns (if requested)
    solar_returns = None
    if include_solar_returns:
        solar_returns = {}
        for age in range(start_age, end_age + 1):
            try:
                sr = calculate_solar_return_chart(profile_name, age=age)
                sr_aspects = find_sr_to_natal_aspects(sr, profile_name, orb=3.0)
                solar_returns[age] = {
                    'chart': sr,
                    'aspects': sr_aspects
                }
            except Exception as e:
                # Skip if SR calculation fails (e.g., age beyond valid range)
                pass

    # Calculate current transits (if date provided)
    transits = None
    if current_date:
        transits_data = calculate_transiting_positions(current_date, include_modern=True)
        transits_data = find_transits_in_natal_houses(transits_data, profile_name)
        transit_aspects = find_transit_aspects_to_natal(transits_data, profile_name, orb=3.0)
        transits = {
            'positions': transits_data,
            'aspects': transit_aspects
        }

    return {
        'profile': profile_name,
        'birth_data': birth_data,
        'age_range': {'start': start_age, 'end': end_age},
        'profections': profections,
        'zr_fortune': zr_fortune,
        'zr_spirit': zr_spirit,
        'progressions': progressions,
        'solar_returns': solar_returns,
        'transits': transits,
    }


def get_year_snapshot(timeline: Dict[str, Any], age: int) -> Dict[str, Any]:
    """Get all active periods for a specific age."""
    snapshot = {
        'age': age,
        'profection': None,
        'fortune_l1': None,
        'fortune_l2': None,
        'spirit_l1': None,
        'spirit_l2': None,
        'progressions': None,
        'solar_return': None,
    }

    # Find profection
    for prof in timeline['profections']:
        if prof['profection']['age'] == age:
            snapshot['profection'] = prof
            break

    # Find Fortune periods
    if timeline['zr_fortune']:
        snapshot['fortune_l1'] = find_current_period(
            timeline['zr_fortune']['l1_periods'], float(age)
        )
        snapshot['fortune_l2'] = find_current_period(
            timeline['zr_fortune']['l2_periods'], float(age)
        )

    # Find Spirit periods
    if timeline['zr_spirit']:
        snapshot['spirit_l1'] = find_current_period(
            timeline['zr_spirit']['l1_periods'], float(age)
        )
        snapshot['spirit_l2'] = find_current_period(
            timeline['zr_spirit']['l2_periods'], float(age)
        )

    # Find progressions
    if timeline['progressions'] and age in timeline['progressions']:
        snapshot['progressions'] = timeline['progressions'][age]

    # Find solar return
    if timeline['solar_returns'] and age in timeline['solar_returns']:
        snapshot['solar_return'] = timeline['solar_returns'][age]

    return snapshot


def format_year_summary(snapshot: Dict[str, Any]) -> str:
    """Format a single year's snapshot."""
    output = []
    age = snapshot['age']

    output.append(f"\n{'='*80}")
    output.append(f"AGE {age}")
    output.append(f"{'='*80}")

    # Profection
    if snapshot['profection']:
        prof = snapshot['profection']['profection']
        lord = snapshot['profection']['lord_natal_position']
        output.append(f"\n📅 ANNUAL PROFECTION:")
        output.append(f"   House {prof['profected_house']} ({prof['profected_sign']})")
        output.append(f"   Lord of Year: {prof['lord_of_year']}")
        if lord:
            output.append(f"   Lord in: {lord['sign']} (House {lord['house']})")

    # Fortune ZR
    if snapshot['fortune_l1'] and snapshot['fortune_l2']:
        output.append(f"\n💰 FORTUNE (Body/Livelihood):")
        output.append(f"   L1: {snapshot['fortune_l1']['sign']} "
                     f"(Ages {snapshot['fortune_l1']['start_age']:.0f}-{snapshot['fortune_l1']['end_age']:.0f})")
        peak = " *** PEAK ***" if snapshot['fortune_l2'].get('is_peak') else ""
        output.append(f"   L2: {snapshot['fortune_l2']['sign']} "
                     f"(Ages {snapshot['fortune_l2']['start_age']:.1f}-{snapshot['fortune_l2']['end_age']:.1f}){peak}")

    # Spirit ZR
    if snapshot['spirit_l1'] and snapshot['spirit_l2']:
        output.append(f"\n🎯 SPIRIT (Mind/Career):")
        output.append(f"   L1: {snapshot['spirit_l1']['sign']} "
                     f"(Ages {snapshot['spirit_l1']['start_age']:.0f}-{snapshot['spirit_l1']['end_age']:.0f})")
        peak = " *** PEAK ***" if snapshot['spirit_l2'].get('is_peak') else ""
        output.append(f"   L2: {snapshot['spirit_l2']['sign']} "
                     f"(Ages {snapshot['spirit_l2']['start_age']:.1f}-{snapshot['spirit_l2']['end_age']:.1f}){peak}")

    # Secondary Progressions
    if snapshot['progressions']:
        prog = snapshot['progressions']
        output.append(f"\n🌙 SECONDARY PROGRESSIONS:")
        # Show key progressed planets (Sun and Moon)
        prog_sun = next((p for p in prog['positions']['progressed_planets'] if p['name'] == 'Sun'), None)
        prog_moon = next((p for p in prog['positions']['progressed_planets'] if p['name'] == 'Moon'), None)
        if prog_sun:
            output.append(f"   Progressed Sun: {prog_sun['sign']} {prog_sun['degree']:.1f}°")
        if prog_moon:
            output.append(f"   Progressed Moon: {prog_moon['sign']} {prog_moon['degree']:.1f}°")
        # Show major progressed aspects (tight orbs only)
        tight_aspects = [a for a in prog['aspects'] if a['orb'] < 1.0]
        if tight_aspects:
            output.append(f"   Major Aspects:")
            for asp in tight_aspects[:3]:  # Show top 3
                output.append(f"      Prog {asp['progressed_planet']} {asp['aspect_type']} Natal {asp['natal_planet']} (orb {asp['orb']:.2f}°)")

    # Solar Return
    if snapshot['solar_return']:
        sr = snapshot['solar_return']
        output.append(f"\n☀️ SOLAR RETURN:")
        output.append(f"   SR Ascendant: {sr['chart']['ascendant']['sign']} {sr['chart']['ascendant']['degree']:.1f}°")
        output.append(f"   SR MC: {sr['chart']['midheaven']['sign']} {sr['chart']['midheaven']['degree']:.1f}°")
        # Show major SR-to-natal aspects (tight orbs only)
        tight_aspects = [a for a in sr['aspects'] if a['orb'] < 1.0]
        if tight_aspects:
            output.append(f"   Major Aspects:")
            for asp in tight_aspects[:3]:  # Show top 3
                output.append(f"      SR {asp['sr_planet']} {asp['aspect_type']} Natal {asp['natal_planet']} (orb {asp['orb']:.2f}°)")

    return "\n".join(output)


def format_period_summary(timeline: Dict[str, Any]) -> str:
    """Format major period transitions within age range."""
    output = []
    start_age = timeline['age_range']['start']
    end_age = timeline['age_range']['end']

    output.append(f"\n{'='*80}")
    output.append(f"LIFE ARC SUMMARY: AGES {start_age}-{end_age}")
    output.append(f"Profile: {timeline['profile']}")
    output.append(f"{'='*80}")

    # Major ZR transitions
    if timeline['zr_fortune']:
        output.append(f"\n💰 FORTUNE PERIODS:")
        fortune_l1_periods = [p for p in timeline['zr_fortune']['l1_periods']
                             if p['start_age'] < end_age and p['end_age'] > start_age]
        for period in fortune_l1_periods:
            output.append(f"   {period['sign']}: Ages {period['start_age']:.0f}-{period['end_age']:.0f} "
                         f"({period['duration']} years, {period['ruler']} time-lord)")

    if timeline['zr_spirit']:
        output.append(f"\n🎯 SPIRIT PERIODS:")
        spirit_l1_periods = [p for p in timeline['zr_spirit']['l1_periods']
                            if p['start_age'] < end_age and p['end_age'] > start_age]
        for period in spirit_l1_periods:
            output.append(f"   {period['sign']}: Ages {period['start_age']:.0f}-{period['end_age']:.0f} "
                         f"({period['duration']} years, {period['ruler']} time-lord)")

    # Profection cycle overview
    output.append(f"\n📅 PROFECTION CYCLE:")
    output.append(f"   12-year cycles within this range:")

    cycle_starts = []
    for age in range(start_age, end_age + 1):
        if age % 12 == 0:
            cycle_starts.append(age)

    if cycle_starts:
        for cycle_age in cycle_starts:
            output.append(f"   Age {cycle_age}: New 12-year cycle begins")
    else:
        first_prof = timeline['profections'][0]['profection']
        output.append(f"   Current cycle started at age {(start_age // 12) * 12}")
        output.append(f"   Next cycle starts at age {((start_age // 12) + 1) * 12}")

    return "\n".join(output)


def format_detailed_timeline(timeline: Dict[str, Any], interval: int = 1) -> str:
    """Format detailed year-by-year timeline."""
    output = []
    output.append(format_period_summary(timeline))

    for age in range(timeline['age_range']['start'], timeline['age_range']['end'] + 1, interval):
        snapshot = get_year_snapshot(timeline, age)
        output.append(format_year_summary(snapshot))

    return "\n".join(output)


def identify_major_transitions(timeline: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Identify major life transitions in the timeline."""
    transitions = []
    start_age = timeline['age_range']['start']
    end_age = timeline['age_range']['end']

    # ZR Fortune L1 transitions
    if timeline['zr_fortune']:
        for i, period in enumerate(timeline['zr_fortune']['l1_periods'][:-1]):
            transition_age = period['end_age']
            if start_age <= transition_age <= end_age:
                next_period = timeline['zr_fortune']['l1_periods'][i + 1]
                transitions.append({
                    'age': transition_age,
                    'type': 'Fortune L1 Transition',
                    'from_sign': period['sign'],
                    'to_sign': next_period['sign'],
                    'description': f"Fortune shifts from {period['sign']} to {next_period['sign']}"
                })

    # ZR Spirit L1 transitions
    if timeline['zr_spirit']:
        for i, period in enumerate(timeline['zr_spirit']['l1_periods'][:-1]):
            transition_age = period['end_age']
            if start_age <= transition_age <= end_age:
                next_period = timeline['zr_spirit']['l1_periods'][i + 1]
                transitions.append({
                    'age': transition_age,
                    'type': 'Spirit L1 Transition',
                    'from_sign': period['sign'],
                    'to_sign': next_period['sign'],
                    'description': f"Spirit shifts from {period['sign']} to {next_period['sign']}"
                })

    # Profection cycle resets (age divisible by 12)
    for age in range(start_age, end_age + 1):
        if age % 12 == 0 and age > 0:
            transitions.append({
                'age': age,
                'type': 'Profection Cycle Reset',
                'description': f"New 12-year profection cycle begins"
            })

    # Sort by age
    transitions.sort(key=lambda x: x['age'])

    return transitions


def format_transitions(timeline: Dict[str, Any]) -> str:
    """Format major transitions list."""
    transitions = identify_major_transitions(timeline)

    output = []
    output.append(f"\n{'='*80}")
    output.append(f"MAJOR TRANSITIONS: AGES {timeline['age_range']['start']}-{timeline['age_range']['end']}")
    output.append(f"{'='*80}\n")

    if not transitions:
        output.append("No major L1 transitions in this age range.")
    else:
        for trans in transitions:
            output.append(f"Age {trans['age']:.1f}: {trans['type']}")
            output.append(f"  → {trans['description']}")
            output.append("")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description='Generate complete life arc timeline with all timing techniques')
    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--current-age', type=int, help='Show current snapshot at this age')
    parser.add_argument('--start-age', type=int, default=0, help='Start age (default 0)')
    parser.add_argument('--end-age', type=int, help='End age (default 40 or current-age+10)')
    parser.add_argument('--age-range', help='Age range (e.g., "30-50")')
    parser.add_argument('--format', choices=['detailed', 'summary', 'transitions'],
                       default='detailed', help='Output format')
    parser.add_argument('--interval', type=int, default=1,
                       help='Year interval for detailed output (default 1)')
    parser.add_argument('--no-fortune', action='store_true', help='Exclude Fortune ZR')
    parser.add_argument('--no-spirit', action='store_true', help='Exclude Spirit ZR')
    parser.add_argument('--include-progressions', action='store_true', help='Include secondary progressions')
    parser.add_argument('--include-sr', action='store_true', help='Include solar returns')
    parser.add_argument('--current-date', help='Date for current transits (YYYY-MM-DD or "today")')
    parser.add_argument('--list-profiles', action='store_true', help='List available profiles')

    args = parser.parse_args()

    if args.list_profiles:
        profiles = list_profiles()
        print(f"Available profiles: {', '.join(profiles)}")
        return

    # Parse age range if provided
    if args.age_range:
        try:
            args.start_age, args.end_age = map(int, args.age_range.split('-'))
        except ValueError:
            print(f"Error: Invalid age range format. Use 'START-END' (e.g., '30-50')", file=sys.stderr)
            sys.exit(1)

    # Set default end_age
    if args.end_age is None:
        if args.current_age is not None:
            args.end_age = args.current_age + 10
        else:
            args.end_age = 40

    # Handle "today" for current_date
    if args.current_date == 'today':
        from datetime import datetime
        args.current_date = datetime.now().strftime('%Y-%m-%d')

    try:
        # Generate timeline
        timeline = generate_life_arc_timeline(
            args.profile,
            args.start_age,
            args.end_age,
            include_fortune=not args.no_fortune,
            include_spirit=not args.no_spirit,
            include_progressions=args.include_progressions,
            include_solar_returns=args.include_sr,
            current_date=args.current_date
        )

        # Format output based on format choice
        if args.format == 'summary':
            print(format_period_summary(timeline))
        elif args.format == 'transitions':
            print(format_transitions(timeline))
        elif args.format == 'detailed':
            if args.current_age is not None:
                # Show single year snapshot
                snapshot = get_year_snapshot(timeline, args.current_age)
                print(format_year_summary(snapshot))
            else:
                # Show full timeline
                print(format_detailed_timeline(timeline, args.interval))

        # Show current transits if provided
        if timeline['transits']:
            print(f"\n{'='*80}")
            print(f"CURRENT TRANSITS - {timeline['transits']['positions']['date']}")
            print(f"{'='*80}\n")
            tight_aspects = [a for a in timeline['transits']['aspects'] if a['orb'] < 1.0]
            if tight_aspects:
                print("🌟 EXACT TRANSITS (< 1° orb):")
                for asp in tight_aspects:
                    exact_marker = " *** EXACT ***" if asp['exact'] else ""
                    print(f"   {asp['transiting_planet']} {asp['aspect_type']} "
                          f"Natal {asp['natal_planet']} (orb {asp['orb']:.2f}°){exact_marker}")

            # Show wider orb aspects
            wider_aspects = [a for a in timeline['transits']['aspects'] if 1.0 <= a['orb'] < 3.0]
            if wider_aspects:
                print(f"\n🌙 APPLYING TRANSITS (1-3° orb):")
                for asp in wider_aspects[:5]:  # Top 5
                    print(f"   {asp['transiting_planet']} {asp['aspect_type']} "
                          f"Natal {asp['natal_planet']} (orb {asp['orb']:.2f}°)")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
