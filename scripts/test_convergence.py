#!/usr/bin/env python3
"""
Test Convergence Detection - Quick Analysis
Calculate convergence scores and show flagged events.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from life_arc_generator import generate_life_arc_timeline, get_year_snapshot

def calculate_convergence_score(snapshot, age, timeline):
    """Calculate convergence score for a given age."""
    score = 0
    reasons = []

    # TIER 1 - RARE MULTI-DECADE EVENTS (20 points)
    # Check ZR L1 transitions (sign changes)
    if snapshot['fortune_l1']:
        fortune_start = snapshot['fortune_l1'].get('start_age', 0)
        if abs(age - fortune_start) < 0.5:  # Within 6 months of transition
            score += 20
            reasons.append(f"ZR Fortune L1 → {snapshot['fortune_l1']['sign']} (20pts)")

    if snapshot['spirit_l1']:
        spirit_start = snapshot['spirit_l1'].get('start_age', 0)
        if abs(age - spirit_start) < 0.5:
            score += 20
            reasons.append(f"ZR Spirit L1 → {snapshot['spirit_l1']['sign']} (20pts)")

    # Check progressed Sun sign changes
    for prog_change in timeline.get('progression_sign_changes', []):
        if abs(age - prog_change['age']) < 0.5:
            score += 20
            reasons.append(f"Progressed Sun → {prog_change['new_sign']} (20pts)")

    # TIER 2 - MAJOR MILESTONES (10-15 points)
    for return_event in timeline.get('planetary_returns', []):
        if abs(age - return_event['age']) < 0.5:
            if return_event['planet'] == 'Saturn':
                score += 15
                reasons.append(f"{return_event['event']} (15pts)")
            elif return_event['planet'] == 'Uranus':
                score += 15
                reasons.append(f"{return_event['event']} (15pts)")
            elif return_event['planet'] == 'Jupiter':
                score += 5
                reasons.append(f"{return_event['event']} (5pts)")

    # Check Firdaria major transitions
    if snapshot['firdaria_major']:
        fir_start = snapshot['firdaria_major'].get('start_age', 0)
        if abs(age - fir_start) < 0.5:
            score += 10
            reasons.append(f"Firdaria → {snapshot['firdaria_major']['planet']} (10pts)")

    # TIER 3 - REGULAR CYCLES (1-2 points)
    # Firdaria sub-period transitions
    if snapshot['firdaria_sub']:
        sub_start = snapshot['firdaria_sub'].get('start_age', 0)
        if abs(age - sub_start) < 0.5:
            score += 2
            reasons.append(f"Firdaria sub → {snapshot['firdaria_sub']['sub_planet']} (2pts)")

    # Annual profection
    score += 1

    return score, reasons


def analyze_convergence(profile_name='darren', start_age=0, end_age=100):
    """Analyze convergence for entire timeline."""
    print(f"\n{'='*80}")
    print(f"CONVERGENCE ANALYSIS: {profile_name.upper()}")
    print(f"{'='*80}\n")

    # Generate timeline
    print("Generating timeline data...")
    timeline = generate_life_arc_timeline(profile_name, start_age, end_age)

    major_events = []
    significant_events = []
    notable_events = []

    # Calculate scores for each year
    for age in range(start_age, end_age + 1):
        snapshot = get_year_snapshot(timeline, age)
        score, reasons = calculate_convergence_score(snapshot, age, timeline)

        if score >= 25:
            major_events.append((age, score, reasons))
        elif score >= 15:
            significant_events.append((age, score, reasons))
        elif score >= 8:
            notable_events.append((age, score, reasons))

    # Display results
    print(f"🔥 MAJOR LIFE EVENTS (25+ points) - Chapter-defining moments")
    print(f"{'='*80}")
    if major_events:
        for age, score, reasons in major_events:
            print(f"\nAge {age}: {score} points")
            for reason in reasons:
                print(f"  • {reason}")
    else:
        print("None found in this age range.\n")

    print(f"\n{'='*80}")
    print(f"⭐ SIGNIFICANT TRANSITIONS (15-24 points) - Major milestones")
    print(f"{'='*80}")
    if significant_events:
        for age, score, reasons in significant_events:
            print(f"\nAge {age}: {score} points")
            for reason in reasons:
                print(f"  • {reason}")
    else:
        print("None found in this age range.\n")

    print(f"\n{'='*80}")
    print(f"✓ NOTABLE PERIODS (8-14 points) - Worth mentioning")
    print(f"{'='*80}")
    if notable_events:
        for age, score, reasons in notable_events:
            print(f"\nAge {age}: {score} points")
            for reason in reasons:
                print(f"  • {reason}")
    else:
        print("None found in this age range.\n")

    print(f"\n{'='*80}")
    print(f"SUMMARY:")
    print(f"  Major Events: {len(major_events)}")
    print(f"  Significant Transitions: {len(significant_events)}")
    print(f"  Notable Periods: {len(notable_events)}")
    print(f"  Total Highlighted: {len(major_events) + len(significant_events) + len(notable_events)}")
    print(f"{'='*80}\n")


if __name__ == '__main__':
    analyze_convergence()
