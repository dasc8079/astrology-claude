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
from firdaria_calculator import calculate_major_periods, calculate_sub_periods, find_active_periods


def calculate_planetary_returns(start_age: int = 0, end_age: int = 100) -> List[Dict[str, Any]]:
    """
    Calculate major planetary return milestones.

    Jupiter return: ~12 years (expansion/growth cycles)
    Saturn return: ~29.5 years (maturity/restructuring)
    Uranus opposition: ~42 years (midlife awakening)

    Returns:
        List of return events with age, planet, and return number
    """
    returns = []

    # Jupiter returns (~11.86 years - approximated to 12)
    jupiter_cycle = 11.86
    jupiter_count = 0
    age = jupiter_cycle
    while age <= end_age:
        if age >= start_age:
            jupiter_count += 1
            returns.append({
                'age': round(age, 1),
                'planet': 'Jupiter',
                'event': f'Jupiter Return #{jupiter_count}',
                'cycle': jupiter_cycle,
                'significance': 'Expansion, growth, opportunity'
            })
        age += jupiter_cycle

    # Saturn returns (~29.46 years - approximated to 29.5)
    saturn_cycle = 29.46
    saturn_count = 0
    age = saturn_cycle
    while age <= end_age:
        if age >= start_age:
            saturn_count += 1
            returns.append({
                'age': round(age, 1),
                'planet': 'Saturn',
                'event': f'Saturn Return #{saturn_count}',
                'cycle': saturn_cycle,
                'significance': 'Maturity, responsibility, restructuring'
            })
        age += saturn_cycle

    # Uranus opposition (~42 years - half of 84-year cycle)
    uranus_opposition = 42.0
    if start_age <= uranus_opposition <= end_age:
        returns.append({
            'age': uranus_opposition,
            'planet': 'Uranus',
            'event': 'Uranus Opposition',
            'cycle': 84.0,  # Full cycle
            'significance': 'Midlife crisis/awakening, radical change'
        })

    # Sort by age
    returns.sort(key=lambda x: x['age'])

    return returns


def calculate_progression_sign_changes(profile_name: str, start_age: int = 0, end_age: int = 100) -> List[Dict[str, Any]]:
    """
    Calculate major progressed sign changes (Sun and angles only).

    These are RARE events marking major identity evolution:
    - Progressed Sun changes sign every ~30 years (only 2-3 times in life)
    - Progressed ASC/MC change signs (timing varies by birth location)

    Returns:
        List of sign change events
    """
    sign_changes = []

    # Get natal positions
    profile = load_profile(profile_name)
    natal_planets = profile.get_planets()
    natal_houses = profile.get_houses()

    # Find natal Sun sign
    natal_sun = next((p for p in natal_planets if p['name'] == 'Sun'), None)
    if not natal_sun:
        return sign_changes

    natal_sun_sign = natal_sun['sign']
    natal_sun_degree = natal_sun['degree']

    # Calculate when progressed Sun changes signs
    # Progressed Sun moves ~1 degree per year
    # Need to reach 30 degrees to change sign
    degrees_to_next_sign = 30.0 - natal_sun_degree
    age_at_first_change = degrees_to_next_sign

    # Track sign changes
    current_age = age_at_first_change
    sign_count = 0

    while current_age <= end_age:
        if current_age >= start_age:
            sign_count += 1
            # Calculate which sign we're entering
            signs = [
                'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
            ]
            natal_sign_index = signs.index(natal_sun_sign)
            new_sign_index = (natal_sign_index + sign_count) % 12
            new_sign = signs[new_sign_index]

            sign_changes.append({
                'age': round(current_age, 1),
                'point': 'Progressed Sun',
                'event': f'Progressed Sun enters {new_sign}',
                'old_sign': signs[(new_sign_index - 1) % 12],
                'new_sign': new_sign,
                'significance': 'Major identity evolution, new life chapter begins'
            })

        # Each sign takes ~30 years
        current_age += 30.0

    # Sort by age
    sign_changes.sort(key=lambda x: x['age'])

    return sign_changes


