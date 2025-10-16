#!/usr/bin/env python3
"""
Generate Life Arc Timeline JSON
Wrapper script to generate timeline JSON for life arc interpretation.
"""

import sys
import json
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from life_arc_generator import generate_life_arc_timeline

def main():
    if len(sys.argv) < 4:
        print("Usage: python generate_life_arc_json.py PROFILE START_AGE END_AGE [OUTPUT_FILE]")
        sys.exit(1)

    profile_name = sys.argv[1]
    start_age = int(sys.argv[2])
    end_age = int(sys.argv[3])
    output_file = sys.argv[4] if len(sys.argv) > 4 else None

    # Generate timeline with V3 enhancements (simplified_mode=False to include all scoring overlays)
    timeline = generate_life_arc_timeline(
        profile_name=profile_name,
        start_age=start_age,
        end_age=end_age,
        include_fortune=True,
        include_spirit=True,
        include_progressions=False,
        include_solar_returns=False,
        current_date=None,
        simplified_mode=False  # Include all scoring overlays (traditional periods, Saturn aftermath, etc.)
    )

    # Convert to JSON-serializable format
    json_data = json.dumps(timeline, indent=2, default=str)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(json_data)
        print(f"Timeline JSON saved to: {output_file}")
    else:
        print(json_data)

if __name__ == '__main__':
    main()
