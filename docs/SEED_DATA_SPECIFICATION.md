# Seed Data Specification

**Version**: 1.0
**Last Updated**: October 12, 2025
**Purpose**: Documents all astrological data points calculated in natal chart seed data

---

## Overview

The seed data generator (`scripts/seed_data_generator.py`) calculates comprehensive astrological data from birth information. This data serves as the foundation for all natal chart interpretations.

**Output Format**: YAML file stored at `/profiles/{Name}/seed_data/natal_interpretation_enhanced.md` or `master_seed_data.yaml`

**Generation**: Run via `python scripts/seed_data_generator.py --profile {Name}`

---

## I. Core Astronomical Data

### Birth Information
- **Date**: YYYY-MM-DD
- **Time**: HH:MM:SS (local time)
- **Location**: City, State/Country
- **Coordinates**: Latitude/Longitude (decimal degrees)
- **Timezone**: Standard timezone identifier
- **Julian Day**: Astronomical time calculation

### Planetary Positions (Traditional Seven + Modern Three)

**Traditional Planets** (Primary interpretive weight):
- Sun
- Moon
- Mercury
- Venus
- Mars
- Jupiter
- Saturn

**Modern Planets** (Secondary psychological context):
- Uranus
- Neptune
- Pluto

**For Each Planet**:
- Longitude (0-360°)
- Latitude
- Speed (daily motion in degrees)
- Retrograde status (direct/retrograde)
- Sign placement (0-12)
- Degree within sign (0-30°)
- House placement (whole-sign, 1-12)

### Houses

**System**: Whole-sign houses (Hellenistic/traditional)

**Calculated**:
- Ascendant (rising sign + exact degree)
- Midheaven (MC)
- Descendant (DSC)
- Imum Coeli (IC)
- 12 house cusps (whole-sign: each house = one complete sign)

**House Meanings** (Traditional):
1. Body, vitality, appearance, life direction
2. Money, possessions, values, resources
3. Siblings, communication, short travel, learning
4. Home, family, parents (especially father), foundation
5. Children, creativity, pleasure, romance
6. Illness, service, work, daily obligations, enemies
7. Marriage, partnerships, open enemies, contracts
8. Death, shared resources, inheritance, transformation
9. Philosophy, religion, long travel, higher education
10. Career, reputation, public standing, honors
11. Friends, groups, hopes, benefactors
12. Hidden matters, seclusion, secret enemies, self-undoing

---

## II. Essential Dignities (Traditional)

### Sect Determination
- **Day Chart**: Sun above horizon at birth
- **Night Chart**: Sun below horizon at birth

**Sect Benefic**:
- Day chart: Jupiter (primary benefic)
- Night chart: Venus (primary benefic)

**Sect Malefic**:
- Day chart: Mars (sect malefic, more challenging)
- Night chart: Saturn (sect malefic, more challenging)

### Dignity Assessments

**For Each Planet**:

**Domicile (Rulership)** - Planet in the sign it rules
- Strongest dignity
- Planet operates with natural authority
- Traditional rulers only (no modern rulerships)

**Exaltation** - Planet in its exaltation sign
- Empowered, honored, elevated
- Second strongest dignity

**Detriment** - Planet opposite its domicile
- Weakened, uncomfortable
- Struggles to express naturally

**Fall** - Planet opposite its exaltation
- Debilitated, dishonored
- Most challenging placement

**Triplicity** - Elemental dignity (day/night/participating ruler)
- Fire: Aries, Leo, Sagittarius
- Earth: Taurus, Virgo, Capricorn
- Air: Gemini, Libra, Aquarius
- Water: Cancer, Scorpio, Pisces

**Bounds/Terms** - Egyptian terms (minor dignity)
- Sub-divisions of each sign ruled by different planets

**Decans/Faces** - 10° divisions of each sign
- Minor dignity, adds texture

### Special Conditions

**Combustion**: Planet within 8.5° of Sun (weakened, "burned up")

**Cazimi**: Planet within 17' of Sun (empowered, "in the heart of the Sun")

**Under the Beams**: Planet within 15° of Sun (hidden, obscured)

**Planetary Strength Score**: 0-10 composite score based on:
- Essential dignities (domicile, exaltation, etc.)
- Accidental dignities (house placement, aspects)
- Special conditions (combustion, retrograde, etc.)

