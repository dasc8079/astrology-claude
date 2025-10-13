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

# Egyptian Terms (Bounds) - degree ranges within each sign
EGYPTIAN_TERMS = {
    'Aries': [(0, 6, 'Jupiter'), (6, 12, 'Venus'), (12, 20, 'Mercury'), (20, 25, 'Mars'), (25, 30, 'Saturn')],
    'Taurus': [(0, 8, 'Venus'), (8, 14, 'Mercury'), (14, 22, 'Jupiter'), (22, 27, 'Saturn'), (27, 30, 'Mars')],
    'Gemini': [(0, 6, 'Mercury'), (6, 12, 'Jupiter'), (12, 17, 'Venus'), (17, 24, 'Mars'), (24, 30, 'Saturn')],
    'Cancer': [(0, 7, 'Mars'), (7, 13, 'Venus'), (13, 19, 'Mercury'), (19, 26, 'Jupiter'), (26, 30, 'Saturn')],
    'Leo': [(0, 6, 'Jupiter'), (6, 11, 'Venus'), (11, 18, 'Saturn'), (18, 24, 'Mercury'), (24, 30, 'Mars')],
    'Virgo': [(0, 7, 'Mercury'), (7, 17, 'Venus'), (17, 21, 'Jupiter'), (21, 28, 'Mars'), (28, 30, 'Saturn')],
    'Libra': [(0, 6, 'Saturn'), (6, 14, 'Mercury'), (14, 21, 'Jupiter'), (21, 28, 'Venus'), (28, 30, 'Mars')],
    'Scorpio': [(0, 7, 'Mars'), (7, 11, 'Venus'), (11, 19, 'Mercury'), (19, 24, 'Jupiter'), (24, 30, 'Saturn')],
    'Sagittarius': [(0, 12, 'Jupiter'), (12, 17, 'Venus'), (17, 21, 'Mercury'), (21, 26, 'Saturn'), (26, 30, 'Mars')],
    'Capricorn': [(0, 7, 'Mercury'), (7, 14, 'Jupiter'), (14, 22, 'Venus'), (22, 26, 'Saturn'), (26, 30, 'Mars')],
    'Aquarius': [(0, 7, 'Mercury'), (7, 13, 'Venus'), (13, 20, 'Jupiter'), (20, 25, 'Mars'), (25, 30, 'Saturn')],
    'Pisces': [(0, 12, 'Venus'), (12, 16, 'Jupiter'), (16, 19, 'Mercury'), (19, 28, 'Mars'), (28, 30, 'Saturn')],
}

