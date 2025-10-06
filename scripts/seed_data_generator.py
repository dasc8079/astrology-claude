#!/usr/bin/env python3
"""
Seed Data Generator
Generates comprehensive natal chart seed data in YAML format.

Usage:
    python seed_data_generator.py --name "John Doe" --date "1990-01-15" \\
        --time "14:30:00" --location "New York, NY" --lat 40.7128 --lon -74.0060 \\
        --timezone "EST"
"""

import argparse
import swisseph as swe
import yaml
from datetime import datetime
from pathlib import Path
import pytz

# Constants
PLANETS = {
    'Sun': swe.SUN,
    'Moon': swe.MOON,
    'Mercury': swe.MERCURY,
    'Venus': swe.VENUS,
    'Mars': swe.MARS,
    'Jupiter': swe.JUPITER,
    'Saturn': swe.SATURN,
    'Uranus': swe.URANUS,  # Modern
    'Neptune': swe.NEPTUNE,  # Modern
    'Pluto': swe.PLUTO,  # Modern
}

TRADITIONAL_PLANETS = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']
MODERN_PLANETS = ['Uranus', 'Neptune', 'Pluto']

SIGNS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer',
    'Leo', 'Virgo', 'Libra', 'Scorpio',
    'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

PLANET_SYMBOLS = {
    'Sun': '☉',
    'Moon': '☽',
    'Mercury': '☿',
    'Venus': '♀',
    'Mars': '♂',
    'Jupiter': '♃',
    'Saturn': '♄',
    'Uranus': '♅',
    'Neptune': '♆',
    'Pluto': '♇',
}

# Dignity tables
DOMICILE = {
    'Aries': 'Mars', 'Taurus': 'Venus', 'Gemini': 'Mercury',
    'Cancer': 'Moon', 'Leo': 'Sun', 'Virgo': 'Mercury',
    'Libra': 'Venus', 'Scorpio': 'Mars', 'Sagittarius': 'Jupiter',
    'Capricorn': 'Saturn', 'Aquarius': 'Saturn', 'Pisces': 'Jupiter'
}

EXALTATION = {
    'Aries': 'Sun', 'Taurus': 'Moon', 'Cancer': 'Jupiter',
    'Virgo': 'Mercury', 'Libra': 'Saturn', 'Capricorn': 'Mars', 'Pisces': 'Venus'
}

DETRIMENT = {
    'Aries': 'Venus', 'Taurus': 'Mars', 'Gemini': 'Jupiter',
    'Cancer': 'Saturn', 'Leo': 'Saturn', 'Virgo': 'Jupiter',
    'Libra': 'Mars', 'Scorpio': 'Venus', 'Sagittarius': 'Mercury',
    'Capricorn': 'Moon', 'Aquarius': 'Sun', 'Pisces': 'Mercury'
}

FALL = {
    'Aries': 'Saturn', 'Taurus': 'Uranus', 'Cancer': 'Mars',
    'Virgo': 'Venus', 'Libra': 'Sun', 'Capricorn': 'Jupiter', 'Pisces': 'Mercury'
}

# Triplicity rulers (day/night/participating)
TRIPLICITIES = {
    'fire': {'day': 'Sun', 'night': 'Jupiter', 'participating': 'Saturn'},  # Aries, Leo, Sag
    'earth': {'day': 'Venus', 'night': 'Moon', 'participating': 'Mars'},  # Taurus, Virgo, Cap
    'air': {'day': 'Saturn', 'night': 'Mercury', 'participating': 'Jupiter'},  # Gemini, Libra, Aquarius
    'water': {'day': 'Venus', 'night': 'Mars', 'participating': 'Moon'},  # Cancer, Scorpio, Pisces
}

SIGN_TO_ELEMENT = {
    'Aries': 'fire', 'Leo': 'fire', 'Sagittarius': 'fire',
    'Taurus': 'earth', 'Virgo': 'earth', 'Capricorn': 'earth',
    'Gemini': 'air', 'Libra': 'air', 'Aquarius': 'air',
    'Cancer': 'water', 'Scorpio': 'water', 'Pisces': 'water',
}

SIGN_TO_MODALITY = {
    'Aries': 'cardinal', 'Cancer': 'cardinal', 'Libra': 'cardinal', 'Capricorn': 'cardinal',
    'Taurus': 'fixed', 'Leo': 'fixed', 'Scorpio': 'fixed', 'Aquarius': 'fixed',
    'Gemini': 'mutable', 'Virgo': 'mutable', 'Sagittarius': 'mutable', 'Pisces': 'mutable',
}

ASPECTS = {
    'conjunction': 0,
    'sextile': 60,
    'square': 90,
    'trine': 120,
    'opposition': 180,
}

