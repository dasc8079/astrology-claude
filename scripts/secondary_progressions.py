#!/usr/bin/env python3
"""
Secondary Progressions Calculator
Calculates progressed chart positions using day-for-a-year method.

In secondary progressions:
- 1 day after birth = 1 year of life
- Day 30 after birth = age 30
- Most important: Progressed Moon (completes cycle in ~27-28 years)

Usage:
    python secondary_progressions.py --profile darren --age 36
    python secondary_progressions.py --profile darren --age-range 30-40
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import swisseph as swe

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from profile_loader import load_profile, list_profiles

# Constants
SIGNS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

PLANET_NAMES = {
    swe.SUN: 'Sun',
    swe.MOON: 'Moon',
    swe.MERCURY: 'Mercury',
    swe.VENUS: 'Venus',
    swe.MARS: 'Mars',
    swe.JUPITER: 'Jupiter',
    swe.SATURN: 'Saturn',
}

TRADITIONAL_PLANETS = [swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS, swe.JUPITER, swe.SATURN]


def get_sign_from_longitude(longitude: float) -> tuple[str, float]:
    """Convert ecliptic longitude to sign and degree within sign."""
    sign_index = int(longitude / 30)
    degree_in_sign = longitude % 30
    return SIGNS[sign_index], degree_in_sign


def calculate_julian_day(date_str: str, time_str: str, utc_offset: str) -> float:
    """Calculate Julian Day from date, time, and UTC offset."""
    dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")

    # Parse UTC offset
    offset_hours = int(utc_offset[:3])
    offset_minutes = int(utc_offset[0] + utc_offset[4:]) if len(utc_offset) > 3 else 0

    # Convert to UTC
    dt_utc = dt - timedelta(hours=offset_hours, minutes=offset_minutes)

    year = dt_utc.year
    month = dt_utc.month
    day = dt_utc.day
    hour = dt_utc.hour + dt_utc.minute / 60.0 + dt_utc.second / 3600.0

    return swe.julday(year, month, day, hour)


def calculate_progressed_positions(profile_name: str, age: float) -> Dict[str, Any]:
    """
    Calculate secondary progressed positions for given age.

    Args:
        profile_name: Profile to use
        age: Age in years (can be fractional)

    Returns:
        Dictionary with progressed planetary positions
    """
    profile = load_profile(profile_name)
    birth_data = profile.get_birth_data()

    # Calculate birth Julian Day
    birth_jd = calculate_julian_day(
        birth_data['date'],
        birth_data['time'],
        birth_data['utc_offset']
    )

    # Secondary progressions: 1 day = 1 year
    # For age 36, we calculate positions 36 days after birth
    progressed_jd = birth_jd + age

    # Calculate progressed planet positions
    progressed_planets = []

    for planet_id in TRADITIONAL_PLANETS:
        planet_name = PLANET_NAMES[planet_id]

        # Calculate position at progressed date
        position, _ = swe.calc_ut(progressed_jd, planet_id)
        longitude = position[0]
        speed = position[3]

        sign, degree = get_sign_from_longitude(longitude)

        # Determine house (using whole sign from natal Ascendant)
        natal_asc_sign = profile.seed_data['chart_framework']['ascendant']['sign']
        natal_asc_index = SIGNS.index(natal_asc_sign)
        sign_index = SIGNS.index(sign)
        house = ((sign_index - natal_asc_index) % 12) + 1

        progressed_planets.append({
            'name': planet_name,
            'longitude': longitude,
            'sign': sign,
            'degree': degree,
            'dms': f"{int(degree)}°{int((degree % 1) * 60)}'{int(((degree * 60) % 1) * 60)}\"",
            'house': house,
            'speed': speed,
            'retrograde': speed < 0
        })

    return {
        'profile': profile_name,
        'age': age,
        'birth_date': birth_data['date'],
        'progressed_date': (datetime.strptime(birth_data['date'], '%Y-%m-%d') + timedelta(days=age)).strftime('%Y-%m-%d'),
        'progressed_planets': progressed_planets,
    }


def find_progressed_aspects_to_natal(profile_name: str, age: float, orb: float = 3.0) -> List[Dict[str, Any]]:
    """
    Find aspects between progressed planets and natal planets.

    Args:
        profile_name: Profile to use
        age: Age in years
        orb: Orb in degrees for aspects (default 3°)

    Returns:
        List of aspect dictionaries
    """
    profile = load_profile(profile_name)
    progressed = calculate_progressed_positions(profile_name, age)

    aspects = []
    aspect_angles = {
        'conjunction': 0,
        'sextile': 60,
        'square': 90,
        'trine': 120,
        'opposition': 180
    }

    # Get natal planets
    natal_planets = {p['name']: p['longitude'] for p in profile.get_planets(traditional_only=True)}

    # Check each progressed planet against each natal planet
    for prog_planet in progressed['progressed_planets']:
        for natal_name, natal_long in natal_planets.items():
            # Don't aspect planet to itself
            if prog_planet['name'] == natal_name:
                continue

            # Calculate angular distance
            diff = abs(prog_planet['longitude'] - natal_long)
            if diff > 180:
                diff = 360 - diff

            # Check each aspect type
            for aspect_name, aspect_angle in aspect_angles.items():
                orb_diff = abs(diff - aspect_angle)

                if orb_diff <= orb:
                    aspects.append({
                        'progressed_planet': prog_planet['name'],
                        'natal_planet': natal_name,
                        'aspect_type': aspect_name,
                        'orb': orb_diff,
                        'applying': True,  # Would need speed comparison for exact determination
                    })

    return aspects


def track_progressed_moon_cycle(profile_name: str, start_age: int = 0, end_age: int = 100) -> List[Dict[str, Any]]:
    """
    Track progressed Moon through signs from start to end age.
    Progressed Moon completes full zodiac cycle in ~27-28 years.

    Returns:
        List of Moon sign changes with ages
    """
    profile = load_profile(profile_name)
    moon_cycles = []

    current_sign = None
    sign_start_age = start_age

    # Check Moon position every 2.3 years (average time in each sign)
    for age in range(start_age, end_age + 1):
        progressed = calculate_progressed_positions(profile_name, float(age))
        moon = next(p for p in progressed['progressed_planets'] if p['name'] == 'Moon')

        if moon['sign'] != current_sign:
            if current_sign is not None:
                # Record completed period
                moon_cycles.append({
                    'sign': current_sign,
                    'start_age': sign_start_age,
                    'end_age': age,
                    'duration': age - sign_start_age
                })

            current_sign = moon['sign']
            sign_start_age = age

    # Add final period
    if current_sign is not None:
        moon_cycles.append({
            'sign': current_sign,
            'start_age': sign_start_age,
            'end_age': end_age,
            'duration': end_age - sign_start_age
        })

    return moon_cycles


def format_progressed_chart(progressed_data: Dict[str, Any], show_natal: bool = False) -> str:
    """Format progressed chart positions for display."""
    output = []

    output.append(f"\n{'='*80}")
    output.append(f"SECONDARY PROGRESSIONS - AGE {progressed_data['age']}")
    output.append(f"{'='*80}")
    output.append(f"Profile: {progressed_data['profile']}")
    output.append(f"Birth Date: {progressed_data['birth_date']}")
    output.append(f"Progressed Date: {progressed_data['progressed_date']} ({progressed_data['age']:.1f} days after birth)")
    output.append(f"\n{'Progressed Planetary Positions':^80}")
    output.append(f"{'-'*80}")

    for planet in progressed_data['progressed_planets']:
        retro = " R" if planet['retrograde'] else ""
        output.append(f"{planet['name']:12} {planet['sign']:12} {planet['dms']:>10}{retro:3} (House {planet['house']})")

    return "\n".join(output)


def format_progressed_aspects(aspects: List[Dict[str, Any]]) -> str:
    """Format progressed-to-natal aspects."""
    if not aspects:
        return "\nNo major progressed-to-natal aspects within orb.\n"

    output = []
    output.append(f"\n{'Progressed-to-Natal Aspects':^80}")
    output.append(f"{'-'*80}")

    for aspect in aspects:
        output.append(f"Progressed {aspect['progressed_planet']} {aspect['aspect_type']} "
                     f"Natal {aspect['natal_planet']} (orb {aspect['orb']:.2f}°)")

    return "\n".join(output)


def format_moon_cycle(moon_cycles: List[Dict[str, Any]]) -> str:
    """Format progressed Moon cycle through signs."""
    output = []
    output.append(f"\n{'Progressed Moon Cycle':^80}")
    output.append(f"{'-'*80}")

    for cycle in moon_cycles:
        output.append(f"Ages {cycle['start_age']}-{cycle['end_age']}: "
                     f"{cycle['sign']} ({cycle['duration']} years)")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description='Calculate secondary progressions')
    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--age', type=float, help='Current age for progressed chart')
    parser.add_argument('--age-range', help='Age range for Moon cycle (e.g., "0-50")')
    parser.add_argument('--show-aspects', action='store_true', help='Show progressed-to-natal aspects')
    parser.add_argument('--moon-cycle', action='store_true', help='Show progressed Moon cycle')
    parser.add_argument('--list-profiles', action='store_true', help='List available profiles')

    args = parser.parse_args()

    if args.list_profiles:
        profiles = list_profiles()
        print(f"Available profiles: {', '.join(profiles)}")
        return

    try:
        # Single age progressed chart
        if args.age is not None:
            progressed = calculate_progressed_positions(args.profile, args.age)
            print(format_progressed_chart(progressed))

            if args.show_aspects:
                aspects = find_progressed_aspects_to_natal(args.profile, args.age)
                print(format_progressed_aspects(aspects))

        # Moon cycle tracking
        if args.moon_cycle or args.age_range:
            start_age = 0
            end_age = 50

            if args.age_range:
                try:
                    start_age, end_age = map(int, args.age_range.split('-'))
                except ValueError:
                    print(f"Error: Invalid age range format. Use 'START-END' (e.g., '0-50')", file=sys.stderr)
                    sys.exit(1)

            moon_cycles = track_progressed_moon_cycle(args.profile, start_age, end_age)
            print(format_moon_cycle(moon_cycles))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
