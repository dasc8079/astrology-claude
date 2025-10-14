#!/usr/bin/env python3
"""
Profile Settings Loader
Centralized parser for profile.md settings files.

Usage:
    from profile_settings_loader import load_profile_settings

    settings = load_profile_settings('Darren_S')
    if settings['include_chiron']:
        # Include Chiron in calculations
"""

from pathlib import Path
from typing import Dict, Any


DEFAULT_SETTINGS = {
    # Traditional techniques
    'include_house_rulers': True,
    'include_lots': True,
    'include_nodes': True,
    'include_receptions': True,
    'include_bonification': True,
    'include_triplicity': True,
    'include_antiscia': True,
    'include_fixed_stars': True,

    # Modern points (optional)
    'include_chiron': False,
    'include_lilith': False,

    # Modern methods (optional overlays)
    'include_psychological': True,
    'include_modern_planets': True,  # Uranus, Neptune, Pluto as SECONDARY context

    # Timing techniques (for Life Arc mode)
    'include_firdaria': True,
    'include_progressions': True,
    'include_solar_returns': True,
    'include_profections': True,
    'include_zodiacal_releasing': True,

    # Output preferences
    'include_cite_sources': True,
    'include_process_file': True,
    'synthesis_depth': 'comprehensive',  # comprehensive, moderate, concise
}