ORB_TOLERANCE = {
    'conjunction': 8,
    'sextile': 6,
    'square': 8,
    'trine': 8,
    'opposition': 8,
}


def decimal_to_dms(decimal_degrees):
    """Convert decimal degrees to degree-minute-second format."""
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = int(((decimal_degrees - degrees) * 60 - minutes) * 60)
    return f"{degrees}°{minutes}'{seconds}\""


def get_sign_and_degree(longitude):
    """Convert ecliptic longitude to sign and degree within sign."""
    sign_num = int(longitude / 30)
    degree = longitude % 30
    return SIGNS[sign_num], degree


def calculate_julian_day(date_str, time_str, timezone_str):
    """Calculate Julian day number from date, time, and timezone."""
    dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")

    # Convert to UTC
    tz = pytz.timezone(timezone_str) if timezone_str not in ['UTC', 'GMT'] else pytz.UTC
    dt_local = tz.localize(dt)
    dt_utc = dt_local.astimezone(pytz.UTC)

    jd = swe.julday(dt_utc.year, dt_utc.month, dt_utc.day,
                     dt_utc.hour + dt_utc.minute/60.0 + dt_utc.second/3600.0)
    return jd, dt_utc


def calculate_planets(jd):
    """Calculate positions of all planets."""
    planet_data = []

    for name, planet_id in PLANETS.items():
        result = swe.calc_ut(jd, planet_id)
        longitude = result[0][0]
        speed = result[0][3]

        sign, degree = get_sign_and_degree(longitude)

        planet_data.append({
            'name': name,
            'symbol': PLANET_SYMBOLS[name],
            'traditional': name in TRADITIONAL_PLANETS,
            'longitude': longitude,
            'sign': sign,
            'degree': degree,
            'dms': decimal_to_dms(degree),
            'speed': speed,
            'retrograde': speed < 0,
        })

    return planet_data


def calculate_houses(jd, lat, lon):
    """Calculate house cusps using whole-sign system."""
    # Get ascendant
    houses = swe.houses(jd, lat, lon, b'W')  # 'W' = whole sign
    asc_longitude = houses[1][0]  # Ascendant
    mc_longitude = houses[1][1]   # MC

    asc_sign, asc_degree = get_sign_and_degree(asc_longitude)
    mc_sign, mc_degree = get_sign_and_degree(mc_longitude)

    # Whole sign houses: each house is a complete sign
    # 1st house = rising sign, then continue in order
    asc_sign_num = SIGNS.index(asc_sign)

    house_data = []
    for i in range(12):
        house_num = i + 1
        sign_num = (asc_sign_num + i) % 12
        sign = SIGNS[sign_num]

        house_data.append({
            'number': house_num,
            'sign': sign,
            'cusp_degree': 0.0,  # Whole sign: always starts at 0°
        })

    return {
        'houses': house_data,
        'ascendant': {
            'sign': asc_sign,
            'degree': asc_degree,
            'dms': decimal_to_dms(asc_degree),
            'longitude': asc_longitude,
        },
        'midheaven': {
            'sign': mc_sign,
            'degree': mc_degree,
            'dms': decimal_to_dms(mc_degree),
            'longitude': mc_longitude,
        },
    }


def determine_sect(planet_data, asc_data):
    """Determine if chart is day or night sect."""
    sun = next(p for p in planet_data if p['name'] == 'Sun')
    sun_longitude = sun['longitude']
    asc_longitude = asc_data['longitude']

    # Calculate if Sun is above horizon
    # Sun above horizon = day chart, below = night chart
    desc_longitude = (asc_longitude + 180) % 360

    if asc_longitude < desc_longitude:
        is_day = asc_longitude < sun_longitude < desc_longitude
    else:
        is_day = not (desc_longitude < sun_longitude < asc_longitude)

    return {
        'type': 'day' if is_day else 'night',
        'determined_by': f"Sun {'above' if is_day else 'below'} horizon"
    }


def calculate_dignities(planet, sect_type):
    """Calculate essential dignities for a planet."""
    sign = planet['sign']
    planet_name = planet['name']

    dignities = {
        'essential': {
            'domicile': DOMICILE.get(sign) == planet_name,
            'exaltation': EXALTATION.get(sign) == planet_name,
            'detriment': DETRIMENT.get(sign) == planet_name,
            'fall': FALL.get(sign) == planet_name,
            'triplicity': None,
            'term': None,  # Egyptian terms would need full table
            'face': None,  # Faces/decans would need full table
        },
        'accidental': {
            'angular': False,  # Will be determined when house is assigned
            'succedent': False,
            'cadent': False,
            'rejoicing': False,
        }
    }

    # Triplicity
    element = SIGN_TO_ELEMENT.get(sign)
    if element:
        trip = TRIPLICITIES[element]
        if trip['day'] == planet_name and sect_type == 'day':
            dignities['essential']['triplicity'] = 'day'
        elif trip['night'] == planet_name and sect_type == 'night':
            dignities['essential']['triplicity'] = 'night'
        elif trip['participating'] == planet_name:
            dignities['essential']['triplicity'] = 'participating'

    return dignities


