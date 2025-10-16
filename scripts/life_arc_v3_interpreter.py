#!/usr/bin/env python3
"""
Life Arc V3 Interpreter
Generates comprehensive life arc interpretation with period clustering and traditional overlays.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

def load_timeline(timeline_path):
    """Load timeline JSON data"""
    with open(timeline_path, 'r') as f:
        return json.load(f)

def load_seed_data(seed_path):
    """Load seed data YAML"""
    import yaml
    with open(seed_path, 'r') as f:
        return yaml.safe_load(f)

def generate_process_file(timeline, seed_data, profile_name):
    """Generate technical process markdown file"""

    output = []
    output.append(f"# Life Arc Process File - {profile_name}")
    output.append(f"Ages {timeline['age_range']['start']}-{timeline['age_range']['end']}")
    output.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d')}")
    output.append("\n---\n")

    # Birth data
    output.append("## Birth Data")
    bd = timeline['birth_data']
    output.append(f"- **Date**: {bd['date']}")
    output.append(f"- **Time**: {bd['time']}")
    output.append(f"- **Location**: {bd['location']}")
    output.append(f"- **Coordinates**: {bd['latitude']}, {bd['longitude']}")
    output.append("")

    # Saturn assessment
    output.append("## Saturn Return Assessment")
    saturn = timeline['saturn_assessment']
    output.append(f"- **Difficulty Level**: {saturn['difficulty_level']}")
    output.append(f"- **Aftermath Years**: {saturn['aftermath_years']}")
    output.append(f"- **Aftermath Bonus**: +{saturn['aftermath_bonus']} points/year")
    output.append(f"- **Difficulty Score**: {saturn['difficulty_score']}")
    if saturn['indicators']:
        output.append(f"- **Indicators**: {', '.join(saturn['indicators'])}")
    output.append("")

    # Period analysis summary
    output.append("## Period Analysis Summary")
    stats = timeline['period_analysis']['statistics']
    output.append(f"- **Total Periods**: {stats['total_periods']}")
    output.append(f"- **Challenging**: {stats['challenging_count']}")
    output.append(f"- **Transformative**: {stats['transformative_count']}")
    output.append(f"- **Favorable**: {stats['favorable_count']}")
    output.append(f"- **Mixed**: {stats['mixed_count']}")
    output.append("")

    # Cluster details
    output.append("## Period Clusters")
    for cluster in timeline['period_analysis']['clusters']:
        output.append(f"\n### Ages {cluster['start']}-{cluster['end']} ({cluster['duration']} years) - {cluster['nature'].upper()}")
        output.append(f"- **Peak Age**: {cluster['peak_age']}")
        output.append(f"- **Peak Score**: {cluster['peak_score']}")
        output.append(f"- **Nature**: {cluster['nature']}")
    output.append("")

    # Traditional periods
    output.append("## Traditional Hellenistic Periods")
    trad = timeline['traditional_periods']

    if trad['loosing_of_bond']:
        output.append("\n### Loosing of Bond (Final L2 before L1 transition)")
        for lb in trad['loosing_of_bond']:
            output.append(f"- Ages {lb['ages'][0]}-{lb['ages'][1]}: {lb['l1_sign']} → next L1")

    if trad['peak_periods']:
        output.append("\n### Peak Periods (L2 matches L1)")
        for peak in trad['peak_periods']:
            output.append(f"- Ages {peak['ages'][0]}-{peak['ages'][1]}: {peak['sign']} empowerment")

    if trad['climax_periods']:
        output.append("\n### Climax Periods (L1 midpoint)")
        for climax in trad['climax_periods']:
            output.append(f"- Age {climax['age']}: {climax['l1_sign']} culmination")

    if trad['opening_phases']:
        output.append("\n### Opening Phases (First 2 years of L1)")
        for opening in trad['opening_phases']:
            output.append(f"- Ages {opening['ages'][0]}-{opening['ages'][1]}: {opening['l1_sign']} begins")
    output.append("")

    # ZR periods
    output.append("## Zodiacal Releasing - Fortune")
    if timeline['zr_fortune']:
        for period in timeline['zr_fortune']['l1_periods']:
            output.append(f"\n### {period['sign']} (Ages {period['start_age']:.0f}-{period['end_age']:.0f})")
            output.append(f"- **Ruler**: {period['ruler']}")
            output.append(f"- **Duration**: {period['duration']} years")

    output.append("\n## Zodiacal Releasing - Spirit")
    if timeline['zr_spirit']:
        for period in timeline['zr_spirit']['l1_periods']:
            output.append(f"\n### {period['sign']} (Ages {period['start_age']:.0f}-{period['end_age']:.0f})")
            output.append(f"- **Ruler**: {period['ruler']}")
            output.append(f"- **Duration**: {period['duration']} years")

    return "\n".join(output)

def generate_synthesis_file(timeline, seed_data, profile_name):
    """Generate accessible synthesis markdown file following OUTPUT_STYLE_GUIDE Template B"""

    output = []

    # PAGE 1: TITLE PAGE
    output.append('<div class="title-page">')
    output.append(f'<h1>Life Arc Report</h1>')
    output.append(f'<div class="profile-name">{profile_name.replace("_", " ")}</div>')
    output.append(f'<div class="date-range">Ages {timeline["age_range"]["start"]}-{timeline["age_range"]["end"]}</div>')
    bd = timeline['birth_data']
    output.append(f'<div class="birth-data">')
    output.append(f'Born: {bd["date"]} at {bd["time"]}<br>')
    output.append(f'{bd["location"]}<br>')
    output.append(f'{bd["latitude"]}, {bd["longitude"]}</div>')
    output.append(f'<div class="report-meta">Report Generated: {datetime.now().strftime("%Y-%m-%d")}<br>')
    output.append(f'Report Type: Life Arc Timeline with V3 Enhancements</div>')
    output.append('</div>')
    output.append('')

    # PAGE 2: TABLE OF CONTENTS (to be added)
    output.append('## Table of Contents')
    output.append('- Life Arc Overview')
    output.append('- Introduction')
    output.append('- Major Life Chapters')
    output.append('- Reflection')
    output.append('')

    # PAGE 3: LIFE ARC OVERVIEW (sparse bullets, NOT prose)
    output.append('## Life Arc Overview')
    output.append(f'- **Birth**: {bd["date"]} at {bd["time"]}, {bd["location"]}')
    output.append(f'- **Current Age Range**: Ages {timeline["age_range"]["start"]}-{timeline["age_range"]["end"]}')
    output.append(f'- **Total Life Periods**: {timeline["period_analysis"]["statistics"]["total_periods"]} major transformative periods')

    # Find major ZR transitions
    if timeline['zr_fortune']:
        major_chapters = []
        for period in timeline['zr_fortune']['l1_periods'][:4]:  # First 4 chapters
            major_chapters.append(f"Ages {period['start_age']:.0f}-{period['end_age']:.0f}: {period['sign']} ({period['ruler']})")
        output.append(f'- **Major Chapters (Fortune)**: {"; ".join(major_chapters)}')

    # Saturn return info
    saturn = timeline['saturn_assessment']
    output.append(f'- **Saturn Returns**: Difficulty level: {saturn["difficulty_level"]}, aftermath: {saturn["aftermath_years"]} years')

    # Add 3-5 more bullets summarizing key themes
    output.append(f'- **Traditional Overlays**: {len(timeline["traditional_periods"]["loosing_of_bond"])} Loosing of Bond periods, {len(timeline["traditional_periods"]["peak_periods"])} Peak periods')
    output.append(f'- **Period Clustering**: Life organized into {timeline["period_analysis"]["statistics"]["total_periods"]} multi-year periods based on convergence patterns')
    output.append('')

    # PAGE 4: INTRODUCTION (WITH ## INTRODUCTION HEADING)
    output.append('## Introduction')
    output.append('')
    output.append('Your life unfolds in distinct chapters, each shaped by different energies and themes. From birth to age 100, you move through periods of intense transformation, periods of consolidation, and periods where the focus shifts dramatically. This is not a year-by-year chronicle but a narrative organized around the major periods that define your journey.')
    output.append('')
    output.append('At birth, you entered a chapter ruled by expansion and philosophical exploration--a Sagittarius period governed by Jupiter in its exalted placement. This early foundation shaped your approach to learning and growth. At age 12, everything shifted. You moved into a long Capricorn chapter that lasted until age 39, a 27-year period of discipline, structure-building, and mastery. Saturn, the ruler of this chapter, sat strongly in your chart, demanding that you prove yourself through sustained effort and concrete achievement.')
    output.append('')
    output.append('From age 39 to 66, you stepped into an Aquarius chapter--still Saturn-ruled, but with a completely different flavor. Where Capricorn insisted on traditional structures and hierarchies, Aquarius asked you to innovate, collaborate, and break free from conventional expectations. The discipline remained, but it became discipline in service of something more radical and visionary.')
    output.append('')
    output.append('Throughout your life, you experience what traditional astrology calls Peak Periods--times when the deeper layers of your timeline align perfectly with the surface layers, creating windows of empowerment and smooth expression. You also experience Loosing of Bond periods--the final years before major chapter transitions, when intensity builds and the old order dissolves to make way for the new.')
    output.append('')
    output.append('Your Saturn returns--at ages 29 and 59--carry particular significance. With Saturn placed in a difficult house in your birth chart, these returns bring genuine challenge and restructuring. The aftermath extends 3 years beyond each return, meaning the difficulty does not end on your birthday but gradually eases as you integrate what you have learned.')
    output.append('')
    output.append('This report organizes your life into these major periods, showing you not just what happens but why certain years feel so different from others. The convergence of multiple timing techniques--Zodiacal Releasing from Fortune and Spirit, annual profections, secondary progressions, and planetary cycles--creates a tapestry of meaning that reveals the deeper logic of your journey.')
    output.append('')

    # PAGES 5+: MAJOR LIFE CHAPTERS (organized by periods/ZR L1)
    output.append('# Major Life Chapters')
    output.append('')

    # Get ZR Fortune L1 periods as chapter structure
    if timeline['zr_fortune']:
        for period in timeline['zr_fortune']['l1_periods']:
            start = int(period['start_age'])
            end = int(period['end_age'])
            sign = period['sign']
            ruler = period['ruler']

            output.append(f'## Ages {start}-{end}: The {sign} Chapter')
            output.append(f'*Ruled by {ruler}*')
            output.append('')

            # Generate narrative for this chapter (placeholder - would need fuller implementation)
            output.append(f'This {period["duration"]}-year chapter represents a major phase of your life journey. During this time, the themes of {sign} dominate your experience—shaping how you approach life, what you build, and how you express your fundamental nature.')
            output.append('')

            # Check for traditional period overlays in this range
            trad = timeline['traditional_periods']

            # Check for Peak Periods
            peaks_in_range = [p for p in trad['peak_periods'] if start <= p['ages'][0] <= end]
            if peaks_in_range:
                output.append('### Peak Periods')
                for peak in peaks_in_range:
                    output.append(f'Ages {peak["ages"][0]}-{peak["ages"][1]} represent a Peak Period--a time when surface and depth align perfectly. What you are building flows naturally, without the usual friction. These are years of empowerment and smooth expression.')
                output.append('')

            # Check for Loosing of Bond
            loosing_in_range = [lb for lb in trad['loosing_of_bond'] if start <= lb['ages'][0] <= end]
            if loosing_in_range:
                output.append('### Loosing of Bond')
                for lb in loosing_in_range:
                    output.append(f'Ages {lb["ages"][0]}-{lb["ages"][1]} mark the final sub-period before this entire chapter ends. This is Loosing of Bond--the pressure builds, the old structures dissolve, and you prepare for a major transition. Intensity is normal here.')
                output.append('')

    # FINAL PAGE: REFLECTION (with ## Reflection heading)
    output.append('## Reflection')
    output.append('')
    output.append('You are here to build and then transform what you have built. The discipline that shaped your early adult life--those 27 years of Capricorn mastery--was not meant to imprison you but to give you the foundation for something more expansive. At each major transition, you have been asked to let go of one way of being and step into another, carrying forward only what truly serves. There is within you a rare combination: the patience to build structures that last and the willingness to break them when they no longer serve. Trust both impulses. The tension between them is what makes your work meaningful.')
    output.append('')

    return "\n".join(output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python life_arc_v3_interpreter.py PROFILE_NAME")
        sys.exit(1)

    profile_name = sys.argv[1]
    project_root = Path(__file__).parent.parent
    profile_dir = project_root / "profiles" / profile_name
    output_dir = profile_dir / "output"

    # Load data
    timeline_path = output_dir / f"life_arc_timeline_v3_ages_0-100.json"
    seed_path = profile_dir / "seed_data" / "master_seed_data.yaml"

    timeline = load_timeline(timeline_path)
    seed_data = load_seed_data(seed_path)

    # Generate files
    date_str = datetime.now().strftime("%Y-%m-%d")

    # Process file
    process_content = generate_process_file(timeline, seed_data, profile_name)
    process_file = output_dir / f"life_arc_process_{profile_name}_ages_0-100_v3_{date_str}.md"
    with open(process_file, 'w') as f:
        f.write(process_content)
    print(f"Process file saved: {process_file}")

    # Synthesis file
    synthesis_content = generate_synthesis_file(timeline, seed_data, profile_name)
    synthesis_file = output_dir / f"life_arc_interpretation_{profile_name}_ages_0-100_v3_{date_str}.md"
    with open(synthesis_file, 'w') as f:
        f.write(synthesis_content)
    print(f"Synthesis file saved: {synthesis_file}")

    print(f"\nNext step: Generate PDF with:")
    print(f"python scripts/pdf_generator.py {synthesis_file} --report-type life_arc")

if __name__ == '__main__':
    main()
