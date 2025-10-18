#!/usr/bin/env python3
"""
Generate Life Arc Report from timeline JSON data
This script loads the timeline JSON and generates both process and synthesis markdown files
"""

import json
import sys
from datetime import datetime
from pathlib import Path

def load_timeline_data(json_path):
    """Load timeline JSON data"""
    with open(json_path, 'r') as f:
        return json.load(f)

def get_zr_fortune_periods(data):
    """Extract ZR Fortune L1 periods"""
    periods = []
    if 'zr_fortune' in data and 'l1_periods' in data['zr_fortune']:
        for period in data['zr_fortune']['l1_periods']:
            periods.append({
                'start_age': period['start_age'],
                'end_age': period['end_age'],
                'sign': period['sign'],
                'lord': period.get('ruler', period.get('lord', 'Unknown')),
                'duration': period['duration']
            })
    return periods

def get_zr_spirit_periods(data):
    """Extract ZR Spirit L1 periods"""
    periods = []
    if 'zr_spirit' in data and 'l1_periods' in data['zr_spirit']:
        for period in data['zr_spirit']['l1_periods']:
            periods.append({
                'start_age': period['start_age'],
                'end_age': period['end_age'],
                'sign': period['sign'],
                'lord': period.get('ruler', period.get('lord', 'Unknown')),
                'duration': period['duration']
            })
    return periods

def get_firdaria_periods(data):
    """Extract Firdaria major and sub periods"""
    firdaria = {'sect': None, 'major_periods': [], 'sub_periods': []}
    if 'firdaria' in data:
        firdaria['sect'] = data['firdaria'].get('sect', 'unknown')
        firdaria['major_periods'] = data['firdaria'].get('major_periods', [])
        firdaria['sub_periods'] = data['firdaria'].get('sub_periods', [])
    return firdaria

def get_planetary_returns(data):
    """Extract planetary returns"""
    returns = []
    if 'planetary_returns' in data:
        returns = data['planetary_returns']
    return returns

def get_progression_sign_changes(data):
    """Extract progressed Sun sign changes"""
    changes = []
    if 'progression_sign_changes' in data:
        changes = data['progression_sign_changes']
    return changes

def get_convergences(data):
    """Extract convergence events"""
    convergences = {'major': [], 'significant': [], 'notable': []}
    if 'convergence' in data:
        convergences = data['convergence']
    return convergences

def generate_process_file(data, output_path):
    """Generate the process markdown file with technical details"""
    profile = data.get('profile', 'Unknown')
    birth_data = data.get('birth_data', {})
    age_range = data.get('age_range', {'start': 0, 'end': 100})

    content = f"""# Life Arc Process File
**Profile**: {profile}
**Birth**: {birth_data.get('date')} at {birth_data.get('time')}
**Location**: {birth_data.get('location')}
**Age Range**: {age_range['start']}-{age_range['end']}
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Zodiacal Releasing from Fortune (L1 Periods)

"""

    fortune_periods = get_zr_fortune_periods(data)
    for period in fortune_periods:
        content += f"- **{period['sign']}** (Ages {period['start_age']}-{period['end_age']}): {period['duration']} years, {period['lord']} time-lord\n"

    content += "\n## Zodiacal Releasing from Spirit (L1 Periods)\n\n"

    spirit_periods = get_zr_spirit_periods(data)
    for period in spirit_periods:
        content += f"- **{period['sign']}** (Ages {period['start_age']}-{period['end_age']}): {period['duration']} years, {period['lord']} time-lord\n"

    content += "\n## Firdaria\n\n"
    firdaria = get_firdaria_periods(data)
    content += f"**Chart Sect**: {firdaria['sect']}\n\n"
    content += "### Major Periods (Ages 0-75)\n\n"
    for period in firdaria['major_periods']:
        content += f"- **{period['planet']}** (Ages {period['start_age']}-{period['end_age']}): {period['duration']} years\n"

    content += "\n## Planetary Returns\n\n"
    returns = get_planetary_returns(data)
    for ret in returns:
        content += f"- **{ret['event']}** at age {ret['age']:.1f}\n"

    content += "\n## Progressed Sun Sign Changes\n\n"
    prog_changes = get_progression_sign_changes(data)
    for change in prog_changes:
        content += f"- Age {change['age']}: {change['point']} → {change['new_sign']}\n"

    content += "\n## Convergence Events\n\n"
    convergences = get_convergences(data)

    content += "### MAJOR Convergences (25+ points)\n\n"
    for event in convergences.get('major', []):
        content += f"- **Age {event['age']}** ({event['score']} points):\n"
        for reason in event['reasons']:
            content += f"  - {reason}\n"

    content += "\n### SIGNIFICANT Convergences (15-24 points)\n\n"
    for event in convergences.get('significant', []):
        content += f"- **Age {event['age']}** ({event['score']} points):\n"
        for reason in event['reasons']:
            content += f"  - {reason}\n"

    content += "\n### NOTABLE Convergences (8-14 points)\n\n"
    for event in convergences.get('notable', []):
        content += f"- **Age {event['age']}** ({event['score']} points):\n"
        for reason in event['reasons']:
            content += f"  - {reason}\n"

    content += "\n---\n\n*Technical process file for Life Arc report - V3 system*\n"

    with open(output_path, 'w') as f:
        f.write(content)

    print(f"✓ Process file written to: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_life_arc_report.py <timeline_json_path>")
        sys.exit(1)

    json_path = sys.argv[1]

    if not Path(json_path).exists():
        print(f"Error: JSON file not found: {json_path}")
        sys.exit(1)

    # Load data
    print(f"Loading timeline data from {json_path}...")
    data = load_timeline_data(json_path)

    # Determine output paths
    json_file = Path(json_path)
    output_dir = json_file.parent
    profile = data.get('profile', 'unknown')
    age_range = data.get('age_range', {'start': 0, 'end': 100})
    today = datetime.now().strftime('%Y-%m-%d')

    process_path = output_dir / f"life_arc_process_{profile}_ages_{age_range['start']}-{age_range['end']}_v3_{today}.md"

    # Generate process file
    generate_process_file(data, process_path)

    print("\n" + "="*80)
    print("PROCESS FILE GENERATION COMPLETE")
    print("="*80)
    print(f"\nProcess file: {process_path}")
    print(f"\nNOTE: Synthesis file must be written manually by life-arc-interpreter agent")
    print("      based on the timeline data and process file.\n")

if __name__ == '__main__':
    main()
