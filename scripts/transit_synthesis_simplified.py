#!/usr/bin/env python3
"""
Transit Synthesis - Simplified (No RAG)
Generates basic transit report from calculator JSON data.

Purpose: Quick testing and data structure validation
- Template-based interpretations (no RAG database queries)
- ~2K word markdown output
- Validates JSON structure is synthesizable

Usage:
    python transit_synthesis_simplified.py --json-file transit_data_darren_2025-01-15_to_2025-07-15.json
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

# Simple interpretation templates
ASPECT_TEMPLATES = {
    'conjunction': {
        'benefic': "brings opportunities and growth through {area}",
        'malefic': "tests and challenges in {area}, requiring discipline",
        'neutral': "activates {area} with significant intensity"
    },
    'sextile': {
        'benefic': "offers favorable opportunities in {area}",
        'malefic': "presents manageable challenges in {area}",
        'neutral': "supports development in {area}"
    },
    'square': {
        'benefic': "creates tension requiring adjustment in {area}",
        'malefic': "presents significant obstacles in {area}",
        'neutral': "demands action and resolution in {area}"
    },
    'trine': {
        'benefic': "flows easily and harmoniously in {area}",
        'malefic': "eases difficulties in {area}",
        'neutral': "supports natural expression in {area}"
    },
    'opposition': {
        'benefic': "requires balancing priorities in {area}",
        'malefic': "polarizes and externalizes challenges in {area}",
        'neutral': "brings awareness through contrast in {area}"
    }
}

def get_quality_label(score: int) -> str:
    """Get quality label from score."""
    if score > 3:
        return 'benefic'
    elif score < -3:
        return 'malefic'
    else:
        return 'neutral'

def get_planet_area(planet: str) -> str:
    """Get life area associated with planet."""
    areas = {
        'Sun': 'identity and vitality',
        'Moon': 'emotional life and home',
        'Mercury': 'communication and thinking',
        'Venus': 'relationships and values',
        'Mars': 'action and assertiveness',
        'Jupiter': 'growth and opportunity',
        'Saturn': 'structure and responsibility',
        'Uranus': 'change and innovation',
        'Neptune': 'ideals and spirituality',
        'Pluto': 'transformation and power'
    }
    return areas.get(planet, 'this area of life')

def interpret_transit(transit: dict) -> str:
    """Generate simple interpretation for a transit."""
    trans_planet = transit['transiting_planet']
    natal_planet = transit['natal_planet']
    aspect = transit['aspect_type']
    score = transit['quality_score']['score']
    quality = get_quality_label(score)

    # Get template
    template = ASPECT_TEMPLATES.get(aspect, {}).get(quality, "affects {area}")
    area = get_planet_area(natal_planet)
    interpretation = template.format(area=area)

    # Build full description
    text = f"**Transiting {trans_planet} {aspect} Natal {natal_planet}**"
    text += f" (orb {transit['orb']:.1f}°"
    if transit.get('exact'):
        text += ", EXACT"
    text += f", quality score: {score:+d})\n\n"
    text += f"This transit {interpretation}. "

    # Add exact/applying note
    if transit.get('exact'):
        text += "The aspect is exact, making this a particularly potent time. "
    elif transit.get('applying'):
        text += "The aspect is applying (building in strength). "

    return text

def synthesize_report(json_data: dict) -> str:
    """Generate simplified synthesis from JSON data."""

    profile = json_data['profile']
    date_range = json_data['date_range']
    age = json_data['current_age']
    timing = json_data['current_timing']

    # Start report
    report = f"# Transit Report: {profile.title()}\n\n"
    report += f"**Period**: {date_range['start']} to {date_range['end']} ({date_range['days']} days)\n\n"
    report += f"**Current Age**: {age}\n\n"
    report += "---\n\n"

    # Current Timing Context
    report += "## Current Timing Context\n\n"

    profection = timing.get('profection', {})
    if profection:
        profection_data = profection.get('profection', {})
        lord = profection_data.get('lord_of_year')
        house = profection_data.get('profected_house')
        report += f"This period occurs during your **{age}th year**, with **{lord} as Lord of the Year**. "
        report += f"This activates your natal **{house} house**, making {lord} themes particularly significant.\n\n"

    # ZR context
    zr_f_l1 = timing.get('zr_fortune_l1')
    if zr_f_l1:
        sign = zr_f_l1.get('period_sign')
        ruler = zr_f_l1.get('ruler')
        report += f"You are currently in a **{sign} period** of Zodiacal Releasing from Fortune "
        report += f"(ruled by {ruler}), a major life chapter focused on material circumstances and bodily well-being.\n\n"

    zr_f_l2 = timing.get('zr_fortune_l2')
    if zr_f_l2:
        sign = zr_f_l2.get('period_sign')
        ruler = zr_f_l2.get('ruler')
        is_peak = zr_f_l2.get('is_peak', False)
        report += f"Within this chapter, you're in a **{sign} sub-period** (ruled by {ruler})"
        if is_peak:
            report += " — a **peak period** of heightened significance"
        report += ".\n\n"

    firdaria = timing.get('firdaria')
    if firdaria:
        major = firdaria.get('major_period_lord')
        sub = firdaria.get('sub_period_lord')
        if major and sub:
            report += f"The Firdaria time-lord system places you in a **{major}/{sub} period**, "
            report += f"emphasizing {major} themes with {sub} sub-themes.\n\n"

    report += "---\n\n"

    # Critical Transits
    critical = json_data['transits_by_tier']['critical']
    if critical:
        report += "## Critical Transits\n\n"
        report += f"These {len(critical)} transits are of highest importance, involving the Lord of the Year, "
        report += "sect light, or exact aspects:\n\n"

        for t in critical[:10]:  # Limit to 10 most critical
            report += interpret_transit(t) + "\n"

        if len(critical) > 10:
            report += f"\n*({len(critical) - 10} additional critical transits not shown for brevity)*\n\n"
    else:
        report += "## Critical Transits\n\nNo critical transits during this period.\n\n"

    report += "---\n\n"

    # Important Transits
    important = json_data['transits_by_tier']['important']
    if important:
        report += "## Important Transits\n\n"
        report += f"These {len(important)} transits are significant, though not at the critical tier:\n\n"

        for t in important[:5]:  # Show first 5
            report += interpret_transit(t) + "\n"

        if len(important) > 5:
            report += f"\n*({len(important) - 5} additional important transits not shown for brevity)*\n\n"
    else:
        report += "## Important Transits\n\nNo important transits during this period.\n\n"

    # Eclipses
    eclipses = json_data.get('eclipses', [])
    if eclipses:
        report += "---\n\n## Eclipses\n\n"
        for eclipse in eclipses:
            report += f"- **{eclipse['date']}**: {eclipse['type']} Eclipse at {eclipse['sign']} {eclipse['degree']}°\n"
        report += "\n"

    # Summary
    report += "---\n\n## Summary\n\n"
    total = len(json_data['all_transits'])
    report += f"This {date_range['days']}-day period contains **{total} total transits** "
    report += f"({len(critical)} critical, {len(important)} important). "

    if critical:
        report += "Focus your attention on the critical transits listed above, "
        report += "as these have the greatest impact during this timeframe. "

    if timing.get('profection'):
        profection_data = timing['profection'].get('profection', {})
        lord = profection_data.get('lord_of_year')
        if lord:
            report += f"Throughout this period, remember that **{lord}** is your Lord of the Year, "
            report += f"making transits involving {lord} especially significant.\n\n"

    report += f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
    report += f"*Source: Simplified synthesis (template-based, no RAG)*\n"

    return report

def main():
    parser = argparse.ArgumentParser(
        description='Generate simplified transit synthesis from JSON data'
    )
    parser.add_argument('--json-file', required=True, help='Path to transit JSON data file')
    parser.add_argument('--output', help='Output markdown file (default: auto-generate)')

    args = parser.parse_args()

    # Load JSON data
    json_path = Path(args.json_file)
    if not json_path.exists():
        print(f"❌ JSON file not found: {json_path}")
        return 1

    with open(json_path) as f:
        json_data = json.load(f)

    # Generate synthesis
    print(f"📝 Generating simplified synthesis...")
    report = synthesize_report(json_data)

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        # Auto-generate from JSON filename
        base_name = json_path.stem.replace('transit_data_', 'transit_report_')
        output_path = json_path.parent / f"{base_name}_simplified.md"

    # Save report
    with open(output_path, 'w') as f:
        f.write(report)

    word_count = len(report.split())
    print(f"\n✅ Synthesis complete!")
    print(f"   Output: {output_path}")
    print(f"   Length: {word_count} words")
    print(f"   Transits: {len(json_data['all_transits'])} total")

    return 0

if __name__ == '__main__':
    sys.exit(main())