---

## III. Classical Aspects

**Aspects Calculated** (Ptolemaic/Classical only):
- **Conjunction** (0°): Blending, intensity, fusion
- **Sextile** (60°): Support, opportunity, ease (benefic aspect)
- **Square** (90°): Tension, challenge, dynamic friction
- **Trine** (120°): Harmony, flow, natural ease (benefic aspect)
- **Opposition** (180°): Polarity, balance/conflict, awareness

**Orbs**:
- Major aspects: ±8° (traditional maximum)
- Exactness window: ±3° (strongest effect)

**For Each Aspect**:
- Planets involved
- Aspect type
- Orb (exact distance from perfect aspect)
- Applying/Separating (approaching exactness vs. moving away)

**NOT Calculated** (not traditional):
- Harmonic aspects (quintile, septile, etc.)
- Midpoints
- Minor aspects

---

## IV. House Rulers (PRIMARY Traditional Technique)

**Purpose**: Shows HOW each life area manifests

**For Each House** (1-12):
- **Ruling Planet**: Planet that rules the sign on the house cusp
- **Ruler's Sign**: Where the ruler is located
- **Ruler's House**: Which house the ruler occupies
- **Ruler's Condition**: Strength assessment (strong/moderate/weak/weakened)
  - Angular (houses 1, 4, 7, 10): Strong
  - Succedent (houses 2, 5, 8, 11): Moderate
  - Cadent (houses 3, 6, 9, 12): Weak
  - Additional conditions: combust, retrograde, dignities
- **Ruler's Aspects**: Key aspects to other planets

**Interpretation**: Ruler's placement shows the PATH for that house's themes

Example: 10th house ruler in 5th house → Career path through creativity

---

## V. Lots (Hellenistic Hermetic Tradition)

**Calculation Method**: Specific formula for each lot using planetary positions and Ascendant

**Lots Calculated**:

1. **Lot of Fortune** (Body/Health/Livelihood)
   - Day: ASC + Moon - Sun
   - Night: ASC + Sun - Moon
   - Traditional "Part of Fortune"

2. **Lot of Spirit** (Career/Action/Vitality)
   - Day: ASC + Sun - Moon
   - Night: ASC + Moon - Sun
   - Reveals soul's animating principle

3. **Lot of Eros** (Desires/Love/Attraction)
   - Reveals what attracts and compels

4. **Lot of Necessity** (Fate/Constraint/Limitation)
   - Shows areas of fated limitation

5. **Lot of Courage** (Boldness/Bravery/Risk-taking)
   - Reveals capacity for courage

6. **Lot of Victory** (Success/Triumph/Achievement)
   - Shows potential for success

7. **Lot of Basis** (Foundation/Stability/Security)
   - Foundation upon which life is built

8. **Lot of Exaltation** (Peak Periods/Honors/Recognition)
   - Times and areas of maximum elevation

9. **Lot of Nemesis** (Challenges/Rivals/Opposition)
   - Sources of difficulty and rivalry

10. **Lot of Marriage** (Partnership Themes)
    - Nature and quality of partnerships

11. **Lot of Children** (Generativity/Legacy/Offspring)
    - Creative and generative capacity

12. **Lot of Siblings** (Peer Relationships/Equals)
    - Relationship with equals and peers

**For Each Lot**:
- Longitude (position in zodiac)
- Sign placement
- House placement
- Aspects to planets
- Ruler of the lot's sign

---

## VI. Lunar Nodes

**North Node (Rahu)**: Evolutionary direction, soul's growth path
**South Node (Ketu)**: Past patterns, what must be released

**Calculated**:
- Longitude
- Sign placement
- House placement
- Aspects to planets

**Interpretation**:
- South Node: Comfort zone, past life skills, area to release
- North Node: Growth edge, soul's evolutionary intention

---

## VII. Angles & Special Points

### Angles (The Four Pillars)

**Ascendant (ASC) - 1st House Cusp**:
- Physical body, appearance, approach to life
- Most personal point in chart
- Ruler = Chart Ruler (primary significator of self)

**Midheaven (MC) - 10th House Cusp**:
- Career, reputation, public standing
- Visible achievements and honors

**Descendant (DSC) - 7th House Cusp**:
- Partnerships, marriage, open enemies
- Shadow self, what we project onto others