def assess_saturn_return_difficulty(profile_name: str, return_age: float) -> Dict[str, Any]:
    """
    Assess Saturn return difficulty based on Saturn's CURRENT condition at return age.

    Uses progressed Saturn position to determine difficulty, allowing first and second
    returns to have different assessments if Saturn's condition changes over time.

    Checks:
    - House placement (6H/8H/12H = difficult) - uses PROGRESSED position
    - Sect (malefic contrary to sect = difficult) - natal, doesn't change
    - Dignity (detriment/fall = challenged) - uses PROGRESSED position
    - Afflictions (difficult aspects from Mars/Saturn) - uses PROGRESSED aspects

    Args:
        profile_name: Profile to analyze
        return_age: Age of Saturn return (typically ~29 or ~59)

    Returns:
        {
            'return_age': float,
            'difficulty_level': 'extreme' | 'difficult' | 'moderate' | 'easy',
            'indicators': [list of difficulty factors],
            'aftermath_years': int (1-5),
            'aftermath_bonus': int (3-8 per year),
            'difficulty_score': int
        }
    """
    profile = load_profile(profile_name)
    seed_data = profile.seed_data

    if not seed_data:
        # Default to moderate if can't assess
        return {
            'return_age': return_age,
            'difficulty_level': 'moderate',
            'indicators': [],
            'aftermath_years': 2,
            'aftermath_bonus': 5,
            'difficulty_score': 1
        }

    difficulty_score = 0
    indicators = []

    # Calculate progressed Saturn position at return age
    try:
        prog_positions = calculate_progressed_positions(profile_name, return_age)
        prog_planets = prog_positions.get('progressed_planets', [])
        prog_saturn = next((p for p in prog_planets if p['name'] == 'Saturn'), None)

        if not prog_saturn:
            # Fall back to natal if progression calculation fails
            planets = seed_data.get('planets', [])
            prog_saturn = next((p for p in planets if p['name'] == 'Saturn'), None)
            indicators.append("Using natal position (progression unavailable)")
    except Exception as e:
        # Fall back to natal if any error occurs
        planets = seed_data.get('planets', [])
        prog_saturn = next((p for p in planets if p['name'] == 'Saturn'), None)
        indicators.append("Using natal position (progression error)")

    if not prog_saturn:
        return {
            'return_age': return_age,
            'difficulty_level': 'moderate',
            'indicators': ['Saturn data not found'],
            'aftermath_years': 2,
            'aftermath_bonus': 5,
            'difficulty_score': 1
        }

    # Get chart framework for sect (natal - doesn't change)
    framework = seed_data.get('chart_framework', {})
    sect_data = framework.get('sect', {})
    sect_type = sect_data.get('type', 'day')

    # Check house placement (6H/8H/12H = difficult) - PROGRESSED
    saturn_house = prog_saturn.get('house')
    if saturn_house in [6, 8, 12]:
        difficulty_score += 2
        house_names = {6: '6H (health/service)', 8: '8H (death/crisis)', 12: '12H (loss/isolation)'}
        indicators.append(house_names.get(saturn_house, f'{saturn_house}H placement'))

    # Check sect (malefic contrary to sect = difficult) - NATAL
    # Saturn is malefic of sect in day charts, benefic of sect in night charts
    if sect_type == 'day':
        difficulty_score += 2
        indicators.append("Malefic contrary to sect (Saturn in day chart)")

    # Check dignity (detriment/fall = challenged) - PROGRESSED
    dignities = prog_saturn.get('dignities', {})
    essential = dignities.get('essential', {})

    if essential.get('detriment'):
        difficulty_score += 1
        indicators.append("Detriment (Cancer)")
    elif essential.get('fall'):
        difficulty_score += 1
        indicators.append("Fall (Aries)")

    # Check afflictions (difficult aspects from Mars/Saturn) - PROGRESSED
    try:
        prog_aspects = find_progressed_aspects_to_natal(profile_name, return_age, orb=3.0)
        saturn_afflictions = []

        for aspect in prog_aspects:
            # Check if progressed Saturn is involved in difficult aspects
            if aspect.get('progressed_planet') == 'Saturn':
                aspect_type = aspect.get('aspect_type', '')
                natal_planet = aspect.get('natal_planet')

                # Count difficult aspects to Mars or other malefics
                if aspect_type in ['square', 'opposition'] and natal_planet in ['Mars', 'Saturn']:
                    saturn_afflictions.append(f"{aspect_type} natal {natal_planet}")

        if len(saturn_afflictions) >= 2:
            difficulty_score += 1
            indicators.append(f"{len(saturn_afflictions)} difficult aspects ({', '.join(saturn_afflictions[:2])})")
    except Exception as e:
        # Skip affliction check if progression aspects fail
        pass

    # Determine level and aftermath based on difficulty score
    if difficulty_score >= 4:
        level = 'extreme'
        aftermath_years = 5
        aftermath_bonus = 8
    elif difficulty_score >= 2:
        level = 'difficult'
        aftermath_years = 3
        aftermath_bonus = 8
    elif difficulty_score == 1:
        level = 'moderate'
        aftermath_years = 2
        aftermath_bonus = 5
    else:
        level = 'easy'
        aftermath_years = 1
        aftermath_bonus = 3

    return {
        'return_age': return_age,
        'difficulty_level': level,
        'indicators': indicators,
        'aftermath_years': aftermath_years,
        'aftermath_bonus': aftermath_bonus,
        'difficulty_score': difficulty_score
    }


