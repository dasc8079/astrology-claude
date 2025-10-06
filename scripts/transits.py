#!/usr/bin/env python3
"""
Transits Calculator
Calculates current transiting planet positions and aspects to natal chart.

Transits show real-time planetary triggers activating natal chart themes.
Most immediate and concrete timing technique.

Usage:
    python transits.py --profile darren --date 2025-01-15
    python transits.py --profile darren --date today
    python transits.py --profile darren --date 2025-01-15 --orb 1
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
    swe.URANUS: 'Uranus',
    swe.NEPTUNE: 'Neptune',
    swe.PLUTO: 'Pluto',
}

TRADITIONAL_PLANETS = [swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS, swe.JUPITER, swe.SATURN]
MODERN_PLANETS = [swe.URANUS, swe.NEPTUNE, swe.PLUTO]
ALL_PLANETS = TRADITIONAL_PLANETS + MODERN_PLANETS


def get_sign_from_longitude(longitude: float) -> Tuple[str, float]:
    """Convert ecliptic longitude to sign and degree within sign."""
    sign_index = int(longitude / 30)
    degree_in_sign = longitude % 30
    return SIGNS[sign_index], degree_in_sign


def calculate_julian_day(date_str: str) -> float:
    """Calculate Julian Day from date string (YYYY-MM-DD) at noon UTC."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return swe.julday(dt.year, dt.month, dt.day, 12.0)


def calculate_transiting_positions(date_str: str, include_modern: bool = True) -> Dict[str, Any]:
    """
    Calculate transiting planet positions for given date.

    Args:
        date_str: Date in YYYY-MM-DD format
        include_modern: Include Uranus, Neptune, Pluto

    Returns:
        Dictionary with transiting positions
    """
    jd = calculate_julian_day(date_str)

    planets_to_calc = ALL_PLANETS if include_modern else TRADITIONAL_PLANETS

    transiting_planets = []

    for planet_id in planets_to_calc:
        planet_name = PLANET_NAMES[planet_id]

        position, _ = swe.calc_ut(jd, planet_id)
        longitude = position[0]
        speed = position[3]

        sign, degree = get_sign_from_longitude(longitude)

        transiting_planets.append({
            'name': planet_name,
            'longitude': longitude,
            'sign': sign,
            'degree': degree,
            'dms': f"{int(degree)}°{int((degree % 1) * 60)}'{int(((degree * 60) % 1) * 60)}\"",
            'speed': speed,
            'retrograde': speed < 0,
            'traditional': planet_id in TRADITIONAL_PLANETS
        })

    return {
        'date': date_str,
        'julian_day': jd,
        'planets': transiting_planets,
    }


