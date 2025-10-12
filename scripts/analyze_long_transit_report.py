#!/usr/bin/env python3
"""
Analyze Long-Term Transit Report
Generates comprehensive analysis of transits October 2025 - December 2027
Focus: Health trajectory, work capacity, career direction, Fortune L2 shift
"""

import json
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path


def load_transit_data(profile_name, start_date, end_date):
    """Load transit data JSON file."""
    filename = f"transit_data_{profile_name}_{start_date}_to_{end_date}.json"
    filepath = Path(__file__).parent.parent / 'profiles' / profile_name / 'output' / filename

    with open(filepath, 'r') as f:
        return json.load(f)


def group_transits_by_quarter(transits, start_date, end_date):
    """Group transits by calendar quarter."""
    quarters = {}

    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')

    current_quarter_start = start_dt.replace(day=1)

    while current_quarter_start <= end_dt:
        # Determine quarter
        year = current_quarter_start.year
        month = current_quarter_start.month
        quarter = (month - 1) // 3 + 1

        quarter_key = f"{year} Q{quarter}"

        # Calculate quarter boundaries
        quarter_start_month = (quarter - 1) * 3 + 1
        quarter_end_month = quarter_start_month + 2

        quarter_start = current_quarter_start.replace(month=quarter_start_month, day=1)

        # Handle year boundary for Q4
        if quarter == 4:
            quarter_end = datetime(year=year + 1, month=1, day=1) - timedelta(days=1)
        else:
            quarter_end = datetime(year=year, month=quarter_end_month + 1, day=1) - timedelta(days=1)

        # Filter transits in this quarter
        quarter_transits = []
        for transit in transits:
            transit_date = datetime.strptime(transit['date'], '%Y-%m-%d')
            if quarter_start <= transit_date <= quarter_end:
                quarter_transits.append(transit)

        quarters[quarter_key] = {
            'start': quarter_start.strftime('%Y-%m-%d'),
            'end': quarter_end.strftime('%Y-%m-%d'),
            'transits': quarter_transits
        }

        # Move to next quarter
        if quarter == 4:
            current_quarter_start = datetime(year=year + 1, month=1, day=1)
        else:
            current_quarter_start = current_quarter_start.replace(month=quarter_start_month + 3)

    return quarters


def identify_sixth_house_transits(transits):
    """
    Identify transits to 6th house planets (Sun, Saturn, Uranus, Neptune).
    These are CRITICAL for health/work capacity assessment.
    """
    sixth_house_planets = ['Sun', 'Saturn', 'Uranus', 'Neptune']

    health_transits = [
        t for t in transits
        if t['natal_planet'] in sixth_house_planets
    ]

    return health_transits


def identify_career_transits(transits):
    """
    Identify transits to career-related planets:
    - Venus (rules MC in Taurus)
    - Jupiter (in 10th house, mutual reception with Venus)
    """
    career_planets = ['Venus', 'Jupiter']

    career_transits = [
        t for t in transits
        if t['natal_planet'] in career_planets
    ]

    return career_transits


def identify_saturn_square_event(transits):
    """
    Find Saturn square Sun/Saturn transits (March 2026).
    This is THE major test period.
    """
    saturn_squares = []

    for t in transits:
        if t['transiting_planet'] == 'Saturn':
            if t['aspect_type'] == 'square':
                if t['natal_planet'] in ['Sun', 'Saturn']:
                    saturn_squares.append(t)

    return saturn_squares


def analyze_fortune_l2_shift(data):
    """
    Analyze Fortune L2 shift from Scorpio (Mars) to Sagittarius (Jupiter).
    Expected around June 2026 based on ZR timing.
    """
    zr_fortune_l2 = data['current_timing']['zr_fortune_l2']

    # Current L2: Scorpio (Mars), ends at age 37.44
    # Next L2: Sagittarius (Jupiter)

    # Calculate date when age 37.44 occurs
    birth_date = datetime(1988, 12, 27)
    age_37_44_date = birth_date + timedelta(days=int(37.44 * 365.25))

    return {
        'shift_date': age_37_44_date.strftime('%Y-%m-%d'),
        'before': 'Scorpio (Mars-ruled)',
        'after': 'Sagittarius (Jupiter-ruled)',
        'age': 37.44,
        'interpretation': 'Shift from Mars-ruled crisis/testing period to Jupiter-ruled expansion/opportunity'
    }


