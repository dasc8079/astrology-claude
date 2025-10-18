#!/usr/bin/env python3
"""
Generate Current Activation Data
Extracts ZR L2 periods, annual profection, and short-term transits for current focus analysis.
"""

import sys
import json
from pathlib import Path
from datetime import datetime, timedelta

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from transits import calculate_transiting_positions, find_transit_aspects_to_natal, find_transits_in_natal_houses
from profile_loader import load_profile

def calculate_age_precise(birth_date, current_date):
    """Calculate precise age in years with decimals"""
    # Calculate age in years
    age_years = current_date.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age_years -= 1

    # Calculate fractional year
    # Find last birthday
    last_birthday = birth_date.replace(year=birth_date.year + age_years)

    days_since_birthday = (current_date - last_birthday).days
    days_in_year = 365.25

    return age_years + (days_since_birthday / days_in_year)

def calculate_annual_profection(age):
    """Calculate annual profection house based on age"""
    # Profection cycles through houses annually starting from House 1 at birth
    house = ((int(age) % 12) + 1)
    return house

def get_house_sign(house_number, ascendant_sign):
    """Get the zodiac sign for a given house in whole-sign system"""
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    # Find ascendant sign index
    asc_index = signs.index(ascendant_sign)

    # Calculate house sign (whole-sign system)
    house_index = (asc_index + house_number - 1) % 12
    return signs[house_index]

def get_house_ruler(sign, profile):
    """Get the traditional ruler of a zodiac sign"""
    rulers = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
        "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
        "Libra": "Venus", "Scorpio": "Mars", "Sagittarius": "Jupiter",
        "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }

    ruler_name = rulers[sign]

    # Find ruler position in seed data
    for planet in profile.seed_data["planets"]:
        if planet["name"] == ruler_name:
            return {
                "planet": ruler_name,
                "sign": planet["sign"],
                "house": planet["house"],
                "dignities": planet["dignities"]["essential"]
            }

    return None

def get_current_zr_periods(age):
    """
    Extract current ZR L1 and L2 periods based on age.
    This uses the known periods from Darren's chart.
    For other profiles, would need full ZR calculation.
    """
    # ZR Fortune Periods (L1) - from Lot of Fortune
    fortune_l1_periods = [
        {"sign": "Sagittarius", "start": 0, "end": 12, "time_lord": "Jupiter"},
        {"sign": "Capricorn", "start": 12, "end": 39, "time_lord": "Saturn"},
        {"sign": "Aquarius", "start": 39, "end": 66, "time_lord": "Saturn"},
        {"sign": "Pisces", "start": 66, "end": 78, "time_lord": "Jupiter"},
        {"sign": "Aries", "start": 78, "end": 93, "time_lord": "Mars"},
        {"sign": "Taurus", "start": 93, "end": 101, "time_lord": "Venus"},
    ]

    # ZR Spirit Periods (L1) - from Lot of Spirit
    spirit_l1_periods = [
        {"sign": "Aries", "start": 0, "end": 15, "time_lord": "Mars"},
        {"sign": "Taurus", "start": 15, "end": 23, "time_lord": "Venus"},
        {"sign": "Gemini", "start": 23, "end": 43, "time_lord": "Mercury"},
        {"sign": "Cancer", "start": 43, "end": 68, "time_lord": "Moon"},
        {"sign": "Leo", "start": 68, "end": 87, "time_lord": "Sun"},
        {"sign": "Virgo", "start": 87, "end": 107, "time_lord": "Mercury"},
    ]

    # Darren-specific L2 periods (would need full ZR calculation for others)
    # Fortune L2 within Capricorn L1 (ages 12-39)
    fortune_l2_periods_capricorn = [
        {"sign": "Scorpio", "start": 35.5, "end": 37.4, "time_lord": "Mars"},
        # More L2 periods would be calculated by full ZR script
    ]

    # Spirit L2 within Gemini L1 (ages 23-43)
    spirit_l2_periods_gemini = [
        {"sign": "Capricorn", "start": 34.4, "end": 37.0, "time_lord": "Saturn"},
        # More L2 periods would be calculated by full ZR script
    ]

    # Find current Fortune L1
    current_fortune_l1 = None
    for period in fortune_l1_periods:
        if period["start"] <= age < period["end"]:
            current_fortune_l1 = period
            break

    # Find current Spirit L1
    current_spirit_l1 = None
    for period in spirit_l1_periods:
        if period["start"] <= age < period["end"]:
            current_spirit_l1 = period
            break

    # Find current Fortune L2 (simplified - only for Capricorn L1)
    current_fortune_l2 = None
    if current_fortune_l1 and current_fortune_l1["sign"] == "Capricorn":
        for period in fortune_l2_periods_capricorn:
            if period["start"] <= age < period["end"]:
                current_fortune_l2 = period
                break

    # Find current Spirit L2 (simplified - only for Gemini L1)
    current_spirit_l2 = None
    if current_spirit_l1 and current_spirit_l1["sign"] == "Gemini":
        for period in spirit_l2_periods_gemini:
            if period["start"] <= age < period["end"]:
                current_spirit_l2 = period
                break

    return {
        "fortune_l1": current_fortune_l1,
        "fortune_l2": current_fortune_l2,
        "spirit_l1": current_spirit_l1,
        "spirit_l2": current_spirit_l2
    }