def find_transit_aspects_to_natal(
    transits: Dict[str, Any],
    profile_name: str,
    orb: float = 3.0,
    aspects_to_check: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Find aspects between transiting planets and natal planets.

    Args:
        transits: Transit data from calculate_transiting_positions
        profile_name: Profile to compare against
        orb: Orb in degrees (default 3°)
        aspects_to_check: List of aspect types, or None for all

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

    if aspects_to_check:
        aspect_angles = {k: v for k, v in aspect_angles.items() if k in aspects_to_check}

    # Get natal planets
    natal_planets = {p['name']: p['longitude'] for p in profile.get_planets(traditional_only=False)}

    # Check each transiting planet against each natal planet
    for trans_planet in transits['planets']:
        for natal_name, natal_long in natal_planets.items():
            # Calculate angular distance
            diff = abs(trans_planet['longitude'] - natal_long)
            if diff > 180:
                diff = 360 - diff

            # Check each aspect type
            for aspect_name, aspect_angle in aspect_angles.items():
                orb_diff = abs(diff - aspect_angle)

                if orb_diff <= orb:
                    # Determine if applying or separating (simplified)
                    applying = trans_planet['speed'] > 0  # Simplified: direct motion = applying

                    aspects.append({
                        'transiting_planet': trans_planet['name'],
                        'natal_planet': natal_name,
                        'aspect_type': aspect_name,
                        'orb': orb_diff,
                        'exact': orb_diff < 0.5,
                        'applying': applying,
                        'transit_retrograde': trans_planet['retrograde']
                    })

    # Sort by orb (tightest first)
    aspects.sort(key=lambda x: x['orb'])

    return aspects


def find_transits_in_natal_houses(transits: Dict[str, Any], profile_name: str) -> Dict[str, Any]:
    """
    Determine which natal houses transiting planets are in.

    Args:
        transits: Transit data
        profile_name: Profile to use for natal chart

    Returns:
        Transit data with natal house placements added
    """
    profile = load_profile(profile_name)
    natal_asc_sign = profile.seed_data['chart_framework']['ascendant']['sign']
    natal_asc_index = SIGNS.index(natal_asc_sign)

    for planet in transits['planets']:
        planet_sign_index = SIGNS.index(planet['sign'])
        natal_house = ((planet_sign_index - natal_asc_index) % 12) + 1
        planet['natal_house'] = natal_house

    return transits


def format_transiting_positions(transits: Dict[str, Any], show_natal_houses: bool = False) -> str:
    """Format transiting positions for display."""
    output = []

    output.append(f"\n{'='*80}")
    output.append(f"TRANSITING POSITIONS - {transits['date']}")
    output.append(f"{'='*80}\n")

    # Group by traditional/modern
    traditional = [p for p in transits['planets'] if p.get('traditional', True)]
    modern = [p for p in transits['planets'] if not p.get('traditional', True)]

    if traditional:
        output.append(f"{'Traditional Planets':^80}")
        output.append(f"{'-'*80}")
        for planet in traditional:
            retro = " R" if planet['retrograde'] else ""
            house_info = f" (Natal House {planet['natal_house']})" if show_natal_houses and 'natal_house' in planet else ""
            output.append(f"{planet['name']:12} {planet['sign']:12} {planet['dms']:>10}{retro:3}{house_info}")

    if modern:
        output.append(f"\n{'Modern Planets':^80}")
        output.append(f"{'-'*80}")
        for planet in modern:
            retro = " R" if planet['retrograde'] else ""
            house_info = f" (Natal House {planet['natal_house']})" if show_natal_houses and 'natal_house' in planet else ""
            output.append(f"{planet['name']:12} {planet['sign']:12} {planet['dms']:>10}{retro:3}{house_info}")

    return "\n".join(output)


def format_transit_aspects(aspects: List[Dict[str, Any]]) -> str:
    """Format transit-to-natal aspects."""
    if not aspects:
        return "\nNo major transit-to-natal aspects within orb.\n"

    output = []
    output.append(f"\n{'Transit-to-Natal Aspects':^80}")
    output.append(f"{'-'*80}")

    for aspect in aspects:
        exact_marker = " *** EXACT ***" if aspect['exact'] else ""
        applying_marker = " (applying)" if aspect['applying'] else " (separating)"
        retro_marker = " [R]" if aspect['transit_retrograde'] else ""

        output.append(
            f"{aspect['transiting_planet']:10} {aspect['aspect_type']:12} "
            f"Natal {aspect['natal_planet']:10} "
            f"(orb {aspect['orb']:.2f}°){applying_marker}{retro_marker}{exact_marker}"
        )

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description='Calculate transits')
    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--date', default='today', help='Date (YYYY-MM-DD or "today")')
    parser.add_argument('--orb', type=float, default=3.0, help='Orb in degrees (default 3°)')
    parser.add_argument('--aspects-only', action='store_true', help='Show only aspects (skip positions)')
    parser.add_argument('--show-natal-houses', action='store_true', help='Show natal house placements')
    parser.add_argument('--traditional-only', action='store_true', help='Traditional planets only (no Uranus/Neptune/Pluto)')
    parser.add_argument('--tight-orbs-only', action='store_true', help='Show only tight orbs (<1°)')
    parser.add_argument('--list-profiles', action='store_true', help='List available profiles')

    args = parser.parse_args()

    if args.list_profiles:
        profiles = list_profiles()
        print(f"Available profiles: {', '.join(profiles)}")
        return

    # Handle "today"
    if args.date == 'today':
        args.date = datetime.now().strftime('%Y-%m-%d')

    try:
        # Calculate transits
        transits = calculate_transiting_positions(args.date, include_modern=not args.traditional_only)

        # Add natal house placements if requested
        if args.show_natal_houses:
            transits = find_transits_in_natal_houses(transits, args.profile)

        # Show positions unless aspects-only
        if not args.aspects_only:
            print(format_transiting_positions(transits, show_natal_houses=args.show_natal_houses))

        # Find and show aspects
        aspects = find_transit_aspects_to_natal(transits, args.profile, orb=args.orb)

        # Filter tight orbs if requested
        if args.tight_orbs_only:
            aspects = [a for a in aspects if a['orb'] < 1.0]

        print(format_transit_aspects(aspects))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