# Decans/Faces - each 10° division ruled by a planet
DECANS = {
    'Aries': [(0, 10, 'Mars'), (10, 20, 'Sun'), (20, 30, 'Venus')],
    'Taurus': [(0, 10, 'Mercury'), (10, 20, 'Moon'), (20, 30, 'Saturn')],
    'Gemini': [(0, 10, 'Jupiter'), (10, 20, 'Mars'), (20, 30, 'Sun')],
    'Cancer': [(0, 10, 'Venus'), (10, 20, 'Mercury'), (20, 30, 'Moon')],
    'Leo': [(0, 10, 'Saturn'), (10, 20, 'Jupiter'), (20, 30, 'Mars')],
    'Virgo': [(0, 10, 'Sun'), (10, 20, 'Venus'), (20, 30, 'Mercury')],
    'Libra': [(0, 10, 'Moon'), (10, 20, 'Saturn'), (20, 30, 'Jupiter')],
    'Scorpio': [(0, 10, 'Mars'), (10, 20, 'Sun'), (20, 30, 'Venus')],
    'Sagittarius': [(0, 10, 'Mercury'), (10, 20, 'Moon'), (20, 30, 'Saturn')],
    'Capricorn': [(0, 10, 'Jupiter'), (10, 20, 'Mars'), (20, 30, 'Sun')],
    'Aquarius': [(0, 10, 'Venus'), (10, 20, 'Mercury'), (20, 30, 'Moon')],
    'Pisces': [(0, 10, 'Saturn'), (10, 20, 'Jupiter'), (20, 30, 'Mars')],
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


def determine_sect(planet_data, asc_data, jd, latitude, longitude):
    """
    Determine if chart is day or night sect.

    Uses Sun's altitude: above horizon = day, below horizon = night.
    """
    sun = next(p for p in planet_data if p['name'] == 'Sun')

    # Calculate Sun's altitude (angle above/below horizon)
    # azalt returns (azimuth, true_altitude, apparent_altitude)
    geopos = (longitude, latitude, 0)  # longitude, latitude, altitude in meters
    azalt_result = swe.azalt(jd, swe.ECL2HOR, geopos, 0, 0, [sun['longitude'], 0, 1.0])

    # true_altitude is index 1
    # Positive = above horizon (day), Negative = below horizon (night)
    sun_altitude = azalt_result[1]

    is_day = sun_altitude > 0

    return {
        'type': 'day' if is_day else 'night',
        'determined_by': f"Sun {'above' if is_day else 'below'} horizon (altitude: {sun_altitude:.2f}°)"
    }


def calculate_dignities(planet, sect_type):
    """Calculate essential dignities for a planet."""
    sign = planet['sign']
    planet_name = planet['name']
    degree = planet['degree']

    dignities = {
        'essential': {
            'domicile': DOMICILE.get(sign) == planet_name,
            'exaltation': EXALTATION.get(sign) == planet_name,
            'detriment': DETRIMENT.get(sign) == planet_name,
            'fall': FALL.get(sign) == planet_name,
            'triplicity': None,
            'term': None,
            'face': None,
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

    # Egyptian Terms (Bounds)
    if sign in EGYPTIAN_TERMS:
        for start, end, ruler in EGYPTIAN_TERMS[sign]:
            if start <= degree < end:
                dignities['essential']['term'] = ruler
                break

    # Decans (Faces)
    if sign in DECANS:
        for start, end, ruler in DECANS[sign]:
            if start <= degree < end:
                dignities['essential']['face'] = ruler
                break

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


def calculate_house_rulers(house_data, planet_data):
    """Calculate ruler for each house and track its position."""
    for house in house_data:
        house_sign = house['sign']
        ruler_name = DOMICILE.get(house_sign)

        if ruler_name:
            # Find the ruling planet's position
            ruler_planet = next((p for p in planet_data if p['name'] == ruler_name), None)

            if ruler_planet:
                # Get essential dignity summary for the ruler
                dignities = ruler_planet.get('dignities', {}).get('essential', {})
                dignity_summary = []

                if dignities.get('domicile'):
                    dignity_summary.append('domicile')
                if dignities.get('exaltation'):
                    dignity_summary.append('exaltation')
                if dignities.get('detriment'):
                    dignity_summary.append('detriment')
                if dignities.get('fall'):
                    dignity_summary.append('fall')
                if dignities.get('triplicity'):
                    dignity_summary.append(f"triplicity ({dignities['triplicity']})")

                dignity_str = ', '.join(dignity_summary) if dignity_summary else 'peregrine'

                house['ruler'] = {
                    'planet': ruler_name,
                    'position': {
                        'sign': ruler_planet['sign'],
                        'house': ruler_planet['house'],
                        'dignities': dignity_str,
                    }
                }

                # List planets in this house
                planets_in_house = [
                    {'name': p['name'], 'degree': round(p['degree'], 2)}
                    for p in planet_data
                    if p['house'] == house['number'] and p['traditional']  # Only traditional planets
                ]
                house['planets_in_house'] = planets_in_house

    return house_data


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


def calculate_angle_aspects(planet_data, asc_longitude, mc_longitude):
    """Calculate aspects from planets to chart angles (ASC, MC, DSC, IC)."""
    angle_aspects = []

    # Define angles
    angles = {
        'Ascendant': asc_longitude,
        'Midheaven': mc_longitude,
        'Descendant': (asc_longitude + 180) % 360,
        'IC': (mc_longitude + 180) % 360,
    }

    # Check each planet for aspects to each angle
    for planet in planet_data:
        planet_lon = planet['longitude']

        for angle_name, angle_lon in angles.items():
            # Calculate angular separation
            diff = abs(planet_lon - angle_lon)
            if diff > 180:
                diff = 360 - diff

            # Check for aspects (using classical aspects only)
            for aspect_name, aspect_angle in ASPECTS.items():
                orb = abs(diff - aspect_angle)
                if orb <= ORB_TOLERANCE[aspect_name]:
                    angle_aspects.append({
                        'planet': planet['name'],
                        'angle': angle_name,
                        'aspect_type': aspect_name,
                        'orb': round(orb, 2),
                        'traditional': planet['traditional'],
                        'interpretation_notes': {
                            'nature': 'harmonious' if aspect_name in ['sextile', 'trine'] else 'challenging' if aspect_name in ['square', 'opposition'] else 'neutral',
                            'strength': 'strong' if orb < 3 else 'moderate' if orb < 6 else 'weak',
                            'significance': 'high' if angle_name in ['Ascendant', 'Midheaven'] else 'moderate',
                        }
                    })

    return angle_aspects


def calculate_lots(jd, asc_longitude, planet_data, sect_type):
    """Calculate Hermetic lots (Fortune, Spirit, and 5 additional lots)."""
    sun = next(p for p in planet_data if p['name'] == 'Sun')
    moon = next(p for p in planet_data if p['name'] == 'Moon')
    mercury = next(p for p in planet_data if p['name'] == 'Mercury')
    venus = next(p for p in planet_data if p['name'] == 'Venus')
    mars = next(p for p in planet_data if p['name'] == 'Mars')
    jupiter = next(p for p in planet_data if p['name'] == 'Jupiter')
    saturn = next(p for p in planet_data if p['name'] == 'Saturn')

    sun_lon = sun['longitude']
    moon_lon = moon['longitude']
    mercury_lon = mercury['longitude']
    venus_lon = venus['longitude']
    mars_lon = mars['longitude']
    jupiter_lon = jupiter['longitude']
    saturn_lon = saturn['longitude']

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

    # Lot of Eros (desires, love, passionate attachment)
    # Day: ASC + Venus - Spirit
    # Night: ASC + Spirit - Venus
    if sect_type == 'day':
        eros_lon = (asc_longitude + venus_lon - spirit_lon) % 360
    else:
        eros_lon = (asc_longitude + spirit_lon - venus_lon) % 360

    eros_sign, eros_degree = get_sign_and_degree(eros_lon)

    # Lot of Necessity (fate, constraint, compulsion)
    # Day: ASC + Fortune - Mercury
    # Night: ASC + Mercury - Fortune
    if sect_type == 'day':
        necessity_lon = (asc_longitude + fortune_lon - mercury_lon) % 360
    else:
        necessity_lon = (asc_longitude + mercury_lon - fortune_lon) % 360

    necessity_sign, necessity_degree = get_sign_and_degree(necessity_lon)

    # Lot of Courage (Mars activity, bravery, assertion)
    # Day: ASC + Fortune - Mars
    # Night: ASC + Mars - Fortune
    if sect_type == 'day':
        courage_lon = (asc_longitude + fortune_lon - mars_lon) % 360
    else:
        courage_lon = (asc_longitude + mars_lon - fortune_lon) % 360

    courage_sign, courage_degree = get_sign_and_degree(courage_lon)

    # Lot of Victory (Jupiter success, expansion, recognition)
    # Day: ASC + Spirit - Jupiter
    # Night: ASC + Jupiter - Spirit
    if sect_type == 'day':
        victory_lon = (asc_longitude + spirit_lon - jupiter_lon) % 360
    else:
        victory_lon = (asc_longitude + jupiter_lon - spirit_lon) % 360

    victory_sign, victory_degree = get_sign_and_degree(victory_lon)

    # Lot of Basis/Foundation (Saturn structure, foundation, stability)
    # Day: ASC + Fortune - Saturn
    # Night: ASC + Saturn - Fortune
    if sect_type == 'day':
        basis_lon = (asc_longitude + fortune_lon - saturn_lon) % 360
    else:
        basis_lon = (asc_longitude + saturn_lon - fortune_lon) % 360

    basis_sign, basis_degree = get_sign_and_degree(basis_lon)

    # Lot of Exaltation (career peak, honors, public recognition)
    # Same formula for day and night charts
    exaltation_lon = (asc_longitude + mars_lon - sun_lon) % 360
    exaltation_sign, exaltation_degree = get_sign_and_degree(exaltation_lon)

    # Lot of Marriage (partnership, committed relationships)
    # Same formula for day and night charts
    marriage_lon = (asc_longitude + venus_lon - saturn_lon) % 360
    marriage_sign, marriage_degree = get_sign_and_degree(marriage_lon)

    # Lot of Children (offspring, generativity, legacy)
    # Day (masculine): ASC + Jupiter - Saturn
    # Night (feminine): ASC + Saturn - Jupiter
    if sect_type == 'day':
        children_lon = (asc_longitude + jupiter_lon - saturn_lon) % 360
    else:
        children_lon = (asc_longitude + saturn_lon - jupiter_lon) % 360
    children_sign, children_degree = get_sign_and_degree(children_lon)

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
        },
        {
            'name': 'Lot of Eros',
            'symbol': '♡',
            'position': {
                'sign': eros_sign,
                'degree': round(eros_degree, 4),
                'dms': decimal_to_dms(eros_degree),
            },
            'calculation': {
                'formula': 'ASC + Venus - Spirit (day) / ASC + Spirit - Venus (night)',
                'day_formula': 'ASC + Venus - Spirit',
                'night_formula': 'ASC + Spirit - Venus',
            }
        },
        {
            'name': 'Lot of Necessity',
            'symbol': '⚙',
            'position': {
                'sign': necessity_sign,
                'degree': round(necessity_degree, 4),
                'dms': decimal_to_dms(necessity_degree),
            },
            'calculation': {
                'formula': 'ASC + Fortune - Mercury (day) / ASC + Mercury - Fortune (night)',
                'day_formula': 'ASC + Fortune - Mercury',
                'night_formula': 'ASC + Mercury - Fortune',
            }
        },
        {
            'name': 'Lot of Courage',
            'symbol': '⚔',
            'position': {
                'sign': courage_sign,
                'degree': round(courage_degree, 4),
                'dms': decimal_to_dms(courage_degree),
            },
            'calculation': {
                'formula': 'ASC + Fortune - Mars (day) / ASC + Mars - Fortune (night)',
                'day_formula': 'ASC + Fortune - Mars',
                'night_formula': 'ASC + Mars - Fortune',
            }
        },
        {
            'name': 'Lot of Victory',
            'symbol': '🏆',
            'position': {
                'sign': victory_sign,
                'degree': round(victory_degree, 4),
                'dms': decimal_to_dms(victory_degree),
            },
            'calculation': {
                'formula': 'ASC + Spirit - Jupiter (day) / ASC + Jupiter - Spirit (night)',
                'day_formula': 'ASC + Spirit - Jupiter',
                'night_formula': 'ASC + Jupiter - Spirit',
            }
        },
        {
            'name': 'Lot of Basis',
            'symbol': '⚓',
            'position': {
                'sign': basis_sign,
                'degree': round(basis_degree, 4),
                'dms': decimal_to_dms(basis_degree),
            },
            'calculation': {
                'formula': 'ASC + Fortune - Saturn (day) / ASC + Saturn - Fortune (night)',
                'day_formula': 'ASC + Fortune - Saturn',
                'night_formula': 'ASC + Saturn - Fortune',
            }
        },
        {
            'name': 'Lot of Exaltation',
            'symbol': '👑',
            'position': {
                'sign': exaltation_sign,
                'degree': round(exaltation_degree, 4),
                'dms': decimal_to_dms(exaltation_degree),
            },
            'calculation': {
                'formula': 'ASC + Mars - Sun',
                'day_formula': 'ASC + Mars - Sun',
                'night_formula': 'ASC + Mars - Sun',
            }
        },
        {
            'name': 'Lot of Marriage',
            'symbol': '💍',
            'position': {
                'sign': marriage_sign,
                'degree': round(marriage_degree, 4),
                'dms': decimal_to_dms(marriage_degree),
            },
            'calculation': {
                'formula': 'ASC + Venus - Saturn',
                'day_formula': 'ASC + Venus - Saturn',
                'night_formula': 'ASC + Venus - Saturn',
            }
        },
        {
            'name': 'Lot of Children',
            'symbol': '👶',
            'position': {
                'sign': children_sign,
                'degree': round(children_degree, 4),
                'dms': decimal_to_dms(children_degree),
            },
            'calculation': {
                'formula': 'ASC + Jupiter - Saturn (day) / ASC + Saturn - Jupiter (night)',
                'day_formula': 'ASC + Jupiter - Saturn',
                'night_formula': 'ASC + Saturn - Jupiter',
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


def calculate_antiscia(planet_data):
    """
    Calculate antiscia and contra-antiscia for all planets.

    Antiscia: Mirror degrees across 0° Cancer/Capricorn axis (solstice points)
    Contra-antiscia: 180° from antiscion

    Traditional technique showing hidden connections and symmetries.
    """
    antiscia_data = []

    for planet in planet_data:
        lon = planet['longitude']

        # Calculate antiscion (mirror across 0° Cancer/Capricorn)
        # Formula: antiscion = 180° - longitude
        antiscion_lon = (180 - lon) % 360
        antiscion_sign, antiscion_degree = get_sign_and_degree(antiscion_lon)

        # Calculate contra-antiscion (180° from antiscion)
        contra_lon = (antiscion_lon + 180) % 360
        contra_sign, contra_degree = get_sign_and_degree(contra_lon)

        antiscia_data.append({
            'planet': planet['name'],
            'natal_position': {
                'sign': planet['sign'],
                'degree': planet['degree'],
                'longitude': lon
            },
            'antiscion': {
                'sign': antiscion_sign,
                'degree': round(antiscion_degree, 4),
                'longitude': round(antiscion_lon, 4),
                'dms': decimal_to_dms(antiscion_degree)
            },
            'contra_antiscion': {
                'sign': contra_sign,
                'degree': round(contra_degree, 4),
                'longitude': round(contra_lon, 4),
                'dms': decimal_to_dms(contra_degree)
            }
        })

    return antiscia_data


def calculate_fixed_stars(jd, planet_data, house_data):
    """
    Calculate major fixed stars and check for conjunctions to planets/angles.

    Uses Swiss Ephemeris fixstar_ut() for precise fixed star positions.
    Only reports conjunctions within 1° orb (traditional).
    """
    # Major 5 fixed stars (Royal Stars + important traditional stars)
    FIXED_STARS = {
        'Regulus': {
            'traditional_name': 'Cor Leonis (Heart of the Lion)',
            'nature': 'Success, royalty, honor, leadership',
            'magnitude': 1.4
        },
        'Spica': {
            'traditional_name': 'Spica Virginis (Ear of Wheat)',
            'nature': 'Gifts, protection, success through skill',
            'magnitude': 1.0
        },
        'Algol': {
            'traditional_name': "Caput Medusae (Medusa's Head)",
            'nature': 'Violence, danger, challenges (use with caution)',
            'magnitude': 2.1
        },
        'Antares': {
            'traditional_name': 'Cor Scorpii (Heart of Scorpion)',
            'nature': 'Conflict, courage, obsession',
            'magnitude': 1.0
        },
        'Aldebaran': {
            'traditional_name': 'Oculus Tauri (Eye of the Bull)',
            'nature': 'Honor, integrity, achievement',
            'magnitude': 0.9
        }
    }

    ORB = 1.0  # Traditional 1° orb for fixed stars

    fixed_star_data = []
    conjunctions = []

    # Calculate each fixed star position
    for star_name, star_info in FIXED_STARS.items():
        try:
            result = swe.fixstar_ut(star_name, jd)
            star_lon = result[0][0]
            star_sign, star_degree = get_sign_and_degree(star_lon)

            star_data = {
                'name': star_name,
                'traditional_name': star_info['traditional_name'],
                'nature': star_info['nature'],
                'magnitude': star_info['magnitude'],
                'position': {
                    'sign': star_sign,
                    'degree': round(star_degree, 4),
                    'longitude': round(star_lon, 4),
                    'dms': decimal_to_dms(star_degree)
                },
                'conjunctions': []
            }

            # Check conjunctions to planets
            for planet in planet_data:
                orb = abs(star_lon - planet['longitude'])
                if orb > 180:
                    orb = 360 - orb

                if orb <= ORB:
                    conjunction_data = {
                        'type': 'planet',
                        'body': planet['name'],
                        'orb': round(orb, 2),
                        'applying': planet['longitude'] < star_lon
                    }
                    star_data['conjunctions'].append(conjunction_data)

                    conjunctions.append({
                        'star': star_name,
                        'planet': planet['name'],
                        'orb': round(orb, 2),
                        'nature': star_info['nature']
                    })

            # Check conjunctions to angles (ASC, MC, DSC, IC)
            angles = {
                'Ascendant': house_data['ascendant']['longitude'],
                'Midheaven': house_data['midheaven']['longitude'],
                'Descendant': (house_data['ascendant']['longitude'] + 180) % 360,
                'IC': (house_data['midheaven']['longitude'] + 180) % 360
            }

            for angle_name, angle_lon in angles.items():
                orb = abs(star_lon - angle_lon)
                if orb > 180:
                    orb = 360 - orb

                if orb <= ORB:
                    conjunction_data = {
                        'type': 'angle',
                        'body': angle_name,
                        'orb': round(orb, 2)
                    }
                    star_data['conjunctions'].append(conjunction_data)

                    conjunctions.append({
                        'star': star_name,
                        'angle': angle_name,
                        'orb': round(orb, 2),
                        'nature': star_info['nature']
                    })

            fixed_star_data.append(star_data)

        except Exception as e:
            print(f"Warning: Could not calculate {star_name}: {e}")
            continue

    return {
        'stars': fixed_star_data,
        'conjunctions_summary': conjunctions
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


def calculate_stelliums(planet_data):
    """
    Calculate stelliums (3+ traditional planets in same sign OR house).
    Returns list of stelliums with their ruling planet.
    """
    stelliums = []

    # Check by sign
    sign_groups = {}
    for planet in planet_data:
        if planet['traditional']:
            sign = planet['sign']
            if sign not in sign_groups:
                sign_groups[sign] = []
            sign_groups[sign].append(planet['name'])

    for sign, planets in sign_groups.items():
        if len(planets) >= 3:
            ruler = DOMICILE.get(sign, 'None')
            stelliums.append({
                'type': 'sign',
                'location': sign,
                'planets': planets,
                'count': len(planets),
                'ruler': ruler
            })

    # Check by house
    house_groups = {}
    for planet in planet_data:
        if planet['traditional'] and 'house' in planet:
            house = planet['house']
            if house not in house_groups:
                house_groups[house] = []
            house_groups[house].append(planet['name'])

    for house, planets in house_groups.items():
        if len(planets) >= 3:
            # Find the sign of this house to determine ruler
            # (This would need house_data passed in, or we'll add it in integration)
            stelliums.append({
                'type': 'house',
                'location': f"House {house}",
                'planets': planets,
                'count': len(planets),
                'ruler': None  # Will be filled in during integration
            })

    return stelliums


def calculate_hayz(planet_data, sect_type, house_data):
    """
    Calculate hayz condition for each planet.
    Hayz = planet in optimal sect condition:
    - Diurnal planets (Sun, Jupiter, Saturn) above horizon by day in masculine sign
    - Nocturnal planets (Moon, Venus, Mars) below horizon by night in feminine sign
    """
    MASCULINE_SIGNS = ['Aries', 'Gemini', 'Leo', 'Libra', 'Sagittarius', 'Aquarius']
    FEMININE_SIGNS = ['Taurus', 'Cancer', 'Virgo', 'Scorpio', 'Capricorn', 'Pisces']

    DIURNAL_PLANETS = ['Sun', 'Jupiter', 'Saturn']
    NOCTURNAL_PLANETS = ['Moon', 'Venus', 'Mars']

    hayz_conditions = {}

    for planet in planet_data:
        name = planet['name']
        sign = planet['sign']
        house = planet.get('house', 0)

        # Determine if above or below horizon (houses 7-12 = above, 1-6 = below)
        above_horizon = house in [7, 8, 9, 10, 11, 12]
        below_horizon = house in [1, 2, 3, 4, 5, 6]

        # Check hayz condition
        in_hayz = False

        if name in DIURNAL_PLANETS:
            # Diurnal planet needs: day chart + above horizon + masculine sign
            if sect_type == 'day' and above_horizon and sign in MASCULINE_SIGNS:
                in_hayz = True
        elif name in NOCTURNAL_PLANETS:
            # Nocturnal planet needs: night chart + below horizon + feminine sign
            if sect_type == 'night' and below_horizon and sign in FEMININE_SIGNS:
                in_hayz = True

        hayz_conditions[name] = {
            'in_hayz': in_hayz,
            'planet_sect': 'diurnal' if name in DIURNAL_PLANETS else 'nocturnal' if name in NOCTURNAL_PLANETS else 'neutral',
            'chart_sect': sect_type,
            'position': 'above horizon' if above_horizon else 'below horizon',
            'sign_gender': 'masculine' if sign in MASCULINE_SIGNS else 'feminine'
        }

    return hayz_conditions


def calculate_planetary_conditions(planet_data, aspects):
    """
    Calculate various planetary conditions (stationary, swift/slow, oriental/occidental, peregrine, feral).
    Returns dict of conditions for each planet.
    """
    # Mean daily motions (approximate degrees per day)
    MEAN_MOTIONS = {
        'Sun': 0.9856,
        'Moon': 13.176,
        'Mercury': 1.383,
        'Venus': 1.602,
        'Mars': 0.524,
        'Jupiter': 0.083,
        'Saturn': 0.033,
    }

    conditions = {}
    sun = next((p for p in planet_data if p['name'] == 'Sun'), None)
    sun_lon = sun['longitude'] if sun else 0

    for planet in planet_data:
        name = planet['name']
        if name not in TRADITIONAL_PLANETS:
            continue

        speed = planet.get('speed', 0)
        mean_speed = MEAN_MOTIONS.get(name, 0)

        # Stationary check (within 10% of zero speed for outer planets, 20% for inner)
        station_threshold = 0.1 if name in ['Mars', 'Jupiter', 'Saturn'] else 0.2
        is_stationary = abs(speed) < (mean_speed * station_threshold)

        # Swift/slow check
        is_swift = speed > (mean_speed * 1.1)
        is_slow = 0 < speed < (mean_speed * 0.9)

        # Oriental/Occidental (only for Mercury, Venus, Mars, Jupiter, Saturn)
        oriental = False
        occidental = False
        if name != 'Sun' and name != 'Moon':
            # Oriental = rises before Sun (planet longitude < Sun longitude, accounting for wrap)
            diff = (planet['longitude'] - sun_lon) % 360
            if 0 < diff < 180:
                occidental = True
            else:
                oriental = True

        # Peregrine check (no essential dignities)
        dignities = planet.get('dignities', {}).get('essential', {})
        is_peregrine = not any([
            dignities.get('domicile'),
            dignities.get('exaltation'),
            dignities.get('triplicity'),
            dignities.get('term'),
            dignities.get('face')
        ])

        # Feral check (no major aspects)
        planet_aspects = [a for a in aspects if planet['name'] in [a['planet_1'], a['planet_2']]]
        is_feral = len(planet_aspects) == 0

        conditions[name] = {
            'stationary': is_stationary,
            'swift': is_swift,
            'slow': is_slow,
            'oriental': oriental,
            'occidental': occidental,
            'peregrine': is_peregrine,
            'feral': is_feral,
            'speed': speed,
            'mean_speed': mean_speed,
        }

    return conditions


def calculate_aspect_dynamics(aspects, planet_data):
    """
    Calculate overcoming and enclosure/besiegement from aspects.
    """
    dynamics = {}

    # Overcoming: planet in superior position in square/opposition
    # Superior = later in zodiacal order within the aspect
    for aspect in aspects:
        if aspect['aspect_type'] in ['square', 'opposition']:
            p1 = next(p for p in planet_data if p['name'] == aspect['planet_1'])
            p2 = next(p for p in planet_data if p['name'] == aspect['planet_2'])

            lon1 = p1['longitude']
            lon2 = p2['longitude']

            # Determine which is ahead in zodiacal order
            diff = (lon2 - lon1) % 360
            if diff < 180:
                # p2 is ahead, so p2 overcomes p1
                if p2['name'] not in dynamics:
                    dynamics[p2['name']] = {'overcomes': [], 'overcome_by': []}
                if p1['name'] not in dynamics:
                    dynamics[p1['name']] = {'overcomes': [], 'overcome_by': []}
                dynamics[p2['name']]['overcomes'].append(p1['name'])
                dynamics[p1['name']]['overcome_by'].append(p2['name'])
            else:
                # p1 is ahead, so p1 overcomes p2
                if p1['name'] not in dynamics:
                    dynamics[p1['name']] = {'overcomes': [], 'overcome_by': []}
                if p2['name'] not in dynamics:
                    dynamics[p2['name']] = {'overcomes': [], 'overcome_by': []}
                dynamics[p1['name']]['overcomes'].append(p2['name'])
                dynamics[p2['name']]['overcome_by'].append(p1['name'])

    # Enclosure/Besiegement: planet between two others within ~15°
    BENEFICS = ['Venus', 'Jupiter']
    MALEFICS = ['Mars', 'Saturn']

    sorted_planets = sorted([p for p in planet_data if p['traditional']],
                           key=lambda x: x['longitude'])

    enclosure = {}
    for i, planet in enumerate(sorted_planets):
        if i == 0 or i == len(sorted_planets) - 1:
            continue  # Skip first and last

        prev_planet = sorted_planets[i-1]
        next_planet = sorted_planets[i+1]

        # Check if within ~15° on each side
        dist_prev = abs(planet['longitude'] - prev_planet['longitude'])
        dist_next = abs(next_planet['longitude'] - planet['longitude'])

        if dist_prev <= 15 and dist_next <= 15:
            prev_name = prev_planet['name']
            next_name = next_planet['name']

            # Determine enclosure type
            if prev_name in BENEFICS and next_name in BENEFICS:
                enclosure_type = 'benefic_enclosure'
            elif prev_name in MALEFICS and next_name in MALEFICS:
                enclosure_type = 'malefic_besiegement'
            else:
                enclosure_type = 'mixed_enclosure'

            enclosure[planet['name']] = {
                'type': enclosure_type,
                'between': [prev_name, next_name],
                'distances': {'prev': round(dist_prev, 2), 'next': round(dist_next, 2)}
            }

    return {'overcoming': dynamics, 'enclosure': enclosure}


def generate_seed_data(args):
    """Main function to generate complete seed data."""
    # Initialize Swiss Ephemeris
    swe.set_ephe_path(None)  # Use default ephemeris

    # Calculate Julian day
    jd, dt_utc = calculate_julian_day(args.date, args.time, args.timezone)

    # Calculate chart components
    planet_data = calculate_planets(jd)
    house_info = calculate_houses(jd, args.lat, args.lon)
    sect = determine_sect(planet_data, house_info['ascendant'], jd, args.lat, args.lon)

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

    # Calculate house rulers (must be after dignities are assigned)
    house_info['houses'] = calculate_house_rulers(house_info['houses'], planet_data)

    # Calculate aspects
    aspects = calculate_aspects(planet_data)

    # Calculate angle aspects (aspects from planets to ASC/MC/DSC/IC)
    angle_aspects = calculate_angle_aspects(planet_data, house_info['ascendant']['longitude'], house_info['midheaven']['longitude'])

    # Calculate lots
    lots = calculate_lots(jd, house_info['ascendant']['longitude'], planet_data, sect['type'])

    # Calculate nodes
    nodes = calculate_nodes(jd)

    # Calculate antiscia
    antiscia = calculate_antiscia(planet_data)

    # Calculate fixed stars
    fixed_stars = calculate_fixed_stars(jd, planet_data, house_info)

    # Calculate elemental balance
    elements, modalities = calculate_elemental_balance(planet_data)

    # Calculate new planetary conditions
    stelliums = calculate_stelliums(planet_data)
    hayz_conditions = calculate_hayz(planet_data, sect['type'], house_info['houses'])
    planetary_conditions = calculate_planetary_conditions(planet_data, aspects)
    aspect_dynamics = calculate_aspect_dynamics(aspects, planet_data)

    # Assemble complete seed data
    seed_data = {
        'metadata': {
            'profile_name': args.name,
            'generated_at': datetime.now().isoformat(),
            'schema_version': '1.1',  # Bumped for new calculations
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
        'angle_aspects': angle_aspects,
        'lots': lots,
        'lunar_nodes': nodes,
        'antiscia': antiscia,
        'fixed_stars': fixed_stars,
        'stelliums': stelliums,
        'hayz_conditions': hayz_conditions,
        'planetary_conditions': planetary_conditions,
        'aspect_dynamics': aspect_dynamics,
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