def generate_quarter_summary(quarter_key, quarter_data, natal_chart, timing_context):
    """Generate detailed quarter analysis."""
    transits = quarter_data['transits']

    # Separate by natal planet focus
    health_transits = identify_sixth_house_transits(transits)
    career_transits = identify_career_transits(transits)

    # Calculate quality scores
    total_score = sum(t['quality_score']['score'] for t in transits)
    health_score = sum(t['quality_score']['score'] for t in health_transits)
    career_score = sum(t['quality_score']['score'] for t in career_transits)

    # Find major transits (exact aspects, slow planets)
    major_transits = [
        t for t in transits
        if t['transiting_planet'] in ['Saturn', 'Jupiter', 'Uranus', 'Neptune', 'Pluto']
        and t['orb'] < 1.0
    ]

    return {
        'period': quarter_key,
        'date_range': f"{quarter_data['start']} to {quarter_data['end']}",
        'total_transits': len(transits),
        'health_transits': len(health_transits),
        'career_transits': len(career_transits),
        'major_transits': len(major_transits),
        'quality_scores': {
            'overall': total_score,
            'health': health_score,
            'career': career_score
        },
        'assessment': assess_quarter_quality(total_score, health_score, career_score),
        'key_transits': major_transits[:5]  # Top 5 major transits
    }


def assess_quarter_quality(overall_score, health_score, career_score):
    """Assess quarter as supportive, challenging, or mixed."""
    if overall_score > 20:
        overall = "Highly Supportive"
    elif overall_score > 0:
        overall = "Moderately Supportive"
    elif overall_score == 0:
        overall = "Neutral/Mixed"
    elif overall_score > -20:
        overall = "Moderately Challenging"
    else:
        overall = "Highly Challenging"

    if health_score > 10:
        health = "Strong health/energy support"
    elif health_score > 0:
        health = "Moderate health support"
    elif health_score == 0:
        health = "Neutral health indicators"
    elif health_score > -10:
        health = "Some health challenges"
    else:
        health = "Significant health strain risk"

    if career_score > 10:
        career = "Strong career opportunities"
    elif career_score > 0:
        career = "Moderate career support"
    elif career_score == 0:
        career = "Neutral career indicators"
    elif career_score > -10:
        career = "Some career obstacles"
    else:
        career = "Significant career challenges"

    return {
        'overall': overall,
        'health': health,
        'career': career
    }


