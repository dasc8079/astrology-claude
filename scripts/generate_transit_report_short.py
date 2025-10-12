#!/usr/bin/env python3
"""
Generate Short-Range Transit Report
Implements transit-analyzer-short agent logic
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

def load_transit_data(filepath):
    """Load transit data JSON"""
    with open(filepath) as f:
        return json.load(f)

def analyze_movements(transits, start_date, end_date):
    """
    Analyze transits to identify 2-4 thematic movements
    Returns list of movements with their transit clusters
    """
    # Group transits by week
    weekly_groups = defaultdict(list)

    for transit in transits:
        date_str = transit['date']
        date = datetime.strptime(date_str, '%Y-%m-%d')
        week_key = date.strftime('%Y-W%U')  # Week number
        weekly_groups[week_key].append(transit)

    # Analyze themes across weeks to detect movements
    movements = []
    current_movement = None
    movement_transits = []

    sorted_weeks = sorted(weekly_groups.keys())

    for week in sorted_weeks:
        week_transits = weekly_groups[week]

        # Analyze dominant themes in this week
        themes = analyze_themes(week_transits)

        if not current_movement:
            # Start first movement
            current_movement = themes['primary']
            movement_transits = week_transits
        else:
            # Check if theme continues or shifts
            if themes['primary'] == current_movement:
                # Continue current movement
                movement_transits.extend(week_transits)
            else:
                # New movement detected
                movements.append({
                    'theme': current_movement,
                    'transits': movement_transits,
                    'start': movement_transits[0]['date'],
                    'end': movement_transits[-1]['date']
                })
                current_movement = themes['primary']
                movement_transits = week_transits

    # Add final movement
    if movement_transits:
        movements.append({
            'theme': current_movement,
            'transits': movement_transits,
            'start': movement_transits[0]['date'],
            'end': movement_transits[-1]['date']
        })

    return movements

def analyze_themes(transits):
    """Identify primary and secondary themes in a set of transits"""
    theme_scores = {
        'career_authority': 0,
        'relationships_values': 0,
        'communication_learning': 0,
        'action_desire': 0,
        'structure_limitation': 0,
        'expansion_growth': 0,
        'transformation': 0,
        'home_family': 0
    }

    for t in transits:
        # Score based on planets involved
        transiting = t['transiting_planet']
        natal = t['natal_planet']
        aspect = t['aspect_type']

        # Saturn themes
        if transiting == 'Saturn' or natal == 'Saturn':
            theme_scores['structure_limitation'] += 2
            theme_scores['career_authority'] += 1

        # Jupiter themes
        if transiting == 'Jupiter' or natal == 'Jupiter':
            theme_scores['expansion_growth'] += 2
            theme_scores['relationships_values'] += 1

        # Mars themes
        if transiting == 'Mars' or natal == 'Mars':
            theme_scores['action_desire'] += 2
            theme_scores['career_authority'] += 1

        # Venus themes
        if transiting == 'Venus' or natal == 'Venus':
            theme_scores['relationships_values'] += 2

        # Mercury themes
        if transiting == 'Mercury' or natal == 'Mercury':
            theme_scores['communication_learning'] += 2

        # Moon themes
        if transiting == 'Moon' or natal == 'Moon':
            theme_scores['home_family'] += 1

        # Outer planets
        if transiting in ['Uranus', 'Neptune', 'Pluto'] or natal in ['Uranus', 'Neptune', 'Pluto']:
            theme_scores['transformation'] += 1

    # Find primary and secondary themes
    sorted_themes = sorted(theme_scores.items(), key=lambda x: x[1], reverse=True)

    return {
        'primary': sorted_themes[0][0] if sorted_themes[0][1] > 0 else 'mixed',
        'secondary': sorted_themes[1][0] if len(sorted_themes) > 1 and sorted_themes[1][1] > 0 else None,
        'scores': theme_scores
    }

def generate_movement_title(theme, transits):
    """Generate evocative movement title based on theme"""
    theme_titles = {
        'career_authority': [
            "The Professional Reckoning",
            "Authority Reclaimed",
            "The Climb to Mastery"
        ],
        'relationships_values': [
            "The Heart's Alignment",
            "Relational Deepening",
            "Values Clarified"
        ],
        'communication_learning': [
            "The Voice Emerges",
            "Mental Restructuring",
            "The Messenger's Journey"
        ],
        'action_desire': [
            "The Catalyst of Change",
            "Momentum Gathered",
            "The Warrior's Path"
        ],
        'structure_limitation': [
            "Sacred Constraints",
            "The Refining Fire",
            "Foundations Rebuilt"
        ],
        'expansion_growth': [
            "The Opening",
            "Horizons Broadened",
            "The Harvest Begins"
        ],
        'transformation': [
            "The Deep Work",
            "Threshold Crossing",
            "Emergence"
        ],
        'home_family': [
            "Roots Examined",
            "The Inner Sanctum",
            "Ancestral Reckoning"
        ]
    }

    # Select title based on theme
    if theme in theme_titles:
        # Use first title (could be randomized or contextual)
        return theme_titles[theme][0]
    else:
        return "Transition Period"

def format_transit_description(transit):
    """Format single transit for technical appendix"""
    planet = transit['transiting_planet']
    aspect = transit['aspect_type']
    natal = transit['natal_planet']
    orb = abs(transit['orb'])
    exact = "exact" if transit['exact'] else f"orb {orb:.1f}°"
    applying = "applying" if transit['applying'] else "separating"

    return f"{planet} {aspect} natal {natal} ({exact}, {applying})"

def main():
    # Load data
    transit_file = sys.argv[1] if len(sys.argv) > 1 else '/Users/darrenschaeffer/Documents/Claude/Astrogy_Claude/profiles/darren/output/transit_data_darren_2025-10-11_to_2026-02-11.json'

    print(f"Loading transit data from: {transit_file}")
    data = load_transit_data(transit_file)

    # Get all critical and important transits
    all_transits = data['transits_by_tier']['critical'] + data['transits_by_tier']['important']
    all_transits.sort(key=lambda x: x['date'])

    print(f"\nTotal transits to analyze: {len(all_transits)}")
    print(f"Date range: {data['date_range']['start']} to {data['date_range']['end']}")
    print(f"Duration: {data['date_range']['days']} days")

    # Analyze movements
    print("\nAnalyzing thematic movements...")
    movements = analyze_movements(all_transits, data['date_range']['start'], data['date_range']['end'])

    print(f"\nDetected {len(movements)} movements:")
    for i, m in enumerate(movements, 1):
        print(f"\n  Movement {i}: {generate_movement_title(m['theme'], m['transits'])}")
        print(f"    Theme: {m['theme']}")
        print(f"    Period: {m['start']} to {m['end']}")
        print(f"    Transits: {len(m['transits'])}")
        print(f"    Key transits:")
        for t in m['transits'][:5]:  # Show first 5
            print(f"      - {t['date']}: {format_transit_description(t)}")

    return movements, data

if __name__ == '__main__':
    movements, data = main()
