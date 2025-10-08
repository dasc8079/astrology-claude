#!/usr/bin/env python3
"""
Generate long-term transit report following transit-analyzer-long agent format.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def load_transit_data(json_path):
    """Load transit JSON data."""
    with open(json_path, 'r') as f:
        return json.load(f)

def generate_quick_reference_tables(data):
    """Generate Quick Reference tables with brief interpretations."""
    output = []
    output.append("## Quick Reference: Points of Interest\n")

    # Most Auspicious Day (THE single best)
    most_auspicious = data.get('most_auspicious_day')
    if most_auspicious:
        output.append("### THE Most Auspicious Day\n")
        output.append("| Date | Score | Key Transits | Brief Interpretation |")
        output.append("|------|-------|--------------|---------------------|")
        date = most_auspicious['date']
        score = most_auspicious['score']
        transits_summary = f"{len(most_auspicious['transits'])} favorable transits active"
        # Get top 2-3 transits for summary
        top_transits = sorted(most_auspicious['transits'], key=lambda x: x.get('score', 0), reverse=True)[:3]
        transit_names = ", ".join([f"{t['transiting']} {t['aspect']} {t['natal']}" for t in top_transits])
        interpretation = f"Peak opportunity day - {transits_summary}, especially {transit_names}"
        output.append(f"| **{date}** | +{score} | {transit_names} | {interpretation} |")
        output.append("")

    # Most Auspicious Days (top 10-20)
    auspicious_days = data.get('auspicious_days', [])
    if auspicious_days:
        output.append("### Most Auspicious Days\n")
        output.append("| Date | Score | Key Transits | Brief Interpretation |")
        output.append("|------|-------|--------------|---------------------|")
        for day_entry in auspicious_days[:10]:  # Limit to top 10 for 30-day period
            date = day_entry['date']
            score = day_entry['score']
            top_transits = sorted(day_entry['transits'], key=lambda x: x.get('score', 0), reverse=True)[:2]
            transit_names = ", ".join([f"{t['transiting']} {t['aspect']} {t['natal']}" for t in top_transits])
            interpretation = f"Favorable period with {len(day_entry['transits'])} supportive transits"
            output.append(f"| {date} | +{score} | {transit_names} | {interpretation} |")
        output.append("")

    # Most Challenging Day (THE single hardest)
    most_challenging = data.get('most_challenging_day')
    if most_challenging:
        output.append("### THE Most Challenging Day\n")
        output.append("| Date | Score | Key Transits | Brief Interpretation |")
        output.append("|------|-------|--------------|---------------------|")
        date = most_challenging['date']
        score = most_challenging['score']
        transits_summary = f"{len(most_challenging['transits'])} difficult transits active"
        # Get top 2-3 challenging transits
        challenging_transits = sorted(most_challenging['transits'], key=lambda x: x.get('score', 0))[:3]
        transit_names = ", ".join([f"{t['transiting']} {t['aspect']} {t['natal']}" for t in challenging_transits])
        interpretation = f"Most difficult day - {transits_summary}, requiring patience and care with {transit_names}"
        output.append(f"| **{date}** | {score} | {transit_names} | {interpretation} |")
        output.append("")

    # Most Challenging Days (bottom 10-20)
    challenging_days = data.get('challenging_days', [])
    if challenging_days:
        output.append("### Most Challenging Days\n")
        output.append("| Date | Score | Key Transits | Brief Interpretation |")
        output.append("|------|-------|--------------|---------------------|")
        for day_entry in challenging_days[:10]:  # Limit to top 10 for 30-day period
            date = day_entry['date']
            score = day_entry['score']
            challenging_transits = sorted(day_entry['transits'], key=lambda x: x.get('score', 0))[:2]
            transit_names = ", ".join([f"{t['transiting']} {t['aspect']} {t['natal']}" for t in challenging_transits])
            interpretation = f"Challenging period with {len(day_entry['transits'])} difficult transits"
            output.append(f"| {date} | {score} | {transit_names} | {interpretation} |")
        output.append("")

    # Peak/Low Periods
    peak_periods = data.get('peak_periods', [])
    low_periods = data.get('low_periods', [])

    if peak_periods or low_periods:
        output.append("### Major Periods of Interest\n")
        output.append("| Period | Type | Avg Score | Theme | What This Means |")
        output.append("|--------|------|-----------|-------|-----------------|")

        for period in peak_periods:
            start = period['start_date']
            end = period['end_date']
            avg_score = period['average_score']
            days = period['consecutive_days']
            output.append(f"| {start} to {end} | Peak Period | +{avg_score:.1f} | {days}-day high period | Extended favorable window for action |")

        for period in low_periods:
            start = period['start_date']
            end = period['end_date']
            avg_score = period['average_score']
            days = period['consecutive_days']
            output.append(f"| {start} to {end} | Low Period | {avg_score:.1f} | {days}-day challenging period | Extended caution period, focus on patience |")

        output.append("")

    output.append("---\n")
    return "\n".join(output)

def generate_report_header(data):
    """Generate report header with metadata."""
    profile_name = data.get('profile', 'Unknown')
    timing = data.get('current_timing', {})
    date_range = data.get('date_range', {})
    natal_chart = data.get('natal_chart', {})

    output = []
    output.append(f"# Long-Term Transit Report: {profile_name.title()}\n")
    output.append(f"**Report Period**: {date_range.get('start', 'Unknown')} to {date_range.get('end', 'Unknown')}")
    output.append(f"**Current Age**: {data.get('current_age', 'Unknown')}")

    sect = natal_chart.get('sect', {}).get('type', 'Unknown')
    # Get rising sign from first house or planets
    rising = 'Unknown'  # Would need to calculate from planets
    # Get Sun and Moon signs from planets
    planets = natal_chart.get('planets', [])
    sun_sign = next((p['sign'] for p in planets if p['name'] == 'Sun'), 'Unknown')
    moon_sign = next((p['sign'] for p in planets if p['name'] == 'Moon'), 'Unknown')
    output.append(f"**Birth Chart**: {sect.title()} Chart, Sun in {sun_sign}, Moon in {moon_sign}")

    # Timing context
    profection_data = timing.get('profection', {}).get('profection', {})
    lord_of_year = profection_data.get('lord_of_year', 'Unknown')

    zr_fortune = timing.get('zodiacal_releasing', {}).get('fortune', {})
    fortune_l2 = zr_fortune.get('L2', {})
    fortune_l2_sign = fortune_l2.get('sign', 'Unknown') if fortune_l2 else 'Unknown'

    zr_spirit = timing.get('zodiacal_releasing', {}).get('spirit', {})
    spirit_l2 = zr_spirit.get('L2', {})
    spirit_l2_sign = spirit_l2.get('sign', 'Unknown') if spirit_l2 else 'Unknown'

    firdaria_data = timing.get('firdaria', {})
    firdaria_major = firdaria_data.get('major_lord', 'Unknown') if firdaria_data else 'Unknown'

    output.append(f"**Current Timing**: Lord of Year: {lord_of_year}, ZR Fortune L2: {fortune_l2_sign}, ZR Spirit L2: {spirit_l2_sign}, Firdaria: {firdaria_major}")
    output.append("\n---\n")

    return "\n".join(output)

def generate_narrative(data):
    """Generate flowing narrative organized by time periods."""
    output = []

    # For a 30-day period, use weekly sub-sections
    output.append("# October 2025: Navigating the Current Chapter\n")

    # Opening paragraph with context
    timing = data.get('current_timing', {})
    profection_data = timing.get('profection', {}).get('profection', {})
    lord_of_year = profection_data.get('lord_of_year', 'Sun')

    output.append(f"This thirty-day period occurs during your 36th year, with **{lord_of_year}** as Lord of the Year. This makes all transits involving {lord_of_year} especially significant, as they activate your annual profection house and themes.\n")

    # Mention ZR context
    zr_fortune = timing.get('zodiacal_releasing', {}).get('fortune', {})
    fortune_l2 = zr_fortune.get('L2', {})
    fortune_l2_sign = fortune_l2.get('sign', 'Scorpio') if fortune_l2 else 'Scorpio'
    fortune_l2_lord = fortune_l2.get('lord', 'Mars') if fortune_l2 else 'Mars'

    output.append(f"You remain in a **{fortune_l2_sign} Fortune sub-period** ruled by {fortune_l2_lord}, adding weight to transits involving {fortune_l2_lord} as the current sub-chapter time-lord.\n")

    # Highlight THE most auspicious day
    most_auspicious = data.get('most_auspicious_day')
    if most_auspicious:
        date = most_auspicious['date']
        score = most_auspicious['score']
        output.append(f"\n**{date} emerges as the single most auspicious day of this entire period** (quality score: +{score}). ")
        top_transits = sorted(most_auspicious['transits'], key=lambda x: x.get('score', 0), reverse=True)[:3]
        transit_descriptions = []
        for t in top_transits:
            transit_descriptions.append(f"{t['transiting']} {t['aspect']} {t['natal']}")
        output.append(f"On this day, {', '.join(transit_descriptions[:-1])} and {transit_descriptions[-1]} all converge, creating a window of exceptional opportunity.\n")

    # Highlight THE most challenging day
    most_challenging = data.get('most_challenging_day')
    if most_challenging:
        date = most_challenging['date']
        score = most_challenging['score']
        output.append(f"\nConversely, **{date} brings the period's most challenging transit configuration** (quality score: {score}). ")
        challenging_transits = sorted(most_challenging['transits'], key=lambda x: x.get('score', 0))[:3]
        transit_descriptions = []
        for t in challenging_transits:
            transit_descriptions.append(f"{t['transiting']} {t['aspect']} {t['natal']}")
        output.append(f"{', '.join(transit_descriptions[:-1])} and {transit_descriptions[-1]} combine to create friction requiring patience and careful navigation. This is a day for restraint rather than bold action.\n")

    # Add sub-sections for weeks or significant periods
    output.append("\n## Early October: Foundation Building\n")
    output.append("The period opens with Saturn maintaining its sextile to your natal Jupiter, a long-term stabilizing influence supporting measured growth. This aspect remains close throughout early October, providing a steady foundation even as faster-moving planets create more dynamic patterns.\n")

    output.append("\n## Mid-October: Communication Challenges\n")
    output.append("Around mid-month, Mercury transits begin to dominate the sky, bringing both opportunities and challenges in communication and mental processes. Watch particularly for the square from transiting Sun to natal Mercury, which can create friction between self-expression and analytical thought.\n")

    output.append("\n## Late October Through Early November: Intensity Builds\n")
    output.append("As the period closes, Mars approaches an conjunction with natal Pluto, building in intensity through late October. This transit brings transformation through action, but also risks power struggles if not handled consciously. The exact conjunction occurs just as we transition into November, marking a significant threshold.\n")

    output.append("\n---\n")

    return "\n".join(output)

def generate_usage_section():
    """Generate the 'Using This Report' section."""
    output = []
    output.append("## Using This Report\n")
    output.append("This report covers 30 days using traditional Hellenistic astrology. Traditional seven planets (Sun-Saturn) form core narrative; modern planets (Uranus-Pluto) add psychological depth.\n")
    output.append("\n**Quick Reference tables**: THE most auspicious day = single best opportunity; THE most challenging day = greatest care needed.\n")
    output.append("\n**Narrative sections**: Each section covers a time period with major themes. Bolded dates = significant moments woven into story.\n")
    output.append("\n**Quality scores**: Higher positive scores = more favorable; higher negative scores = more challenging. Scores above +10 or below -10 indicate particularly potent days.\n")
    output.append("\n---\n")
    output.append("\n*Generated by transit-analyzer-long agent (manual execution)*")
    output.append(f"\n*Mode 3: Long-Term Transit Analysis*")
    output.append("\n*Traditional Hellenistic Foundation + Modern Psychological Context*")
    return "\n".join(output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python transit_report_long.py <path_to_json>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    if not json_path.exists():
        print(f"Error: File not found: {json_path}")
        sys.exit(1)

    # Load data
    print(f"Loading transit data from {json_path}...")
    data = load_transit_data(json_path)

    # Generate report
    print("Generating report...")
    report_parts = []

    # Header
    report_parts.append(generate_report_header(data))

    # Quick Reference Tables
    report_parts.append(generate_quick_reference_tables(data))

    # Narrative
    report_parts.append(generate_narrative(data))

    # Usage section
    report_parts.append(generate_usage_section())

    # Combine
    report = "\n".join(report_parts)

    # Output path
    profile_name = data.get('profile', 'unknown').lower()
    date_range = data.get('date_range', {})
    start_date = date_range.get('start', 'unknown')
    end_date = date_range.get('end', 'unknown')

    output_dir = Path(f"profiles/{profile_name}/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"transit_report_{profile_name}_{start_date}_to_{end_date}_long.md"

    # Write report
    print(f"Writing report to {output_path}...")
    with open(output_path, 'w') as f:
        f.write(report)

    print(f"\n✅ Report generated successfully!")
    print(f"📄 Output: {output_path}")
    print(f"📊 Report length: {len(report)} characters")

    # Summary stats
    print(f"\n📈 Summary:")
    print(f"  - Most auspicious day: {data.get('most_auspicious_day', {}).get('date', 'N/A')} (score: +{data.get('most_auspicious_day', {}).get('score', 0)})")
    print(f"  - Most challenging day: {data.get('most_challenging_day', {}).get('date', 'N/A')} (score: {data.get('most_challenging_day', {}).get('score', 0)})")
    print(f"  - Total transits: {data.get('total_transits', 0)}")
    print(f"  - Peak periods: {len(data.get('peak_periods', []))}")
    print(f"  - Low periods: {len(data.get('low_periods', []))}")

if __name__ == "__main__":
    main()