def generate_comprehensive_report(data):
    """Generate full long-term transit report."""

    print("\n" + "="*80)
    print("LONG-TERM TRANSIT REPORT: October 2025 - December 2027")
    print("Profile: Darren (Age 36.8 - 39.0)")
    print("="*80)

    # Extract data
    transits = data['all_transits']
    natal_chart = data['natal_chart']
    timing_context = data['current_timing']

    print(f"\nTotal Transits Analyzed: {len(transits)}")
    print(f"Date Range: {data['date_range']['start']} to {data['date_range']['end']}")
    print(f"Duration: {data['date_range']['days']} days (~{data['date_range']['days']/365.25:.1f} years)")

    # Group by quarter
    quarters = group_transits_by_quarter(
        transits,
        data['date_range']['start'],
        data['date_range']['end']
    )

    print(f"\n{len(quarters)} quarters analyzed")

    # EXECUTIVE SUMMARY
    print("\n" + "-"*80)
    print("EXECUTIVE SUMMARY")
    print("-"*80)

    # Identify key timing windows
    all_health_transits = identify_sixth_house_transits(transits)
    all_career_transits = identify_career_transits(transits)
    saturn_squares = identify_saturn_square_event(transits)

    print(f"\n6th House (Health/Work) Transits: {len(all_health_transits)}")
    print(f"Career Indicator Transits: {len(all_career_transits)}")
    print(f"Saturn Square Sun/Saturn Events: {len(saturn_squares)}")

    # Fortune L2 Shift
    fortune_shift = analyze_fortune_l2_shift(data)
    print(f"\nFortune L2 Shift: {fortune_shift['shift_date']}")
    print(f"  Before: {fortune_shift['before']}")
    print(f"  After: {fortune_shift['after']}")
    print(f"  Significance: {fortune_shift['interpretation']}")

    # Peak/Low Periods
    print(f"\nPeak Periods: {len(data['peak_periods'])}")
    print(f"Low Periods: {len(data['low_periods'])}")

    if data.get('most_auspicious_day'):
        print(f"\nMost Auspicious Day: {data['most_auspicious_day']['date']} (score: {data['most_auspicious_day']['score']:+d})")

    if data.get('most_challenging_day'):
        print(f"Most Challenging Day: {data['most_challenging_day']['date']} (score: {data['most_challenging_day']['score']:+d})")

    # QUARTER-BY-QUARTER ANALYSIS
    print("\n" + "-"*80)
    print("QUARTER-BY-QUARTER ANALYSIS")
    print("-"*80)

    sorted_quarters = sorted(quarters.items(), key=lambda x: x[0])

    for quarter_key, quarter_data in sorted_quarters:
        summary = generate_quarter_summary(quarter_key, quarter_data, natal_chart, timing_context)

        print(f"\n{summary['period']}: {summary['date_range']}")
        print(f"  Total Transits: {summary['total_transits']}")
        print(f"  Health/Work Transits: {summary['health_transits']}")
        print(f"  Career Transits: {summary['career_transits']}")
        print(f"  Major Transits (exact): {summary['major_transits']}")
        print(f"\n  Quality Scores:")
        print(f"    Overall: {summary['quality_scores']['overall']:+d} ({summary['assessment']['overall']})")
        print(f"    Health: {summary['quality_scores']['health']:+d} ({summary['assessment']['health']})")
        print(f"    Career: {summary['quality_scores']['career']:+d} ({summary['assessment']['career']})")

        if summary['key_transits']:
            print(f"\n  Key Transits:")
            for transit in summary['key_transits']:
                print(f"    - {transit['date']}: {transit['transiting_planet']} {transit['aspect_type']} natal {transit['natal_planet']} (orb: {transit['orb']:.2f}°, score: {transit['quality_score']['score']:+d})")

    # MAJOR TRANSIT EVENTS
    print("\n" + "-"*80)
    print("MAJOR TRANSIT EVENTS")
    print("-"*80)

    if saturn_squares:
        print("\nSaturn Square Sun/Saturn (CRITICAL TEST):")
        for sq in saturn_squares:
            print(f"  {sq['date']}: Saturn {sq['aspect_type']} natal {sq['natal_planet']}")
            print(f"    Orb: {sq['orb']:.2f}°, Quality Score: {sq['quality_score']['score']:+d}")
            if sq.get('duration'):
                print(f"    Duration: {sq['duration']['applying_date']} to {sq['duration']['separating_date']}")

    # CAREER DIRECTION ASSESSMENT
    print("\n" + "-"*80)
    print("CAREER DIRECTION ASSESSMENT")
    print("-"*80)

    # Analyze Venus vs Jupiter transit support
    venus_transits = [t for t in transits if t['natal_planet'] == 'Venus']
    jupiter_transits = [t for t in transits if t['natal_planet'] == 'Jupiter']

    venus_score = sum(t['quality_score']['score'] for t in venus_transits)
    jupiter_score = sum(t['quality_score']['score'] for t in jupiter_transits)

    print(f"\nVenus (rules MC, creativity, design): {len(venus_transits)} transits, total score: {venus_score:+d}")
    print(f"Jupiter (10th house, career expansion): {len(jupiter_transits)} transits, total score: {jupiter_score:+d}")

    if venus_score > jupiter_score:
        print("\n→ STRONGER SUPPORT: Creative/design work path")
        print("  Venus transits indicate better support for hands-on creative expression")
    elif jupiter_score > venus_score:
        print("\n→ STRONGER SUPPORT: Technical/expansion work path")
        print("  Jupiter transits indicate better support for growth, learning, innovation")
    else:
        print("\n→ BALANCED SUPPORT: Hybrid approach recommended")
        print("  Equal transit support suggests combining creative work with technical projects")

    # SPECIFIC TIMING RECOMMENDATIONS
    print("\n" + "-"*80)
    print("SPECIFIC TIMING RECOMMENDATIONS")
    print("-"*80)

    # Find best application windows (high career + health scores)
    print("\nBest Work Application Windows:")
    for quarter_key, quarter_data in sorted_quarters:
        summary = generate_quarter_summary(quarter_key, quarter_data, natal_chart, timing_context)
        if summary['quality_scores']['overall'] > 15 and summary['quality_scores']['health'] > 5:
            print(f"  - {summary['period']}: {summary['date_range']}")
            print(f"    Overall: {summary['quality_scores']['overall']:+d}, Health: {summary['quality_scores']['health']:+d}")

    print("\nBest Work Start Dates (from auspicious days):")
    if data.get('auspicious_days'):
        for day in data['auspicious_days'][:10]:
            print(f"  - {day['date']}: Score {day['score']:+d}")

    print("\nAvoid Major Commitments:")
    if data.get('challenging_days'):
        for day in data['challenging_days'][:10]:
            print(f"  - {day['date']}: Score {day['score']:+d}")

    print("\n" + "="*80)
    print("END OF REPORT")
    print("="*80)


def main():
    # Load transit data
    profile_name = 'darren'
    start_date = '2025-10-01'
    end_date = '2027-12-31'

    print(f"Loading transit data for {profile_name}...")
    data = load_transit_data(profile_name, start_date, end_date)

    # Generate comprehensive report
    generate_comprehensive_report(data)


if __name__ == '__main__':
    main()
