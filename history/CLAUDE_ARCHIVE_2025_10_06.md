# Astrology RAG Database Project

## Project Overview

This project creates a comprehensive Retrieval-Augmented Generation (RAG) database for traditional and Hellenistic astrology. The goal is to extract, structure, and index astrological knowledge from authoritative reference books, making it queryable by AI agents for birth chart interpretation and astrological analysis.

### Primary Objectives

1. Extract structured astrological knowledge from foundational reference texts
2. Create a queryable database with semantic search capabilities
3. Maintain source attribution and cross-reference validation
4. Support AI agents in generating accurate, traditional-based astrological interpretations
5. Provide context-aware retrieval for chart delineation, predictive techniques, and timing systems

### Target Use Cases

- Birth chart interpretation (natal astrology)
- Predictive techniques (progressions, profections, transits)
- Dignity and debility assessment
- Aspect analysis and synthesis
- Timing method implementation
- Traditional technique validation

---

## Astrology Application Project

Building on the RAG database foundation, this project is developing a comprehensive astrology application with three main modes and two rolling chat interfaces.

### Application Vision

**Three Main Modes**:
1. **Natal Horoscope**: Generate comprehensive birth chart interpretations using traditional/Hellenistic methods
2. **Life Arc Report**: Generate comprehensive life timeline from birth to age 100 showing major chapters, turning points, and timing patterns
3. **Transit Report**: Analyze current and upcoming transits with exact timing
4. **Additional Timing Techniques**: Profections, progressions, returns, and other predictive methods

**Two Rolling Chat Interfaces**:
1. **Horoscope Inquirer**: Deep-dive questions about natal chart
2. **Transit/Advice Chatbot**: Transit-specific questions and astrological guidance

**Technical Stack**:
- **Interpretation/Synthesis**: Claude Code agents (natal-interpreter, transit-analyzer, timing technique agents)
- **Astronomical Calculations**: Swiss Ephemeris for planetary positions, houses, aspects, transits
- **Knowledge Base**: RAG database for traditional interpretations
- **Embeddings**: OpenAI API (embeddings only, not for LLM calls)
- **Output**: `/reports/` folder for all generated horoscopes and transit reports
- **Migration Path**: Can migrate to GPT-5 API later if desired; agent instructions serve as approved "prompts"

**Full Planning Document**: See `/docs/session_goals.md` for complete vision, staged implementation plan, and technical specifications.

### Current Status

**Stage -1: RAG Database Enhancement** - COMPLETE ✅
- Created session_goals.md with North Star vision and staged implementation plan
- Added 223 new chunks from Liz Greene's "The Horoscope in Manifestation"
- Total database: 2,472 chunks (up from 2,249)
- Assessed literature redundancy (all 6 sources provide unique value)
- Created `/reports/` folder for generated horoscopes and transit reports

**Stage 0: Research Timing Techniques** - COMPLETE ✅
- Researched 8 traditional timing techniques using RAG database queries
- Identified 3 core techniques for implementation (Mode 3+):
  - Annual Profections (REQUIRED for transit filtering)
  - Zodiacal Releasing
  - Secondary Progressions
- Created comprehensive timing techniques plan: `/docs/timing_techniques_plan.md` (25+ pages)
- Critical discovery: Annual profections required for transit priority system
- Updated session_goals.md with Stage 0 findings

**Infrastructure Improvement: Documentation Automation** - COMPLETE ✅
- Strengthened documentation update automation system
- Added proactive triggers to docs-updater-astrology agent
- Added proactive triggers to astrology-rag-builder agent
- Defined clear agent division of labor for session_goals.md
- Updated all agent configuration files
- Created comprehensive documentation update protocol in Development Guidelines
- Both critical agents (docs-updater and rag-builder) now trigger automatically

**Mode 1: Natal Horoscope Generator** - COMPLETE ✅
- **Stage 1.1**: Created natal-interpreter agent (`.claude/agents/natal-interpreter.md`) ✅
- **Stage 1.2**: Built horoscope_generator.py script ✅
- **Stage 1.3**: Natal Interpretation Enhancement Research - COMPLETE ✅
- **Stage 1.4**: Natal Interpretation Enhancements - PENDING ⏳
- **Current capabilities:**
  - Generate comprehensive natal psychological profiles using traditional/Hellenistic methods
  - Two-part output structure: Accessible synthesis + Technical analysis
  - Hellenistic foundation with modern psychological overlay
  - RAG database integration for traditional interpretations
  - Sect-based interpretation with planetary strength assessment
  - Multi-profile system with isolated directories
  - PDF generation capability
  - Automated workflow (create profile → generate seed → synthesize → create PDF)
- **Successfully tested** with Darren's natal chart

**Mode 2: Life Arc Report Generator** - IN PROGRESS 🔄

**Stage 0: Life Arc Research & Design** - COMPLETE ✅
- Completed comprehensive research and design for life arc timeline system
- Created `/docs/life_arc_report_design.md` (105+ pages of detailed specifications)
- **Key Design Elements:**
  - 10-lot Hellenistic system (Fortune, Spirit, Eros, Necessity, Courage, Victory, Exaltation, Marriage, plus optional Children/Basis)
  - 6 timing techniques: Zodiacal Releasing, Saturn Returns, Jupiter Returns, Outer Planet Milestones, Progressed Lunation Cycle, Key Profection Years
  - 4-tier event prioritization system (Tier 1: Life-defining, Tier 2: Major milestones, Tier 3: Significant events, Tier 4: Notable periods)
  - Timeline span: Birth to age 100
  - Output format: Similar to natal horoscope (technical document 50-100+ pages, synthesis PDF 15-25 pages with graphics)
  - Visual timeline: Multi-layer approach showing life chapters, turning points, and technique overlays
- **7-Stage Implementation Plan:** (~5-6 weeks total)
  - Stage 1: Core calculation engine (profections, progressions, ZR, returns)
  - Stage 2: Event prioritization system
  - Stage 3: Life chapter detection
  - Stage 4: Technical document generation
  - Stage 5: Synthesis agent creation
  - Stage 6: Visual timeline graphics
  - Stage 7: Integration & testing
- **Purpose:** Answer "When do struggles end? When does success happen? When do relationships form?"
- **Status:** Research complete, ready to begin Stage 1 implementation

**Stage 1: Core Calculation Engine** - PENDING
- Build calculation modules for all 6 timing techniques
- Implement lot calculations (10-lot system)
- Create event detection algorithms
- Integrate with Swiss Ephemeris for astronomical data
- Awaiting approval to begin implementation

**Mode 3: Transit Report Generator** - PENDING
- Transit analysis with exact timing
- Will be implemented after Life Arc Report
- Design documents available: `/docs/transit_interpretation_design.md`, `/docs/transit_staged_implementation.md`

**📝 NOTE:** `/docs/session_goals.md` needs updating by workflow-planner-2 to reflect:
- Life Arc Report is now Mode 2 (before Transit Report)
- Transit Report is now Mode 3
- Life Arc Stage 0 (research & design) is complete
- Ready to begin Life Arc Stage 1 (core calculation engine)

### Speculative Features (Future)

- Claude Code API integration
- Birth data entry via chat interface
- Transit story timeline visualization
- Module refinement and enhancement
- Synastry (relationship astrology)
- Electional astrology (choosing optimal timing)

See `/docs/session_goals.md` for detailed feature descriptions and implementation roadmap.

---

## Reference Materials

All reference materials are located in `/Referendces/` folder:

### 1. Hellenistic Astrology: The Study of Fate and Fortune (Chris Brennan)
- **Status**: Foundation text
- **Focus**: Hellenistic techniques, whole-sign houses, sect, lots/parts, time-lord systems
- **File**: `Hellenistic Astrology The Study of Fate and Fortune (Chris Brennan).pdf`
- **Priority**: Primary source for traditional methods

### 2. Astrology and the Authentic Self: Integrating Traditional and Modern Astrology (Demetra George)
- **Status**: Integration methods
- **Focus**: Bridging traditional and modern approaches, psychological integration
- **File**: `Demetra George - Astrology and the Authentic Self_ Integrating Traditional and Modern Astrology.pdf`
- **Priority**: Secondary source for synthesis