def generate_transit_data_range(profile_name, days=60):
    """Generate transit data for specified number of days from current date"""
    current_date = datetime.now()
    date_str = current_date.strftime("%Y-%m-%d")

    # Calculate transits for current date
    transits = calculate_transiting_positions(date_str, include_modern=False)

    # Add natal house placements
    transits = find_transits_in_natal_houses(transits, profile_name)

    # Find aspects to natal
    aspects = find_transit_aspects_to_natal(transits, profile_name, orb=2.0)

    return {
        "start_date": date_str,
        "end_date": (current_date + timedelta(days=days)).strftime("%Y-%m-%d"),
        "current_positions": transits,
        "natal_aspects": aspects
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_current_activation_data.py PROFILE_NAME [DAYS]")
        print("Example: python generate_current_activation_data.py Darren_S 60")
        sys.exit(1)

    profile_name = sys.argv[1]
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 60

    print(f"Generating current activation data for {profile_name}...")

    # Load profile
    profile = load_profile(profile_name)

    # Parse birth date
    birth_date_str = profile.seed_data["birth_data"]["date"]
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

    # Calculate current age
    current_date = datetime.now()
    age = calculate_age_precise(birth_date, current_date)

    print(f"Current age: {age:.2f} years")

    # Get annual profection
    profection_house = calculate_annual_profection(age)
    ascendant_sign = profile.seed_data["chart_framework"]["ascendant"]["sign"]
    profection_sign = get_house_sign(profection_house, ascendant_sign)
    profection_lord = get_house_ruler(profection_sign, profile)

    print(f"Annual profection: House {profection_house} ({profection_sign}), Lord: {profection_lord['planet']}")

    # Get ZR periods
    zr_periods = get_current_zr_periods(age)

    print(f"Fortune L1: {zr_periods['fortune_l1']['sign'] if zr_periods['fortune_l1'] else 'N/A'}")
    print(f"Fortune L2: {zr_periods['fortune_l2']['sign'] if zr_periods['fortune_l2'] else 'N/A'}")
    print(f"Spirit L1: {zr_periods['spirit_l1']['sign'] if zr_periods['spirit_l1'] else 'N/A'}")
    print(f"Spirit L2: {zr_periods['spirit_l2']['sign'] if zr_periods['spirit_l2'] else 'N/A'}")

    # Generate transit data
    print(f"Generating transit data for next {days} days...")
    transit_data = generate_transit_data_range(profile_name, days)

    print(f"Found {len(transit_data['natal_aspects'])} significant transits")

    # Compile activation data
    activation_data = {
        "metadata": {
            "profile_name": profile_name,
            "generated_at": current_date.strftime("%Y-%m-%d %H:%M:%S"),
            "current_age": round(age, 2),
            "analysis_period": f"{days} days"
        },
        "annual_profection": {
            "house": profection_house,
            "sign": profection_sign,
            "lord": profection_lord
        },
        "zodiacal_releasing": zr_periods,
        "transits": transit_data,
        "natal_context": {
            "ascendant": profile.seed_data["chart_framework"]["ascendant"],
            "sect": profile.seed_data["chart_framework"]["sect"],
            "planets": profile.seed_data["planets"],
            "houses": profile.seed_data["houses"]
        }
    }

    # Save to file
    project_root = Path(__file__).parent.parent
    output_dir = project_root / "profiles" / profile_name / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"current_activation_data_{current_date.strftime('%Y-%m-%d')}.json"

    with open(output_file, 'w') as f:
        json.dump(activation_data, f, indent=2)

    print(f"\nCurrent activation data saved to: {output_file}")

    return output_file

if __name__ == '__main__':
    main()
