"""
Profile Loader Utility
Manages loading and accessing astrology profiles.
"""

import yaml
from pathlib import Path
from typing import Optional, List, Dict, Any


class Profile:
    """Represents an astrology profile with birth data and seed data."""

    def __init__(self, name: str, base_dir: str = "profiles"):
        self.name = name
        self.base_dir = Path(base_dir)
        self.profile_dir = self.base_dir / name
        self.seed_data_dir = self.profile_dir / "seed_data"
        self.output_dir = self.profile_dir / "output"

        # Check if profile exists
        if not self.profile_dir.exists():
            raise ValueError(f"Profile '{name}' does not exist at {self.profile_dir}")

        # Load seed data if available
        self.seed_data_path = self.seed_data_dir / "master_seed_data.yaml"
        self._seed_data = None

    @property
    def seed_data(self) -> Optional[Dict[str, Any]]:
        """Load and cache seed data."""
        if self._seed_data is None and self.seed_data_path.exists():
            with open(self.seed_data_path, 'r') as f:
                self._seed_data = yaml.safe_load(f)
        return self._seed_data

    def get_seed_data_path(self, filename: str = "master_seed_data.yaml") -> Path:
        """Get path to seed data file."""
        return self.seed_data_dir / filename

    def get_output_path(self, filename: str) -> Path:
        """Get path to output file."""
        return self.output_dir / filename

    def get_birth_data(self) -> Optional[Dict[str, Any]]:
        """Get birth data from seed data."""
        if self.seed_data:
            return self.seed_data.get('birth_data')
        return None

    def get_chart_framework(self) -> Optional[Dict[str, Any]]:
        """Get chart framework (ascendant, MC, sect, etc.)."""
        if self.seed_data:
            return self.seed_data.get('chart_framework')
        return None

    def get_planets(self, traditional_only: bool = False) -> List[Dict[str, Any]]:
        """Get planet data, optionally filtered to traditional planets only."""
        if self.seed_data:
            planets = self.seed_data.get('planets', [])
            if traditional_only:
                return [p for p in planets if p.get('traditional', False)]
            return planets
        return []

    def get_houses(self) -> List[Dict[str, Any]]:
        """Get house data with rulers."""
        if self.seed_data:
            return self.seed_data.get('houses', [])
        return []

    def get_aspects(self, traditional_only: bool = False) -> List[Dict[str, Any]]:
        """Get aspect data, optionally filtered to traditional aspects only."""
        if self.seed_data:
            aspects = self.seed_data.get('aspects', [])
            if traditional_only:
                return [a for a in aspects if a.get('traditional', False)]
            return aspects
        return []

    def get_lots(self) -> List[Dict[str, Any]]:
        """Get Hermetic lots data."""
        if self.seed_data:
            return self.seed_data.get('lots', [])
        return []

    def get_nodes(self) -> Optional[Dict[str, Any]]:
        """Get lunar nodes data."""
        if self.seed_data:
            return self.seed_data.get('lunar_nodes')
        return None

    def get_elemental_balance(self) -> Optional[Dict[str, int]]:
        """Get elemental balance counts."""
        if self.seed_data:
            return self.seed_data.get('elemental_balance')
        return None

    def get_modality_balance(self) -> Optional[Dict[str, int]]:
        """Get modality balance counts."""
        if self.seed_data:
            return self.seed_data.get('modality_balance')
        return None

    def __repr__(self):
        return f"Profile(name='{self.name}', dir='{self.profile_dir}')"


def list_profiles(base_dir: str = "profiles") -> List[str]:
    """List all available profile names."""
    profiles_path = Path(base_dir)

    if not profiles_path.exists():
        return []

    # List directories that contain seed_data subdirectory
    profile_names = []
    for item in profiles_path.iterdir():
        if item.is_dir() and (item / "seed_data").exists():
            profile_names.append(item.name)

    return sorted(profile_names)


def load_profile(name: str, base_dir: str = "profiles") -> Profile:
    """Load a profile by name."""
    return Profile(name, base_dir)


def get_default_profile(base_dir: str = "profiles") -> Optional[Profile]:
    """Get the default profile.

    Returns 'darren' if available, otherwise the first alphabetically.
    """
    profiles = list_profiles(base_dir)

    if not profiles:
        return None

    # Prefer 'darren' if available
    if 'darren' in profiles:
        return load_profile('darren', base_dir)

    # Otherwise return first alphabetically
    return load_profile(profiles[0], base_dir)


def profile_exists(name: str, base_dir: str = "profiles") -> bool:
    """Check if a profile exists."""
    profile_path = Path(base_dir) / name
    return profile_path.exists() and (profile_path / "seed_data").exists()


# Convenience functions for quick access
def get_profile_seed_data(name: str, base_dir: str = "profiles") -> Optional[Dict[str, Any]]:
    """Quick function to get seed data for a profile."""
    try:
        profile = load_profile(name, base_dir)
        return profile.seed_data
    except ValueError:
        return None


def get_profile_birth_data(name: str, base_dir: str = "profiles") -> Optional[Dict[str, Any]]:
    """Quick function to get birth data for a profile."""
    try:
        profile = load_profile(name, base_dir)
        return profile.get_birth_data()
    except ValueError:
        return None