**Imum Coeli (IC) - 4th House Cusp**:
- Home, family, roots, foundation
- Private life, inner world

### Aspect to Angles

**Calculated**:
- Planetary aspects to ASC, MC, DSC, IC
- Only major aspects (conjunction, sextile, square, trine, opposition)
- Orbs: ±8°

**Significance**: Planets aspecting angles gain extra importance in chart

---

## VIII. Chart Patterns

### Stelliums
**Definition**: 3+ planets in same sign OR same house
**Calculated**:
- Sign stelliums (by zodiac sign)
- House stelliums (by house placement)

**Significance**: Concentration of energy, dominant theme

### Elemental Balance

**Elements Calculated**:
- Fire: Aries, Leo, Sagittarius (initiative, spirit, vision)
- Earth: Taurus, Virgo, Capricorn (practicality, stability, manifestation)
- Air: Gemini, Libra, Aquarius (intellect, communication, ideas)
- Water: Cancer, Scorpio, Pisces (emotion, intuition, depth)

**Count**: Number of planets in each element

**Dominant Element**: Element with most planets (4+)

### Modality Balance

**Modalities Calculated**:
- Cardinal: Aries, Cancer, Libra, Capricorn (initiation, leadership)
- Fixed: Taurus, Leo, Scorpio, Aquarius (stability, persistence)
- Mutable: Gemini, Virgo, Sagittarius, Pisces (adaptability, flexibility)

**Count**: Number of planets in each modality

**Dominant Modality**: Modality with most planets (4+)

---

## IX. Receptions (Traditional Technique)

### Mutual Reception
**Definition**: Two planets each in the sign ruled by the other

**Example**: Mars in Libra + Venus in Aries
- Mars is in Venus's sign (Libra)
- Venus is in Mars's sign (Aries)
- Creates mutual support, exchange of power

**Calculated**:
- All mutual receptions between planets
- Type of reception (domicile, exaltation, etc.)

**Significance**: Planets in mutual reception can "help each other out," mitigating difficult placements

---

## X. Bonification (Benefic Support)

**Definition**: Benefic (Venus or Jupiter) supporting a malefic (Mars or Saturn) through aspect or placement

