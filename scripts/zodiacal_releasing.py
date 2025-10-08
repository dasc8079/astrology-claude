#!/usr/bin/env python3
"""
Zodiacal Releasing Calculator
Traditional Hellenistic time-lord technique for major life periods.

Zodiacal Releasing (ZR) divides life into periods based on the Lot of Fortune
(body/livelihood/fortune) or Lot of Spirit (mind/career/action). Shows major
life chapters, peak periods, and critical transitions.

Formula:
    - Start from Lot of Fortune or Spirit
    - Cycle through signs in zodiacal order
    - Each sign has a period length based on its planetary ruler
    - L1 = main periods, L2 = sub-periods, L3 = sub-sub-periods
    - Peak periods occur when L1 and L2 are in same sign

Usage:
    python zodiacal_releasing.py --profile darren --lot fortune --start-age 0 --end-age 40
    python zodiacal_releasing.py --profile darren --lot spirit --current-age 35
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from profile_loader import load_profile, list_profiles

# Sign order (zodiacal)
SIGNS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer',
    'Leo', 'Virgo', 'Libra', 'Scorpio',
    'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

# Period lengths in years (based on planetary years in traditional astrology)
PERIOD_LENGTHS = {
    'Aries': 15,      # Mars
    'Taurus': 8,      # Venus
    'Gemini': 20,     # Mercury
    'Cancer': 25,     # Moon
    'Leo': 19,        # Sun
    'Virgo': 20,      # Mercury
    'Libra': 8,       # Venus
    'Scorpio': 15,    # Mars
    'Sagittarius': 12, # Jupiter
    'Capricorn': 27,   # Saturn
    'Aquarius': 27,    # Saturn (traditional)
    'Pisces': 12,      # Jupiter
}

# Domicile rulers
DOMICILE = {
    'Aries': 'Mars', 'Taurus': 'Venus', 'Gemini': 'Mercury',
    'Cancer': 'Moon', 'Leo': 'Sun', 'Virgo': 'Mercury',
    'Libra': 'Venus', 'Scorpio': 'Mars', 'Sagittarius': 'Jupiter',
    'Capricorn': 'Saturn', 'Aquarius': 'Saturn', 'Pisces': 'Jupiter'
}


def get_next_sign(current_sign: str) -> str:
    """Get the next sign in zodiacal order."""
    current_index = SIGNS.index(current_sign)
    next_index = (current_index + 1) % 12
    return SIGNS[next_index]


def calculate_l1_periods(lot_sign: str, birth_date: str, max_age: int = 100) -> List[Dict[str, Any]]:
    """
    Calculate L1 (Level 1) periods from Lot position.

    Args:
        lot_sign: Sign where Lot of Fortune or Spirit is located
        birth_date: Birth date (YYYY-MM-DD)
        max_age: Maximum age to calculate (default 100)

    Returns:
        List of L1 periods with start/end ages and dates
    """
    periods = []
    current_sign = lot_sign
    current_age = 0.0

    # Parse birth date
    birth = datetime.strptime(birth_date, '%Y-%m-%d')

    while current_age < max_age:
        period_length = PERIOD_LENGTHS[current_sign]
        end_age = current_age + period_length

        # Calculate dates
        start_date = birth + timedelta(days=365.25 * current_age)
        end_date = birth + timedelta(days=365.25 * end_age)

        periods.append({
            'level': 1,
            'sign': current_sign,
            'ruler': DOMICILE[current_sign],
            'start_age': round(current_age, 2),
            'end_age': round(end_age, 2),
            'duration': period_length,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
        })

        # Move to next sign
        current_sign = get_next_sign(current_sign)
        current_age = end_age

    return periods


def calculate_l2_periods(l1_period: Dict[str, Any], birth_date: str) -> List[Dict[str, Any]]:
    """
    Calculate L2 (Level 2) sub-periods within an L1 period.

    L2 periods cycle through all 12 signs starting from the L1 sign,
    with lengths proportional to the parent L1 period.

    Args:
        l1_period: The parent L1 period
        birth_date: Birth date (YYYY-MM-DD)

    Returns:
        List of L2 periods
    """
    l2_periods = []
    current_sign = l1_period['sign']
    l1_duration = l1_period['duration']

    # Calculate total of all sign periods for proportion
    total_sign_years = sum(PERIOD_LENGTHS.values())  # 228 years total

    # Starting point
    current_age = l1_period['start_age']
    birth = datetime.strptime(birth_date, '%Y-%m-%d')

    # Cycle through all 12 signs
    for i in range(12):
        # Calculate proportional duration for this L2 period
        sign_years = PERIOD_LENGTHS[current_sign]
        l2_duration = (sign_years / total_sign_years) * l1_duration
        end_age = current_age + l2_duration

        # Calculate dates
        start_date = birth + timedelta(days=365.25 * current_age)
        end_date = birth + timedelta(days=365.25 * end_age)

        # Check if this is a peak period (L1 and L2 same sign)
        is_peak = current_sign == l1_period['sign']

        l2_periods.append({
            'level': 2,
            'sign': current_sign,
            'ruler': DOMICILE[current_sign],
            'start_age': round(current_age, 2),
            'end_age': round(end_age, 2),
            'duration': round(l2_duration, 2),
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'parent_sign': l1_period['sign'],
            'is_peak': is_peak,
        })

        current_sign = get_next_sign(current_sign)
        current_age = end_age

    return l2_periods


def calculate_l3_periods(l2_period: Dict[str, Any], birth_date: str) -> List[Dict[str, Any]]:
    """
    Calculate L3 (Level 3) sub-periods within an L2 period.

    L3 periods cycle through all 12 signs starting from the L2 sign,
    with lengths proportional to the parent L2 period.

    Args:
        l2_period: The parent L2 period
        birth_date: Birth date (YYYY-MM-DD)

    Returns:
        List of L3 periods
    """
    l3_periods = []
    current_sign = l2_period['sign']
    l2_duration = l2_period['duration']

    # Calculate total of all sign periods for proportion
    total_sign_years = sum(PERIOD_LENGTHS.values())  # 228 years total

    # Starting point
    current_age = l2_period['start_age']
    birth = datetime.strptime(birth_date, '%Y-%m-%d')

    # Cycle through all 12 signs
    for i in range(12):
        # Calculate proportional duration for this L3 period
        sign_years = PERIOD_LENGTHS[current_sign]
        l3_duration = (sign_years / total_sign_years) * l2_duration
        end_age = current_age + l3_duration

        # Calculate dates
        start_date = birth + timedelta(days=365.25 * current_age)
        end_date = birth + timedelta(days=365.25 * end_age)

        # Check if this is a peak period (L2 and L3 same sign, or L1/L2/L3 all same)
        is_peak_l2 = current_sign == l2_period['sign']
        is_peak_l1 = current_sign == l2_period.get('parent_sign')

        l3_periods.append({
            'level': 3,
            'sign': current_sign,
            'ruler': DOMICILE[current_sign],
            'start_age': round(current_age, 4),
            'end_age': round(end_age, 4),
            'duration': round(l3_duration, 4),
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'parent_l2_sign': l2_period['sign'],
            'parent_l1_sign': l2_period.get('parent_sign'),
            'is_peak_l2': is_peak_l2,  # L3 matches L2
            'is_peak_l1': is_peak_l1,  # L3 matches L1 (rare, powerful)
        })

        current_sign = get_next_sign(current_sign)
        current_age = end_age

    return l3_periods


def find_current_period(periods: List[Dict[str, Any]], current_age: float) -> Optional[Dict[str, Any]]:
    """Find the period that contains the current age."""
    for period in periods:
        if period['start_age'] <= current_age < period['end_age']:
            return period
    return None


def calculate_zr_from_lot(profile_name: str, lot_type: str, max_age: int = 100) -> Dict[str, Any]:
    """
    Calculate complete Zodiacal Releasing from a Lot.

    Args:
        profile_name: Profile to load
        lot_type: 'fortune' or 'spirit'
        max_age: Maximum age to calculate (default 100)

    Returns:
        Dictionary with L1 and L2 periods, lot info, and birth data
    """
    # Load profile
    profile = load_profile(profile_name)

    # Get birth data
    birth_data = profile.get_birth_data()
    if not birth_data:
        raise ValueError(f"No seed data found for profile '{profile_name}'")

    birth_date = birth_data['date']

    # Get Lot position
    lots = profile.get_lots()
    if not lots:
        raise ValueError(f"No lots calculated for profile '{profile_name}'")

    # Find the requested Lot
    lot_name = f"Lot of {'Fortune' if lot_type == 'fortune' else 'Spirit'}"
    lot = next((l for l in lots if l['name'] == lot_name), None)

    if not lot:
        raise ValueError(f"{lot_name} not found in profile")

    lot_sign = lot['position']['sign']
    lot_degree = lot['position']['degree']

    # Calculate L1 periods
    l1_periods = calculate_l1_periods(lot_sign, birth_date, max_age)

    # Calculate L2 periods for each L1 period
    all_l2_periods = []
    for l1_period in l1_periods:
        l2_periods = calculate_l2_periods(l1_period, birth_date)
        all_l2_periods.extend(l2_periods)

    # Calculate L3 periods for each L2 period
    all_l3_periods = []
    for l2_period in all_l2_periods:
        l3_periods = calculate_l3_periods(l2_period, birth_date)
        all_l3_periods.extend(l3_periods)

    return {
        'profile': profile_name,
        'lot_type': lot_type,
        'lot_info': {
            'name': lot_name,
            'sign': lot_sign,
            'degree': round(lot_degree, 2),
        },
        'birth_date': birth_date,
        'l1_periods': l1_periods,
        'l2_periods': all_l2_periods,
        'l3_periods': all_l3_periods,
    }


def format_period_output(period: Dict[str, Any], level: int = 1) -> str:
    """Format a single period for output."""
    indent = "  " * (level - 1)
    output = []

    if level == 1:
        output.append(f"{indent}{'='*60}")
        output.append(f"{indent}L1 PERIOD: {period['sign']} (Ages {period['start_age']}-{period['end_age']})")
        output.append(f"{indent}{'='*60}")
    else:
        peak_marker = " *** PEAK PERIOD ***" if period.get('is_peak') else ""
        output.append(f"{indent}L2: {period['sign']} (Ages {period['start_age']:.1f}-{period['end_age']:.1f}){peak_marker}")

    output.append(f"{indent}  Ruler: {period['ruler']}")
    output.append(f"{indent}  Duration: {period['duration']} years")
    output.append(f"{indent}  Dates: {period['start_date']} to {period['end_date']}")

    return "\n".join(output)


def format_zr_summary(zr_data: Dict[str, Any], current_age: Optional[float] = None) -> str:
    """Format complete ZR data for terminal output."""
    output = []

    output.append("=" * 80)
    output.append(f"ZODIACAL RELEASING FROM {zr_data['lot_info']['name'].upper()}")
    output.append("=" * 80)
    output.append("")
    output.append(f"Profile: {zr_data['profile']}")
    output.append(f"Lot Position: {zr_data['lot_info']['sign']} {zr_data['lot_info']['degree']}°")
    output.append(f"Birth Date: {zr_data['birth_date']}")

    if current_age is not None:
        output.append(f"Current Age: {current_age}")

        # Find current L1 and L2
        current_l1 = find_current_period(zr_data['l1_periods'], current_age)
        current_l2 = find_current_period(zr_data['l2_periods'], current_age)

        if current_l1:
            output.append(f"\nCurrent L1 Period: {current_l1['sign']} (Ages {current_l1['start_age']}-{current_l1['end_age']})")
        if current_l2:
            peak = " *** PEAK PERIOD ***" if current_l2.get('is_peak') else ""
            output.append(f"Current L2 Period: {current_l2['sign']} (Ages {current_l2['start_age']:.1f}-{current_l2['end_age']:.1f}){peak}")

    output.append("")
    output.append("-" * 80)

    return "\n".join(output)


def format_age_range(zr_data: Dict[str, Any], start_age: float, end_age: float) -> str:
    """Format ZR periods within an age range."""
    output = []
    output.append(format_zr_summary(zr_data))
    output.append(f"\nPERIODS FROM AGE {start_age} TO {end_age}")
    output.append("-" * 80)
    output.append("")

    # Filter L1 periods that overlap with age range
    relevant_l1 = [p for p in zr_data['l1_periods']
                   if p['start_age'] < end_age and p['end_age'] > start_age]

    for l1 in relevant_l1:
        output.append(format_period_output(l1, level=1))
        output.append("")

        # Get L2 periods within this L1
        l2_periods = [p for p in zr_data['l2_periods']
                     if p['parent_sign'] == l1['sign'] and
                     p['start_age'] < end_age and p['end_age'] > start_age]

        for l2 in l2_periods:
            output.append(format_period_output(l2, level=2))

        output.append("")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description='Calculate Zodiacal Releasing')
    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--lot', required=True, choices=['fortune', 'spirit'],
                       help='Lot to use (fortune or spirit)')
    parser.add_argument('--current-age', type=float, help='Show current period at this age')
    parser.add_argument('--start-age', type=float, default=0, help='Start age for range (default 0)')
    parser.add_argument('--end-age', type=float, help='End age for range (default 40 or current-age+10)')
    parser.add_argument('--max-age', type=int, default=100, help='Maximum age to calculate (default 100)')
    parser.add_argument('--list-profiles', action='store_true', help='List available profiles')

    args = parser.parse_args()

    if args.list_profiles:
        profiles = list_profiles()
        print(f"Available profiles: {', '.join(profiles)}")
        return

    # Set default end_age
    if args.end_age is None:
        if args.current_age is not None:
            args.end_age = args.current_age + 10
        else:
            args.end_age = 40

    try:
        # Calculate ZR
        zr_data = calculate_zr_from_lot(args.profile, args.lot, args.max_age)

        # Show current period
        if args.current_age is not None:
            print(format_zr_summary(zr_data, args.current_age))
            print()

        # Show age range
        print(format_age_range(zr_data, args.start_age, args.end_age))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