def load_profile_settings(profile_name: str) -> Dict[str, Any]:
    """
    Load settings from profile.md file.

    Args:
        profile_name: Name of profile directory (e.g., 'Darren_S')

    Returns:
        Dictionary of settings with defaults applied for missing values

    Example:
        >>> settings = load_profile_settings('Darren_S')
        >>> if settings['include_chiron']:
        ...     print("Chiron enabled")
    """
    profile_path = Path(f'profiles/{profile_name}/profile.md')

    # Start with defaults
    settings = DEFAULT_SETTINGS.copy()

    if not profile_path.exists():
        print(f"Warning: Profile not found at {profile_path}, using default settings")
        return settings

    try:
        with open(profile_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse settings from profile.md
        # Settings can be in plain format OR inside ```ini code blocks
        # Format: setting_name: true/false  // optional comment

        in_code_block = False
        for line in content.split('\n'):
            # Track code block boundaries
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue

            # Only process lines (either in code block or plain text)
            line = line.strip()

            # Skip empty lines and section headers
            if not line or line.startswith('##') or line.startswith('['):
                continue

            # Skip lines that are just comments
            if line.startswith('#') and not ':' in line:
                continue

            # Strip C-style comments (// ...)
            if '//' in line:
                line = line.split('//')[0].strip()

            # Look for key: value pairs
            if ':' in line:
                parts = line.split(':', 1)
                if len(parts) != 2:
                    continue

                key = parts[0].strip()
                value = parts[1].strip().lower()

                # Parse boolean values
                if key in settings:
                    if value in ['true', 'yes', 'on', '1']:
                        settings[key] = True
                    elif value in ['false', 'no', 'off', '0']:
                        settings[key] = False
                    elif value in ['comprehensive', 'moderate', 'concise']:
                        settings[key] = value

        return settings

    except Exception as e:
        print(f"Warning: Could not parse profile settings: {e}")
        print(f"Using default settings")
        return settings


def get_enabled_features(profile_name: str) -> Dict[str, list]:
    """
    Get lists of enabled features organized by category.

    Args:
        profile_name: Name of profile directory

    Returns:
        Dictionary with categories and enabled features:
        {
            'traditional_techniques': ['house_rulers', 'lots', ...],
            'modern_points': ['chiron', 'lilith'],
            'timing_techniques': ['firdaria', 'profections', ...],
            'output_preferences': ['cite_sources', 'process_file']
        }
    """
    settings = load_profile_settings(profile_name)

    enabled = {
        'traditional_techniques': [],
        'modern_points': [],
        'modern_planets': [],
        'timing_techniques': [],
        'output_preferences': []
    }

    # Traditional techniques
    traditional_keys = [
        'house_rulers', 'lots', 'nodes', 'receptions', 'bonification',
        'triplicity', 'antiscia', 'fixed_stars'
    ]
    for key in traditional_keys:
        setting_key = f'include_{key}'
        if settings.get(setting_key, False):
            enabled['traditional_techniques'].append(key)

    # Modern points
    if settings.get('include_chiron', False):
        enabled['modern_points'].append('chiron')
    if settings.get('include_lilith', False):
        enabled['modern_points'].append('lilith')

    # Modern planets
    if settings.get('include_modern_planets', False):
        enabled['modern_planets'] = ['uranus', 'neptune', 'pluto']

    # Timing techniques
    timing_keys = [
        'firdaria', 'progressions', 'solar_returns',
        'profections', 'zodiacal_releasing'
    ]
    for key in timing_keys:
        setting_key = f'include_{key}'
        if settings.get(setting_key, False):
            enabled['timing_techniques'].append(key)

    # Output preferences
    if settings.get('include_cite_sources', False):
        enabled['output_preferences'].append('cite_sources')
    if settings.get('include_process_file', False):
        enabled['output_preferences'].append('process_file')
    enabled['output_preferences'].append(f"depth_{settings.get('synthesis_depth', 'comprehensive')}")

    return enabled


def validate_profile_settings(profile_name: str) -> Dict[str, Any]:
    """
    Validate profile settings and return validation report.

    Args:
        profile_name: Name of profile directory

    Returns:
        Dictionary with validation results:
        {
            'valid': True/False,
            'warnings': [...],
            'errors': [...],
            'settings': {...}
        }
    """
    result = {
        'valid': True,
        'warnings': [],
        'errors': [],
        'settings': {}
    }

    profile_path = Path(f'profiles/{profile_name}/profile.md')

    if not profile_path.exists():
        result['valid'] = False
        result['errors'].append(f"Profile not found: {profile_path}")
        return result

    # Load settings
    settings = load_profile_settings(profile_name)
    result['settings'] = settings

    # Validation checks

    # Check if both Chiron and Lilith are disabled in a psychological profile
    if settings.get('include_psychological') and not settings.get('include_chiron') and not settings.get('include_lilith'):
        result['warnings'].append(
            "Psychological overlay enabled but Chiron and Lilith disabled. "
            "Consider enabling at least one for shadow work/healing themes."
        )

    # Check if antiscia is disabled
    if not settings.get('include_antiscia'):
        result['warnings'].append(
            "Antiscia disabled. This is a high-value traditional technique with easy implementation."
        )

    # Check if fixed stars are disabled
    if not settings.get('include_fixed_stars'):
        result['warnings'].append(
            "Fixed stars disabled. This is a high-value traditional technique for dignity analysis."
        )

    # Check if no timing techniques are enabled (for Life Arc mode)
    timing_enabled = any([
        settings.get('include_firdaria'),
        settings.get('include_progressions'),
        settings.get('include_solar_returns'),
        settings.get('include_profections'),
        settings.get('include_zodiacal_releasing')
    ])
    if not timing_enabled:
        result['warnings'].append(
            "No timing techniques enabled. Life Arc reports will be limited."
        )

    return result


def print_settings_summary(profile_name: str):
    """
    Print a human-readable summary of profile settings.

    Args:
        profile_name: Name of profile directory
    """
    print(f"\n{'='*60}")
    print(f"Profile Settings: {profile_name}")
    print(f"{'='*60}\n")

    enabled = get_enabled_features(profile_name)

    print("TRADITIONAL TECHNIQUES:")
    if enabled['traditional_techniques']:
        for technique in enabled['traditional_techniques']:
            print(f"  ✅ {technique.replace('_', ' ').title()}")
    else:
        print("  (none enabled)")

    print("\nMODERN POINTS:")
    if enabled['modern_points']:
        for point in enabled['modern_points']:
            print(f"  ✅ {point.title()}")
    else:
        print("  (none enabled)")

    print("\nMODERN PLANETS (SECONDARY):")
    if enabled['modern_planets']:
        for planet in enabled['modern_planets']:
            print(f"  ✅ {planet.title()}")
    else:
        print("  (disabled)")

    print("\nTIMING TECHNIQUES:")
    if enabled['timing_techniques']:
        for technique in enabled['timing_techniques']:
            print(f"  ✅ {technique.replace('_', ' ').title()}")
    else:
        print("  (none enabled)")

    print("\nOUTPUT PREFERENCES:")
    for pref in enabled['output_preferences']:
        print(f"  ✅ {pref.replace('_', ' ').title()}")

    # Validation
    validation = validate_profile_settings(profile_name)
    if validation['warnings']:
        print(f"\n⚠️  WARNINGS ({len(validation['warnings'])}):")
        for warning in validation['warnings']:
            print(f"  • {warning}")

    if validation['errors']:
        print(f"\n❌ ERRORS ({len(validation['errors'])}):")
        for error in validation['errors']:
            print(f"  • {error}")

    print(f"\n{'='*60}\n")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python profile_settings_loader.py <profile_name>")
        print("Example: python profile_settings_loader.py Darren_S")
        sys.exit(1)

    profile_name = sys.argv[1]
    print_settings_summary(profile_name)