### 3. Planets in Transit: Life Cycles for Living (Robert Hand)
- **Status**: Predictive techniques (OCR'd text)
- **Focus**: Transit interpretation, life cycles, planetary periods
- **File**: `Planets in transit  life cycles for living (Robert Hand) OCR.pdf`
- **Priority**: Primary source for transits
- **Note**: OCR errors require additional quality control

### 4. Predictive Astrology: The Eagle and the Lark (Bernadette Brady)
- **Status**: Timing systems
- **Focus**: Predictive timing, visual astrology, parans
- **File**: `Predictive Astrology The Eagle and the Lark (Bernadette Brady).pdf`
- **Priority**: Secondary source for predictive work

### 5. Delineation of Progressions (Sophia Mason)
- **Status**: Progression specifics
- **Focus**: Secondary progressions, progressed Moon, progressed angles
- **File**: `Delineation of Progressions (Sophia Mason).pdf`
- **Priority**: Specialized source for progressions

### 6. The Horoscope in Manifestation (Liz Greene)
- **Status**: Horoscope writing methodology
- **Focus**: Psychological/Jungian astrology, horoscope synthesis, writing best practices
- **File**: `Greene, Liz - The Horoscope in Manifestation.pdf`
- **Priority**: Secondary source for psychological depth and synthesis
- **Note**: Added in Stage -1 (223 chunks)

### RAG Database Statistics

- **Total chunks**: 2,472 (as of Stage -1 completion)
- **Total sources**: 6 reference books
- **Database location**: `/output/database/astrology_rag_database.jsonl`
- **Redundancy assessment**: All 6 sources provide unique value - see `/output/literature_redundancy_assessment.md`

---

## User Birth Data Context

**File**: `/Darren_Profile.txt`

Contains natal chart data for the project owner. This is provided as context only and should NOT be used for unsolicited chart analysis. Reference only when explicitly requested for testing, validation, or example purposes.

### Settings Block System

The birth data file now uses a **settings block system** for interpretation customization, replacing CLI input flags. This allows fine-grained control over interpretation depth and methods.

**Settings Block Format**:
```
[SETTINGS]
interpretation_depth: standard|deep|comprehensive
include_house_rulers: true|false
include_lots: basic|extended|full
include_angles_aspects: true|false (toggle if birth time uncertain)
include_nodes: true|false
include_lilith: true|false (default: true, but toggleable)
include_chiron: true|false (default: true, but toggleable)
include_receptions: true|false
include_psychological: basic|deep
modern_methods: conservative|moderate|extensive
```

**Traditional Foundation Protection**:
- All modern methods clearly labeled as supplementary
- Hierarchical interpretation: Traditional primary, modern secondary
- Modern additions never override traditional dignities or core methods
- Hellenistic/traditional foundation remains unchanged
- User can disable modern methods entirely via settings

**Topics Being Researched** (15 total):

**Traditional Methods** (fits current foundation):
1. House Rulers / Derivative Houses
2. Lots / Arabic Parts (extended system)
3. Angles as Chart Points (ASC/MC/DC/IC aspects)
4. Lunar Nodes (North/South Node)
5. Receptions (Mutual, Mixed)
6. Bonification / Maltreatment
7. Triplicities (detailed analysis)
8. Egyptian Bounds (detailed analysis)
9. Antiscia (reflection points)

**Modern Methods** (supplementary only):
10. Lilith (Black Moon) - toggleable, default ON
11. Chiron (Wounded Healer) - toggleable, default ON
12. Psychological/Jungian depth (Liz Greene methods)
13. Harmonic/Minor Aspects (quintile, septile)
14. Midpoints (Ebertin method)
15. Vertex (fated encounters)

**Implementation Phases**:
- Phase 1: Documentation update ✓ (this update)
- Phase 2: RAG agent debug/fix
- Phase 3: RAG database coverage scan (15 topics)
- Phase 4: Ultrathink workflow & architecture design
- Phase 5: Create enhancement deliverables (design doc, implementation plan)

---

## Technical Approach

### Astrological Systems Used

This project adheres to traditional/Hellenistic astrological systems with limited modern additions:

#### House System
- **Primary**: Whole-sign houses (WSH)
- Each house spans one complete zodiacal sign
- Rising sign becomes the entire 1st house
- No house cusp calculations required

#### Rulerships
- **Traditional rulerships only**:
  - Sun: Leo
  - Moon: Cancer
  - Mercury: Gemini, Virgo
  - Venus: Taurus, Libra
  - Mars: Aries, Scorpio
  - Jupiter: Sagittarius, Pisces
  - Saturn: Capricorn, Aquarius

#### Dignities and Debilities
- **Domicile**: Planet in its own sign (rulership)
- **Exaltation**: Planet in sign of exaltation
- **Detriment**: Planet opposite its domicile
- **Fall**: Planet opposite its exaltation
- **Triplicity**: Elemental dignity (day/night rulers)
- **Bounds/Terms**: Division of signs into planetary sections
- **Decans/Faces**: 10-degree divisions of signs

#### Sect (Day/Night Chart Analysis)
- **Diurnal charts**: Sun above horizon at birth
- **Nocturnal charts**: Sun below horizon at birth
- Sect light: Sun (day) or Moon (night)
- Benefics of sect: Jupiter (day), Venus (night)
- Malefics of sect: Saturn (day), Mars (night)

#### Aspects
**Classical aspects only**:
- Conjunction: 0° (orb: 8-10°)
- Sextile: 60° (orb: 3-6°)
- Square: 90° (orb: 7-8°)
- Trine: 120° (orb: 7-8°)
- Opposition: 180° (orb: 8-10°)

Modern aspects (quintile, septile, etc.) are excluded.

#### Planetary Set
**Primary (Traditional Seven)**:
- Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn

**Secondary (Modern, context only)**:
- Uranus, Neptune, Pluto
- Used for supplementary interpretation only
- Never primary rulers or dignity holders

#### Planetary Conditions
- **Combust**: Within 8.5° of Sun (weakened)
- **Under the beams**: Within 15° of Sun (obscured)
- **Cazimi**: Within 17' of Sun (empowered)
- **Retrograde**: Apparent backward motion
- **Stationary**: Turning retrograde or direct
- **Angular**: In houses 1, 4, 7, 10 (strong)
- **Succedent**: In houses 2, 5, 8, 11 (moderate)
- **Cadent**: In houses 3, 6, 9, 12 (weak)

---

## Swiss Ephemeris Integration

The project now includes live astronomical calculation capabilities via the Swiss Ephemeris library (pyswisseph v2.10.3.2), enabling precise planetary positions, house calculations, aspects, transits, and eclipse data.

### Overview

**Location**: Helper script at `/Users/darrenschaeffer/Library/Mobile Documents/com~apple~CloudDocs/Astrogy_Claude/scripts/ephemeris_helper.py`

**Installation**: pyswisseph installed in project virtual environment

**Ephemeris Data**: Built-in ephemeris files (can be extended with custom ephemeris data files)

### Capabilities

#### 1. Planetary Positions

Calculate precise astronomical positions for all traditional and modern planets:

**Planets Supported**:
- Traditional Seven (primary): Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn
- Modern Planets (secondary context): Uranus, Neptune, Pluto
- Special Points: North Node, South Node, Chiron

**Data Returned**:
- Longitude (0-360°)
- Latitude
- Distance from Earth
- Speed (daily motion)
- Zodiacal sign
- Degree within sign
- Formatted position (e.g., "17°57'22\" Libra")
- Retrograde status (True/False)

#### 2. House Calculations

Calculate house cusps for multiple house systems:

**Primary System**: Whole-sign houses ('W')

**Supported Systems**:
- Placidus ('P')
- Koch ('K')
- Equal ('E')
- Campanus ('C')
- Regiomontanus ('R')
- Porphyry ('O')
- And others

**Data Returned**:
- House cusps (1-12)
- Ascendant (rising degree)
- Midheaven (MC)
- ARMC (Right Ascension of MC)
- Vertex

#### 3. Aspect Calculations

Calculate aspects between planetary positions using traditional methods:

**Classical Aspects Only**:
- Conjunction (0°)
- Sextile (60°)
- Square (90°)
- Trine (120°)
- Opposition (180°)

**Aspect Analysis**:
- Exact orb calculation
- Applying vs. separating status
- Traditional orbs:
  - Conjunction/Opposition: 10°
  - Square/Trine: 7-8°
  - Sextile: 6-8°

**Data Returned**:
- Aspect type
- Exact orb (degrees)
- Applying or separating
- Whether aspect is within orb

#### 4. Transit Calculations

Calculate transiting planetary positions and their aspects to natal positions:

**Features**:
- Current positions of transiting planets
- Aspects between transits and natal positions
- Retrograde status of transiting planets
- Speed of transiting planets
- Exact orb calculations

**Use Cases**:
- Current transits to natal chart
- Historical transit reconstruction
- Future transit predictions
- Transit timing analysis

#### 5. Eclipse Calculations

Find lunar and solar eclipse dates within specified time ranges:

**Eclipse Types**:
- Lunar eclipses (total, partial, penumbral)
- Solar eclipses (total, annular, partial)

**Data Returned**:
- Eclipse date and time (UTC)
- Eclipse type
- Zodiacal position of eclipse
- Formatted position

### Usage for Agents

Import the helper functions and use them for astronomical calculations:

```python
from scripts.ephemeris_helper import (
    get_planetary_positions,
    calculate_houses,
    calculate_aspect,
    calculate_transit,
    get_eclipse_dates,
    datetime_to_julian,
    julian_to_datetime,
    degrees_to_sign,
    format_position,
    cleanup
)
from datetime import datetime

# Get current planetary positions
positions = get_planetary_positions(datetime.utcnow())

# Calculate houses for specific location (whole-sign system)
houses = calculate_houses(
    datetime.utcnow(),
    latitude=40.7128,
    longitude=-74.0060,
    house_system='W',
    utc=True
)

# Calculate aspect between two positions
aspect = calculate_aspect(long1=120.5, long2=240.3, orb=8.0)

# Calculate transit to natal position
transit = calculate_transit(
    natal_position=180.0,
    transit_date=datetime.utcnow(),
    planet='Saturn',
    utc=True
)

# Find upcoming eclipses
eclipses = get_eclipse_dates(
    datetime.utcnow(),
    num_eclipses=5,
    eclipse_type='lunar'  # or 'solar'
)

# Convert between datetime and Julian day
jd = datetime_to_julian(datetime.utcnow(), utc=True)
dt = julian_to_datetime(jd)

# Convert longitude to sign and degree
sign_data = degrees_to_sign(197.956)  # Returns: ('Libra', 17.956)

# Format position for display
formatted = format_position(197.956)  # Returns: "17°57'22\" Libra"

# Clean up when done (close ephemeris files)
cleanup()
```

### Key Functions Reference

#### `get_planetary_positions(dt, utc=True, include_modern=True)`

Get positions for all planets at a specific date/time.

**Parameters**:
- `dt`: datetime object
- `utc`: True if datetime is UTC, False if local (default: True)
- `include_modern`: Include Uranus, Neptune, Pluto (default: True)

**Returns**: Dictionary with planet names as keys and position data as values

#### `calculate_houses(dt, latitude, longitude, house_system='W', utc=True)`

Calculate house cusps for a specific time and location.

**Parameters**:
- `dt`: datetime object
- `latitude`: Geographic latitude (positive north, negative south)
- `longitude`: Geographic longitude (positive east, negative west)
- `house_system`: House system code (default: 'W' for whole-sign)
- `utc`: True if datetime is UTC (default: True)

**Returns**: Dictionary with house cusps, Ascendant, MC, ARMC, Vertex

#### `calculate_aspect(long1, long2, orb=8.0)`

Calculate aspect between two longitude positions.

**Parameters**:
- `long1`: First longitude (0-360°)
- `long2`: Second longitude (0-360°)
- `orb`: Maximum orb to consider (default: 8.0°)

**Returns**: Dictionary with aspect type, orb, applying/separating status, or None if no aspect

#### `calculate_transit(natal_position, transit_date, planet, utc=True)`

Calculate transit of a planet to a natal position.

**Parameters**:
- `natal_position`: Natal longitude (0-360°)
- `transit_date`: datetime for transit calculation
- `planet`: Planet name ('Sun', 'Moon', 'Mercury', etc.)
- `utc`: True if datetime is UTC (default: True)

**Returns**: Dictionary with transit position, aspect to natal, retrograde status

#### `get_eclipse_dates(start_date, num_eclipses=5, eclipse_type='lunar')`

Find eclipse dates starting from a given date.

**Parameters**:
- `start_date`: datetime to start searching
- `num_eclipses`: Number of eclipses to find (default: 5)
- `eclipse_type`: 'lunar' or 'solar' (default: 'lunar')

**Returns**: List of dictionaries with eclipse date, type, and position

#### `datetime_to_julian(dt, utc=True)`

Convert datetime to Julian day number.

**Parameters**:
- `dt`: datetime object
- `utc`: True if datetime is UTC (default: True)

**Returns**: Julian day number (float)

#### `julian_to_datetime(jd)`

Convert Julian day number to datetime.

**Parameters**:
- `jd`: Julian day number

**Returns**: datetime object (UTC)

#### `degrees_to_sign(longitude)`

Convert ecliptic longitude to zodiacal sign and degree.

**Parameters**:
- `longitude`: Ecliptic longitude (0-360°)

**Returns**: Tuple of (sign_name, degree_in_sign)

#### `format_position(longitude)`

Format longitude as human-readable position.

**Parameters**:
- `longitude`: Ecliptic longitude (0-360°)

**Returns**: Formatted string (e.g., "17°57'22\" Libra")

#### `cleanup()`

Close Swiss Ephemeris files and clean up resources. Call when finished with ephemeris calculations.

### Time Handling

**Default Time Zone**: UTC (recommended for astronomical calculations)

**UTC Parameter**: Most functions accept `utc=True/False` parameter
- `utc=True`: Input datetime is treated as UTC (default)
- `utc=False`: Input datetime is treated as local time

**Julian Day Conversions**: Use for precise astronomical calculations
- Swiss Ephemeris uses Julian day numbers internally
- Helper functions provided for conversions
- Julian day allows fractional days for precise time

**Date/Time Precision**: Calculations accurate to the second

### Output Format

#### Planetary Position Dictionary

```python
{
    'Sun': {
        'longitude': 197.956,      # Ecliptic longitude (0-360°)
        'latitude': 0.0,           # Ecliptic latitude
        'distance': 1.002,         # Distance from Earth (AU)
        'speed': 0.987,            # Daily motion (degrees/day)
        'sign': 'Libra',           # Zodiacal sign
        'degree_in_sign': 17.956,  # Degree within sign (0-30)
        'formatted': "17°57'22\" Libra",  # Human-readable format
        'retrograde': False        # Retrograde status
    },
    'Moon': { ... },
    'Mercury': { ... },
    # ... other planets
}
```

#### House Dictionary

```python
{
    'houses': [
        {'cusp': 1, 'longitude': 135.456},
        {'cusp': 2, 'longitude': 165.456},
        # ... houses 3-12
    ],
    'ascendant': 135.456,    # Rising degree
    'mc': 45.789,            # Midheaven
    'armc': 12.345,          # Right Ascension of MC
    'vertex': 234.567        # Vertex point
}
```

#### Aspect Dictionary

```python
{
    'aspect': 'square',       # Aspect type
    'orb': 2.35,             # Exact orb in degrees
    'applying': True,        # True if applying, False if separating
    'in_orb': True          # True if within specified orb
}
```

#### Transit Dictionary

```python
{
    'planet': 'Saturn',
    'transit_position': 285.678,
    'natal_position': 180.0,
    'aspect': {
        'aspect': 'square',
        'orb': 1.5,
        'applying': False,
        'in_orb': True
    },
    'retrograde': True,
    'speed': -0.05
}
```

#### Eclipse Data

```python
[
    {
        'date': datetime(2025, 3, 14, 6, 30, 15),  # UTC
        'type': 'Total Lunar Eclipse',
        'position': 353.789,
        'formatted_position': "23°47'20\" Pisces"
    },
    # ... more eclipses
]
```

### Integration with RAG Database

Agents can now combine Swiss Ephemeris calculations with RAG database queries:

#### Workflow Example

1. **Calculate Current Positions**: Use `get_planetary_positions()` to get current planetary positions
2. **Query RAG Database**: Search database for interpretations of those positions
3. **Calculate Aspects**: Use `calculate_aspect()` to find aspects between planets
4. **Query Aspect Interpretations**: Search database for aspect delineations
5. **Calculate Transits**: Use `calculate_transit()` for transit analysis
6. **Query Transit Interpretations**: Search database for transit meanings
7. **Synthesize**: Combine ephemeris data with traditional delineations

#### Example Integration

```python
from scripts.ephemeris_helper import get_planetary_positions, calculate_aspect
from datetime import datetime

# Get current positions
positions = get_planetary_positions(datetime.utcnow())

# Extract Mars and Saturn positions
mars_long = positions['Mars']['longitude']
saturn_long = positions['Saturn']['longitude']

# Calculate aspect
aspect = calculate_aspect(mars_long, saturn_long)

if aspect and aspect['aspect'] == 'square':
    # Query RAG database for "Mars square Saturn" interpretations
    # Combine with current positions, signs, retrograde status
    # Generate interpretation using traditional delineations
    pass
```

### Traditional Astrology Compliance

The Swiss Ephemeris integration maintains alignment with traditional astrological principles:

**Whole-Sign Houses**: Default house system ('W')
- Each house spans exactly 30° (one sign)
- Rising sign = entire 1st house
- Consistent with Hellenistic practice

**Classical Aspects Only**:
- Conjunction, sextile, square, trine, opposition
- No modern aspects (quintile, septile, etc.)
- Traditional orbs enforced

**Retrograde Detection**:
- Accurate retrograde status for all planets
- Essential for traditional interpretation
- Speed values indicate daily motion

**Traditional Orbs**:
- Conjunction/Opposition: 10° maximum
- Square/Trine: 7-8° recommended
- Sextile: 6-8° recommended
- Configurable via function parameters

**Sect Awareness**:
- Day/night chart determination via Sun position
- Ascendant calculation for sect light identification
- Foundation for benefic/malefic sect analysis (in development)

**Traditional Seven Planets**:
- Sun through Saturn as primary
- Modern planets (Uranus, Neptune, Pluto) as secondary
- Consistent with project's traditional focus

### Testing and Verification

The ephemeris helper script has been tested and verified for accuracy.

**Test the Script**:
```bash
# Navigate to project directory
cd "/Users/darrenschaeffer/Library/Mobile Documents/com~apple~CloudDocs/Astrogy_Claude"

# Activate virtual environment
source venv/bin/activate

# Run test script
python scripts/ephemeris_helper.py
```

**Expected Output**:
- Current planetary positions
- Sample house calculations
- Sample aspect calculations
- Sample transit data
- Upcoming eclipse dates

**Verification**:
- Compare output with astronomical ephemeris tables
- Cross-check with astrology software (Astro.com, Solar Fire, etc.)
- Verify retrograde stations against published data
- Confirm eclipse dates with NASA eclipse data

### Error Handling

The helper script includes error handling for common issues:

**Missing Ephemeris Files**: Built-in ephemeris data used automatically

**Invalid Date Ranges**: Ephemeris data typically covers 1800-2400 CE

**Invalid Coordinates**: Latitude must be -90° to +90°, longitude -180° to +180°

**Invalid Planet Names**: Validation against supported planet list

**Time Zone Issues**: Always prefer UTC for consistency

### Performance Considerations

**Initialization**: Swiss Ephemeris files loaded once per session

**Calculation Speed**: Astronomical calculations are fast (<1ms per planet)

**Resource Cleanup**: Call `cleanup()` when finished to close ephemeris files

**Batch Calculations**: For multiple dates, reuse function calls efficiently

### Future Enhancements

**Planned Features**:
- Progressed positions (secondary progressions, solar arc)
- Profection calculations (annual time-lord system)
- Zodiacal releasing calculations
- Planetary returns (solar, lunar, Jupiter, Saturn)
- Paran calculations (visual astrology)
- Fixed star positions and conjunctions
- Lot/Part calculations (Lot of Fortune, Lot of Spirit, etc.)

**Integration Roadmap**:
- Direct integration with RAG database queries
- Automated chart interpretation pipelines
- Transit tracking and notifications
- Historical event correlation
- Predictive technique automation

---

## Static Astrology Reference Data

The project includes a comprehensive Python module containing all static astrological reference data. This serves as a single source of truth for traditional and Hellenistic astrology constants, dignity tables, and lookup data.

### Overview

**Location**: `/Users/darrenschaeffer/Library/Mobile Documents/com~apple~CloudDocs/Astrogy_Claude/scripts/astrology_reference.py`

**Format**: Python module (directly importable)

**Purpose**: Provide fast, programmatic access to static astrological data without needing to query the RAG database or parse documentation.

### Contents

#### 1. Essential Dignity Tables (Complete)

**Domicile/Rulership**: All traditional planetary rulerships
- Sun: Leo
- Moon: Cancer
- Mercury: Gemini, Virgo
- Venus: Taurus, Libra
- Mars: Aries, Scorpio
- Jupiter: Sagittarius, Pisces
- Saturn: Capricorn, Aquarius

**Exaltation**: Sign and exact degree for each planet
- Includes exaltation degree (e.g., Sun exalts at 19° Aries)

**Detriment**: Opposite of domicile

**Fall**: Opposite of exaltation

**Triplicity Rulers**: Day, night, and participating rulers for each element
- Fire, Earth, Air, Water
- Includes sect-based variations

**Egyptian Bounds/Terms**: Complete degree ranges for all 12 signs
- 5 planetary divisions per sign
- Exact start/end degrees

**Decans/Faces**: 10-degree divisions for all signs
- 3 decans per sign (0-10°, 10-20°, 20-30°)
- Planetary rulers for each decan

#### 2. Planetary Data (All 10 Planets)

Complete profiles for each planet including:
- Domicile signs (what it rules)
- Exaltation sign and degree
- Detriment signs
- Fall sign and degree
- Natural significations and keywords
- Sect status (diurnal/nocturnal, benefic/malefic)
- Planetary joys (house and sign)
- Qualities (hot/cold, dry/moist)
- People, body parts, and qualities signified
- Modern planet flag (True for Uranus/Neptune/Pluto)

#### 3. Sign Data (All 12 Signs)

Complete profiles for each sign including:
- Element (Fire, Earth, Air, Water)
- Modality (Cardinal, Fixed, Mutable)
- Polarity (Masculine, Feminine)
- Planetary ruler
- Exaltation ruler
- Detriment and fall rulers
- Season association
- Symbol and glyph
- Qualities and characteristics
- Keywords

#### 4. House Significations (Houses 1-12)

Detailed data for each house:
- House name
- Natural ruler (planet)
- Natural sign
- Angularity status (angular/succedent/cadent)
- Planetary joys
- Traditional topics and themes
- Significations (physical, psychological, life areas)
- Keywords

#### 5. Aspect Data (Classical Aspects Only)

For each of the 5 classical aspects:
- Angle (0°, 60°, 90°, 120°, 180°)
- Traditional orbs
- Nature (harmonious/challenging/neutral)
- Symbol
- Keywords
- Strength indicators
- Planet-specific orb variations (luminaries get larger orbs)

#### 6. Sect Assignments

- Diurnal planets: Sun, Jupiter, Saturn
- Nocturnal planets: Moon, Venus, Mars
- Neutral planets: Mercury (adapts to chart)
- Greater/lesser benefic designations
- Greater/lesser malefic designations

#### 7. Planetary Conditions (Exact Values)

- **Combust**: Within 8.5° of Sun (weakened)
- **Under the beams**: Within 15° of Sun (obscured)
- **Cazimi**: Within 17' (0.283°) of Sun (empowered)
- **Retrograde**: Speed < 0
- **Stationary**: Speed ≈ 0
- **Angularity**: Houses 1/4/7/10 (angular), 2/5/8/11 (succedent), 3/6/9/12 (cadent)

#### 8. Lot/Part Formulas

Calculation formulas for traditional lots:
- Lot of Fortune (day/night formulas)
- Lot of Spirit (day/night formulas)
- Lot of Eros
- Lot of Necessity
- Lot of Courage
- Lot of Victory

Each with significations and interpretations.

#### 9. Helper Functions

Convenient lookup functions:
- `check_dignity(planet, sign)` - Returns dignity type or None
- `get_planet_dignities(planet)` - All dignities for planet
- `get_triplicity_ruler(element, chart_type)` - Get triplicity ruler
- `get_bounds_ruler(sign, degree)` - Bounds ruler for degree
- `get_decan_ruler(sign, degree)` - Decan ruler for degree
- `get_sign_element(sign)` - Element for sign
- `get_sign_modality(sign)` - Modality for sign
- `get_sign_ruler(sign)` - Traditional ruler
- `get_house_topics(house_num)` - House significations
- `get_aspect_orb(aspect_type, planet1, planet2)` - Traditional orb
- `is_benefic(planet)` - Check if benefic
- `is_malefic(planet)` - Check if malefic
- `get_sect_status(planet, chart_type)` - Sect status
- `check_combust(planet_long, sun_long)` - Combustion check
- `check_cazimi(planet_long, sun_long)` - Cazimi check
- `check_under_beams(planet_long, sun_long)` - Under beams check
- `get_house_angularity(house_num)` - Angular/succedent/cadent

#### 10. Constants and Mappings

- Planet symbols → text (☉→Sun, ♂→Mars, etc.)
- Sign symbols → text (♈→Aries, ♌→Leo, etc.)
- Aspect symbols → text (☌→conjunction, △→trine, etc.)
- Element groupings (Fire, Earth, Air, Water signs)
- Modality groupings (Cardinal, Fixed, Mutable signs)
- Polarity groupings (Masculine, Feminine signs)
- House system codes (W, P, K, E, etc.)

### Usage for Agents

Import reference data and helper functions directly:

```python
from scripts.astrology_reference import (
    PLANETS, SIGNS, HOUSES, ASPECTS,
    check_dignity, get_triplicity_ruler, get_bounds_ruler
)

# Check dignity
dignity = check_dignity('Mars', 'Aries')  # Returns: 'domicile'

# Get planet data
mars_data = PLANETS['Mars']
print(mars_data['keywords'])  # ['action', 'conflict', 'desire', 'courage', 'aggression', 'severance']

# Get sign ruler
ruler = get_sign_ruler('Scorpio')  # Returns: 'Mars'

# Get house topics
topics = get_house_topics(1)  # Returns: ['body', 'appearance', 'vitality', 'character', ...]

# Check triplicity
fire_ruler = get_triplicity_ruler('Fire', 'diurnal')  # Returns: 'Sun'

# Get bounds ruler
bounds = get_bounds_ruler('Aries', 10)  # Returns: 'Venus' (Aries 6-14° is Venus bounds)

# Get decan ruler
decan = get_decan_ruler('Leo', 15)  # Returns: 'Jupiter' (Leo 10-20° is Jupiter decan)

# Check combustion
is_combust = check_combust(planet_long=120.5, sun_long=125.0)  # Returns: True (within 8.5°)

# Get sect status
status = get_sect_status('Jupiter', 'diurnal')  # Returns: 'of sect'
```

### Integration with Other Systems

The static reference data complements:

1. **RAG Database**: Use reference for lookups, RAG for interpretations
   - Reference: "What sign does Mars rule?" → Quick lookup
   - RAG: "What does Mars in Aries mean?" → Semantic search

2. **Swiss Ephemeris**: Use ephemeris for calculations, reference for context
   - Ephemeris: Calculate current Mars position → 15° Scorpio
   - Reference: Check dignity → Mars in domicile
   - RAG: Query interpretation → "Mars in Scorpio in domicile..."

3. **Workflow Example**:
   ```python
   from scripts.ephemeris_helper import get_planetary_positions
   from scripts.astrology_reference import check_dignity, PLANETS
   from datetime import datetime

   # Calculate positions
   positions = get_planetary_positions(datetime.utcnow())
   mars_sign = positions['Mars']['sign']
   mars_long = positions['Mars']['longitude']

   # Check dignity
   dignity = check_dignity('Mars', mars_sign)

   # Get interpretation context
   mars_keywords = PLANETS['Mars']['keywords']

   # Query RAG database with context
   query = f"Mars in {mars_sign}"
   if dignity:
       query += f" in {dignity}"
   # ... query RAG database for interpretation
   ```

### Benefits

1. **Fast Lookups**: No semantic search needed for factual data
2. **Single Source of Truth**: All static data in one authoritative location
3. **Type Safety**: Python dictionaries with consistent structure
4. **Direct Access**: Import and use immediately
5. **No Parsing**: Pre-structured data, no text processing
6. **Extensible**: Easy to add new data or functions
7. **Exportable**: Can convert to JSON for non-Python uses

### Data Accuracy

All dignity tables, planetary data, and significations are based on traditional and Hellenistic sources:
- Egyptian Bounds: Traditional tables
- Decans: Chaldean order
- Triplicity: Dorothean system
- Sect assignments: Hellenistic practice
- Modern planets: Clearly marked, no traditional dignities

### Testing

Test the reference module:
```bash
cd "/Users/darrenschaeffer/Library/Mobile Documents/com~apple~CloudDocs/Astrogy_Claude"
source venv/bin/activate
python scripts/astrology_reference.py
```

Expected output includes example lookups demonstrating all helper functions.

---

## Extraction Strategy

### Processing Pipeline

#### 1. PDF Extraction
- Extract text from reference PDFs
- Preserve page numbers for citation
- Handle OCR corrections (especially Hand text)
- Maintain chapter/section structure

#### 2. Content Identification
Extract the following content types:

**Delineations**:
- Planet in sign interpretations
- Planet in house placements
- Aspect interpretations (planet-to-planet)
- House cusp ruler placements

**Techniques**:
- Profections (annual time-lord system)
- Progressions (secondary, solar arc)
- Directions (primary, zodiacal releasing)
- Returns (solar, lunar, planetary)
- Transits (outer planet cycles)

**Dignities/Debilities**:
- Essential dignity tables
- Accidental dignity conditions
- Sect considerations
- Reception and mutual reception

**Keywords & Principles**:
- Core planetary significations
- Sign characteristics
- House topics and themes
- Aspect qualities

**Examples & Case Studies**:
- Chart examples from texts
- Historical cases
- Technique demonstrations

#### 3. Semantic Chunking
- **Chunk size**: 200-800 tokens per chunk
- **Overlap**: 50 tokens between chunks
- **Boundaries**: Preserve complete concepts
- **Context**: Include surrounding interpretive context

#### 4. Metadata Tagging
Each chunk receives structured metadata:

```json
{
  "source": "Book title",
  "author": "Author name",
  "page": 123,
  "chapter": "Chapter title",
  "tradition": "Hellenistic | Modern | Traditional",
  "content_type": "delineation | technique | dignity | keyword | example | principle",
  "entities": {
    "planets": ["Sun", "Mars"],
    "signs": ["Aries", "Leo"],
    "houses": [1, 10],
    "aspects": ["square", "trine"],
    "dignities": ["domicile", "exaltation"]
  },
  "keywords": ["sect", "angular", "malefic"],
  "difficulty": "beginner | intermediate | advanced",
  "technique": "profections | progressions | transits | etc.",
  "timestamp": "ISO-8601 timestamp"
}
```

---

## Normalization & Ontology

### Controlled Vocabulary

To ensure consistency and accurate retrieval, all astrological terms are normalized to a controlled vocabulary.

#### Planets
**Standard forms**:
- Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn
- Uranus, Neptune, Pluto (secondary only)

**Symbols to convert**:
- ☉ → Sun
- ☽ → Moon
- ☿ → Mercury
- ♀ → Venus
- ♂ → Mars
- ♃ → Jupiter
- ♄ → Saturn
- ♅ → Uranus
- ♆ → Neptune
- ♇ → Pluto

#### Signs
**Standard forms**:
- Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces

**Symbols to convert**:
- ♈ → Aries
- ♉ → Taurus
- ♊ → Gemini
- ♋ → Cancer
- ♌ → Leo
- ♍ → Virgo
- ♎ → Libra
- ♏ → Scorpio
- ♐ → Sagittarius
- ♑ → Capricorn
- ♒ → Aquarius
- ♓ → Pisces

#### Houses
**Standard forms**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

**System specification**: "whole-sign" (WSH)

#### Aspects
**Standard forms**:
- conjunction (0°)
- sextile (60°)
- square (90°)
- trine (120°)
- opposition (180°)

**Symbols to convert**:
- ☌ → conjunction
- ⚹ → sextile
- □ → square
- △ → trine
- ☍ → opposition

#### Dignities
**Standard forms**:
- domicile (rulership)
- exaltation
- detriment
- fall
- triplicity
- bounds (terms)
- decans (faces)

#### Sect
**Standard forms**:
- diurnal (day chart)
- nocturnal (night chart)
- sect light
- benefic of sect
- malefic of sect
- contrary to sect

#### Planetary Conditions
**Standard forms**:
- combust
- under the beams
- cazimi
- retrograde
- stationary
- direct
- angular
- succedent
- cadent

### Synonym Mapping

Map variant terminology to standard forms:

#### House System Synonyms
- "whole sign" → "whole-sign"
- "WSH" → "whole-sign"
- "houses" → "houses" (context: whole-sign)
- "places" → "houses"

#### Dignity Synonyms
- "bounds" ↔ "terms" (use "bounds" as standard)
- "decans" ↔ "faces" (use "decans" as standard)
- "rulership" → "domicile"
- "ruler" → context-dependent (domicile ruler, exaltation ruler, etc.)

#### Aspect Synonyms
- "trine aspect" → "trine"
- "in trine to" → "trine"
- "applying square" → "square" + aspect_phase: "applying"
- "separating opposition" → "opposition" + aspect_phase: "separating"

#### Sect Synonyms
- "day chart" → "diurnal"
- "night chart" → "nocturnal"
- "benefic in sect" → "benefic of sect"
- "malefic out of sect" → "malefic contrary to sect"

#### General Synonyms
- "planet" ↔ "luminary" (for Sun/Moon)
- "natal chart" ↔ "birth chart" ↔ "nativity" ↔ "radix"
- "lot" ↔ "part" (as in "Lot of Fortune" = "Part of Fortune")

---

## Core Building Blocks

The database extracts and structures the following fundamental astrological components:

### 1. Planet Profiles

Each planet requires comprehensive documentation:

**Structure**:
```json
{
  "planet": "Mars",
  "nature": "Malefic, hot and dry, choleric",
  "domicile": ["Aries", "Scorpio"],
  "exaltation": "Capricorn",
  "detriment": ["Libra", "Taurus"],
  "fall": "Cancer",
  "sect_status": {
    "diurnal": "contrary to sect (malefic)",
    "nocturnal": "of sect (malefic of sect)"
  },
  "joys": {
    "house": 6,
    "sign": "Scorpio"
  },
  "keywords": ["action", "conflict", "courage", "desire", "severance", "injury"],
  "significations": {
    "people": ["soldiers", "athletes", "surgeons", "competitors"],
    "activities": ["warfare", "competition", "cutting", "surgery"],
    "qualities": ["assertiveness", "aggression", "initiative", "rashness"]
  },
  "sources": [
    {"book": "Hellenistic Astrology", "pages": [145-167]},
    {"book": "Planets in Transit", "pages": [89-123]}
  ]
}
```

### 2. Sign Profiles

Each zodiacal sign requires:

**Structure**:
```json
{
  "sign": "Aries",
  "element": "Fire",
  "modality": "Cardinal",
  "ruler": "Mars",
  "exaltation_ruler": "Sun",
  "triplicity_rulers": {
    "day": "Sun",
    "night": "Jupiter",
    "participating": "Saturn"
  },
  "qualities": ["initiating", "impulsive", "courageous", "headstrong"],
  "symbolism": "The Ram",
  "gender": "Masculine",
  "characteristics": "Cardinal fire sign; initiating, assertive, pioneering energy",
  "sources": [
    {"book": "Hellenistic Astrology", "pages": [201-215]}
  ]
}
```

### 3. House Meanings

Each house (1-12) requires:

**Structure**:
```json
{
  "house": 1,
  "name": "House of Self",
  "topics": ["body", "appearance", "vitality", "character", "life direction"],
  "natural_ruler": "Mars",
  "natural_sign": "Aries",
  "angularity": "Angular",
  "joys": "Mercury (classical)",
  "significations": {
    "physical": ["body", "health", "appearance", "vitality"],
    "psychological": ["identity", "character", "temperament"],
    "life_areas": ["self-presentation", "life path", "approach to life"]
  },
  "sources": [
    {"book": "Hellenistic Astrology", "pages": [267-289]}
  ]
}
```

### 4. Aspect Interpretations

Planet-to-planet aspect delineations:

**Structure**:
```json
{
  "aspect": "square",
  "planet1": "Mars",
  "planet2": "Saturn",
  "nature": "Malefic square malefic - challenging, restrictive, frustrating",
  "interpretation": {
    "natal": "Frustration, delayed action, controlled aggression, disciplined force",
    "transit": "Obstacles, setbacks, forced patience, constructive frustration",
    "progression": "Period of testing will and persistence"
  },
  "keywords": ["frustration", "delay", "discipline", "patience", "obstruction"],
  "orb": 7,
  "strength_factors": ["applying stronger than separating", "consider sect"],
  "sources": [
    {"book": "Planets in Transit", "pages": [234-239]}
  ]
}
```

### 5. Dignity/Debility Tables

Complete essential dignity tables:

**Structure**:
```json
{
  "sign": "Aries",
  "ruler": "Mars",
  "exaltation": {"planet": "Sun", "degree": 19},
  "triplicity": {
    "day_ruler": "Sun",
    "night_ruler": "Jupiter",
    "participating_ruler": "Saturn"
  },
  "bounds": [
    {"planet": "Jupiter", "degrees": "0-6"},
    {"planet": "Venus", "degrees": "6-14"},
    {"planet": "Mercury", "degrees": "14-21"},
    {"planet": "Mars", "degrees": "21-26"},
    {"planet": "Saturn", "degrees": "26-30"}
  ],
  "decans": [
    {"planet": "Mars", "degrees": "0-10"},
    {"planet": "Sun", "degrees": "10-20"},
    {"planet": "Venus", "degrees": "20-30"}
  ]
}
```

### 6. Timing Techniques

Extract formulas and methods for:

**Profections**:
- Annual profection calculation (house activation)
- Lord of the year identification
- Profected Moon/angles

**Progressions**:
- Secondary progression formulas (1 day = 1 year)
- Solar arc directions
- Progressed Moon phases and returns
- Progressed angles and house cusps

**Directions**:
- Primary directions
- Zodiacal releasing
- Time-lord periods and sub-periods

**Returns**:
- Solar return calculation and interpretation
- Lunar return cycles
- Planetary returns (Jupiter, Saturn)

**Transits**:
- Outer planet cycles
- Transit-to-natal aspects
- Transit timing and orbs

**Structure**:
```json
{
  "technique": "Annual Profections",
  "type": "time-lord",
  "tradition": "Hellenistic",
  "formula": "Add age to Ascendant in whole-sign houses",
  "calculation": "Age modulo 12 = profected house from Ascendant",
  "interpretation": "Activated house topics, lord of year becomes primary significator",
  "example": {
    "age": 35,
    "ascendant_sign": "Cancer",
    "profected_house": 12,
    "profected_sign": "Gemini",
    "lord_of_year": "Mercury"
  },
  "sources": [
    {"book": "Hellenistic Astrology", "pages": [456-489]}
  ]
}
```

### 7. Lots/Parts

Formulas and interpretations:

**Structure**:
```json
{
  "lot": "Lot of Fortune",
  "formula": {
    "day_chart": "Ascendant + Moon - Sun",
    "night_chart": "Ascendant + Sun - Moon"
  },
  "significations": ["body", "health", "livelihood", "material circumstances"],
  "interpretation": "Primary lot for physical well-being and material fortune",
  "by_house": {
    "1": "Strong vitality, good fortune with body and health",
    "2": "Fortune through resources, financial well-being",
    "10": "Fortune through career and public standing"
  },
  "sources": [
    {"book": "Hellenistic Astrology", "pages": [289-312]}
  ]
}
```

---

## Database Structure

### Output Format

**Primary**: JSON/JSONL with vector embeddings

**Vector Store**: OpenAI API (credentials in `.env` file)

**Schema**:
```json
{
  "id": "unique-chunk-id",
  "text": "The actual content chunk",
  "embedding": [0.123, -0.456, ...],
  "metadata": {
    "source": "Book title",
    "author": "Author name",
    "page": 123,
    "chapter": "Chapter title",
    "tradition": "Hellenistic",
    "content_type": "delineation",
    "entities": {
      "planets": ["Mars", "Saturn"],
      "signs": ["Aries"],
      "houses": [1, 10],
      "aspects": ["square"],
      "dignities": ["domicile", "detriment"]
    },
    "keywords": ["malefic", "sect", "frustration"],
    "difficulty": "intermediate",
    "technique": null,
    "timestamp": "2025-10-03T14:00:00Z"
  }
}
```

### Indexing Strategy

The database is indexed by multiple facets for efficient retrieval:

#### Entity Indexes
- **Planet index**: All content mentioning specific planets
- **Sign index**: All content mentioning specific signs
- **House index**: All content mentioning specific houses
- **Aspect index**: All content about specific aspects
- **Dignity index**: Essential and accidental dignities

#### Content Type Index
- Delineations
- Techniques
- Dignities
- Keywords
- Examples
- Principles

#### Source/Author Index
- By book title
- By author
- By page range
- By tradition (Hellenistic, Traditional, Modern)

#### Technique Index
- Profections
- Progressions
- Directions
- Returns
- Transits
- Zodiacal releasing

### Query Patterns

The database supports the following query types:

#### 1. Direct Delineation Queries
- "Mars in Aries in the 1st house"
- "Moon square Saturn"
- "Venus in detriment in Scorpio"

#### 2. Technique Queries
- "How to calculate annual profections"
- "Progressed Moon return interpretation"
- "Saturn return timing"

#### 3. Dignity Queries
- "Saturn triplicity rulers"
- "Bounds of Mars in Taurus"
- "Planets in fall"

#### 4. Synthesis Queries
- "Malefic in angular house"
- "Benefic of sect in domicile"
- "Combust planet interpretation"

#### 5. Example/Case Study Queries
- "Historical examples of Mars-Saturn square"
- "Case studies of profections"

### Semantic Search

Uses vector similarity for context-aware retrieval:
- Embedding model: OpenAI text-embedding-3-large (or similar)
- Similarity metric: Cosine similarity
- Top-K retrieval: Typically 5-10 most relevant chunks
- Re-ranking: By source authority, tradition match, content type

---

## Quality Control

### OCR Error Detection

**Issue**: Robert Hand's "Planets in Transit" is OCR'd and may contain errors.

**Detection methods**:
- Dictionary validation for common words
- Known astrological term validation
- Pattern matching for typical OCR errors:
  - "rn" → "m"
  - "l" → "1" or "I"
  - "0" → "O"
  - Broken words
  - Missing spaces

**Correction strategy**:
- Manual review of flagged passages
- Context-based correction suggestions
- Cross-reference with other sources for validation

### Cross-Reference Validation

**Process**:
1. Extract same topic from multiple sources
2. Compare interpretations
3. Flag significant discrepancies
4. Note tradition differences (Hellenistic vs. Modern)
5. Preserve both interpretations with clear attribution

**Example**:
```json
{
  "topic": "Mars in Cancer",
  "sources": [
    {
      "source": "Hellenistic Astrology",
      "interpretation": "Mars in fall, weakened, difficulty taking action",
      "tradition": "Hellenistic"
    },
    {
      "source": "Modern Astrology Text",
      "interpretation": "Protective action, emotional assertiveness",
      "tradition": "Modern"
    }
  ],
  "discrepancy": "Traditional views Mars as debilitated; modern views as emotionally expressive",
  "resolution": "Both valid within their traditions; prefer traditional for this project"
}
```

### Contradiction Flagging

**Types of contradictions**:
1. **Technical**: Different dignity assignments, aspect orbs
2. **Interpretive**: Conflicting delineations
3. **Traditional**: Hellenistic vs. Medieval vs. Modern differences
4. **Calculation**: Formula variations

**Flagging system**:
```json
{
  "contradiction_id": "unique-id",
  "type": "interpretive",
  "topic": "Saturn in 5th house",
  "conflicting_sources": [
    {"source": "Source A", "view": "Delays children", "tradition": "Traditional"},
    {"source": "Source B", "view": "Responsible parenting", "tradition": "Modern"}
  ],
  "resolution": "Traditional interpretation takes precedence for this project",
  "notes": "Modern psychological view noted as secondary"
}
```

### Tradition Markers

Every extracted piece of content is marked with its astrological tradition:

**Tradition categories**:
- **Hellenistic**: Greco-Roman astrology (1st century BCE - 7th century CE)
- **Medieval**: Arabic and European medieval astrology (8th - 17th century)
- **Traditional**: Pre-modern astrology using traditional techniques
- **Modern**: Post-17th century astrology (especially psychological)
- **Contemporary**: Current traditional revival (Hellenistic focus)

**Marker application**:
```json
{
  "text": "Mars in Cancer is in fall...",
  "tradition": "Hellenistic",
  "tradition_markers": ["dignity", "fall", "essential dignity"],
  "modern_applicable": false
}
```

---

## Edge Cases

### Modern Planets (Uranus, Neptune, Pluto)

**Handling strategy**:
- Extract interpretations as **secondary content only**
- Never assign as primary rulers
- Never include in essential dignity schemes
- Mark all content with `modern_planet: true` flag
- Use for supplementary interpretation only

**Example**:
```json
{
  "planet": "Uranus",
  "modern_planet": true,
  "secondary_ruler": "Aquarius (modern only)",
  "traditional_ruler": "Saturn (primary)",
  "usage": "Supplementary interpretation only",
  "note": "Not used for essential dignities or primary chart analysis"
}
```

### Multi-Source Synthesis

When multiple sources address the same topic:

**Strategy**:
1. Extract all interpretations separately with full attribution
2. Create synthesis entries that note commonalities
3. Preserve source-specific nuances
4. Note tradition differences
5. Flag contradictions

**Example structure**:
```json
{
  "synthesis_id": "mars-square-saturn-001",
  "topic": "Mars square Saturn",
  "common_themes": ["frustration", "delayed action", "discipline"],
  "source_variations": [
    {
      "source": "Hellenistic Astrology",
      "emphasis": "Malefic-malefic conflict, sect considerations"
    },
    {
      "source": "Planets in Transit",
      "emphasis": "Constructive frustration, building endurance"
    }
  ],
  "recommended_interpretation": "Combines traditional dignity assessment with modern psychological insight"
}
```

### Example/Case Study Preservation

Chart examples from source texts are valuable and should be preserved:

**Extraction requirements**:
- Full chart data (date, time, place if available)
- Interpretation context from source
- Technique being demonstrated
- Historical or celebrity context
- Source attribution

**Structure**:
```json
{
  "example_id": "unique-id",
  "source": "Hellenistic Astrology",
  "page": 456,
  "chart_data": {
    "date": "1969-07-20",
    "time": "20:17",
    "place": "Sea of Tranquility, Moon",
    "context": "Apollo 11 Moon landing"
  },
  "technique_demonstrated": "Annual profections",
  "interpretation": "Example shows profected Ascendant activating 9th house of travel...",
  "teaching_point": "Demonstrates profection timing for major event"
}
```

### Orb Variations

Different sources use different orbs for aspects:

**Strategy**:
- Extract orb specifications from each source
- Note source-specific orb ranges
- Provide default/recommended orbs
- Allow flexible orb queries

**Structure**:
```json
{
  "aspect": "trine",
  "orb_ranges": [
    {"source": "Hellenistic Astrology", "orb": 7, "context": "whole sign aspects"},
    {"source": "Modern source", "orb": 8, "context": "degree-based"},
    {"source": "Transit work", "orb": 5, "context": "applying aspects only"}
  ],
  "recommended_orb": 7,
  "notes": "Whole-sign aspects may not use orbs; degree-based work typically 7-8°"
}
```

---

## Deliverables

### 1. Structured RAG Database
**Format**: JSON/JSONL with vector embeddings
**Location**: TBD (specify output directory)
**Contents**:
- Chunked text content
- Vector embeddings
- Complete metadata
- Entity indexes
- Source attribution

### 2. Controlled Vocabulary/Ontology File
**Format**: JSON
**Contents**:
- Complete list of normalized terms
- Entity categories (planets, signs, houses, aspects, dignities)
- Valid values for each category
- Enumerated content types and traditions

**Example**:
```json
{
  "planets": {
    "traditional": ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn"],
    "modern": ["Uranus", "Neptune", "Pluto"]
  },
  "signs": ["Aries", "Taurus", ...],
  "houses": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
  "aspects": ["conjunction", "sextile", "square", "trine", "opposition"],
  "dignities": ["domicile", "exaltation", "detriment", "fall", "triplicity", "bounds", "decans"]
}
```

### 3. Synonym Mapping Reference
**Format**: JSON
**Contents**:
- All synonym variations mapped to standard terms
- Symbol-to-text conversions
- Abbreviation expansions
- Common variant spellings

**Example**:
```json
{
  "symbols": {
    "☉": "Sun",
    "☽": "Moon",
    "☿": "Mercury"
  },
  "terms": {
    "whole sign": "whole-sign",
    "WSH": "whole-sign",
    "bounds": "bounds",
    "terms": "bounds"
  },
  "aspects": {
    "△": "trine",
    "in trine to": "trine"
  }
}
```

### 4. Source Attribution Index
**Format**: JSON
**Contents**:
- Complete bibliography
- Page range coverage by topic
- Author expertise areas
- Tradition classification
- Quality/authority ratings

**Example**:
```json
{
  "sources": [
    {
      "title": "Hellenistic Astrology: The Study of Fate and Fortune",
      "author": "Chris Brennan",
      "tradition": "Hellenistic",
      "authority": "primary",
      "topics": ["dignities", "houses", "lots", "profections", "zodiacal releasing"],
      "page_coverage": {
        "dignities": [145-200],
        "houses": [267-350],
        "lots": [289-312]
      }
    }
  ]
}
```

### 5. Quality Control Report
**Format**: Markdown + JSON data
**Contents**:
- OCR error detection results
- Cross-reference validation summary
- Contradiction flags and resolutions
- Missing or incomplete extractions
- Recommendations for manual review

**Example sections**:
- OCR errors found and corrected
- Topics with conflicting interpretations
- Areas needing additional source material
- Validation statistics

---

## Design Documents

This project maintains detailed design and implementation documentation for major enhancements and system improvements.

### Available Design Documents

**Life Arc Report Design** ⭐ CURRENT FOCUS
- Location: `/docs/life_arc_report_design.md`
- Purpose: Complete research and design for life arc timeline system (birth to age 100)
- Contents:
  - 10-lot Hellenistic system specifications
  - 6 timing technique integration (ZR, returns, progressions, profections)
  - 4-tier event prioritization framework
  - Life chapter detection algorithms
  - Visual timeline design
  - Technical document structure
  - Synthesis PDF design with graphics
  - 7-stage implementation plan
- Status: Research & design complete (Stage 0 COMPLETE ✅), ready to begin Stage 1
- **Size:** 105+ pages of detailed specifications
- **Purpose:** Answer "When do struggles end? When does success happen? When do relationships form?"

**Transit Interpretation Enhancement**
- Location: `/docs/transit_interpretation_design.md`
- Purpose: Complete research findings and methodology for transit interpretation enhancement
- Contents: Problem analysis, research approach, findings from traditional sources, recommended implementation strategy
- Status: Research complete, **DEFERRED** (will implement after Life Arc Report)

**Transit Staged Implementation Plan**
- Location: `/docs/transit_staged_implementation.md`
- Purpose: Staged rollout plan for implementing transit interpretation improvements
- Contents: Phase-by-phase implementation strategy, validation approach, testing procedures
- Status: Implementation roadmap defined, **DEFERRED** (will implement after Life Arc Report)

**Timing Techniques Research and Plan**
- Location: `/docs/timing_techniques_plan.md`
- Purpose: Comprehensive research and implementation plan for traditional timing techniques
- Contents: Analysis of 8 timing techniques, RAG coverage assessment, implementation recommendations, priority recommendations
- Status: Research complete (Stage 0), integrated into Life Arc Report design
- Key Finding: Annual profections is REQUIRED (not optional) for transit filtering system

**Natal Interpretation Enhancement Plan**
- Location: `/docs/natal_enhancement_architecture.md`
- Purpose: Research and architecture for expanding horoscope depth and customization
- Contents: Methods research, RAG coverage analysis, settings system design, implementation roadmap
- Status: Research complete (Stage 1.3 COMPLETE ✅)
- Key Features:
  - 15 topics researched (9 traditional + 6 modern methods)
  - Settings block system for interpretation customization
  - Traditional foundation protection (modern methods supplementary only)
  - Hierarchical interpretation approach (traditional primary, modern secondary)

---

## Agents

This project uses multiple specialized agents for development workflow, documentation, and astrological interpretation. Each agent maintains its own documentation to keep this file lean and manageable.

### Custom Project Agents

**workflow-planner-2 (Pink)**
- Role: AI app development expert advisor
- Maintains: `/docs/session_goals.md` (North Star vision and strategic direction)
- Responsibilities: Architecture recommendations, tool/framework selection, agent design, technical approach guidance
- Coordination: Recommends to other agents; does not implement directly

**docs-updater-astrology (Cyan)**
- Role: System cataloger and documentation maintainer
- Maintains: This file (`CLAUDE.md`) as current state document
- Framework: Goal framing, target stack, agents, MCP/tools, data model, integrations, architecture, state/memory, prompts
- Coordination: Catalogs recommendations from workflow-planner-2, updates with completed work, references detailed docs in `/docs/`

**astrology-rag-builder (Orange)**
- Role: RAG database maintenance and queries
- Location: `/agents/astrology_rag_builder_README.md`
- Responsibilities: Database construction, semantic search, quality control
- Coordination: Uses helper scripts (ephemeris, reference data), maintains database integrity
- Proactive Triggers: Automatically activates when references are mentioned, database updates needed, or terminology normalization required

**agent-creator (Pink)**
- Role: Conversational agent creation assistant
- Location: `.claude/agents/agent-creator.md`
- Responsibilities: Helps user create new custom agents through conversation instead of using `/agents` command
- Capabilities:
  - Gathers requirements conversationally (purpose, triggers, capabilities, tools, model, color)
  - Drafts comprehensive agent definitions using official template
  - Iterates based on feedback
  - Writes final agent to `.claude/agents/[name].md`
  - Ensures same quality as `/agents` command
  - Automatically triggers docs-updater-astrology after creating agents
- Coordination: Meta-agent for building other agents; triggers documentation updates automatically
- Proactive Triggers: When user wants to create agents, mentions building agents conversationally, or wants `/agents` quality

### Documentation Hierarchy

**session_goals.md** (North Star) → **/docs/** (detailed specifications) → **CLAUDE.md** (current state)

- **session_goals.md**: Vision, technical approach, simple strategic direction (owned by workflow-planner-2)
- **/docs/**: Design documents, staged implementation plans, technical details
- **CLAUDE.md**: Current progress, system catalog, references to detailed docs (owned by docs-updater-astrology)

### Astrological Interpretation Agents

**Purpose**: Claude Code agents provide interpretation and synthesis for the astrology application. Scripts handle calculations and data retrieval, then call agents to synthesize traditional delineations into cohesive interpretations.

**Architectural Decision**: Using Claude Code agents (not GPT-5 API) for MVP
- No external API calls needed
- Faster (no network latency)
- Better quality (Claude excels at synthesis)
- Easier to test and iterate
- Agent instructions = approved "prompts"
- Can migrate to GPT-5 API later if desired

**natal-interpreter (Purple)** - ACTIVE ✅
- Location: `.claude/agents/natal-interpreter.md`
- Purpose: Generate comprehensive natal psychological profiles using traditional/Hellenistic methods
- Model: Sonnet
- Color: Purple
- Created: Stage 1.1
- Key features:
  - Two-part output: Accessible synthesis (no jargon) + Technical analysis (full astrological detail)
  - RAG database integration for traditional interpretations
  - Sect-based interpretation with planetary strength assessment
  - Hellenistic foundation with modern psychological overlay
  - Scales depth with available data
  - Footnoted citations for all interpretations
- Output structure:
  - I. Chart Overview (technical)
  - II. Synthesis for the Native (accessible - Introduction, Core Personality, Psychological Makeup, Life Path, Strengths, Challenges, Career, Integration)
  - III. Core Identity (technical Sun/Moon/ASC)
  - IV. Planetary Placements (technical)
  - V. Benefic/Malefic Dynamics (technical)
  - VI. Major Life Themes (brief summary)
  - VII. Planetary Strength Table
  - VIII. Sources
- Workflow: Receive chart data from script → Query RAG (optional) → Synthesize delineations → Generate horoscope
- Called by: `horoscope_generator.py` script (to be created in Stage 1.2)
- Invocation: NOT proactive; called explicitly by scripts
- Successfully tested with Darren's natal chart

**Transit Analyzer** (to be created in future stage)
- Location: `/agents/transit_analyzer_README.md` (will be created)
- Purpose: Current and upcoming transit analysis with timing
- Workflow: Receive natal + transit data → Query RAG → Synthesize interpretations → Generate report
- Called by: `transit_report.py` script
- Instructions require user approval before agent is created

**Timing Technique Agents** (to be created in future stages)
- Profections Interpreter
- Zodiacal Releasing Interpreter
- Progressions Interpreter
- Each agent receives calculation results and synthesizes traditional interpretations

### Agent Coordination Pattern

1. User + workflow-planner-2 discover approach and make recommendations
2. workflow-planner-2 recommends specific tools/frameworks/agents/architecture
3. docs-updater-astrology catalogs recommendations in CLAUDE.md
4. Implementation agents execute work using helper scripts and RAG database
5. docs-updater-astrology updates CLAUDE.md with progress
6. When stages complete, docs-updater-astrology updates with next stage plan

### Agent Documentation Pattern

- Each agent creates and maintains its own README in the `/agents/` directory
- Agent READMEs document: purpose, workflow steps, usage examples, known limitations
- Agents update their READMEs as they learn and improve
- This file serves as a central index pointing to agent documentation
- See `/agents/README.md` for complete system architecture, workflows, and helper script integration

---

## Development Guidelines

### For AI Agents Working on This Project

#### ⚠️ CRITICAL: Astrology Information Sources

**ALL astrology information lookups, fact-checking, and research MUST use ONLY local references:**

1. **RAG Database**: `/output/database/astrology_rag_database.jsonl`
   - Primary source for interpretations and delineations
   - Use `scripts/query_rag_database.py` for semantic search

2. **Reference PDFs**: `/Referendces/` folder
   - Hellenistic Astrology (Chris Brennan)
   - Demetra George - Astrology and the Authentic Self
   - Robert Hand - Planets in Transit
   - Bernadette Brady - Predictive Astrology
   - Sophia Mason - Delineation of Progressions
   - Liz Greene - The Horoscope in Manifestation

3. **Static Reference Module**: `/scripts/astrology_reference.py`
   - Essential dignities (domicile, exaltation, detriment, fall, triplicity, bounds, decans)
   - Planetary data and significations
   - Sign and house attributes
   - Aspect definitions and orbs
   - Sect, conditions, and lots

**NEVER use external web searches or online resources for astrology information.** All interpretations must be grounded in the traditional sources provided in this project.

#### Before Starting Extraction
1. Review this CLAUDE.md document thoroughly
2. Understand the astrological systems and terminology
3. Check the controlled vocabulary and synonym mappings
4. Review example structures for each building block
5. Verify access to reference PDFs in `/Referendces/`
6. Review Swiss Ephemeris Integration section for live astronomical data access

#### During Extraction
1. Maintain strict adherence to controlled vocabulary
2. Apply synonym mapping consistently
3. Tag all content with complete metadata
4. Preserve source attribution with page numbers
5. Flag contradictions and edge cases
6. Use semantic chunking (200-800 tokens, 50-token overlap)
7. Apply tradition markers to all content

#### Quality Checks
1. Validate entity extraction accuracy
2. Check metadata completeness
3. Verify cross-references
4. Test query retrieval for sample topics
5. Review OCR-heavy sections (Hand book) carefully
6. Ensure JSON schema compliance

#### Output Requirements
1. Valid JSON/JSONL format
2. Consistent metadata structure
3. Complete source attribution
4. Controlled vocabulary compliance
5. Vector embeddings generated via OpenAI API
6. Quality control documentation

#### Swiss Ephemeris Access for Agents

Agents can access live astronomical calculations through the ephemeris helper script at `/Users/darrenschaeffer/Library/Mobile Documents/com~apple~CloudDocs/Astrogy_Claude/scripts/ephemeris_helper.py`.

**Available Capabilities**:
- Calculate current planetary positions for any date/time
- Compute house cusps for specific locations (default: whole-sign houses)
- Calculate aspects between planetary positions
- Determine transits to natal positions
- Find eclipse dates (lunar and solar)
- Convert between datetime and Julian day numbers
- Format positions in traditional astrological notation

**Integration Workflow**:
1. Use ephemeris helper to calculate current/historical positions
2. Query RAG database for interpretations of those positions
3. Combine ephemeris data with traditional delineations from source texts
4. Generate comprehensive interpretations using both systems

**Example Use Cases**:
- Chart interpretation: Calculate positions, then retrieve delineations from database
- Transit analysis: Calculate current transits, query database for transit interpretations
- Aspect analysis: Calculate aspects between planets, retrieve aspect meanings
- Timing techniques: Use ephemeris for date-based calculations (progressions, profections)
- Chart examples: Verify chart data from source texts using ephemeris calculations

**Important Notes**:
- Always use UTC for consistency in astronomical calculations
- Default house system is whole-sign ('W') to match project standards
- Only classical aspects are calculated (no modern aspects)
- Modern planets (Uranus, Neptune, Pluto) available but marked as secondary
- Call `cleanup()` when finished with ephemeris calculations to free resources

See the "Swiss Ephemeris Integration" section above for complete function reference and usage examples.

#### Static Reference Data Access for Agents

Agents can access all static astrological reference data through the astrology reference module at `/Users/darrenschaeffer/Library/Mobile Documents/com~apple~CloudDocs/Astrogy_Claude/scripts/astrology_reference.py`.

**Available Data**:
- Complete essential dignity tables (domicile, exaltation, triplicity, bounds, decans)
- Planetary profiles with significations, sect status, and keywords
- Sign data with elements, modalities, rulers, and qualities
- House significations and topics (all 12 houses)
- Classical aspect definitions with traditional orbs
- Sect assignments and planetary conditions
- Lot/part calculation formulas

**Helper Functions** (19 total):
- `check_dignity(planet, sign)` - Check dignity status
- `get_planet_dignities(planet)` - Get all dignities for planet
- `get_triplicity_ruler(element, chart_type)` - Get triplicity ruler by sect
- `get_bounds_ruler(sign, degree)` - Get bounds ruler for degree
- `get_decan_ruler(sign, degree)` - Get decan ruler for degree
- `get_sect_status(planet, chart_type)` - Get sect status
- `check_combust()`, `check_cazimi()`, `check_under_beams()` - Condition checks
- And 10 more utility functions

**Integration Workflow**:
1. Import reference module for static lookups
2. Use for dignity checks, ruler lookups, condition verification
3. Combine with ephemeris for calculations
4. Query RAG database for interpretations

**Example Usage**:
```python
from scripts.astrology_reference import check_dignity, PLANETS, get_bounds_ruler
from scripts.ephemeris_helper import get_planetary_positions
from datetime import datetime

# Calculate current positions
positions = get_planetary_positions(datetime.utcnow())
mars_sign = positions['Mars']['sign']
mars_degree = positions['Mars']['degree_in_sign']

# Check dignity from reference
dignity = check_dignity('Mars', mars_sign)

# Get bounds ruler
bounds = get_bounds_ruler(mars_sign, mars_degree)

# Get keywords from reference
keywords = PLANETS['Mars']['keywords']

# Build query for RAG database
query = f"Mars in {mars_sign}"
if dignity:
    query += f" in {dignity}"
# ... query RAG for interpretation
```

**When to Use Reference vs RAG**:
- **Reference Module**: Factual lookups (rulers, dignities, house topics, aspect orbs)
- **RAG Database**: Interpretations, delineations, technique instructions

See the "Static Astrology Reference Data" section above for complete data structures and function reference.

### Important Reminders

**Traditional Focus**: This is a traditional/Hellenistic astrology project. Modern psychological interpretations are secondary.

**Whole-Sign Houses**: All house placements use whole-sign system exclusively.

**Seven Planets**: Traditional seven planets are primary; modern planets are supplementary only.

**Attribution**: Every interpretation must cite source, author, and page number.

**Dignity Priority**: Essential dignities are fundamental; always extract and validate dignity tables.

**Sect Matters**: Sect considerations are critical for interpretation; always note day/night chart context.

**No Unsolicited Analysis**: Do not analyze the user's birth chart (`Darren_Profile.txt`) unless explicitly requested.

### ⚠️ Agent Instructions Approval Workflow

**CRITICAL REQUIREMENT**: All Claude Code agent **instructions** that the application will use must be shown to user for approval BEFORE agents are created.

**Architectural Context**:
- **MVP Approach**: Using Claude Code agents (not GPT-5 API) for interpretation/synthesis
- Agent instructions = the "prompts" that control agent output
- Scripts calculate/query data, then call agents for synthesis
- Can migrate to GPT-5 API later if desired

**What this means:**
- We're approving **agent instruction documents** (the agent definitions)
- NOT conversations during development/building
- The workflow is: design agent instructions → show for approval → user approves/modifies → create agent → scripts call agent

**When this applies:**
- All Mode 1 (Natal Horoscope Generator) agent instructions
- All Mode 2 (Transit Report Generator) agent instructions
- All Mode 3+ (Timing Techniques) agent instructions
- All Stage 3+ (n8n integration or chat interface) agent instructions if applicable

**Workflow:**
1. Agent (or agent-creator) builds complete agent **instruction document** with all components:
   - Agent purpose and role
   - System instructions (how to interpret, synthesize, format)
   - Input data structure (how chart/transit/timing data will be provided)
   - Output format requirements (horoscope structure, sections, tone)
   - RAG database query integration (what to query, how to synthesize)
   - Traditional astrology compliance requirements
   - Example workflows

2. Agent presents instruction document to user with:
   - Clear section labels (Purpose, Instructions, Input Format, Output Format, RAG Integration, Examples)
   - Explanation of what this agent will generate when called by scripts
   - Example input/output scenarios
   - Traditional astrology compliance notes

3. Agent STOPS and waits for user approval/modifications

4. User reviews and either:
   - Approves → Agent is created with approved instructions
   - Requests changes → Agent modifies instructions and presents again
   - Rejects → Agent is not created

**Purpose:**
- Quality control over all AI-generated horoscope content that the application produces
- Ensures agent instructions match user's vision and expectations
- Allows iterative refinement of agent design before implementation

### ⚠️ Synthesis Agent Modification Policy

**CRITICAL**: Agents that generate final synthesis output (horoscopes, reports, interpretations) must NOT be modified without explicit user approval.

**Affected agents**:
- `natal-interpreter` - Generates natal horoscope synthesis
- `transit-analyzer` - Generates transit report synthesis
- Any future synthesis/interpretation agents

**Why this matters**:
- These agents control the **tone, style, and structure** of the final output the user receives
- Changes to these agents can dramatically alter the user experience
- User needs to maintain consistent output quality and style across all generated horoscopes

**Process for modifications**:
1. **Identify the need**: User requests change OR you identify an issue/improvement
2. **Propose changes**: Present proposed modifications to user with clear before/after examples
3. **Get approval**: Wait for explicit user approval before implementing
4. **Document changes**: Note what was changed and why in the agent file header

**What requires approval**:
- Changes to output structure (sections, subsections, formatting)
- Changes to tone or writing style
- Changes to content inclusion/exclusion
- Changes to narrative flow or organization
- Changes to technical detail level

**What does NOT require approval** (but inform user):
- Bug fixes that don't change output
- Updates to internal logic that maintain same output
- Performance optimizations
- Corrections to factual astrological errors

**Example workflow**:
```
User: "The horoscope doesn't look right. The career section doesn't mention house rulers."
Assistant: "I see the issue. The natal-interpreter agent isn't emphasizing house rulers.
           I'd like to propose adding house ruler analysis to the career section.
           This would add language like: 'Your 10th house is ruled by Venus in the 5th,
           indicating career through creativity.'
           Should I make this change?"
User: "Yes, but make sure it's naturally integrated, not technical jargon."
Assistant: [Makes approved change, documents it]
```

### 📋 Documentation Update Protocol

**After every major step, ALWAYS update ALL documentation using the docs-updater-astrology agent:**

**Major steps include:**
- Completing any implementation stage (Stage -1, 0, 1, 2, etc.)
- Adding new features, modes, or CLI commands
- Making architecture or technology decisions
- Discovering critical findings
- Adding/modifying agents or tools
- Completing milestones or sub-stages

**What to update:**
1. **CLAUDE.md** (via docs-updater-astrology agent):
   - Current Status section (mark stages complete ✅)
   - Version History (add new version entry)
   - References to new design docs
   - System component catalog (if changed)

2. **session_goals.md** (via docs-updater-astrology agent for PROGRESS):
   - Mark completed stages/sub-stages as ✅ or COMPLETE
   - Update "Deliverables" sections with checkmarks
   - Track what has been implemented
   - Update "Status" fields (Planning → In Progress → COMPLETE ✅)
   - Add completion timestamps
   - Update "Next Stage" or current stage pointers
   - Keep implementation progress current
   - **Do NOT modify plan structure** (that's workflow-planner-2's job)

3. **Relevant README files** (via docs-updater-astrology):
   - `/agents/[agent]_README.md` if agent capabilities changed
   - Any other affected documentation

**Agent Division of Labor for session_goals.md:**
- **workflow-planner-2**: Creates plan structure, defines stages, makes recommendations (does NOT mark progress)
- **docs-updater-astrology**: Marks progress, checks off deliverables, updates status (does NOT change plan)

**How to trigger:**
- Use the docs-updater-astrology agent proactively
- Don't wait for user to request updates
- Update immediately when major work completes
- Update ALL three documentation types (CLAUDE.md + session_goals.md + READMEs)

This ensures documentation always reflects current project state.

---

## Environment Configuration

**API Credentials**: Stored in `.env` file in project root

Required variables:
```
OPENAI_API_KEY=your_api_key_here
```

**OpenAI API Usage**:
- **Embeddings only**: Used for RAG database vector embeddings (text-embedding-3-large or similar)
- **NOT used for LLM calls**: Interpretation/synthesis handled by Claude Code agents
- Required for RAG database queries and semantic search
- No usage for chat completion or text generation in MVP

**Multi-Profile System**:

The project now supports multiple user profiles with isolated directories for birth data, seed data, and outputs.

**Directory Structure**:
```
/profiles/
  ├── darren/
  │   ├── profile.md               # Birth data and settings (markdown format)
  │   ├── seed_data/               # Enhanced interpretations (input for agents)
  │   │   └── natal_interpretation_enhanced.md
  │   └── output/                  # Final horoscopes and reports
  │       ├── natal_horoscope_synthesis.md
  │       └── natal_horoscope_synthesis.pdf
  ├── [name2]/
  │   ├── profile.md
  │   ├── seed_data/
  │   └── output/
  └── ...
```

## Automated Horoscope Generation Workflow

**When user requests a natal horoscope**, the system automatically performs all steps without verification:

1. **Create profile** (if new person) - `create_profile.py` with birth data
2. **Apply settings** - Chiron, Lilith, technical_sections as requested
3. **Generate seed data** - `natal_interpreter.py --profile [name]`
4. **Generate synthesis** - natal-interpreter agent
5. **Create PDF** - `create_synthesis_pdf.py --profile [name]`
6. **Deliver result** - Show location of markdown + PDF files

**User request format**: "Create a natal horoscope for [person], [birth data], exclude [chiron/lilith/technical sections]"

**Example**:
```
User: "Create a natal horoscope for my sister. 8/5/1991, 6:30 PM, Samcheok-si, South Korea 37.4441° N, 129.1679° E. Exclude chiron, lilith, and technical sections."

System response:
1. Creates profile at /profiles/sister/
2. Generates seed data
3. Generates horoscope synthesis
4. Creates PDF
5. Shows: "✅ Horoscope complete! Files at /profiles/sister/output/"
```

**No verification step** - complete horoscope generation is fully automated.

---

**Creating New Profiles** (`scripts/create_profile.py`):

Automatically create new profiles with calculated chart data:

```bash
python scripts/create_profile.py --name "mom" \
    --date "2/9/1960" \
    --time "2:30 PM" \
    --location "Linton, ND" \
    --lat 46.267 \
    --lon -100.233 \
    --timezone "CST"
```

This script:
- Creates directory structure (`seed_data/` and `output/`)
- Calculates all planetary positions using Swiss Ephemeris
- Calculates house cusps (whole-sign system)
- Generates `profile.md` with complete chart data
- Sets default settings (customize after creation)

**Supported timezones**: EST, CST, MST, PST, UTC

**Coordinate format**:
- Latitude: Positive = North, Negative = South
- Longitude: Positive = East, Negative = West

See `/profiles/README.md` for complete documentation.

**Profile Loader** (`scripts/profile_loader.py`):
- `load_profile(name)` - Load specific profile
- `get_default_profile()` - Get default profile (prefers 'darren', then alphabetically first)
- `list_profiles()` - List all available profiles

**Profile Object Methods**:
- `profile.get_seed_data_path(filename)` - Get path to seed data file
- `profile.get_output_path(filename)` - Get path to output file
- `profile.settings` - Parsed settings from [INTERPRETATION_SETTINGS] block

**Usage in Scripts**:
```python
from scripts.profile_loader import get_default_profile

# Load default profile
profile = get_default_profile()

# Get paths
seed_path = profile.get_seed_data_path('natal_interpretation_enhanced.md')
output_path = profile.get_output_path('natal_horoscope_synthesis.md')

# Access settings
if profile.settings['technical_sections']:
    # Include technical sections
    pass
```

**Legacy Paths** (Deprecated):
- Old single-user files in `/output/` are deprecated
- Old `Darren_Profile.txt` in root is deprecated
- All new work uses `/profiles/[name]/` structure

**Project Root**:
- `/Users/darrenschaeffer/Library/Mobile Documents/com~apple~CloudDocs/Astrogy_Claude`

---

## Glossary of Astrological Terms

For AI agents unfamiliar with astrology, this glossary provides essential definitions:

**Angular**: Houses 1, 4, 7, 10 (strongest house positions)

**Applying aspect**: Aspect forming as planets move toward exactness

**Bounds/Terms**: Division of each sign into 5 unequal segments ruled by different planets

**Cadent**: Houses 3, 6, 9, 12 (weakest house positions)

**Cazimi**: Planet within 17 minutes of the Sun (empowered)

**Combust**: Planet within 8.5° of the Sun (weakened)

**Decans/Faces**: Division of each sign into three 10° segments

**Detriment**: Planet in sign opposite its domicile (weakened)

**Dignity**: Any condition strengthening a planet (essential or accidental)

**Diurnal**: Day chart (Sun above horizon at birth)

**Domicile**: Planet in its own sign (strongest essential dignity)

**Essential dignity**: Strength from zodiacal position (sign-based)

**Exaltation**: Planet in sign of exaltation (second-strongest dignity)

**Fall**: Planet in sign opposite its exaltation (weakened)

**Lot**: Calculated point using formula (Ascendant + Planet A - Planet B)

**Malefic**: Harmful planet (Mars, Saturn traditionally)

**Nocturnal**: Night chart (Sun below horizon at birth)

**Profection**: Annual time-lord system (advance 1 house per year of life)

**Progression**: Predictive system (1 day after birth = 1 year of life)

**Reception**: Planet in sign ruled by another planet

**Retrograde**: Apparent backward motion of planet

**Sect**: Division of planets by day/night chart affinity

**Separating aspect**: Aspect moving past exactness

**Succedent**: Houses 2, 5, 8, 11 (moderate house positions)

**Transit**: Current planetary position relative to natal chart

**Triplicity**: Elemental dignity (fire, earth, air, water rulers)

**Under the beams**: Planet within 15° of Sun (obscured)

**Whole-sign houses**: House system where each house = one complete sign

---

## Version History

*For detailed version history, see [CHANGELOG.md](CHANGELOG.md).*
*For recent changes (last 5 versions below), major milestone snapshots, and period summaries, see [/docs/archive/](/docs/archive/).*

---

**Version 1.11** - 2025-10-05
- **Major Course Change**: Pivoted to implement Life Arc Report before Transit Report
- Updated application modes: Mode 2 is now Life Arc Report, Mode 3 is Transit Report
- **Life Arc Report Stage 0 Complete**: Research and design complete (105+ pages)
- Key Life Arc features:
  - 10-lot Hellenistic system (Fortune, Spirit, Eros, Necessity, Courage, Victory, Exaltation, Marriage, Children, Basis)
  - 6 timing techniques (ZR, Saturn Returns, Jupiter Returns, Outer Planet Milestones, Progressed Lunation, Key Profections)
  - 4-tier event prioritization system
  - Birth to age 100 timeline
  - Technical document (50-100+ pages) + Synthesis PDF (15-25 pages with graphics)
  - 7-stage implementation plan (~5-6 weeks)
- Updated Design Documents section to show Life Arc as current focus
- Marked Transit Report design as deferred (after Life Arc)
- Added note that session_goals.md needs updating by workflow-planner-2
- Ready to begin Life Arc Stage 1 (Core Calculation Engine)

**Version 1.10** - 2025-10-04
- **Stage 1.1 Complete**: Created natal-interpreter agent
- Added natal-interpreter to Agents catalog (Purple, Sonnet model)
- Two-part output structure (accessible synthesis + technical analysis)
- RAG database integration, sect-based interpretation
- Architecture clarification: NOT proactive (called explicitly by scripts)
- Successfully tested with Darren's natal chart

**Version 1.9** - 2025-10-04
- **Major Architectural Decision**: Using Claude Code agents instead of GPT-5 API for interpretation/synthesis in MVP
- Renamed "GPT-5 Prompt Approval Workflow" → "Agent Instructions Approval Workflow"
- Scripts calculate/query, then call agents for synthesis
- Can migrate to GPT-5 API later if desired

**Version 1.8** - 2025-10-04
- Added critical workflow requirement: Agent Instructions Approval (production agents only)
- All Mode 1, 2, 3+ agent instructions require approval before creation
- Purpose: Quality control over production output
- Note: Version 1.9 supersedes this with architectural change to Claude Code agents

**Version 1.7** - 2025-10-04
- Infrastructure improvement: Created agent-creator meta-agent
- Conversational agent creation (instead of `/agents` command)
- Automatically triggers docs-updater-astrology after creating agents

**Version 1.6** - 2025-10-04
- Infrastructure improvement: Added proactive triggers to astrology-rag-builder agent
- All critical agents now have automatic triggers

---

## Contact & Support

**Project Owner**: Darren Schaeffer
**Purpose**: Traditional/Hellenistic astrology RAG database for AI-assisted chart interpretation
**Status**: Active development

For questions about astrological interpretation, consult the reference materials. For technical questions about database structure or extraction methodology, refer to relevant sections above.

---

*This documentation is designed for AI agents working on astrology knowledge extraction. It provides comprehensive context about traditional astrological systems, extraction requirements, and quality standards necessary for building an accurate and useful RAG database.*
