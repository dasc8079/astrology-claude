#!/usr/bin/env python3
"""
Saturn Periods Comparison Analysis
Compares three critical Saturn periods in Darren's life:
1. Saturn Return (ages 29-30, Dec 2017 - Dec 2019)
2. Current Recovery (ages 35-37, Jan 2024 - Dec 2025)
3. Saturn Square (ages 37-38, Oct 2025 - Dec 2027)

Generates comprehensive comparison metrics and interpretation.
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple
from collections import defaultdict

# File paths
PERIOD_1_FILE = Path(__file__).parent.parent / "profiles/darren/output/transit_data_darren_2017-12-01_to_2019-12-31.json"
PERIOD_2_FILE = Path(__file__).parent.parent / "profiles/darren/output/transit_data_darren_2024-01-01_to_2025-12-31.json"
PERIOD_3_FILE = Path(__file__).parent.parent / "profiles/darren/output/transit_data_darren_2025-10-01_to_2027-12-31.json"

def load_transit_data(file_path: Path) -> Dict[str, Any]:
    """Load transit data from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def calculate_period_metrics(data: Dict[str, Any], period_name: str) -> Dict[str, Any]:
    """
    Calculate comprehensive metrics for a transit period.

    Returns:
        Dictionary with all comparison metrics
    """
    # Get daily scores
    daily_scores_data = data.get('daily_scores', {})
    all_transits = data.get('all_transits', [])

    # Initialize counters
    total_transits = len(all_transits)
    critical_count = 0
    important_count = 0
    notable_count = 0

    challenging_transits = 0  # Hard aspects from malefics
    benefic_transits = 0
    malefic_transits = 0

    saturn_transits = 0
    sixth_house_transits = 0

    all_daily_scores = []
    days_below_minus_10 = 0
    days_below_minus_20 = 0
    days_below_minus_30 = 0

    worst_day_score = 0
    worst_day_date = ""
    best_day_score = 0
    best_day_date = ""

    # Aspect categorization
    hard_aspects = ['conjunction', 'square', 'opposition']
    soft_aspects = ['sextile', 'trine']
    malefic_planets = ['Mars', 'Saturn']
    benefic_planets = ['Venus', 'Jupiter']

    # Process daily scores
    for date_str, day_data in daily_scores_data.items():
        # Extract score from dict if needed
        if isinstance(day_data, dict):
            daily_score = day_data.get('score', 0)
        else:
            daily_score = day_data

        all_daily_scores.append(daily_score)

        # Track worst/best days
        if daily_score < worst_day_score:
            worst_day_score = daily_score
            worst_day_date = date_str
        if daily_score > best_day_score:
            best_day_score = daily_score
            best_day_date = date_str

        # Count days with significant challenges
        if daily_score < -10:
            days_below_minus_10 += 1
        if daily_score < -20:
            days_below_minus_20 += 1
        if daily_score < -30:
            days_below_minus_30 += 1

    # Process all transits
    for transit in all_transits:
        # Count by tier
        tier = transit.get('tier', '')
        if tier == 'CRITICAL':
            critical_count += 1
        elif tier == 'IMPORTANT':
            important_count += 1
        elif tier == 'NOTABLE':
            notable_count += 1

        # Identify planet and aspect
        transiting_planet = transit.get('transiting_planet', '')
        aspect_type = transit.get('aspect_type', '')
        natal_planet = transit.get('natal_planet', '')

        # Count Saturn transits
        if transiting_planet == 'Saturn':
            saturn_transits += 1

        # Count 6th house transits (if natal planet is in 6th)
        # Note: This requires natal chart data - simplified check
        if natal_planet in ['Sun', 'Saturn', 'Uranus', 'Neptune']:  # Known 6th house planets
            sixth_house_transits += 1

        # Count malefic/benefic transits
        if transiting_planet in malefic_planets:
            malefic_transits += 1
        if transiting_planet in benefic_planets:
            benefic_transits += 1

        # Count challenging transits (hard aspects from malefics)
        if transiting_planet in malefic_planets and aspect_type in hard_aspects:
            challenging_transits += 1

    # Calculate statistics
    num_days = len(all_daily_scores) if all_daily_scores else 1
    avg_daily_score = sum(all_daily_scores) / num_days if all_daily_scores else 0

    # Calculate standard deviation
    if all_daily_scores:
        variance = sum((x - avg_daily_score) ** 2 for x in all_daily_scores) / num_days
        std_dev = variance ** 0.5
    else:
        std_dev = 0

    return {
        'period_name': period_name,
        'total_days': num_days,
        'total_transits': total_transits,
        'critical_transits': critical_count,
        'important_transits': important_count,
        'notable_transits': notable_count,
        'challenging_transits': challenging_transits,
        'malefic_transits': malefic_transits,
        'benefic_transits': benefic_transits,
        'saturn_transits': saturn_transits,
        'sixth_house_transits': sixth_house_transits,
        'worst_day_score': worst_day_score,
        'worst_day_date': worst_day_date,
        'best_day_score': best_day_score,
        'best_day_date': best_day_date,
        'avg_daily_score': round(avg_daily_score, 2),
        'std_dev_daily_score': round(std_dev, 2),
        'days_below_minus_10': days_below_minus_10,
        'days_below_minus_20': days_below_minus_20,
        'days_below_minus_30': days_below_minus_30,
        'percent_difficult_days': round(100 * days_below_minus_10 / num_days, 1) if num_days else 0,
    }