def detect_traditional_periods(timeline: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Detect traditional Hellenistic significant periods.

    Detects:
    - Loosing of Bond: Final L2 before L1 transitions (intense preparatory phase)
    - Peak Periods: L2 matches L1 sign (empowered/smooth expression)
    - Climax Periods: Midpoint of L1 periods (culmination)
    - Opening Phases: First 2 years of new L1 (new chapter begins)

    Args:
        timeline: Full timeline data with ZR periods

    Returns:
        {
            'loosing_of_bond': [{'ages': (start, end), 'l1_sign': str, 'l2_sign': str}, ...],
            'peak_periods': [{'ages': (start, end), 'sign': str}, ...],
            'climax_periods': [{'age': int, 'l1_sign': str}, ...],
            'opening_phases': [{'ages': (start, end), 'l1_sign': str}, ...]
        }
    """
    periods = {
        'loosing_of_bond': [],
        'peak_periods': [],
        'climax_periods': [],
        'opening_phases': []
    }

    # Process Fortune ZR periods
    if timeline.get('zr_fortune'):
        l1_periods = timeline['zr_fortune'].get('l1_periods', [])
        l2_periods = timeline['zr_fortune'].get('l2_periods', [])

        # Detect Loosing of Bond (final L2 before each L1 transition)
        for i, l1_period in enumerate(l1_periods[:-1]):  # Skip last L1 (no transition after)
            # Find L2 periods within this L1
            l2_in_l1 = [l2 for l2 in l2_periods
                       if l1_period['start_age'] <= l2['start_age'] < l1_period['end_age']]

            if l2_in_l1:
                # Get final L2 period before L1 ends
                final_l2 = l2_in_l1[-1]
                periods['loosing_of_bond'].append({
                    'ages': (int(final_l2['start_age']), int(l1_period['end_age'])),
                    'l1_sign': l1_period['sign'],
                    'l2_sign': final_l2['sign']
                })

        # Detect Peak Periods (L2 matches L1 sign)
        for l1_period in l1_periods:
            l2_in_l1 = [l2 for l2 in l2_periods
                       if l1_period['start_age'] <= l2['start_age'] < l1_period['end_age']]

            for l2 in l2_in_l1:
                if l2['sign'] == l1_period['sign']:
                    periods['peak_periods'].append({
                        'ages': (int(l2['start_age']), int(l2['end_age'])),
                        'sign': l1_period['sign']
                    })

        # Detect Climax (midpoint of L1 periods)
        for l1_period in l1_periods:
            midpoint = (l1_period['start_age'] + l1_period['end_age']) / 2
            periods['climax_periods'].append({
                'age': int(midpoint),
                'l1_sign': l1_period['sign']
            })

        # Detect Opening Phases (first 2 years of L1)
        for l1_period in l1_periods:
            start_age = int(l1_period['start_age'])
            opening_end = min(start_age + 2, int(l1_period['end_age']))
            periods['opening_phases'].append({
                'ages': (start_age, opening_end),
                'l1_sign': l1_period['sign']
            })

    return periods


def calculate_convergence_score(age: int, snapshot: Dict[str, Any], timeline: Dict[str, Any], simplified_mode: bool = False) -> tuple[int, List[str]]:
    """
    Calculate convergence score for a given age.

    Scoring system:
    - TIER 1 (20pts): ZR L1 transitions, Progressed Sun sign changes (rare, decades apart)
    - TIER 2 (10-15pts): Saturn return, Uranus opp, Firdaria major transitions
    - TIER 3 (1-5pts): Jupiter return, Firdaria sub (if not simplified), profection

    Thresholds:
    - 25+ points = MAJOR LIFE EVENT (chapter-defining)
    - 15-24 points = SIGNIFICANT TRANSITION (major milestone)
    - 8-14 points = NOTABLE PERIOD (worth mentioning)
    - <8 points = background (don't highlight)

    Args:
        age: Current age being scored
        snapshot: Snapshot of all active periods at this age
        timeline: Full timeline data
        simplified_mode: If True, exclude L2 periods and Firdaria subs from scoring

    Returns:
        Tuple of (score, list of reasons)
    """
    score = 0
    reasons = []

    # TIER 1 - RARE MULTI-DECADE EVENTS (20 points)
    # ZR L1 transitions (sign changes)
    if snapshot['fortune_l1']:
        fortune_start = snapshot['fortune_l1'].get('start_age', 0)
        if abs(age - fortune_start) <= 0.5:  # FIXED: Changed < to <=
            score += 20
            reasons.append(f"ZR Fortune L1 → {snapshot['fortune_l1']['sign']}")

    if snapshot['spirit_l1']:
        spirit_start = snapshot['spirit_l1'].get('start_age', 0)
        if abs(age - spirit_start) <= 0.5:  # FIXED: Changed < to <=
            score += 20
            reasons.append(f"ZR Spirit L1 → {snapshot['spirit_l1']['sign']}")

    # Progressed Sun sign changes
    for prog_change in timeline.get('progression_sign_changes', []):
        if abs(age - prog_change['age']) <= 0.5:  # FIXED: Changed < to <=
            score += 20
            reasons.append(f"Progressed Sun → {prog_change['new_sign']}")

    # TIER 2 - MAJOR MILESTONES (10-15 points)
    for return_event in timeline.get('planetary_returns', []):
        if abs(age - return_event['age']) <= 0.5:  # FIXED: Changed < to <=
            if return_event['planet'] in ['Saturn', 'Uranus']:
                score += 15
                reasons.append(return_event['event'])
            elif return_event['planet'] == 'Jupiter':
                score += 5
                reasons.append(return_event['event'])

    # Firdaria major transitions
    if snapshot['firdaria_major']:
        fir_start = snapshot['firdaria_major'].get('start_age', 0)
        if abs(age - fir_start) <= 0.5:  # FIXED: Changed < to <=
            score += 10
            reasons.append(f"Firdaria → {snapshot['firdaria_major']['planet']}")

    # TIER 3 - REGULAR CYCLES (1-2 points)
    # Skip Firdaria sub-periods in simplified mode (reduces noise)
    if not simplified_mode and snapshot['firdaria_sub']:
        sub_start = snapshot['firdaria_sub'].get('start_age', 0)
        if abs(age - sub_start) <= 0.5:  # FIXED: Changed < to <=
            score += 2
            reasons.append(f"Firdaria sub → {snapshot['firdaria_sub']['sub_planet']}")

    # Always add 1 point for profection (baseline)
    score += 1

    # TIMING POINT ACTIVATIONS - When profections/ZR activate natal features
    # These add convergence when timing techniques activate special chart points

    # Get profile name and load seed data for activation checks
    profile_name = timeline.get('profile')
    if profile_name and snapshot['profection']:
        try:
            from profile_loader import load_profile
            profile = load_profile(profile_name)
            seed_data = profile.seed_data

            if seed_data:
                profected_house = snapshot['profection']['profection']['profected_house']

                # 1. STELLIUM ACTIVATION (+5 pts): Profection enters house with 3+ planets
                stelliums = seed_data.get('stelliums', [])
                house_stelliums = [s for s in stelliums if s.get('type') == 'house']
                for stellium in house_stelliums:
                    # Extract house number from "House N" format
                    location = stellium.get('location', '')
                    if location.startswith('House '):
                        stellium_house = int(location.split(' ')[1])
                        if stellium_house == profected_house:
                            score += 5
                            planet_names = ', '.join(stellium['planets'])
                            reasons.append(f"Stellium activation: House {profected_house} ({planet_names})")
                            break  # Only count once per house

                # 2. FIXED STAR ACTIVATION (+3 pts): Profection activates natal fixed star
                # Check if any planets in the profected house are conjunct fixed stars
                houses = seed_data.get('houses', [])
                for house in houses:
                    if house.get('number') == profected_house:
                        planets_in_house = house.get('planets_in_house', [])
                        if planets_in_house:
                            fixed_stars_data = seed_data.get('fixed_stars', {})
                            stars = fixed_stars_data.get('stars', [])

                            for planet in planets_in_house:
                                planet_name = planet.get('name')
                                # Check if this planet is conjunct a fixed star
                                for star in stars:
                                    for conj in star.get('conjunctions', []):
                                        if conj.get('planet') == planet_name:
                                            score += 3
                                            star_name = star.get('traditional_name', star.get('name'))
                                            reasons.append(f"Fixed star activation: {planet_name} conjunct {star_name}")
                                            break

                # 3. ANTISCIA ACTIVATION (+2 pts): Profection activates planet's antiscion
                # Check if any planet's antiscion or contra-antiscion falls in the profected house's sign
                antiscia_list = seed_data.get('antiscia', [])
                houses = seed_data.get('houses', [])

                # Get the sign of the profected house
                profected_sign = None
                for house in houses:
                    if house.get('number') == profected_house:
                        profected_sign = house.get('sign')
                        break

                if profected_sign:
                    # Check each planet's antiscia
                    for antiscion_data in antiscia_list:
                        antiscion_sign = antiscion_data.get('antiscion', {}).get('sign')
                        contra_sign = antiscion_data.get('contra_antiscion', {}).get('sign')

                        if antiscion_sign == profected_sign or contra_sign == profected_sign:
                            score += 2
                            planet_name = antiscion_data.get('planet')
                            activation_type = 'antiscion' if antiscion_sign == profected_sign else 'contra-antiscion'
                            reasons.append(f"Antiscia activation: {planet_name} {activation_type} in {profected_sign}")
                            break  # Only count once per profection

                # PROFECTION HOUSE OVERLAYS - Traditional house bonuses
                if profected_house == 11:
                    score += 3
                    reasons.append("11H profection (fortunate - friends, hopes)")
                elif profected_house == 5:
                    score += 2
                    reasons.append("5H profection (joyful - creativity, pleasure)")
                elif profected_house == 10:
                    score += 2
                    reasons.append("10H profection (career, public status)")
                elif profected_house in [6, 8, 12]:
                    score += 3
                    house_names = {6: '6H (health/service)', 8: '8H (death/crisis)', 12: '12H (loss/isolation)'}
                    reasons.append(f"{house_names.get(profected_house)} profection (difficult)")

                # PROFECTION LORD OVERLAYS - Benefic/malefic ruled years
                lord_name = snapshot['profection']['profection'].get('lord_of_year')
                if lord_name:
                    if lord_name in ['Jupiter', 'Venus']:
                        score += 2
                        reasons.append(f"{lord_name} year (benefic)")
                    elif lord_name in ['Saturn', 'Mars']:
                        # Only add bonus if malefic of sect
                        framework = seed_data.get('chart_framework', {})
                        sect_type = framework.get('sect', {}).get('type', 'day')
                        # Saturn malefic in day charts, Mars malefic in night charts
                        if (lord_name == 'Saturn' and sect_type == 'day') or (lord_name == 'Mars' and sect_type == 'night'):
                            score += 2
                            reasons.append(f"{lord_name} year (malefic of sect)")

        except Exception as e:
            # Silently skip if profile loading fails (don't break convergence calculation)
            pass

    # TRADITIONAL PERIOD OVERLAYS - Traditional Hellenistic periods
    # Check if timeline has traditional_periods data
    traditional_periods = timeline.get('traditional_periods')
    if traditional_periods:
        # Loosing of Bond: Final L2 before L1 transition (intense preparatory phase)
        for loosing in traditional_periods.get('loosing_of_bond', []):
            if loosing['ages'][0] <= age <= loosing['ages'][1]:
                score += 10
                reasons.append(f"Loosing of Bond ({loosing['l1_sign']} → next L1)")
                break

        # Peak Periods: L2 matches L1 sign (empowered/smooth expression)
        for peak in traditional_periods.get('peak_periods', []):
            if peak['ages'][0] <= age <= peak['ages'][1]:
                score += 10
                reasons.append(f"Peak Period ({peak['sign']} empowerment)")
                break

        # Climax Periods: Midpoint of L1 (culmination)
        for climax in traditional_periods.get('climax_periods', []):
            if abs(age - climax['age']) <= 0.5:
                score += 5
                reasons.append(f"L1 Climax ({climax['l1_sign']} midpoint)")
                break

        # Opening Phases: First 2 years of L1 (new chapter begins)
        for opening in traditional_periods.get('opening_phases', []):
            if opening['ages'][0] <= age <= opening['ages'][1]:
                score += 5
                reasons.append(f"Opening Phase ({opening['l1_sign']} begins)")
                break

    # SATURN RETURN AFTERMATH - Multi-year difficulty overlay
    # Check if timeline has saturn_assessments data (list of assessments, one per return)
    saturn_assessments = timeline.get('saturn_assessments')
    if saturn_assessments:
        # Match each assessment to its corresponding return age
        for assessment in saturn_assessments:
            return_age = assessment['return_age']
            aftermath_years = assessment['aftermath_years']
            aftermath_bonus = assessment['aftermath_bonus']
            level = assessment['difficulty_level']

            # Check if current age is within aftermath window
            if return_age < age <= return_age + aftermath_years:
                score += aftermath_bonus
                years_after = age - int(return_age)
                reasons.append(f"Saturn aftermath year {years_after}/{aftermath_years} ({level})")

    return score, reasons


def identify_convergence_events(timeline: Dict[str, Any], simplified_mode: bool = False) -> Dict[str, List[Dict[str, Any]]]:
    """
    Identify all convergence events in timeline.

    Args:
        timeline: Complete timeline data
        simplified_mode: If True, exclude L2 periods and Firdaria subs from scoring

    Returns:
        Dictionary with 'major', 'significant', and 'notable' event lists
    """
    major_events = []
    significant_events = []
    notable_events = []

    start_age = timeline['age_range']['start']
    end_age = timeline['age_range']['end']

    for age in range(start_age, end_age + 1):
        snapshot = get_year_snapshot(timeline, age)
        score, reasons = calculate_convergence_score(age, snapshot, timeline, simplified_mode)

        event = {
            'age': age,
            'score': score,
            'reasons': reasons,
            'snapshot': snapshot
        }

        if score >= 25:
            major_events.append(event)
        elif score >= 15:
            significant_events.append(event)
        elif score >= 8:
            notable_events.append(event)

    return {
        'major': major_events,
        'significant': significant_events,
        'notable': notable_events,
    }


def identify_period_clusters(scores: Dict[int, Dict[str, Any]], min_score: int = 8, gap_tolerance: int = 2) -> List[Dict[str, Any]]:
    """
    Identify multi-year periods of elevated astrological activity.

    Groups consecutive ages with elevated convergence scores into cohesive periods,
    allowing for brief gaps (gap_tolerance) to capture extended chapter-like experiences.

    Args:
        scores: Dictionary mapping ages to their score data (score, reasons, snapshot)
        min_score: Minimum score to be considered elevated activity (default 8 = notable threshold)
        gap_tolerance: Number of consecutive low-scoring years allowed within a period (default 2)

    Returns:
        List of period clusters with start/end ages, peak detection, and duration

    Example:
        Ages 27-32 with scores [9, 10, 15, 8, 9, 12] becomes one 6-year period
        even if there's a brief dip, because Saturn return experience extends over time
    """
    clusters = []
    current_cluster = None
    gap_count = 0

    for age in sorted(scores.keys()):
        score_data = scores[age]
        score = score_data['score']

        if score >= min_score:
            if current_cluster is None:
                # Start new cluster
                current_cluster = {
                    'start': age,
                    'end': age,
                    'ages': [age],
                    'peak_age': age,
                    'peak_score': score
                }
            else:
                # Continue cluster
                current_cluster['end'] = age
                current_cluster['ages'].append(age)
                if score > current_cluster['peak_score']:
                    current_cluster['peak_age'] = age
                    current_cluster['peak_score'] = score
            gap_count = 0
        else:
            # Low-scoring year
            if current_cluster is not None:
                gap_count += 1
                if gap_count > gap_tolerance:
                    # Gap too large, end this cluster
                    clusters.append(current_cluster)
                    current_cluster = None
                    gap_count = 0

    # Add final cluster if exists
    if current_cluster:
        clusters.append(current_cluster)

    return clusters


def analyze_period_nature(cluster: Dict[str, Any], scores: Dict[int, Dict[str, Any]]) -> str:
    """
    Determine the nature of a multi-year period based on convergence patterns.

    Classification priority:
    1. Challenging: Saturn return, Uranus opposition, South Node periods
    2. Transformative: Major chapter changes (ZR L1, Progressed Sun sign changes)
    3. Favorable: Jupiter return, North Node periods
    4. Mixed: Significant activity without clear challenging/favorable indicators

    Args:
        cluster: Period cluster with start/end/peak data
        scores: Full score dictionary for looking up reasons

    Returns:
        Classification string: 'challenging', 'transformative', 'favorable', or 'mixed'
    """
    peak_age = cluster['peak_age']
    reasons = scores[peak_age]['reasons']

    # Challenging indicators (hardship, restructuring, crisis)
    challenging = (
        any('Saturn Return' in r for r in reasons) or
        any('Uranus Opposition' in r for r in reasons) or
        any('South Node' in r for r in reasons)
    )

    # Favorable indicators (growth, opportunity, support)
    favorable = (
        any('Jupiter Return' in r for r in reasons) or
        any('North Node' in r for r in reasons)
    )

    # Transformative indicators (major chapter changes - neutral/mixed)
    transformative = (
        any('ZR Fortune L1' in r or 'ZR Spirit L1' in r for r in reasons) or
        any('Progressed Sun' in r for r in reasons)
    )

    # Classification priority (challenging takes precedence over favorable)
    if challenging:
        return 'challenging'
    elif transformative:
        return 'transformative'
    elif favorable:
        return 'favorable'
    else:
        return 'mixed'


def generate_life_arc_timeline(
    profile_name: str,
    start_age: int = 0,
    end_age: int = 100,
    include_fortune: bool = True,
    include_spirit: bool = True,
    include_progressions: bool = False,
    include_solar_returns: bool = False,
    current_date: Optional[str] = None,
    simplified_mode: bool = False
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
        simplified_mode: If True, exclude L2 periods and Firdaria subs from convergence scoring
                         (reduces noise for decades-long life arc analysis)

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

    # Calculate Firdaria (75-year planetary period system)
    framework = profile.get_chart_framework()
    sect = framework.get('sect', {}).get('type', 'day')
    firdaria_major = calculate_major_periods(sect)

    # Calculate all sub-periods for timeline
    firdaria_all_subs = []
    for major in firdaria_major:
        subs = calculate_sub_periods(major, sect)
        firdaria_all_subs.extend(subs)

    firdaria = {
        'sect': sect,
        'major_periods': firdaria_major,
        'sub_periods': firdaria_all_subs,
    }

    # Calculate planetary returns (Jupiter, Saturn, Uranus opposition)
    planetary_returns = calculate_planetary_returns(start_age, end_age)

    # Calculate progressed Sun/angles sign changes (CORE - always included)
    progression_sign_changes = calculate_progression_sign_changes(profile_name, start_age, end_age)

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

    # Get all calculated lots
    lots = profile.get_lots()

    # Build timeline data structure first
    timeline = {
        'profile': profile_name,
        'birth_data': birth_data,
        'age_range': {'start': start_age, 'end': end_age},
        'profections': profections,
        'zr_fortune': zr_fortune,
        'zr_spirit': zr_spirit,
        'firdaria': firdaria,
        'planetary_returns': planetary_returns,
        'progression_sign_changes': progression_sign_changes,
        'progressions': progressions,
        'solar_returns': solar_returns,
        'transits': transits,
        'lots': lots,
    }

    # TRADITIONAL OVERLAYS - Assess Saturn returns and detect traditional periods
    # Must be calculated AFTER timeline is built (needs ZR data) but BEFORE convergence scoring

    # Assess EACH Saturn return individually based on progressed Saturn condition at that age
    saturn_returns = [r for r in planetary_returns if r['planet'] == 'Saturn']
    saturn_assessments = []
    for saturn_return in saturn_returns:
        return_age = saturn_return['age']
        assessment = assess_saturn_return_difficulty(profile_name, return_age)
        saturn_assessments.append(assessment)

    traditional_periods = detect_traditional_periods(timeline)

    # Add traditional analysis to timeline (will be used by calculate_convergence_score)
    timeline['saturn_assessments'] = saturn_assessments  # List of assessments, one per return
    timeline['traditional_periods'] = traditional_periods

    # Calculate convergence events (needs complete timeline data)
    convergence = identify_convergence_events(timeline, simplified_mode)
    timeline['convergence'] = convergence
    timeline['simplified_mode'] = simplified_mode

    # Calculate period clusters (groups consecutive elevated-activity ages into multi-year periods)
    # Build score dictionary for all ages
    scores = {}
    for age in range(start_age, end_age + 1):
        snapshot = get_year_snapshot(timeline, age)
        score, reasons = calculate_convergence_score(age, snapshot, timeline, simplified_mode)
        scores[age] = {
            'score': score,
            'reasons': reasons,
            'snapshot': snapshot
        }

    # Identify period clusters (min_score=8 = notable threshold, gap_tolerance=2 years)
    clusters = identify_period_clusters(scores, min_score=8, gap_tolerance=2)

    # Classify each period's nature
    for cluster in clusters:
        cluster['nature'] = analyze_period_nature(cluster, scores)
        cluster['duration'] = cluster['end'] - cluster['start'] + 1

    # Categorize periods by nature
    period_analysis = {
        'clusters': clusters,
        'by_nature': {
            'challenging': [c for c in clusters if c['nature'] == 'challenging'],
            'transformative': [c for c in clusters if c['nature'] == 'transformative'],
            'favorable': [c for c in clusters if c['nature'] == 'favorable'],
            'mixed': [c for c in clusters if c['nature'] == 'mixed']
        },
        'statistics': {
            'total_periods': len(clusters),
            'challenging_count': len([c for c in clusters if c['nature'] == 'challenging']),
            'transformative_count': len([c for c in clusters if c['nature'] == 'transformative']),
            'favorable_count': len([c for c in clusters if c['nature'] == 'favorable']),
            'mixed_count': len([c for c in clusters if c['nature'] == 'mixed'])
        }
    }

    timeline['period_analysis'] = period_analysis

    return timeline


def get_year_snapshot(timeline: Dict[str, Any], age: int) -> Dict[str, Any]:
    """Get all active periods for a specific age."""
    snapshot = {
        'age': age,
        'profection': None,
        'fortune_l1': None,
        'fortune_l2': None,
        'spirit_l1': None,
        'spirit_l2': None,
        'firdaria_major': None,
        'firdaria_sub': None,
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

    # Find Firdaria periods
    if timeline['firdaria']:
        firdaria_data = find_active_periods(float(age), timeline['firdaria']['sect'])
        if firdaria_data and not firdaria_data.get('beyond_firdaria'):
            snapshot['firdaria_major'] = firdaria_data.get('major_period')
            snapshot['firdaria_sub'] = firdaria_data.get('sub_period')

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