def assign_planets_to_houses(planet_data, house_data):
    """Assign each planet to its house based on whole-sign system."""
    for planet in planet_data:
        planet_sign = planet['sign']
        for house in house_data:
            if house['sign'] == planet_sign:
                planet['house'] = house['number']
                break

    return planet_data


def calculate_aspects(planet_data):
    """Calculate aspects between planets."""
    aspects = []

    for i, p1 in enumerate(planet_data):
        for p2 in planet_data[i+1:]:
            lon1 = p1['longitude']
            lon2 = p2['longitude']

            # Calculate angular separation
            diff = abs(lon1 - lon2)
            if diff > 180:
                diff = 360 - diff

            # Check for aspects
            for aspect_name, aspect_angle in ASPECTS.items():
                orb = abs(diff - aspect_angle)
                if orb <= ORB_TOLERANCE[aspect_name]:
                    # Determine if applying or separating
                    applying = p1['speed'] > p2['speed'] if aspect_angle != 0 else False

                    aspects.append({
                        'aspect_type': aspect_name,
                        'orb': round(orb, 2),
                        'planet_1': p1['name'],
                        'planet_2': p2['name'],
                        'applying': applying,
                        'traditional': p1['traditional'] and p2['traditional'],
                        'interpretation_notes': {
                            'nature': 'harmonious' if aspect_name in ['sextile', 'trine'] else 'challenging' if aspect_name in ['square', 'opposition'] else 'neutral',
                            'strength': 'strong' if orb < 3 else 'moderate' if orb < 6 else 'weak',
                        }
                    })

    return aspects


def calculate_lots(jd, asc_longitude, planet_data, sect_type):
    """Calculate Hermetic lots (Fortune and Spirit)."""
    sun = next(p for p in planet_data if p['name'] == 'Sun')
    moon = next(p for p in planet_data if p['name'] == 'Moon')

    sun_lon = sun['longitude']
    moon_lon = moon['longitude']

    # Lot of Fortune
    # Day: ASC + Moon - Sun
    # Night: ASC + Sun - Moon
    if sect_type == 'day':
        fortune_lon = (asc_longitude + moon_lon - sun_lon) % 360
    else:
        fortune_lon = (asc_longitude + sun_lon - moon_lon) % 360

    fortune_sign, fortune_degree = get_sign_and_degree(fortune_lon)

    # Lot of Spirit (opposite calculation)
    # Day: ASC + Sun - Moon
    # Night: ASC + Moon - Sun
    if sect_type == 'day':
        spirit_lon = (asc_longitude + sun_lon - moon_lon) % 360
    else:
        spirit_lon = (asc_longitude + moon_lon - sun_lon) % 360

    spirit_sign, spirit_degree = get_sign_and_degree(spirit_lon)

    return [
        {
            'name': 'Lot of Fortune',
            'symbol': '⊗',
            'position': {
                'sign': fortune_sign,
                'degree': round(fortune_degree, 4),
                'dms': decimal_to_dms(fortune_degree),
            },
            'calculation': {
                'formula': 'ASC + Moon - Sun (day) / ASC + Sun - Moon (night)',
                'day_formula': 'ASC + Moon - Sun',
                'night_formula': 'ASC + Sun - Moon',
            }
        },
        {
            'name': 'Lot of Spirit',
            'symbol': '⊙',
            'position': {
                'sign': spirit_sign,
                'degree': round(spirit_degree, 4),
                'dms': decimal_to_dms(spirit_degree),
            },
            'calculation': {
                'formula': 'ASC + Sun - Moon (day) / ASC + Moon - Sun (night)',
                'day_formula': 'ASC + Sun - Moon',
                'night_formula': 'ASC + Moon - Sun',
            }
        }
    ]


def calculate_nodes(jd):
    """Calculate lunar nodes."""
    result = swe.calc_ut(jd, swe.TRUE_NODE)
    north_lon = result[0][0]
    south_lon = (north_lon + 180) % 360

    north_sign, north_degree = get_sign_and_degree(north_lon)
    south_sign, south_degree = get_sign_and_degree(south_lon)

    return {
        'north_node': {
            'sign': north_sign,
            'degree': round(north_degree, 4),
            'dms': decimal_to_dms(north_degree),
        },
        'south_node': {
            'sign': south_sign,
            'degree': round(south_degree, 4),
            'dms': decimal_to_dms(south_degree),
        }
    }


