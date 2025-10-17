#!/usr/bin/env python3
"""Test dynamic Saturn return assessments."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from life_arc_generator import generate_life_arc_timeline

# Generate timeline for Darren_S
print("Generating life arc timeline for Darren_S (ages 0-100)...")
timeline = generate_life_arc_timeline(
    'Darren_S',
    start_age=0,
    end_age=100,
    simplified_mode=True
)

# Display Saturn assessment details
print("\n" + "="*80)
print("SATURN RETURN ASSESSMENTS")
print("="*80)

saturn_assessments = timeline.get('saturn_assessments', [])

if not saturn_assessments:
    print("ERROR: No Saturn assessments found!")
else:
    for i, assessment in enumerate(saturn_assessments, 1):
        print(f"\nSaturn Return #{i}:")
        print(f"  Age: {assessment['return_age']}")
        print(f"  Difficulty Level: {assessment['difficulty_level']}")
        print(f"  Difficulty Score: {assessment['difficulty_score']}")
        print(f"  Aftermath Years: {assessment['aftermath_years']}")
        print(f"  Aftermath Bonus: +{assessment['aftermath_bonus']} points per year")
        print(f"  Indicators:")
        for indicator in assessment['indicators']:
            print(f"    - {indicator}")

# Show convergence scores for Saturn return aftermath years
print("\n" + "="*80)
print("CONVERGENCE SCORES FOR SATURN RETURN YEARS")
print("="*80)

for assessment in saturn_assessments:
    return_age = int(assessment['return_age'])
    aftermath_years = assessment['aftermath_years']

    print(f"\nSaturn Return #{saturn_assessments.index(assessment) + 1} (Age {return_age}):")
    print(f"Aftermath extends {aftermath_years} years (ages {return_age+1}-{return_age+aftermath_years})")
    print(f"\nYear | Score | Reasons")
    print("-" * 80)

    # Check ages around the return
    for age in range(return_age - 1, return_age + aftermath_years + 2):
        if age < 0 or age > 100:
            continue

        from life_arc_generator import get_year_snapshot, calculate_convergence_score
        snapshot = get_year_snapshot(timeline, age)
        score, reasons = calculate_convergence_score(age, snapshot, timeline, simplified_mode=True)

        # Filter for Saturn-related reasons
        saturn_reasons = [r for r in reasons if 'Saturn' in r]

        if age == return_age or saturn_reasons:
            marker = " <-- RETURN" if age == return_age else ""
            marker += " <-- AFTERMATH" if return_age < age <= return_age + aftermath_years else ""
            print(f"{age:4d} | {score:5d} | {', '.join(saturn_reasons)}{marker}")

print("\n" + "="*80)
print("TEST COMPLETE")
print("="*80)
