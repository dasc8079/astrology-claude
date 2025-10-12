#!/usr/bin/env python3
"""
Generate comprehensive life arc synthesis for Dylan
"""

from life_arc_generator import generate_life_arc_timeline
import json
from datetime import datetime

def main():
    # Generate timeline
    print("Generating life arc timeline for Dylan...")
    timeline = generate_life_arc_timeline('dylan', start_age=0, end_age=100)

    # Save complete timeline data to JSON for reference
    output_path = 'profiles/dylan/output/life_arc_timeline_data.json'
    with open(output_path, 'w') as f:
        json.dump(timeline, f, indent=2, default=str)
    print(f"Timeline data saved to: {output_path}")

    # Print summary for the agent to work with
    print("\n" + "="*80)
    print("LIFE ARC TIMELINE SUMMARY FOR DYLAN")
    print("="*80)

    print(f"\nProfile: {timeline['profile']}")
    print(f"Birth: {timeline['birth_data']['date']} at {timeline['birth_data']['time']}")
    print(f"Location: {timeline['birth_data']['location']}")
    print(f"Current age: 32 (as of 2025)")

    print("\n" + "-"*80)
    print("ZODIACAL RELEASING FROM FORTUNE (L1 PERIODS - Major Life Chapters)")
    print("-"*80)
    for i, period in enumerate(timeline['zr_fortune']['l1_periods'], 1):
        current_marker = " ⭐ CURRENT" if period['start_age'] <= 32 <= period['end_age'] else ""
        print(f"\nChapter {i}: {period['sign']} Period (Ages {period['start_age']}-{period['end_age']}){current_marker}")
        print(f"  Lord: {period['lord']}")
        print(f"  Duration: {period['duration']} years")
        if period.get('peak_period'):
            print(f"  ✨ Peak period (bonification)")

    print("\n" + "-"*80)
    print("ZODIACAL RELEASING FROM SPIRIT (L1 PERIODS - Mental/Spiritual Thread)")
    print("-"*80)
    for i, period in enumerate(timeline['zr_spirit']['l1_periods'], 1):
        current_marker = " ⭐ CURRENT" if period['start_age'] <= 32 <= period['end_age'] else ""
        print(f"\nChapter {i}: {period['sign']} Period (Ages {period['start_age']}-{period['end_age']}){current_marker}")
        print(f"  Lord: {period['lord']}")
        print(f"  Duration: {period['duration']} years")

    print("\n" + "-"*80)
    print("FIRDARIA (Planetary Time Lords - Ages 0-75)")
    print("-"*80)
    for period in timeline['firdaria']['major_periods']:
        current_marker = " ⭐ CURRENT" if period['start_age'] <= 32 <= period['end_age'] else ""
        print(f"\n{period['planet']} Period: Ages {period['start_age']}-{period['end_age']}{current_marker}")
        print(f"  Duration: {period['duration']} years")

    print("\n" + "-"*80)
    print("MAJOR CONVERGENCE EVENTS (25+ points)")
    print("-"*80)
    for event in timeline['convergence']['major']:
        current_marker = " ⭐ CURRENT" if event['age'] == 32 else ""
        print(f"\nAge {event['age']}: {event['score']} points{current_marker}")
        for reason in event['reasons'][:5]:  # Show first 5 reasons
            print(f"  - {reason}")

    print("\n" + "-"*80)
    print("SIGNIFICANT CONVERGENCE EVENTS (15-24 points)")
    print("-"*80)
    for event in timeline['convergence']['significant']:
        current_marker = " ⭐ CURRENT" if event['age'] == 32 else ""
        print(f"\nAge {event['age']}: {event['score']} points{current_marker}")
        for reason in event['reasons'][:3]:  # Show first 3 reasons
            print(f"  - {reason}")

    print("\n" + "-"*80)
    print("PLANETARY RETURNS & MAJOR TRANSITS")
    print("-"*80)
    for ret in timeline['planetary_returns']:
        current_marker = " ⭐ NEAR" if abs(ret['age'] - 32) < 2 else ""
        print(f"Age {ret['age']:.1f}: {ret['event']}{current_marker}")

    print("\n" + "-"*80)
    print("PROGRESSED SUN SIGN CHANGES (Major Identity Evolution)")
    print("-"*80)
    for change in timeline['progression_sign_changes']:
        print(f"Age {change['age']}: {change['point']} enters {change['new_sign']}")

    print("\n" + "="*80)
    print("CURRENT POSITION DETAIL (Age 32)")
    print("="*80)

    # Find current profection
    current_prof = next((p for p in timeline['profections'] if p['age'] == 32), None)
    if current_prof:
        print(f"\nProfection Year: {current_prof['house']}H ({current_prof['sign']})")
        print(f"  Time Lord: {current_prof['lord']}")
        print(f"  Lord position: {current_prof['lord_position']['sign']} {current_prof['lord_position']['house']}H")

    # Find current ZR Fortune L2
    for l1 in timeline['zr_fortune']['l1_periods']:
        if l1['start_age'] <= 32 <= l1['end_age']:
            print(f"\nZR Fortune L1: {l1['sign']} (Ages {l1['start_age']}-{l1['end_age']})")
            for l2 in l1.get('l2_periods', []):
                if l2['start_age'] <= 32 <= l2['end_age']:
                    print(f"  L2: {l2['sign']} (Ages {l2['start_age']:.1f}-{l2['end_age']:.1f})")

    # Find current ZR Spirit L2
    for l1 in timeline['zr_spirit']['l1_periods']:
        if l1['start_age'] <= 32 <= l1['end_age']:
            print(f"\nZR Spirit L1: {l1['sign']} (Ages {l1['start_age']}-{l1['end_age']})")
            for l2 in l1.get('l2_periods', []):
                if l2['start_age'] <= 32 <= l2['end_age']:
                    print(f"  L2: {l2['sign']} (Ages {l2['start_age']:.1f}-{l2['end_age']:.1f})")

    # Find current Firdaria
    for major in timeline['firdaria']['major_periods']:
        if major['start_age'] <= 32 <= major['end_age']:
            print(f"\nFirdaria: {major['planet']} major period (Ages {major['start_age']}-{major['end_age']})")
            for sub in timeline['firdaria']['sub_periods']:
                if sub['major_planet'] == major['planet'] and sub['start_age'] <= 32 <= sub['end_age']:
                    print(f"  Sub-period: {sub['sub_planet']} (Ages {sub['start_age']:.1f}-{sub['end_age']:.1f})")

    print("\n" + "="*80)
    print(f"\nFull timeline data saved to: {output_path}")
    print("Ready for life-arc-interpreter agent to create synthesis!")
    print("="*80)

if __name__ == '__main__':
    main()