**Types**:
1. **Aspect Bonification**: Benefic trines or sextiles malefic
2. **Reception Bonification**: Benefic receives malefic (malefic in benefic's sign)
3. **Angular Bonification**: Benefic on angle supporting malefic

**Calculated**:
- Venus supporting Mars or Saturn
- Jupiter supporting Mars or Saturn
- Type of bonification
- Strength of support

**Significance**: Softens malefic difficulties, provides mitigation

---

## XI. Modern Points (Optional, Not Traditional)

### Black Moon Lilith
**Definition**: Lunar apogee (point where Moon is farthest from Earth)

**Calculated**:
- Longitude
- Sign placement
- House placement

**Interpretation**: Shadow feminine, primal instincts, rejection themes

**Settings Control**: `include_lilith: true/false`

### Chiron
**Definition**: Minor planet between Saturn and Uranus

**Calculated**:
- Longitude
- Sign placement
- House placement
- Retrograde status

**Interpretation**: Wounded healer archetype, core wound and healing gift

**Settings Control**: `include_chiron: true/false`

### Vertex
**Definition**: Mathematical point (not astronomical body)

**Calculated**:
- Longitude
- Sign placement
- House placement

**Interpretation**: Fated encounters, karmic meetings

**Settings Control**: `include_vertex: true/false`

**Note**: These are NOT part of traditional Hellenistic astrology. They add modern psychological context when enabled.

---

## XII. Data Organization

### File Structure

**Primary Output**: `natal_interpretation_enhanced.md` or `master_seed_data.yaml`

**Sections**:
1. Birth data and chart metadata
2. Sect determination
3. Planetary positions and strengths
4. Houses and angles
5. Essential dignities
6. Classical aspects
7. House rulers
8. Lots
9. Lunar nodes
10. Angle aspects
11. Chart patterns (stelliums, element/modality balance)
12. Receptions
13. Bonification
14. Modern points (if enabled)

### Hierarchical Organization

**I. Traditional Foundation**
- Chart sect
- Planetary strength summary
- Chart patterns

**II. Traditional Enhancements**
- House rulers
- Lunar nodes
- Angle aspects
- Lots
- Receptions
- Bonification

**III. Modern Context** (Optional)
- Chiron
- Lilith
- Jungian/psychological overlays (if enabled)

---

## XIII. Calculation Standards

### Swiss Ephemeris
- **Library**: pyswisseph v2.10.3.2
- **Precision**: 0.0001° accuracy
- **Ephemeris Files**: DE431 (covers 13,000 BCE - 17,000 CE)

### House System
- **Primary**: Whole-sign houses (traditional/Hellenistic)
- **Also Calculated**: Placidus, Koch, Equal (for reference)
- **Standard**: Whole-sign used for all interpretations

### Time Handling
- All times converted to UTC for calculation
- Local time and timezone stored for reference
- Julian day calculation for astronomical precision

### Coordinate System
- Tropical zodiac (not sidereal)
- Geocentric (Earth-centered) perspective
- Ecliptic longitude (0-360°)

---

## XIV. Settings Integration

### Profile-Level Configuration

Each profile's `profile.md` contains settings that control:

**Traditional Techniques** (Usually all enabled):
```ini
include_house_rulers: true
include_lots: true
include_nodes: true
include_receptions: true
include_bonification: true
include_angles_aspects: true
```

**Modern Methods** (Optional):
```ini
include_lilith: true
include_chiron: true
include_psychological: false | "basic" | "deep"
```

**Currently**: Settings exist but are NOT yet read by interpretation agents. This is planned enhancement.

---

## XV. Data Quality & Validation

### Validation Checks

**Birth Data**:
- Date within valid range (1900-2100)
- Time in 24-hour format
- Coordinates within valid ranges (-90° to 90° lat, -180° to 180° lon)
- Timezone recognized

**Calculations**:
- All planetary positions between 0-360°
- House cusps properly ordered
- Aspects within valid orb ranges
- Dignities match reference tables

**Completeness**:
- All 10 planets calculated
- All 12 houses assigned
- All major aspects found
- All lots calculated

---

## XVI. Future Enhancements

### Planned Additions

1. **Antiscia/Contra-antiscia**: Mirror degrees
2. **Fixed Stars**: Major fixed stars conjunct planets/angles
3. **Decans**: Detailed decan analysis (currently calculated but not fully used)
4. **Bounds/Terms**: Detailed Egyptian bounds analysis (currently calculated but not fully used)
5. **Planetary Hours**: Planetary hour of birth
6. **Almuten Figuration**: Most powerful planet calculation
7. **Firdaria Integration**: Link to timing techniques

### Settings-Aware Generation

**Goal**: Seed data generator reads profile.md settings and only calculates what's enabled

**Benefit**: Faster generation, cleaner output, user control

**Status**: Planned for Phase 2

---

## XVII. Usage Examples

### Generating Seed Data

```bash
# Generate from profile
python scripts/seed_data_generator.py --profile Darren_S

# Generate with explicit data
python scripts/seed_data_generator.py \\
  --name "John Doe" \\
  --date "1990-01-15" \\
  --time "14:30:00" \\
  --location "New York, NY" \\
  --lat 40.7128 \\
  --lon -74.0060 \\
  --timezone "America/New_York"
```

### Accessing Seed Data

**In Python**:
```python
import yaml

with open('profiles/Darren_S/seed_data/master_seed_data.yaml') as f:
    data = yaml.safe_load(f)

# Access planetary positions
sun_position = data['planets']['Sun']['longitude']
sun_sign = data['planets']['Sun']['sign']

# Access house rulers
tenth_house_ruler = data['house_rulers']['10']['ruling_planet']

# Access lots
fortune_sign = data['lots']['Fortune']['sign']
```

**In Agents**:
Agents receive seed data and extract needed information for interpretation.

---

## XVIII. Related Documentation

- [PROFILE_STRUCTURE.md](./PROFILE_STRUCTURE.md) - Profile organization
- [OUTPUT_STYLE_GUIDE.md](./OUTPUT_STYLE_GUIDE.md) - Interpretation format standards
- [DATA_FORMATS.md](./DATA_FORMATS.md) - Complete data schemas
- [REFERENCE.md](../REFERENCE.md) - Astrological systems reference

---

**Maintained by**: docs-updater-astrology agent
**Questions**: See TROUBLESHOOTING.md or project documentation
