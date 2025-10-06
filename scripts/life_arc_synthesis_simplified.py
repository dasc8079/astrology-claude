#!/usr/bin/env python3
"""
Life Arc Synthesis Generator - Simplified Version
Generates narrative-focused life arc interpretation using simplified structure.

Output Structure:
1. Your Life Arc Story - Comprehensive narrative with all timing techniques
2. Theme Convergences - Where 2+ techniques align
3. Major Transitions - Key age markers and chapter changes

Usage:
    python life_arc_synthesis_simplified.py --profile darren --start-age 0 --end-age 46
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))
from life_arc_generator import generate_life_arc_timeline, get_year_snapshot
from profile_loader import load_profile
from zodiacal_releasing import find_current_period
from pdf_generator import markdown_to_pdf


def generate_simplified_synthesis(
    profile_name: str,
    start_age: int,
    end_age: int,
    current_age: int,
    output_dir: Path
) -> str:
    """Generate simplified life arc synthesis document."""

    # Generate full timeline data
    timeline = generate_life_arc_timeline(
        profile_name,
        start_age=start_age,
        end_age=end_age,
        include_fortune=True,
        include_spirit=True,
        include_progressions=False,
        include_solar_returns=False,
        current_date=None
    )

    profile = load_profile(profile_name)
    birth_data = profile.get_birth_data()

    # Build document
    doc = []

    # Header
    doc.append(f"# Life Arc Interpretation: {profile_name.title()} (Ages {start_age}-{end_age})")
    doc.append("")
    doc.append(f"**Generated:** {datetime.now().strftime('%B %d, %Y')}")
    doc.append(f"**Birth Data:** {birth_data['date']}, {birth_data['time']}, {birth_data['location']}")
    doc.append(f"**Current Age:** {current_age}")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Section 1: Your Life Arc Story
    doc.append("## Your Life Arc Story")
    doc.append("")
    story = generate_life_arc_story(timeline, current_age, profile_name)
    doc.extend(story)
    doc.append("")

    # Section 2: Theme Convergences
    doc.append("---")
    doc.append("")
    doc.append("## Theme Convergences")
    doc.append("")
    doc.append("*Where two or more timing techniques align to create significant life moments*")
    doc.append("")
    convergences = generate_convergences(timeline, current_age)
    doc.extend(convergences)
    doc.append("")

    # Section 3: Major Transitions
    doc.append("---")
    doc.append("")
    doc.append("## Major Transitions")
    doc.append("")
    doc.append("*Key age markers and chapter changes in your life arc*")
    doc.append("")
    transitions = generate_transitions(timeline, current_age, start_age, end_age)
    doc.extend(transitions)
    doc.append("")

    # Footer
    doc.append("---")
    doc.append("")
    doc.append(f"*This interpretation synthesizes Zodiacal Releasing (Fortune & Spirit), Annual Profections, and natal chart analysis for {profile_name.title()}. All ages are calculated from birth date {birth_data['date']}.*")
    doc.append("")

    return "\n".join(doc)


def generate_life_arc_story(timeline: Dict, current_age: int, profile_name: str) -> List[str]:
    """Generate comprehensive narrative integrating all timing techniques."""

    story = []

    # Get ZR periods
    fortune_l1_periods = timeline['zr_fortune']['l1_periods'] if timeline['zr_fortune'] else []
    spirit_l1_periods = timeline['zr_spirit']['l1_periods'] if timeline['zr_spirit'] else []

    # Find current positions
    current_fortune_l1 = find_current_period(fortune_l1_periods, float(current_age))
    current_spirit_l1 = find_current_period(spirit_l1_periods, float(current_age))

    # Get current snapshot
    current_snapshot = get_year_snapshot(timeline, current_age)

    # NARRATIVE - Write as flowing prose
    story.append("Your life unfolds in distinct chapters marked by profound transitions, each carrying its own signature themes and challenges. Born under specific cosmic conditions, your journey follows a pattern that becomes clearer when we trace the major timing cycles that govern human development.")
    story.append("")

    # Chapter 1: Opening (ages 0-12 or first major period)
    if fortune_l1_periods:
        first_period = fortune_l1_periods[0]
        story.append(f"**The Foundation (Ages {int(first_period['start_age'])}-{int(first_period['end_age'])}):** Your life began under the rulership of {first_period['ruler']}, with Fortune placed in {first_period['sign']}. This {first_period['duration']}-year opening chapter established the material and physical foundations of your existence. Early childhood during this period was characterized by {get_sign_themes(first_period['sign'])}, setting patterns that would echo throughout your life. The Lot of Fortune in {first_period['sign']} speaks to your body, health, livelihood, and material circumstances being fundamentally shaped by these themes.")
        story.append("")

    # Find all L1 periods up to end_age
    relevant_fortune_periods = [p for p in fortune_l1_periods if p['start_age'] <= timeline['age_range']['end']]

    # Chapter 2+: Subsequent major periods
    for i, period in enumerate(relevant_fortune_periods[1:], 1):
        is_current = current_fortune_l1 and period['sign'] == current_fortune_l1['sign']
        current_marker = " ⭐ **YOUR CURRENT CHAPTER**" if is_current else ""

        story.append(f"**{get_period_title(period)} (Ages {int(period['start_age'])}-{int(period['end_age'])}){current_marker}:** ")

        # Find peak subperiod
        if timeline['zr_fortune']:
            l2_periods = [p for p in timeline['zr_fortune']['l2_periods']
                         if p['start_age'] >= period['start_age'] and p['end_age'] <= period['end_age']]
            peak_period = next((p for p in l2_periods if p.get('is_peak')), None)

            if peak_period:
                story.append(f"This {period['duration']}-year chapter under {period['ruler']}'s rulership marks a distinct phase of development. The opening peak period ({period['sign']} L2, ages {peak_period['start_age']:.1f}-{peak_period['end_age']:.1f}) represented a 'loosing of the bond'—a concentrated activation of {period['sign']} themes that set the tone for the entire period. {get_period_narrative(period, current_age, is_current)}")
            else:
                story.append(f"This {period['duration']}-year chapter under {period['ruler']}'s rulership marks a distinct phase of development. {get_period_narrative(period, current_age, is_current)}")

        story.append("")

    # Spirit Thread
    story.append("**The Thread of Conscious Action:** While Fortune describes your body and material circumstances, Spirit reveals the development of your mind, purposeful activity, and career direction. ")

    if spirit_l1_periods:
        relevant_spirit_periods = [p for p in spirit_l1_periods if p['start_age'] <= timeline['age_range']['end']]

        for period in relevant_spirit_periods:
            is_current = current_spirit_l1 and period['sign'] == current_spirit_l1['sign']
            current_marker = " (your current Spirit chapter)" if is_current else ""

            story.append(f"From ages {int(period['start_age'])}-{int(period['end_age'])}, your Spirit operated in {period['sign']}{current_marker}, meaning your conscious choices, mental focus, and career direction were shaped by {get_sign_themes(period['sign'])}. ")

    story.append("")

    # Current Position
    story.append(f"**Where You Stand Now (Age {current_age}):** ")

    current_desc = []
    if current_snapshot['profection']:
        prof = current_snapshot['profection']['profection']
        current_desc.append(f"This year you're in a {prof['profected_house']}th house profection ({prof['profected_sign']}), making {prof['lord_of_year']} your Lord of the Year—the planet that colors all experiences for this twelve-month period.")

    if current_snapshot['fortune_l1'] and current_snapshot['fortune_l2']:
        current_desc.append(f"Your Fortune (body/livelihood) operates in the {current_snapshot['fortune_l1']['sign']} L1 period, specifically within the {current_snapshot['fortune_l2']['sign']} L2 subperiod (ages {current_snapshot['fortune_l2']['start_age']:.1f}-{current_snapshot['fortune_l2']['end_age']:.1f}).")

    if current_snapshot['spirit_l1'] and current_snapshot['spirit_l2']:
        current_desc.append(f"Your Spirit (mind/action) operates in the {current_snapshot['spirit_l1']['sign']} L1 period, specifically within the {current_snapshot['spirit_l2']['sign']} L2 subperiod (ages {current_snapshot['spirit_l2']['start_age']:.1f}-{current_snapshot['spirit_l2']['end_age']:.1f}).")

    story.append(" ".join(current_desc))
    story.append("")

    # What's Ahead
    story.append("**What Lies Ahead:** ")

    future_desc = []

    # Next Fortune L1 transition
    next_fortune_l1 = None
    if current_fortune_l1:
        for i, period in enumerate(fortune_l1_periods):
            if period['sign'] == current_fortune_l1['sign'] and i + 1 < len(fortune_l1_periods):
                next_fortune_l1 = fortune_l1_periods[i + 1]
                break

    if next_fortune_l1:
        years_until = next_fortune_l1['start_age'] - current_age
        future_desc.append(f"In {years_until:.0f} years (age {int(next_fortune_l1['start_age'])}), you'll enter a major life transition as Fortune shifts from {current_fortune_l1['sign']} to {next_fortune_l1['sign']}—a {next_fortune_l1['duration']}-year chapter that will redefine your relationship to body, livelihood, and material circumstances.")

    # Next Spirit L1 transition
    next_spirit_l1 = None
    if current_spirit_l1:
        for i, period in enumerate(spirit_l1_periods):
            if period['sign'] == current_spirit_l1['sign'] and i + 1 < len(spirit_l1_periods):
                next_spirit_l1 = spirit_l1_periods[i + 1]
                break

    if next_spirit_l1:
        years_until = next_spirit_l1['start_age'] - current_age
        future_desc.append(f"At age {int(next_spirit_l1['start_age'])}, your Spirit will shift from {current_spirit_l1['sign']} to {next_spirit_l1['sign']}, marking a new {next_spirit_l1['duration']}-year phase in your conscious action and career development.")

    # Profection cycle
    next_profection_reset = ((current_age // 12) + 1) * 12
    if next_profection_reset <= timeline['age_range']['end']:
        years_until = next_profection_reset - current_age
        future_desc.append(f"Age {next_profection_reset} will mark a new profection cycle—a fresh 12-year chapter beginning with a 1st house year focused on self, identity, and new beginnings.")

    story.append(" ".join(future_desc))
    story.append("")

    # POETIC WRAPUP (no heading, flows naturally as final paragraph)
    story.append(generate_poetic_wrapup(timeline, current_age, current_fortune_l1, next_fortune_l1))

    return story


def generate_convergences(timeline: Dict, current_age: int) -> List[str]:
    """Generate theme convergences section."""

    convergences = []

    # Identify key convergence ages
    fortune_l1_periods = timeline['zr_fortune']['l1_periods'] if timeline['zr_fortune'] else []
    spirit_l1_periods = timeline['zr_spirit']['l1_periods'] if timeline['zr_spirit'] else []

    # Current age convergence
    current_snapshot = get_year_snapshot(timeline, current_age)
    if current_snapshot['profection'] and current_snapshot['fortune_l2'] and current_snapshot['spirit_l2']:
        convergences.append(f"### Age {current_age} — Your Current Convergence")
        convergences.append("")
        convergences.append("**Aligned Techniques:**")

        prof = current_snapshot['profection']['profection']
        convergences.append(f"- **Profection:** {prof['profected_house']}th house ({prof['profected_sign']}), Lord of Year = {prof['lord_of_year']}")
        convergences.append(f"- **Fortune L2:** {current_snapshot['fortune_l2']['sign']} (ages {current_snapshot['fortune_l2']['start_age']:.1f}-{current_snapshot['fortune_l2']['end_age']:.1f})")
        convergences.append(f"- **Spirit L2:** {current_snapshot['spirit_l2']['sign']} (ages {current_snapshot['spirit_l2']['start_age']:.1f}-{current_snapshot['spirit_l2']['end_age']:.1f})")

        convergences.append("")
        convergences.append("**Synthesis:** " + get_convergence_synthesis(current_snapshot, current_age))
        convergences.append("")

    # Major L1 transitions
    for fortune_period in fortune_l1_periods:
        transition_age = int(fortune_period['start_age'])
        if transition_age > 0 and transition_age <= timeline['age_range']['end']:
            snapshot = get_year_snapshot(timeline, transition_age)

            # Check if this is a significant convergence
            if snapshot['profection'] and snapshot['spirit_l1']:
                prof = snapshot['profection']['profection']

                convergences.append(f"### Age {transition_age} — Fortune Chapter Begins")
                convergences.append("")
                convergences.append("**Aligned Techniques:**")
                convergences.append(f"- **Fortune L1:** Shifts to {fortune_period['sign']} ({fortune_period['duration']}-year period begins)")
                convergences.append(f"- **Profection:** {prof['profected_house']}th house ({prof['profected_sign']}), Lord of Year = {prof['lord_of_year']}")
                convergences.append(f"- **Spirit L1:** {snapshot['spirit_l1']['sign']} period")
                convergences.append("")
                convergences.append("**Synthesis:** " + get_transition_synthesis(fortune_period, snapshot, transition_age))
                convergences.append("")

    # Profection cycle resets
    for age in range(12, timeline['age_range']['end'] + 1, 12):
        if age != 0:
            snapshot = get_year_snapshot(timeline, age)
            if snapshot['profection']:
                convergences.append(f"### Age {age} — Profection Cycle Reset")
                convergences.append("")
                convergences.append("**Aligned Techniques:**")
                convergences.append(f"- **Profection:** New 12-year cycle begins (1st house year)")

                if snapshot['fortune_l1']:
                    convergences.append(f"- **Fortune L1:** {snapshot['fortune_l1']['sign']} period")
                if snapshot['spirit_l1']:
                    convergences.append(f"- **Spirit L1:** {snapshot['spirit_l1']['sign']} period")

                convergences.append("")
                convergences.append(f"**Synthesis:** Age {age} marks a fresh beginning in your profection cycle—a return to 1st house themes of identity, body, and self-initiation. Every 12 years, this reset occurs, offering a chance to redefine who you are and what you're becoming.")
                convergences.append("")

    return convergences


def generate_transitions(timeline: Dict, current_age: int, start_age: int, end_age: int) -> List[str]:
    """Generate major transitions timeline."""

    transitions = []

    # Build transition table
    transitions.append("| Age | Transition Type | Details |")
    transitions.append("|-----|----------------|---------|")

    transition_list = []

    # Fortune L1 transitions
    if timeline['zr_fortune']:
        for i, period in enumerate(timeline['zr_fortune']['l1_periods'][:-1]):
            transition_age = period['end_age']
            if start_age <= transition_age <= end_age:
                next_period = timeline['zr_fortune']['l1_periods'][i + 1]
                transition_list.append({
                    'age': transition_age,
                    'type': 'Fortune L1 Shift',
                    'details': f"{period['sign']} → {next_period['sign']} ({next_period['duration']}-year period)"
                })

    # Spirit L1 transitions
    if timeline['zr_spirit']:
        for i, period in enumerate(timeline['zr_spirit']['l1_periods'][:-1]):
            transition_age = period['end_age']
            if start_age <= transition_age <= end_age:
                next_period = timeline['zr_spirit']['l1_periods'][i + 1]
                transition_list.append({
                    'age': transition_age,
                    'type': 'Spirit L1 Shift',
                    'details': f"{period['sign']} → {next_period['sign']} ({next_period['duration']}-year period)"
                })

    # Profection resets
    for age in range(start_age, end_age + 1):
        if age % 12 == 0 and age > 0:
            transition_list.append({
                'age': age,
                'type': 'Profection Cycle',
                'details': 'New 12-year cycle begins (1st house year)'
            })

    # Sort by age
    transition_list.sort(key=lambda x: x['age'])

    # Add to table
    for trans in transition_list:
        current_marker = " ⭐" if abs(trans['age'] - current_age) < 1 else ""
        transitions.append(f"| {trans['age']:.0f}{current_marker} | {trans['type']} | {trans['details']} |")

    return transitions


def get_sign_themes(sign: str) -> str:
    """Get thematic description for a sign."""
    themes = {
        'Aries': 'independence, courage, initiative, and pioneering action',
        'Taurus': 'stability, material security, patience, and building lasting value',
        'Gemini': 'learning, communication, versatility, and intellectual curiosity',
        'Cancer': 'emotional depth, nurturing, home, and protective care',
        'Leo': 'creative expression, leadership, confidence, and generous warmth',
        'Virgo': 'refinement, analysis, service, and practical mastery',
        'Libra': 'partnership, balance, aesthetics, and relational harmony',
        'Scorpio': 'intensity, transformation, depth, and psychological power',
        'Sagittarius': 'expansion, exploration, philosophy, and optimistic vision',
        'Capricorn': 'discipline, structure, mastery, and responsible achievement',
        'Aquarius': 'innovation, independence, humanitarian vision, and unconventional thinking',
        'Pisces': 'compassion, imagination, spiritual sensitivity, and boundless empathy'
    }
    return themes.get(sign, 'distinct qualities')


def get_period_title(period: Dict) -> str:
    """Get descriptive title for a period."""
    sign = period['sign']
    ruler = period['ruler']

    titles = {
        'Aries': f"{ruler}'s Initiative",
        'Taurus': f"{ruler}'s Foundation",
        'Gemini': f"{ruler}'s Learning",
        'Cancer': f"{ruler}'s Nurturing",
        'Leo': f"{ruler}'s Expression",
        'Virgo': f"{ruler}'s Refinement",
        'Libra': f"{ruler}'s Balance",
        'Scorpio': f"{ruler}'s Transformation",
        'Sagittarius': f"{ruler}'s Expansion",
        'Capricorn': f"{ruler}'s Mastery",
        'Aquarius': f"{ruler}'s Innovation",
        'Pisces': f"{ruler}'s Transcendence"
    }
    return titles.get(sign, f"The {sign} Period")


def get_period_narrative(period: Dict, current_age: int, is_current: bool) -> str:
    """Generate narrative description for a period."""

    if is_current:
        years_remaining = period['end_age'] - current_age
        return f"You are currently in the final {years_remaining:.1f} years of this chapter. The themes of {get_sign_themes(period['sign'])} are reaching their culmination in your life, preparing you for the transition ahead."
    else:
        return f"During these years, life demanded engagement with {get_sign_themes(period['sign'])}, shaping your development through {period['ruler']}'s particular lessons."


def get_convergence_synthesis(snapshot: Dict, age: int) -> str:
    """Generate synthesis for a convergence moment."""

    prof = snapshot['profection']['profection']
    house = prof['profected_house']

    house_themes = {
        1: "identity, self, body, and personal initiative",
        2: "resources, values, money, and material security",
        3: "communication, siblings, learning, and local environment",
        4: "home, family, roots, and private foundation",
        5: "creativity, pleasure, children, and self-expression",
        6: "work, health, service, and daily routines",
        7: "partnership, marriage, relationships, and open adversaries",
        8: "transformation, shared resources, death/rebirth, and psychological depth",
        9: "philosophy, travel, higher learning, and meaning-making",
        10: "career, reputation, public life, and vocation",
        11: "friends, groups, hopes, and community",
        12: "solitude, spirituality, hidden matters, and release"
    }

    theme = house_themes.get(house, "distinct life areas")

    return f"This year brings focus to {theme}. The convergence of Fortune in {snapshot['fortune_l2']['sign']}, Spirit in {snapshot['spirit_l2']['sign']}, and a {house}th house profection creates a concentrated moment where body/livelihood, conscious action, and annual focus all align toward these themes."


def get_transition_synthesis(period: Dict, snapshot: Dict, age: int) -> str:
    """Generate synthesis for a transition moment."""

    return f"The beginning of a {period['duration']}-year {period['sign']} period marks a major life chapter. At this age, the shift in Fortune L1 to {period['sign']} themes coincides with the annual profection cycle, creating a powerful threshold moment for reorienting your relationship to body, livelihood, and material circumstances."


def generate_poetic_wrapup(timeline: Dict, current_age: int, current_fortune: Dict, next_fortune: Dict) -> str:
    """Generate 3-5 sentence poetic wrapup paragraph."""

    if next_fortune:
        years_until = next_fortune['start_age'] - current_age

        return f"You stand now in the closing years of a long chapter, carrying within you everything you have learned through {current_fortune['sign']}'s particular form of mastery. The intensity you may feel is not crisis but preparation—the soul's way of consolidating wisdom before a threshold crossing. In {years_until:.0f} years, when {next_fortune['sign']} opens its door, you will step through not as a beginner but as one who has earned the right to the freedom that awaits. Trust what you have built within yourself; it is exactly what you will need for what comes next. This is not an ending but a becoming."
    else:
        return f"You stand in the midst of {current_fortune['sign']}'s long teaching, learning its lessons day by day, year by year. Each challenge you meet, each limitation you work with, each small victory you earn—all of this is the substance of your becoming. The path is not always clear, but it is always purposeful. Trust the process that has brought you here; it knows where you are going."


def main():
    parser = argparse.ArgumentParser(description='Generate simplified life arc synthesis')
    parser.add_argument('--profile', required=True, help='Profile name')
    parser.add_argument('--start-age', type=int, default=0, help='Start age')
    parser.add_argument('--end-age', type=int, required=True, help='End age')
    parser.add_argument('--current-age', type=int, required=True, help='Current age')
    parser.add_argument('--output-dir', help='Output directory (default: profiles/{profile}/output)')
    parser.add_argument('--generate-pdf', action='store_true', help='Generate PDF from markdown')

    args = parser.parse_args()

    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path(__file__).parent.parent / 'profiles' / args.profile / 'output'

    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate synthesis
    print(f"Generating simplified life arc synthesis for {args.profile}...")
    synthesis_content = generate_simplified_synthesis(
        args.profile,
        args.start_age,
        args.end_age,
        args.current_age,
        output_dir
    )

    # Write synthesis markdown
    synthesis_md_path = output_dir / f"life_arc_synthesis_ages_{args.start_age}-{args.end_age}.md"
    with open(synthesis_md_path, 'w', encoding='utf-8') as f:
        f.write(synthesis_content)

    print(f"✅ Synthesis written to: {synthesis_md_path}")

    # Generate PDF if requested
    if args.generate_pdf:
        print("Generating PDF...")
        pdf_path = markdown_to_pdf(
            str(synthesis_md_path),
            title=f"Life Arc: {args.profile.title()} (Ages {args.start_age}-{args.end_age})"
        )
        print(f"✅ PDF generated: {pdf_path}")


if __name__ == '__main__':
    main()
