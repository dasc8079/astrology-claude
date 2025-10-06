#!/usr/bin/env python3
"""
Solar Returns Calculator
Calculates solar return chart for any year of life.

A solar return chart is cast for the moment the Sun returns to its exact
natal position each year. The chart describes themes and events for the
year ahead (birthday to birthday).

Usage:
    python solar_returns.py --profile darren --age 36
    python solar_returns.py --profile darren --year 2024
    python solar_returns.py --profile darren --age 36 --location "New York, NY"
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
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


def get_sign_from_longitude(longitude: float) -> Tuple[str, float]:
    """Convert ecliptic longitude to sign and degree within sign."""
    sign_index = int(longitude / 30)
    degree_in_sign = longitude % 30
    return SIGNS[sign_index], degree_in_sign


def calculate_julian_day(year: int, month: int, day: int, hour: float) -> float:
    """Calculate Julian Day from date and time (UTC)."""
    return swe.julday(year, month, day, hour)


def find_solar_return_moment(natal_sun_longitude: float, birth_year: int, birth_month: int, birth_day: int, return_year: int) -> float:
    """
    Find the exact moment when transiting Sun returns to natal Sun position.

    Args:
        natal_sun_longitude: Natal Sun's ecliptic longitude
        birth_year: Year of birth
        birth_month: Month of birth
        birth_day: Day of birth
        return_year: Year for which to calculate solar return

    Returns:
        Julian Day of exact solar return
    """
    # Approximate starting point (birthday in return year, noon)
    approx_jd = calculate_julian_day(return_year, birth_month, birth_day, 12.0)

    # Search for exact moment (within 2 days of approximate birthday)
    search_start = approx_jd - 2
    search_end = approx_jd + 2

    # Use Swiss Ephemeris to find exact position
    # Binary search for when Sun crosses natal position
    tolerance = 0.0001  # Very tight tolerance for accuracy

    while search_end - search_start > tolerance:
        mid_jd = (search_start + search_end) / 2
        sun_pos, _ = swe.calc_ut(mid_jd, swe.SUN)
        sun_long = sun_pos[0]

        # Handle zodiac wrap-around
        diff = sun_long - natal_sun_longitude
        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360

        if abs(diff) < 0.001:  # Close enough
            return mid_jd
        elif diff < 0:  # Sun hasn't reached position yet
            search_start = mid_jd
        else:  # Sun has passed position
            search_end = mid_jd

    return (search_start + search_end) / 2


def calculate_solar_return_chart(
    profile_name: str,
    age: Optional[int] = None,
    year: Optional[int] = None,
    location: Optional[Dict[str, float]] = None
) -> Dict[str, Any]:
    """
    Calculate solar return chart for given age or year.

    Args:
        profile_name: Profile to use
        age: Age for solar return (e.g., 36 for 36th birthday)
        year: Calendar year for solar return (alternative to age)
        location: Optional dict with 'latitude', 'longitude' for relocation

    Returns:
        Dictionary with solar return chart data
    """
    profile = load_profile(profile_name)
    birth_data = profile.get_birth_data()

    # Get natal Sun position
    natal_planets = profile.get_planets(traditional_only=True)
    natal_sun = next(p for p in natal_planets if p['name'] == 'Sun')
    natal_sun_longitude = natal_sun['longitude']

    # Determine return year
    birth_date_parts = birth_data['date'].split('-')
    birth_year = int(birth_date_parts[0])
    birth_month = int(birth_date_parts[1])
    birth_day = int(birth_date_parts[2])

    if year is not None:
        return_year = year
        age = year - birth_year
    elif age is not None:
        return_year = birth_year + age
    else:
        raise ValueError("Must provide either age or year")

    # Find exact solar return moment
    sr_jd = find_solar_return_moment(natal_sun_longitude, birth_year, birth_month, birth_day, return_year)

    # Convert JD to calendar date/time
    cal = swe.revjul(sr_jd)
    sr_year, sr_month, sr_day, sr_hour = cal[0], cal[1], cal[2], cal[3]

    sr_datetime = datetime(sr_year, sr_month, sr_day, int(sr_hour), int((sr_hour % 1) * 60))

    # Use relocation or natal location
    if location:
        lat = location['latitude']
        lon = location['longitude']
        location_name = location.get('name', f"{lat:.2f}°, {lon:.2f}°")
    else:
        lat = birth_data['latitude']
        lon = birth_data['longitude']
        location_name = birth_data['location']

    # Calculate Ascendant and MC for solar return
    houses = swe.houses(sr_jd, lat, lon, b'W')  # Whole sign houses
    asc_longitude = houses[1][0]  # Ascendant
    mc_longitude = houses[1][1]   # MC

    asc_sign, asc_degree = get_sign_from_longitude(asc_longitude)
    mc_sign, mc_degree = get_sign_from_longitude(mc_longitude)

    # Calculate planet positions at solar return moment
    sr_planets = []

    for planet_id in TRADITIONAL_PLANETS:
        planet_name = PLANET_NAMES[planet_id]

        position, _ = swe.calc_ut(sr_jd, planet_id)
        longitude = position[0]
        speed = position[3]

        sign, degree = get_sign_from_longitude(longitude)

        # Determine house (whole sign from SR Ascendant)
        asc_sign_index = SIGNS.index(asc_sign)
        planet_sign_index = SIGNS.index(sign)
        house = ((planet_sign_index - asc_sign_index) % 12) + 1

        # Also determine natal house placement
        natal_asc_sign = profile.seed_data['chart_framework']['ascendant']['sign']
        natal_asc_index = SIGNS.index(natal_asc_sign)
        natal_house = ((planet_sign_index - natal_asc_index) % 12) + 1

        sr_planets.append({
            'name': planet_name,
            'longitude': longitude,
            'sign': sign,
            'degree': degree,
            'dms': f"{int(degree)}°{int((degree % 1) * 60)}'{int(((degree * 60) % 1) * 60)}\"",
            'sr_house': house,
            'natal_house': natal_house,
            'speed': speed,
            'retrograde': speed < 0
        })

    return {
        'profile': profile_name,
        'age': age,
        'return_year': return_year,
        'sr_datetime': sr_datetime.strftime('%Y-%m-%d %H:%M:%S'),
        'location': location_name,
        'latitude': lat,
        'longitude': lon,
        'ascendant': {
            'sign': asc_sign,
            'degree': asc_degree,
            'dms': f"{int(asc_degree)}°{int((asc_degree % 1) * 60)}'{int(((asc_degree * 60) % 1) * 60)}\"",
            'longitude': asc_longitude
        },
        'midheaven': {
            'sign': mc_sign,
            'degree': mc_degree,
            'dms': f"{int(mc_degree)}°{int((mc_degree % 1) * 60)}'{int(((mc_degree * 60) % 1) * 60)}\"",
            'longitude': mc_longitude
        },
        'planets': sr_planets,
    }


def find_sr_to_natal_aspects(sr_chart: Dict[str, Any], profile_name: str, orb: float = 3.0) -> List[Dict[str, Any]]:
    """
    Find aspects between solar return planets and natal planets.

    Args:
        sr_chart: Solar return chart data
        profile_name: Profile name
        orb: Orb in degrees (default 3°)

    Returns:
        List of aspect dictionaries
    """
    profile = load_profile(profile_name)
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

    # Check each SR planet against each natal planet
    for sr_planet in sr_chart['planets']:
        for natal_name, natal_long in natal_planets.items():
            # Calculate angular distance
            diff = abs(sr_planet['longitude'] - natal_long)
            if diff > 180:
                diff = 360 - diff

            # Check each aspect type
            for aspect_name, aspect_angle in aspect_angles.items():
                orb_diff = abs(diff - aspect_angle)

                if orb_diff <= orb:
                    aspects.append({
                        'sr_planet': sr_planet['name'],
                        'natal_planet': natal_name,
                        'aspect_type': aspect_name,
                        'orb': orb_diff,
                    })

    return aspects


def format_solar_return(sr_chart: Dict[str, Any], show_natal_houses: bool = False) -> str:
    """Format solar return chart for display."""
    output = []

    output.append(f"\n{'='*80}")
    output.append(f"SOLAR RETURN CHART - AGE {sr_chart['age']} ({sr_chart['return_year']})")
    output.append(f"{'='*80}")
    output.append(f"Profile: {sr_chart['profile']}")
    output.append(f"Solar Return: {sr_chart['sr_datetime']}")
    output.append(f"Location: {sr_chart['location']}")
    output.append(f"\n{'Chart Framework':^80}")
    output.append(f"{'-'*80}")
    output.append(f"Ascendant:  {sr_chart['ascendant']['sign']:12} {sr_chart['ascendant']['dms']}")
    output.append(f"Midheaven:  {sr_chart['midheaven']['sign']:12} {sr_chart['midheaven']['dms']}")

    output.append(f"\n{'Solar Return Planetary Positions':^80}")
    output.append(f"{'-'*80}")

    for planet in sr_chart['planets']:
        retro = " R" if planet['retrograde'] else ""
        house_info = f"SR House {planet['sr_house']}"
        if show_natal_houses:
            house_info += f", Natal House {planet['natal_house']}"

        output.append(f"{planet['name']:12} {planet['sign']:12} {planet['dms']:>10}{retro:3} ({house_info})")

    return "\n".join(output)


def format_sr_aspects(aspects: List[Dict[str, Any]]) -> str:
    """Format solar return to natal aspects."""
    if not aspects:
        return "\nNo major SR-to-natal aspects within orb.\n"

    output = []
    output.append(f"\n{'Solar Return to Natal Aspects':^80}")
    output.append(f"{'-'*80}")

    for aspect in aspects:
        output.append(f"SR {aspect['sr_planet']} {aspect['aspect_type']} "
                     f"Natal {aspect['natal_planet']} (orb {aspect['orb']:.2f}°)")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description='Calculate solar return charts')
    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--age', type=int, help='Age for solar return')
    parser.add_argument('--year', type=int, help='Calendar year for solar return')
    parser.add_argument('--location', help='Relocation (e.g., "New York, NY" with coordinates)')
    parser.add_argument('--show-aspects', action='store_true', help='Show SR-to-natal aspects')
    parser.add_argument('--show-natal-houses', action='store_true', help='Show natal house placements')
    parser.add_argument('--list-profiles', action='store_true', help='List available profiles')

    args = parser.parse_args()

    if args.list_profiles:
        profiles = list_profiles()
        print(f"Available profiles: {', '.join(profiles)}")
        return

    if args.age is None and args.year is None:
        print("Error: Must provide either --age or --year", file=sys.stderr)
        sys.exit(1)

    try:
        # Calculate solar return
        location = None
        if args.location:
            # Simple implementation - in real version would geocode location string
            print("Note: Relocation not fully implemented. Using natal location.", file=sys.stderr)

        sr_chart = calculate_solar_return_chart(
            args.profile,
            age=args.age,
            year=args.year,
            location=location
        )

        print(format_solar_return(sr_chart, show_natal_houses=args.show_natal_houses))

        if args.show_aspects:
            aspects = find_sr_to_natal_aspects(sr_chart, args.profile)
            print(format_sr_aspects(aspects))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
