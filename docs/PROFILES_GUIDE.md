# Profiles Guide

## Overview

The astrology application uses a profile-based system to manage birth data and generate natal chart interpretations. Each profile contains:

- Birth data (date, time, location, coordinates)
- Generated seed data (planets, houses, aspects, lots, etc.)
- Output interpretations and reports

## Profile Structure

```
profiles/
└── <profile_name>/
    ├── seed_data/
    │   └── master_seed_data.yaml    # Generated chart calculations
    └── output/
        └── (future: interpretations and reports)
```

## Quick Start

### 1. Generate Seed Data

Create natal chart seed data for a new profile:

```bash
source venv/bin/activate  # Activate virtual environment

python scripts/seed_data_generator.py \
  --name "john_doe" \
  --date "1990-01-15" \
  --time "14:30:00" \
  --location "New York, NY" \
  --lat 40.7128 \
  --lon -74.0060 \
  --timezone "America/New_York"
```

**Parameters**:
- `--name`: Profile identifier (lowercase, use underscores)
- `--date`: Birth date (YYYY-MM-DD format)
- `--time`: Birth time (HH:MM:SS, 24-hour format)
- `--location`: Birth location (descriptive text)
- `--lat`: Latitude in decimal degrees
- `--lon`: Longitude in decimal degrees (negative for West)
- `--timezone`: IANA timezone (e.g., "America/New_York", "Europe/London")

**Finding Coordinates and Timezone**:
- Use [https://www.latlong.net/](https://www.latlong.net/) for coordinates
- Use [https://www.timeanddate.com/worldclock/](https://www.timeanddate.com/worldclock/) for timezone

### 2. Load Profile Data (Python)

Use the profile_loader utility to access profile data:

```python
from scripts.profile_loader import load_profile, list_profiles

# List all profiles
profiles = list_profiles()
print(f"Available profiles: {profiles}")

# Load a specific profile
profile = load_profile("john_doe")

# Access birth data
birth_data = profile.get_birth_data()
print(f"Born: {birth_data['date']} at {birth_data['time']}")

# Access chart framework
framework = profile.get_chart_framework()
print(f"Sect: {framework['sect']['type']}")
print(f"Ascendant: {framework['ascendant']['sign']}")

# Access planets
planets = profile.get_planets(traditional_only=True)
for planet in planets:
    print(f"{planet['name']}: {planet['sign']} (house {planet['house']})")

# Access houses with rulers
houses = profile.get_houses()
for house in houses:
    ruler = house['ruler']
    print(f"House {house['number']} ({house['sign']}): ruled by {ruler['planet']}")

# Access aspects
aspects = profile.get_aspects(traditional_only=True)
for aspect in aspects:
    print(f"{aspect['planet_1']} {aspect['aspect_type']} {aspect['planet_2']}")

# Access Hermetic lots
lots = profile.get_lots()
for lot in lots:
    print(f"{lot['name']}: {lot['position']['sign']} {lot['position']['dms']}")
```

## Seed Data Contents

The `master_seed_data.yaml` file contains:

### Metadata
- Profile name
- Generation timestamp
- Schema version

### Birth Data
- Date, time, location
- Coordinates (latitude, longitude)
- Timezone information

### Chart Framework
- House system (whole-sign)
- Ayanamsa (tropical)
- Sect (day/night chart)
- Ascendant (sign, degree, DMS)
- Midheaven (sign, degree, DMS)

### Planets
For each planet (traditional 7 + modern 3):
- Name, symbol, traditional flag
- Position (longitude, sign, degree, DMS)
- Speed and retrograde status
- House placement
- **Essential dignities**: domicile, exaltation, detriment, fall, triplicity, term, face
- **Accidental dignities**: angular, succedent, cadent, rejoicing
- **Condition**: sect status, bonified/maltreated, speed, combust/cazimi/under beams

### Houses
For each of 12 houses:
- Number, sign, cusp degree (whole-sign = 0°)
- **House ruler**: planet, position (sign, house), dignities
- **Planets in house**: list of traditional planets

### Aspects
Traditional Ptolemaic aspects + modern:
- Type (conjunction, sextile, square, trine, opposition)
- Orb (exact difference in degrees)
- Planets involved
- Applying/separating
- Traditional flag
- Nature (harmonious/challenging/neutral) and strength

### Lots
Hermetic lots (Fortune, Spirit):
- Name and symbol
- Position (sign, degree, DMS)
- Calculation formulas (day/night variations)

### Lunar Nodes
- North node (sign, degree, DMS)
- South node (sign, degree, DMS)

### Balance
- **Elemental**: count of traditional planets in fire/earth/air/water
- **Modality**: count of traditional planets in cardinal/fixed/mutable

## Traditional Hellenistic Approach

This system prioritizes **traditional Hellenistic astrology**:

### Traditional Planets (Primary)
- Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn
- Used for dignity calculations and elemental balance

### Modern Planets (Secondary/Overlay)
- Uranus, Neptune, Pluto
- Clearly marked with `traditional: false`
- Can be filtered out using `traditional_only=True` parameters

### Whole-Sign House System
- Each house = complete 30° zodiac sign
- 1st house = rising sign (entire sign)
- Simple, traditional, no complex cusp calculations

### Essential Dignities
- **Domicile**: planet in own sign (strongest)
- **Exaltation**: planet in exaltation sign
- **Detriment**: planet in opposite of own sign
- **Fall**: planet in opposite of exaltation
- **Triplicity**: element ruler (day/night/participating)
- **Term**: Egyptian terms (future enhancement)
- **Face**: 10° decans (future enhancement)

### Accidental Dignities
- **Angular**: houses 1, 4, 7, 10 (strongest)
- **Succedent**: houses 2, 5, 8, 11 (moderate)
- **Cadent**: houses 3, 6, 9, 12 (weakest)
- **Rejoicing**: planet in its house of joy (future)

### House Rulers (Critical!)
House rulers show how different life areas connect:
- 1st house ruler (chart ruler) shows overall direction
- Where the ruler is placed shows where 1st house energy flows
- Ruler's dignity shows strength of that life area

Example:
```yaml
houses:
- number: 1
  sign: Libra
  ruler:
    planet: Venus
    position:
      sign: Taurus
      house: 8
      dignities: domicile
```

This means:
- 1st house (self, vitality) is in Libra
- Ruled by Venus (relationships, beauty, harmony)
- Venus in Taurus (domicile = very strong)
- Venus in 8th house (transformation, shared resources)
- **Interpretation**: Identity strongly connected to relationships and transformation; powerful ability to harmonize deep psychological themes

## Privacy Note

Profiles contain **personal birth data** and are excluded from git via `.gitignore`. This keeps natal charts private while allowing code to be shared publicly.

## Next Steps

After generating seed data:
1. Build interpretation layer (queries seed data + RAG database)
2. Generate natal horoscope synthesis
3. Add life arc calculations (profections, zodiacal releasing)
4. Create transit reports

See `CURRENT_WORK.md` for project status and roadmap.