def calculate_elemental_balance(planet_data):
    """Calculate elemental and modality balance."""
    elements = {'fire': 0, 'earth': 0, 'air': 0, 'water': 0}
    modalities = {'cardinal': 0, 'fixed': 0, 'mutable': 0}

    # Count traditional planets only
    for planet in planet_data:
        if planet['traditional']:
            sign = planet['sign']
            elements[SIGN_TO_ELEMENT[sign]] += 1
            modalities[SIGN_TO_MODALITY[sign]] += 1

    return elements, modalities


def generate_seed_data(args):
    """Main function to generate complete seed data."""
    # Initialize Swiss Ephemeris
    swe.set_ephe_path(None)  # Use default ephemeris

    # Calculate Julian day
    jd, dt_utc = calculate_julian_day(args.date, args.time, args.timezone)

    # Calculate chart components
    planet_data = calculate_planets(jd)
    house_info = calculate_houses(jd, args.lat, args.lon)
    sect = determine_sect(planet_data, house_info['ascendant'])

    # Assign planets to houses
    planet_data = assign_planets_to_houses(planet_data, house_info['houses'])

    # Calculate dignities for each planet
    for planet in planet_data:
        planet['dignities'] = calculate_dignities(planet, sect['type'])

        # Update accidental dignities based on house
        house_num = planet['house']
        if house_num in [1, 4, 7, 10]:
            planet['dignities']['accidental']['angular'] = True
        elif house_num in [2, 5, 8, 11]:
            planet['dignities']['accidental']['succedent'] = True
        else:
            planet['dignities']['accidental']['cadent'] = True

    # Calculate aspects
    aspects = calculate_aspects(planet_data)

    # Calculate lots
    lots = calculate_lots(jd, house_info['ascendant']['longitude'], planet_data, sect['type'])

    # Calculate nodes
    nodes = calculate_nodes(jd)

    # Calculate elemental balance
    elements, modalities = calculate_elemental_balance(planet_data)

    # Assemble complete seed data
    seed_data = {
        'metadata': {
            'profile_name': args.name,
            'generated_at': datetime.now().isoformat(),
            'schema_version': '1.0',
        },
        'birth_data': {
            'date': args.date,
            'time': args.time,
            'location': args.location,
            'latitude': args.lat,
            'longitude': args.lon,
            'timezone': args.timezone,
            'utc_offset': dt_utc.strftime('%z'),
        },
        'chart_framework': {
            'house_system': 'whole_sign',
            'ayanamsa': 'tropical',
            'sect': sect,
            'ascendant': house_info['ascendant'],
            'midheaven': house_info['midheaven'],
        },
        'planets': planet_data,
        'houses': house_info['houses'],
        'aspects': aspects,
        'lots': lots,
        'lunar_nodes': nodes,
        'elemental_balance': elements,
        'modality_balance': modalities,
    }

    return seed_data


def main():
    parser = argparse.ArgumentParser(description='Generate natal chart seed data')
    parser.add_argument('--name', required=True, help='Profile name')
    parser.add_argument('--date', required=True, help='Birth date (YYYY-MM-DD)')
    parser.add_argument('--time', required=True, help='Birth time (HH:MM:SS)')
    parser.add_argument('--location', required=True, help='Birth location')
    parser.add_argument('--lat', type=float, required=True, help='Latitude (decimal)')
    parser.add_argument('--lon', type=float, required=True, help='Longitude (decimal)')
    parser.add_argument('--timezone', required=True, help='Timezone (e.g., America/New_York)')
    parser.add_argument('--output', help='Output file path (default: profiles/<name>/seed_data/master_seed_data.yaml)')

    args = parser.parse_args()

    # Generate seed data
    seed_data = generate_seed_data(args)

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path(f'profiles/{args.name}/seed_data/master_seed_data.yaml')

    # Create directories if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write to YAML
    with open(output_path, 'w') as f:
        yaml.dump(seed_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"✅ Seed data generated: {output_path}")
    print(f"   Profile: {args.name}")
    print(f"   Sect: {seed_data['chart_framework']['sect']['type']}")
    print(f"   Ascendant: {seed_data['chart_framework']['ascendant']['sign']}")
    print(f"   Planets: {len([p for p in seed_data['planets'] if p['traditional']])} traditional + {len([p for p in seed_data['planets'] if not p['traditional']])} modern")


if __name__ == '__main__':
    main()
