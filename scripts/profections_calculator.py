#!/usr/bin/env python3
"""
Annual Profections Calculator
Traditional Hellenistic timing technique for determining the activated house each year.

Profections cycle through the 12 houses, activating one house per year of life.
The ruler of the profected sign becomes the "Lord of the Year" - the time-lord
for that year.

Formula:
    Profected House = (Age mod 12) + 1
    Starting from natal Ascendant sign

Usage:
    python profections_calculator.py --profile darren --age 35
    python profections_calculator.py --profile darren --age-range 30-40
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from profile_loader import load_profile, list_profiles

# Sign order (zodiacal)
SIGNS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer',
    'Leo', 'Virgo', 'Libra', 'Scorpio',
    'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

# Domicile rulers (for Lord of Year)
DOMICILE = {
    'Aries': 'Mars', 'Taurus': 'Venus', 'Gemini': 'Mercury',
    'Cancer': 'Moon', 'Leo': 'Sun', 'Virgo': 'Mercury',
    'Libra': 'Venus', 'Scorpio': 'Mars', 'Sagittarius': 'Jupiter',
    'Capricorn': 'Saturn', 'Aquarius': 'Saturn', 'Pisces': 'Jupiter'
}


def calculate_profection(natal_ascendant_sign: str, age: int) -> Dict[str, Any]:
    """
    Calculate annual profection for a given age.

    Args:
        natal_ascendant_sign: The natal Ascendant sign
        age: Age in years (0 = birth to 1st birthday)

    Returns:
        Dictionary with profection details:
        - profected_house: House number (1-12)
        - profected_sign: Zodiac sign of profected house
        - lord_of_year: Ruling planet of profected sign
        - age: The age being calculated
    """
    # Calculate which house is profected
    profected_house = (age % 12) + 1

    # Calculate which sign is profected
    # Start from natal Ascendant and count forward
    ascendant_index = SIGNS.index(natal_ascendant_sign)
    profected_sign_index = (ascendant_index + (age % 12)) % 12
    profected_sign = SIGNS[profected_sign_index]

    # Determine Lord of the Year
    lord_of_year = DOMICILE[profected_sign]

    return {
        'age': age,
        'profected_house': profected_house,
        'profected_sign': profected_sign,
        'lord_of_year': lord_of_year,
    }


def calculate_profection_with_natal(profile_name: str, age: int) -> Dict[str, Any]:
    """
    Calculate profection with full natal chart context.

    Args:
        profile_name: Profile to load
        age: Age in years

    Returns:
        Dictionary with profection and natal context:
        - profection: Basic profection data
        - natal_ascendant: Natal Ascendant details
        - lord_natal_position: Where the Lord of Year is in natal chart
        - profected_house_natal: What's in the profected house natally
    """
    # Load profile
    profile = load_profile(profile_name)

    # Get natal chart data
    framework = profile.get_chart_framework()
    if not framework:
        raise ValueError(f"No seed data found for profile '{profile_name}'")

    natal_ascendant_sign = framework['ascendant']['sign']
    natal_ascendant_degree = framework['ascendant']['degree']

    # Calculate basic profection
    profection = calculate_profection(natal_ascendant_sign, age)

    # Get natal houses and planets
    houses = profile.get_houses()
    planets = profile.get_planets(traditional_only=True)

    # Find Lord of Year in natal chart
    lord_planet = next((p for p in planets if p['name'] == profection['lord_of_year']), None)

    if lord_planet:
        lord_natal_position = {
            'planet': lord_planet['name'],
            'sign': lord_planet['sign'],
            'house': lord_planet['house'],
            'degree': round(lord_planet['degree'], 2),
            'retrograde': lord_planet['retrograde'],
            'dignities': lord_planet['dignities']['essential'],
        }
    else:
        lord_natal_position = None

    # Get profected house details from natal chart
    profected_house_number = profection['profected_house']
    profected_house_natal = next((h for h in houses if h['number'] == profected_house_number), None)

    # Find what planets are in the profected house natally
    planets_in_profected_house = []
    if profected_house_natal:
        planets_in_profected_house = profected_house_natal.get('planets_in_house', [])

    return {
        'profile': profile_name,
        'profection': profection,
        'natal_ascendant': {
            'sign': natal_ascendant_sign,
            'degree': round(natal_ascendant_degree, 2),
        },
        'lord_natal_position': lord_natal_position,
        'profected_house_natal': {
            'number': profected_house_number,
            'sign': profection['profected_sign'],
            'planets': planets_in_profected_house,
        }
    }


def calculate_profection_range(profile_name: str, start_age: int, end_age: int) -> List[Dict[str, Any]]:
    """
    Calculate profections for a range of ages.

    Args:
        profile_name: Profile to load
        start_age: Starting age (inclusive)
        end_age: Ending age (inclusive)

    Returns:
        List of profection dictionaries
    """
    profections = []
    for age in range(start_age, end_age + 1):
        profection_data = calculate_profection_with_natal(profile_name, age)
        profections.append(profection_data)
    return profections


def format_profection_output(profection_data: Dict[str, Any]) -> str:
    """Format profection data for terminal output."""
    prof = profection_data['profection']
    lord = profection_data['lord_natal_position']
    natal_house = profection_data['profected_house_natal']

    output = []
    output.append(f"{'='*60}")
    output.append(f"PROFECTION FOR AGE {prof['age']}")
    output.append(f"{'='*60}")
    output.append(f"")
    output.append(f"Profected House:  {prof['profected_house']} ({prof['profected_sign']})")
    output.append(f"Lord of Year:     {prof['lord_of_year']}")
    output.append(f"")

    if lord:
        output.append(f"Lord of Year Natal Position:")
        output.append(f"  Location:       {lord['sign']} (House {lord['house']})")
        output.append(f"  Degree:         {lord['degree']}°")
        output.append(f"  Retrograde:     {lord['retrograde']}")

        # Format dignities
        dignities = []
        if lord['dignities']['domicile']:
            dignities.append('domicile')
        if lord['dignities']['exaltation']:
            dignities.append('exaltation')
        if lord['dignities']['detriment']:
            dignities.append('detriment')
        if lord['dignities']['fall']:
            dignities.append('fall')
        if lord['dignities']['triplicity']:
            dignities.append(f"triplicity ({lord['dignities']['triplicity']})")

        dignity_str = ', '.join(dignities) if dignities else 'peregrine'
        output.append(f"  Dignities:      {dignity_str}")

    output.append(f"")
    output.append(f"Profected House (Natal):")

    if natal_house['planets']:
        output.append(f"  Planets:        {', '.join([p['name'] for p in natal_house['planets']])}")
    else:
        output.append(f"  Planets:        None")

    output.append(f"")
    output.append(f"Interpretation:")
    output.append(f"  This year activates the {prof['profected_house']} house ({prof['profected_sign']}).")
    output.append(f"  {prof['lord_of_year']} becomes the time-lord, showing primary themes.")

    if lord:
        output.append(f"  {prof['lord_of_year']} in natal {lord['sign']} (house {lord['house']}) indicates")
        output.append(f"  where this year's energy flows and what topics are emphasized.")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description='Calculate annual profections')
    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--age', type=int, help='Single age to calculate')
    parser.add_argument('--age-range', help='Age range (e.g., "30-40")')
    parser.add_argument('--list-profiles', action='store_true', help='List available profiles')

    args = parser.parse_args()

    if args.list_profiles:
        profiles = list_profiles()
        print(f"Available profiles: {', '.join(profiles)}")
        return

    if not args.age and not args.age_range:
        parser.error("Either --age or --age-range is required")

    # Single age calculation
    if args.age:
        try:
            profection_data = calculate_profection_with_natal(args.profile, args.age)
            print(format_profection_output(profection_data))
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    # Age range calculation
    elif args.age_range:
        try:
            start_age, end_age = map(int, args.age_range.split('-'))
            profections = calculate_profection_range(args.profile, start_age, end_age)

            for prof_data in profections:
                print(format_profection_output(prof_data))
                print()  # Blank line between ages

        except ValueError:
            print(f"Error: Invalid age range format. Use 'START-END' (e.g., '30-40')", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
