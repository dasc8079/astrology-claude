#!/usr/bin/env python3
"""
Firdaria Calculator
Persian time-lord system dividing life into planetary periods (ages 0-75).

Firdaria is a medieval Persian timing technique where each planet rules for
a fixed number of years. The sequence differs based on chart sect (day/night).

Major Periods:
    Day charts start with Sun, Night charts start with Moon
    Each planet rules for 2-13 years (total 75 years)

Sub-Periods:
    Each major period is divided into 7 sub-periods
    Sub-period length = (Major Years) × (Sub-Planet Years) ÷ 75

Usage:
    python firdaria_calculator.py --profile darren --age 36
    python firdaria_calculator.py --profile darren --age-range 30-40
    python firdaria_calculator.py --profile darren --full-timeline
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from profile_loader import load_profile, list_profiles

# Planet period lengths (years)
PLANET_YEARS = {
    'Sun': 10,
    'Venus': 8,
    'Mercury': 13,
    'Moon': 9,
    'Saturn': 11,
    'Jupiter': 12,
    'Mars': 7,
    'North Node': 3,
    'South Node': 2,
}

# Day chart sequence (starts with Sun - diurnal sect light)
DAY_SEQUENCE = [
    'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars',
    'North Node', 'South Node'
]

# Night chart sequence (starts with Moon - nocturnal sect light)
NIGHT_SEQUENCE = [
    'Moon', 'Saturn', 'Jupiter', 'Mars', 'North Node', 'South Node',
    'Sun', 'Venus', 'Mercury'
]


def calculate_major_periods(sect: str) -> List[Dict[str, Any]]:
    """
    Calculate all major Firdaria periods based on chart sect.

    Args:
        sect: 'day' or 'night'

    Returns:
        List of major period dictionaries with start_age, end_age, planet
    """
    sequence = DAY_SEQUENCE if sect == 'day' else NIGHT_SEQUENCE
    periods = []
    current_age = 0.0

    for planet in sequence:
        years = PLANET_YEARS[planet]
        periods.append({
            'planet': planet,
            'start_age': current_age,
            'end_age': current_age + years,
            'duration': years,
            'period_number': len(periods) + 1,
        })
        current_age += years

    return periods


def calculate_sub_periods(major_period: Dict[str, Any], sect: str) -> List[Dict[str, Any]]:
    """
    Calculate sub-periods within a major period.

    Each major period is divided into 7 sub-periods ruled by the seven
    traditional planets (excluding nodes) in sect-based sequence.

    Args:
        major_period: Major period dictionary
        sect: 'day' or 'night'

    Returns:
        List of sub-period dictionaries
    """
    # Sub-period sequence (7 traditional planets only, no nodes)
    sub_sequence = ['Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars'] if sect == 'day' else \
                   ['Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury']

    major_planet = major_period['planet']
    major_start = major_period['start_age']
    major_duration = major_period['duration']

    sub_periods = []
    current_age = major_start

    for sub_planet in sub_sequence:
        # Sub-period duration = (Major Years) × (Sub-Planet Years) ÷ 75
        sub_duration = (major_duration * PLANET_YEARS[sub_planet]) / 75.0

        sub_periods.append({
            'major_planet': major_planet,
            'sub_planet': sub_planet,
            'start_age': current_age,
            'end_age': current_age + sub_duration,
            'duration': sub_duration,
            'label': f"{major_planet}/{sub_planet}",
        })
        current_age += sub_duration

    return sub_periods


def find_active_periods(age: float, sect: str) -> Dict[str, Any]:
    """
    Find active major and sub-period for a given age.

    Args:
        age: Age in years (can be decimal)
        sect: 'day' or 'night'

    Returns:
        Dictionary with active major and sub-period, or None if beyond age 75
    """
    if age >= 75.0:
        return {
            'age': age,
            'beyond_firdaria': True,
            'message': 'Age beyond Firdaria coverage (75 years)'
        }

    # Find active major period
    major_periods = calculate_major_periods(sect)
    active_major = None

    for period in major_periods:
        if period['start_age'] <= age < period['end_age']:
            active_major = period
            break

    if not active_major:
        return None

    # Find active sub-period within the major period
    sub_periods = calculate_sub_periods(active_major, sect)
    active_sub = None

    for sub_period in sub_periods:
        if sub_period['start_age'] <= age < sub_period['end_age']:
            active_sub = sub_period
            break

    return {
        'age': age,
        'sect': sect,
        'major_period': active_major,
        'sub_period': active_sub,
        'beyond_firdaria': False,
    }


def calculate_firdaria_for_profile(profile_name: str, age: Optional[float] = None) -> Dict[str, Any]:
    """
    Calculate Firdaria periods for a profile with natal chart context.

    Args:
        profile_name: Profile to load
        age: Optional age to find active periods (None = full timeline)

    Returns:
        Dictionary with Firdaria data and natal context
    """
    # Load profile
    profile = load_profile(profile_name)

    # Get birth data
    birth_data = profile.get_birth_data()
    if not birth_data:
        raise ValueError(f"No seed data found for profile '{profile_name}'")

    # Get chart sect
    framework = profile.get_chart_framework()
    sect = framework.get('sect', {}).get('type', 'day')

    # Calculate major periods
    major_periods = calculate_major_periods(sect)

    result = {
        'profile': profile_name,
        'sect': sect,
        'major_periods': major_periods,
    }

    # If age provided, find active periods
    if age is not None:
        active = find_active_periods(age, sect)
        result['active_at_age'] = active

        # Add all sub-periods for the active major period
        if active and not active.get('beyond_firdaria'):
            active_major = active['major_period']
            result['active_major_sub_periods'] = calculate_sub_periods(active_major, sect)

    # If age not provided, calculate all sub-periods
    else:
        result['all_sub_periods'] = []
        for major in major_periods:
            subs = calculate_sub_periods(major, sect)
            result['all_sub_periods'].extend(subs)

    return result


def format_period(period: Dict[str, Any], indent: int = 0) -> str:
    """Format a period for display."""
    prefix = "  " * indent
    start = period['start_age']
    end = period['end_age']
    duration = period['duration']

    if 'sub_planet' in period:
        # Sub-period
        return f"{prefix}{period['label']}: Ages {start:.2f}-{end:.2f} ({duration:.2f} years)"
    else:
        # Major period
        planet = period['planet']
        return f"{prefix}{planet}: Ages {start:.1f}-{end:.1f} ({duration} years)"


def main():
    parser = argparse.ArgumentParser(description='Calculate Firdaria periods')
    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--age', type=float, help='Calculate for specific age')
    parser.add_argument('--age-range', help='Age range (e.g., 30-40)')
    parser.add_argument('--full-timeline', action='store_true', help='Show all periods 0-75')
    parser.add_argument('--show-sub-periods', action='store_true', help='Show sub-periods')

    args = parser.parse_args()

    # Single age
    if args.age is not None:
        result = calculate_firdaria_for_profile(args.profile, args.age)

        print(f"\n{'='*80}")
        print(f"FIRDARIA FOR {result['profile'].upper()} AT AGE {args.age}")
        print(f"{'='*80}")
        print(f"Chart Sect: {result['sect'].capitalize()}")

        active = result.get('active_at_age')
        if active and not active.get('beyond_firdaria'):
            major = active['major_period']
            sub = active['sub_period']

            print(f"\n🌟 ACTIVE MAJOR PERIOD:")
            print(f"   {format_period(major)}")

            if sub:
                print(f"\n🔹 ACTIVE SUB-PERIOD:")
                print(f"   {format_period(sub, indent=1)}")

            if args.show_sub_periods and 'active_major_sub_periods' in result:
                print(f"\n📋 ALL SUB-PERIODS IN {major['planet']} PERIOD:")
                for sp in result['active_major_sub_periods']:
                    print(f"   {format_period(sp, indent=1)}")
        elif active and active.get('beyond_firdaria'):
            print(f"\n⚠️  {active['message']}")

    # Age range
    elif args.age_range:
        start, end = map(int, args.age_range.split('-'))
        result = calculate_firdaria_for_profile(args.profile)

        print(f"\n{'='*80}")
        print(f"FIRDARIA FOR {result['profile'].upper()} (Ages {start}-{end})")
        print(f"{'='*80}")
        print(f"Chart Sect: {result['sect'].capitalize()}\n")

        for age in range(start, end + 1):
            active = find_active_periods(float(age), result['sect'])
            if active and not active.get('beyond_firdaria'):
                major = active['major_period']
                sub = active['sub_period']
                print(f"Age {age}: {major['planet']} / {sub['sub_planet']}")

    # Full timeline
    elif args.full_timeline:
        result = calculate_firdaria_for_profile(args.profile)

        print(f"\n{'='*80}")
        print(f"COMPLETE FIRDARIA TIMELINE FOR {result['profile'].upper()}")
        print(f"{'='*80}")
        print(f"Chart Sect: {result['sect'].capitalize()}\n")

        print("MAJOR PERIODS (Ages 0-75):")
        for major in result['major_periods']:
            print(f"  {format_period(major)}")

        if args.show_sub_periods:
            print(f"\n{'='*80}")
            print("COMPLETE SUB-PERIOD BREAKDOWN:")
            print(f"{'='*80}\n")

            for major in result['major_periods']:
                print(f"\n{major['planet']} Major Period ({major['start_age']:.1f}-{major['end_age']:.1f}):")
                subs = calculate_sub_periods(major, result['sect'])
                for sub in subs:
                    print(f"  {format_period(sub, indent=1)}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