def identify_saturn_aspects(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Find all Saturn transits to natal Sun and Saturn.
    Returns list of significant Saturn aspects.
    """
    saturn_aspects = []

    all_transits = data.get('all_transits', [])
    for transit in all_transits:
        if transit.get('transiting_planet') == 'Saturn':
            natal = transit.get('natal_planet', '')
            aspect = transit.get('aspect_type', '')
            orb = abs(transit.get('orb', 0))
            date_str = transit.get('date', '')

            # Focus on Sun and Saturn natal planets
            if natal in ['Sun', 'Saturn'] and orb < 2.0:
                saturn_aspects.append({
                    'date': date_str,
                    'aspect': aspect,
                    'natal_planet': natal,
                    'orb': round(orb, 2)
                })

    return saturn_aspects

def generate_report(metrics: List[Dict[str, Any]], saturn_aspects_data: Dict[str, List]) -> str:
    """Generate comprehensive comparison report."""

    report = """# SATURN PERIODS COMPARISON ANALYSIS
## Three Critical Saturn Periods for Darren

---

## EXECUTIVE SUMMARY

"""

    # Find which period was hardest
    period_names = [m['period_name'] for m in metrics]
    worst_scores = [m['worst_day_score'] for m in metrics]
    avg_scores = [m['avg_daily_score'] for m in metrics]
    difficult_day_percents = [m['percent_difficult_days'] for m in metrics]

    hardest_worst_day = period_names[worst_scores.index(min(worst_scores))]
    hardest_avg = period_names[avg_scores.index(min(avg_scores))]
    hardest_duration = period_names[difficult_day_percents.index(max(difficult_day_percents))]

    report += f"""**Hardest Single Day**: {hardest_worst_day} ({min(worst_scores)} score)
**Lowest Average Daily Quality**: {hardest_avg} ({min(avg_scores):.1f} average)
**Highest % Difficult Days**: {hardest_duration} ({max(difficult_day_percents):.1f}% days below -10)

"""

    # Period 2 vs Period 1 comparison
    p1_avg = metrics[0]['avg_daily_score']
    p2_avg = metrics[1]['avg_daily_score']
    p1_worst = metrics[0]['worst_day_score']
    p2_worst = metrics[1]['worst_day_score']

    if p2_avg < p1_avg:
        comparison_1_2 = f"Current recovery period (2024-2025) is MORE challenging than Saturn return (avg {p2_avg:.1f} vs {p1_avg:.1f})"
    else:
        comparison_1_2 = f"Current recovery period (2024-2025) is LESS challenging than Saturn return (avg {p2_avg:.1f} vs {p1_avg:.1f})"

    # Period 3 vs Period 1 comparison
    p3_avg = metrics[2]['avg_daily_score']
    p3_worst = metrics[2]['worst_day_score']

    if p3_avg < p1_avg:
        comparison_1_3 = f"Saturn square period (2025-2027) will be MORE challenging than Saturn return (avg {p3_avg:.1f} vs {p1_avg:.1f})"
    else:
        comparison_1_3 = f"Saturn square period (2025-2027) will be LESS challenging than Saturn return (avg {p3_avg:.1f} vs {p1_avg:.1f})"

    report += f"""**Key Findings**:
- {comparison_1_2}
- {comparison_1_3}
- Worst single day across all periods: {min(worst_scores)} ({hardest_worst_day})

---

## DETAILED COMPARISON TABLE

| Metric | Saturn Return (29-30) | Current Recovery (35-37) | Saturn Square (37-38) |
|--------|----------------------|-------------------------|----------------------|
"""

    # Add all metrics to table
    metrics_to_compare = [
        ('Date Range', 'Dec 2017 - Dec 2019', 'Jan 2024 - Dec 2025', 'Oct 2025 - Dec 2027'),
        ('Total Days', metrics[0]['total_days'], metrics[1]['total_days'], metrics[2]['total_days']),
        ('Total Transits', metrics[0]['total_transits'], metrics[1]['total_transits'], metrics[2]['total_transits']),
        ('Critical Transits', metrics[0]['critical_transits'], metrics[1]['critical_transits'], metrics[2]['critical_transits']),
        ('Challenging Transits', metrics[0]['challenging_transits'], metrics[1]['challenging_transits'], metrics[2]['challenging_transits']),
        ('Worst Day Score', metrics[0]['worst_day_score'], metrics[1]['worst_day_score'], metrics[2]['worst_day_score']),
        ('Average Daily Score', f"{metrics[0]['avg_daily_score']:.1f}", f"{metrics[1]['avg_daily_score']:.1f}", f"{metrics[2]['avg_daily_score']:.1f}"),
        ('Days < -10', metrics[0]['days_below_minus_10'], metrics[1]['days_below_minus_10'], metrics[2]['days_below_minus_10']),
        ('Days < -20', metrics[0]['days_below_minus_20'], metrics[1]['days_below_minus_20'], metrics[2]['days_below_minus_20']),
        ('Days < -30', metrics[0]['days_below_minus_30'], metrics[1]['days_below_minus_30'], metrics[2]['days_below_minus_30']),
        ('% Difficult Days', f"{metrics[0]['percent_difficult_days']:.1f}%", f"{metrics[1]['percent_difficult_days']:.1f}%", f"{metrics[2]['percent_difficult_days']:.1f}%"),
        ('6th House Transits', metrics[0]['sixth_house_transits'], metrics[1]['sixth_house_transits'], metrics[2]['sixth_house_transits']),
        ('Saturn Transits', metrics[0]['saturn_transits'], metrics[1]['saturn_transits'], metrics[2]['saturn_transits']),
    ]

    for label, val1, val2, val3 in metrics_to_compare:
        report += f"| {label} | {val1} | {val2} | {val3} |\n"

    report += "\n---\n\n"

    # Period-by-period analysis
    for i, m in enumerate(metrics, 1):
        report += f"""## PERIOD {i}: {m['period_name'].upper()}

**Saturn's Role**: {get_saturn_context(i, saturn_aspects_data[f'period_{i}'])}

**Major Transit Events**:
"""

        # Add Saturn aspects
        aspects = saturn_aspects_data[f'period_{i}']
        if aspects:
            report += "- **Saturn Aspects**:\n"
            for asp in aspects[:10]:  # Limit to first 10
                report += f"  - {asp['date']}: Saturn {asp['aspect']} natal {asp['natal_planet']} (orb {asp['orb']}°)\n"
        else:
            report += "- No exact Saturn aspects to Sun or natal Saturn in this period\n"

        report += f"""
**Health/Work Indicators**:
- 6th house transits: {m['sixth_house_transits']}
- Malefic transits: {m['malefic_transits']}
- Challenging aspects: {m['challenging_transits']}

**Difficulty Assessment**: {assess_difficulty(m)}/10

**Key Statistics**:
- Worst day: {m['worst_day_date']} (score: {m['worst_day_score']})
- Best day: {m['best_day_date']} (score: {m['best_day_score']})
- Average daily quality: {m['avg_daily_score']:.1f}
- {m['percent_difficult_days']:.1f}% of days had significant challenges (< -10)

---

"""

    # Interpretation section
    report += """## INTERPRETATION & CONTEXT

"""

    # Answer specific questions
    report += f"""### 1. Which Period Was Objectively Hardest?

**By Worst Single Day**: {hardest_worst_day} had the most difficult day ({min(worst_scores)} score)

**By Average Daily Quality**: {hardest_avg} had the lowest average daily quality ({min(avg_scores):.1f} average)

**By Duration of Difficulty**: {hardest_duration} had the highest percentage of difficult days ({max(difficult_day_percents):.1f}%)

**Overall Assessment**: """

    # Determine overall hardest
    scores = {p: 0 for p in period_names}
    scores[hardest_worst_day] += 1
    scores[hardest_avg] += 1
    scores[hardest_duration] += 1

    hardest_overall = max(scores.items(), key=lambda x: x[1])
    report += f"{hardest_overall[0]} appears to be the most consistently difficult period.\n\n"

    report += f"""### 2. How Does Current Recovery (2024-2025) Compare to Saturn Return?

{comparison_1_2}

**Detailed Comparison**:
- Worst day severity: Saturn return was {abs(p1_worst - p2_worst):.0f} points worse
- Average daily quality: {"Current period is harder" if p2_avg < p1_avg else "Saturn return was harder"} by {abs(p2_avg - p1_avg):.1f} points
- Duration: {"Current period has more difficult days" if metrics[1]['percent_difficult_days'] > metrics[0]['percent_difficult_days'] else "Saturn return had more difficult days"}

**Context**: The current recovery period (ages 35-37) is {"more" if p2_avg < p1_avg else "less"} challenging than the Saturn return period on average, though {"not as severe on the worst days" if p2_worst > p1_worst else "with worse individual days"}.

### 3. Will Saturn Square (2026) Be Worse Than Saturn Return Was?

{comparison_1_3}

**Detailed Comparison**:
- Worst day severity: {"Saturn square will be worse" if p3_worst < p1_worst else "Saturn return was worse"} (difference: {abs(p3_worst - p1_worst):.0f} points)
- Average daily quality: {"Saturn square will be harder" if p3_avg < p1_avg else "Saturn return was harder"} (difference: {abs(p3_avg - p1_avg):.1f} points)
- 6th house stress: {"Saturn square will be more stressful on work/health" if metrics[2]['sixth_house_transits'] > metrics[0]['sixth_house_transits'] else "Saturn return was more stressful on work/health"}

**Outlook**: The Saturn square period (especially March-April 2026) {"is projected to be more challenging than the Saturn return" if p3_avg < p1_avg else "may be less intense than the Saturn return"}.

### 4. Context for "Challenging Transits Ages 29-30"

The user's question about challenging transits at ages 29-30 refers to the **Saturn Return** period, which is:

- One of the most significant astrological milestones in a lifetime
- Occurs when transiting Saturn returns to its natal position (approximately every 29.5 years)
- Often brings major life restructuring, responsibility, and maturity themes
- For Darren, this occurred in mid-2018 with natal Saturn in Capricorn at 5°03'

**Severity Assessment**:
- The Saturn return period had {metrics[0]['days_below_minus_10']} days with significant challenges out of {metrics[0]['total_days']} total days ({metrics[0]['percent_difficult_days']:.1f}%)
- Worst day reached a score of {metrics[0]['worst_day_score']}
- Average daily quality: {metrics[0]['avg_daily_score']:.1f}

This {"was" if metrics[0]['avg_daily_score'] < -5 else "was not"} an unusually difficult period compared to typical life phases.

### 5. Larger Life Narrative Context

**Saturn Cycle Milestones**:
- **Age ~29.5 (mid-2018)**: Saturn Return - First major Saturn cycle completion, life restructuring
- **Age ~37 (Mar-Apr 2026)**: Saturn Square - First quarter tension, adjustment of structures built during return
- **Age ~44 (2032)**: Saturn Opposition - Mid-cycle peak, external pressures
- **Age ~58.5 (2047)**: Second Saturn Return - Mastery, wisdom, legacy

**6th House Emphasis**: With natal Sun, Saturn, Uranus, and Neptune all in the 6th house (work/health), Saturn transits have amplified impact on:
- Work structure and career direction
- Health patterns and lifestyle
- Daily routines and responsibilities
- Service and meaningful contribution

**Psychological Themes Across Periods**:
1. **Saturn Return (29-30)**: Foundational restructuring, accepting adult responsibilities
2. **Current Recovery (35-37)**: Integration, healing, refinement of structures
3. **Saturn Square (37-38)**: Testing and adjustment, course correction, renewed commitment

### 6. Is 2026 "The Hardest"?

Based on this analysis, {"YES" if metrics[2]['avg_daily_score'] < min(metrics[0]['avg_daily_score'], metrics[1]['avg_daily_score']) else "NO"} - the Saturn square period (2026) {"will be the most challenging of these three periods" if metrics[2]['avg_daily_score'] < min(metrics[0]['avg_daily_score'], metrics[1]['avg_daily_score']) else "will not be worse than " + ("the Saturn return" if metrics[0]['avg_daily_score'] < metrics[2]['avg_daily_score'] else "the current period")}.

{"However" if metrics[2]['avg_daily_score'] >= min(metrics[0]['avg_daily_score'], metrics[1]['avg_daily_score']) else "Additionally"}, it's important to note:
- The worst single day may not be as severe as previous periods
- Average difficulty matters more than peak difficulty for overall life quality
- The presence of supportive transits can mitigate challenging ones
- Personal growth and wisdom from previous Saturn experiences provide resources

---

## CONCLUSION

The three Saturn periods represent different phases of the Saturn cycle, each with distinct themes:

1. **Saturn Return (29-30)**: The foundational restructuring period
2. **Current Recovery (35-37)**: The integration and refinement period
3. **Saturn Square (37-38)**: The testing and adjustment period

{"The current period appears to be the most consistently challenging" if metrics[1]['avg_daily_score'] == min(avg_scores) else "The Saturn return was the most challenging overall" if metrics[0]['avg_daily_score'] == min(avg_scores) else "The upcoming Saturn square will be the most challenging"}, {"but" if metrics[2]['avg_daily_score'] < -5 else "and"} the Saturn square in 2026 {"will require careful attention and self-care" if metrics[2]['avg_daily_score'] < -5 else "appears manageable with preparation"}.

**Key Recommendation**: {"Given the intensity of the upcoming Saturn square, proactive planning for March-April 2026 is advisable" if metrics[2]['avg_daily_score'] < -5 else "The upcoming period is challenging but not unprecedented - use lessons from previous Saturn experiences"}.

---

*Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
*Analysis Period: December 2017 - December 2027*
*Transit data calculated using traditional astrological methods*
"""

    return report

def get_saturn_context(period_num: int, aspects: List[Dict[str, Any]]) -> str:
    """Generate Saturn context description for each period."""
    if period_num == 1:
        if any(a['aspect'] == 'conjunction' and a['natal_planet'] == 'Saturn' for a in aspects):
            return "Saturn Return - transiting Saturn conjunct natal Saturn (major life restructuring)"
        return "Saturn Return period (ages 29-30)"
    elif period_num == 2:
        return "Recovery period between Saturn return and square (integration phase)"
    elif period_num == 3:
        if any(a['aspect'] == 'square' for a in aspects):
            return "Saturn Square - transiting Saturn square natal Saturn and Sun (testing structures built during return)"
        return "Saturn Square period approaching"
    return "Unknown period"

def assess_difficulty(metrics: Dict[str, Any]) -> int:
    """
    Assess overall difficulty on 1-10 scale.

    Factors:
    - Average daily score
    - Percentage of difficult days
    - Worst day severity
    """
    score = 5  # Baseline

    # Average daily quality impact
    if metrics['avg_daily_score'] < -10:
        score += 3
    elif metrics['avg_daily_score'] < -5:
        score += 2
    elif metrics['avg_daily_score'] < 0:
        score += 1
    elif metrics['avg_daily_score'] > 5:
        score -= 1

    # Difficult days percentage impact
    if metrics['percent_difficult_days'] > 30:
        score += 2
    elif metrics['percent_difficult_days'] > 20:
        score += 1

    # Worst day severity impact
    if metrics['worst_day_score'] < -30:
        score += 1

    return max(1, min(10, score))

def main():
    """Main execution."""
    print("🔍 Saturn Periods Comparison Analysis")
    print("=" * 60)

    # Load all three periods
    print("\nLoading transit data for three periods...")

    try:
        period1_data = load_transit_data(PERIOD_1_FILE)
        print(f"✅ Period 1 (Saturn Return): {PERIOD_1_FILE.name}")
    except Exception as e:
        print(f"❌ Error loading Period 1: {e}")
        sys.exit(1)

    try:
        period2_data = load_transit_data(PERIOD_2_FILE)
        print(f"✅ Period 2 (Current Recovery): {PERIOD_2_FILE.name}")
    except Exception as e:
        print(f"❌ Error loading Period 2: {e}")
        sys.exit(1)

    try:
        period3_data = load_transit_data(PERIOD_3_FILE)
        print(f"✅ Period 3 (Saturn Square): {PERIOD_3_FILE.name}")
    except Exception as e:
        print(f"❌ Error loading Period 3: {e}")
        sys.exit(1)

    # Calculate metrics for each period
    print("\nCalculating comparison metrics...")

    metrics = [
        calculate_period_metrics(period1_data, "Saturn Return (29-30)"),
        calculate_period_metrics(period2_data, "Current Recovery (35-37)"),
        calculate_period_metrics(period3_data, "Saturn Square (37-38)"),
    ]

    # Identify Saturn aspects for each period
    saturn_aspects = {
        'period_1': identify_saturn_aspects(period1_data),
        'period_2': identify_saturn_aspects(period2_data),
        'period_3': identify_saturn_aspects(period3_data),
    }

    print(f"✅ Period 1: {metrics[0]['total_transits']} transits, avg daily score {metrics[0]['avg_daily_score']:.1f}")
    print(f"✅ Period 2: {metrics[1]['total_transits']} transits, avg daily score {metrics[1]['avg_daily_score']:.1f}")
    print(f"✅ Period 3: {metrics[2]['total_transits']} transits, avg daily score {metrics[2]['avg_daily_score']:.1f}")

    # Generate report
    print("\nGenerating comprehensive comparison report...")
    report = generate_report(metrics, saturn_aspects)

    # Save report
    output_path = Path(__file__).parent.parent / "profiles/darren/output/SATURN_PERIODS_COMPARISON.md"
    with open(output_path, 'w') as f:
        f.write(report)

    print(f"\n✅ Report saved: {output_path}")
    print("\n" + "=" * 60)
    print("Analysis complete!")

if __name__ == '__main__':
    main()
