# Data Formats Reference

**Purpose**: Complete schemas and data structures for all JSON files, profile formats, and data exchanges in the Astrogy_Claude system.

**Last Updated**: 2025-10-11

---

## Quick Index

- [Profile Formats](#profile-formats)
- [Life Arc Timeline Data](#life-arc-timeline-data)
- [Transit Data](#transit-data)
- [Seed Data (Future)](#seed-data-future)
- [RAG Database Format](#rag-database-format)
- [Agent Communication Formats](#agent-communication-formats)

---

## Profile Formats

### Profile.txt (Simple Format)

**Location**: `/profiles/{name}/profile.txt`

**Purpose**: Stores basic birth data for profiles using simple text format.

**Format**:
```
Name: [Full Name]
Birth Date: [Month Day, Year]
Birth Time: [HH:MM AM/PM]
Birth Location: [City, State/Country]
Timezone: [IANA timezone identifier]
Latitude: [decimal degrees]
Longitude: [decimal degrees]
```

**Example**:
```
Name: Dylan
Birth Date: October 25, 1992
Birth Time: 7:00 PM
Birth Location: Miami, FL
Timezone: America/New_York
Latitude: 25.7617
Longitude: -80.1918
```

**Notes**:
- Used for simpler profiles without settings customization
- Time format: 12-hour with AM/PM
- Latitude: Positive = North, Negative = South
- Longitude: Positive = East, Negative = West

### Profile.md (Settings Format)

**Location**: `/profiles/{name}/profile.md`

**Purpose**: Stores birth data + interpretation settings for advanced customization.

**Format**:
```markdown
# Natal Chart Profile - [Name]

## Interpretation Settings

Configure what analysis modules and output styles to include in your natal interpretation.

```ini
[INTERPRETATION_SETTINGS]

# DEPTH CONTROL
# Options: "minimal" | "standard" | "deep" | "comprehensive"
depth = "deep"

# HOUSE RULER ANALYSIS
# Include detailed house ruler placement and condition analysis
house_rulers = true

# LOTS/ARABIC PARTS
# Include Fortune, Spirit, and other Hermetic lots
lots = true

# PSYCHOLOGICAL OVERLAY
# Include psychological/growth-oriented interpretation
psychological_overlay = true

# MODERN METHODS
# Include modern planetary aspects (Uranus, Neptune, Pluto)
modern_methods = false

# OUTPUT FORMAT
# Options: "markdown" | "pdf" | "both"
output_format = "both"

# TECHNICAL APPENDIX
# Include detailed technical data (positions, aspects, dignities)
technical_appendix = true
```

## Birth Data

Name: [Full Name]
Date of Birth: [YYYY-MM-DD]
Time of Birth: [HH:MM] ([Timezone])
Place of Birth: [City, State/Country]
Coordinates: [Latitude], [Longitude]
```

**Example**:
```markdown
# Natal Chart Profile - Jamie

## Interpretation Settings

```ini
[INTERPRETATION_SETTINGS]
depth = "deep"
house_rulers = true
lots = true
psychological_overlay = true
modern_methods = false
output_format = "both"
technical_appendix = true
```

## Birth Data

Name: Jamie Doe
Date of Birth: 1985-03-15
Time of Birth: 14:30 (America/New_York)
Place of Birth: New York, NY
Coordinates: 40.7128, -74.0060
```

**Notes**:
- Settings block is optional (defaults used if missing)
- Date format: ISO 8601 (YYYY-MM-DD)
- Time format: 24-hour (HH:MM)

---

## Life Arc Timeline Data

**Location**: `/profiles/{name}/output/life_arc_timeline_data.json`

**Purpose**: Complete life timeline data including profections, progressions, solar returns, zodiacal releasing, and firdaria for Mode 2 (Life Arc Reports).

**Schema**:

### Top Level
```json
{
  "profile": "string",
  "birth_data": { /* Birth data object */ },
  "age_range": { /* Age range object */ },
  "profections": [ /* Array of profection objects */ ],
  "progressions": [ /* Array of progression objects */ ],
  "solar_returns": [ /* Array of solar return objects */ ],
  "zodiacal_releasing_fortune": { /* ZR Fortune object */ },
  "zodiacal_releasing_spirit": { /* ZR Spirit object */ },
  "firdaria": [ /* Array of firdaria period objects */ ],
  "convergence_events": [ /* Array of convergence objects */ ]
}
```

### Birth Data Object
```json
{
  "date": "YYYY-MM-DD",
  "time": "HH:MM:SS",
  "location": "City, State/Country",
  "latitude": 25.7617,
  "longitude": -80.1918,
  "timezone": "America/New_York",
  "utc_offset": "+0000"
}
```

### Age Range Object
```json
{
  "start": 0,
  "end": 100
}
```

### Profection Object
```json
{
  "profile": "string",
  "profection": {
    "age": 0,
    "profected_house": 1,
    "profected_sign": "Taurus",
    "lord_of_year": "Venus"
  },
  "natal_ascendant": {
    "sign": "Taurus",
    "degree": 26.5
  },
  "lord_natal_position": {
    "planet": "Venus",
    "sign": "Sagittarius",
    "house": 8,
    "degree": 7.6,
    "retrograde": false,
    "dignities": {
      "domicile": false,
      "exaltation": false,
      "detriment": false,
      "fall": false,
      "triplicity": "participating" | "cooperating" | "agreeing" | null,
      "term": "string" | null,
      "face": "string" | null
    }
  },
  "profected_house_natal": {
    "number": 1,
    "sign": "Taurus",
    "planets": [
      {
        "name": "Mars",
        "degree": 20.94
      }
    ]
  }
}
```

**Notes**:
- One profection object per year (0-100)
- Lord of year = ruler of profected sign
- `lord_natal_position` shows where that planet sits in natal chart
- `profected_house_natal` shows natal planets in the profected house

### Progression Object
```json
{
  "age": 32,
  "date": "2025-03-15",
  "progressed_sun": {
    "sign": "Aries",
    "degree": 15.234,
    "house": 10
  },
  "progressed_moon": {
    "sign": "Cancer",
    "degree": 8.567,
    "house": 1
  },
  "progressed_ascendant": {
    "sign": "Leo",
    "degree": 12.890
  },
  "progressed_mc": {
    "sign": "Taurus",
    "degree": 5.432
  }
}
```

**Notes**:
- Secondary progressions (day-for-year)
- Progressed Sun advances ~1° per year
- Progressed Moon advances ~13° per year (full cycle ~28 years)
- Progressed ASC/MC advance ~1° per year

### Solar Return Object
```json
{
  "year": 2025,
  "age": 33,
  "return_date": "2025-03-15T14:32:18",
  "location": {
    "city": "Miami, FL",
    "latitude": 25.7617,
    "longitude": -80.1918
  },
  "ascendant": {
    "sign": "Virgo",
    "degree": 18.234
  },
  "mc": {
    "sign": "Gemini",
    "degree": 12.567
  },
  "planets": [ /* Array of planet positions */ ],
  "houses": [ /* Array of house cusps */ ]
}
```

**Notes**:
- Solar return calculated for exact Sun return moment
- Location can be natal or relocated
- Full planetary positions for SR chart

### Zodiacal Releasing Object
```json
{
  "starting_lot": "Fortune" | "Spirit",
  "natal_lot_position": {
    "sign": "Gemini",
    "degree": 15.234
  },
  "periods": [
    {
      "level": 1,
      "sign": "Gemini",
      "ruler": "Mercury",
      "start_date": "1992-10-25",
      "end_date": "2012-10-25",
      "start_age": 0,
      "end_age": 20,
      "peak_period": false,
      "loosing_of_the_bond": false,
      "subperiods": [
        {
          "level": 2,
          "sign": "Gemini",
          "ruler": "Mercury",
          "start_date": "1992-10-25",
          "end_date": "1995-10-25",
          "start_age": 0,
          "end_age": 3,
          "peak_period": true
        },
        {
          "level": 2,
          "sign": "Cancer",
          "ruler": "Moon",
          "start_date": "1995-10-25",
          "end_date": "2004-10-25",
          "start_age": 3,
          "end_age": 12,
          "peak_period": false
        }
      ]
    }
  ]
}
```

**Notes**:
- ZR calculated from Lot of Fortune or Lot of Spirit
- L1 periods: 8-30 years per sign
- L2 periods: Sub-divisions within L1
- Peak period: L2 sign = L1 sign
- Loosing of bond: Transition to next L1 period

### Firdaria Object
```json
{
  "age": 0,
  "start_date": "1992-10-25",
  "end_date": "2001-10-25",
  "planet": "Moon",
  "duration_years": 9,
  "subperiods": [
    {
      "planet": "Moon",
      "start_date": "1992-10-25",
      "end_date": "1994-01-25",
      "duration_months": 15.43
    },
    {
      "planet": "Saturn",
      "start_date": "1994-01-25",
      "end_date": "1995-04-25",
      "duration_months": 15.43
    }
  ]
}
```

**Notes**:
- Persian timing system
- Day charts start with Sun, night charts start with Moon
- Fixed planetary order and durations

### Convergence Event Object
```json
{
  "date": "2025-06-15",
  "age": 32.6,
  "score": 25,
  "level": "MAJOR",
  "techniques": [
    {
      "technique": "profection",
      "detail": "Saturn year, Saturn transiting profected house"
    },
    {
      "technique": "zodiacal_releasing",
      "detail": "L2 peak period (Gemini-Gemini)"
    },
    {
      "technique": "progression",
      "detail": "Progressed Moon conjunct natal Sun"
    },
    {
      "technique": "solar_return",
      "detail": "SR Mars angular in 10th house"
    }
  ]
}
```

**Notes**:
- Convergence = multiple techniques aligning on same date
- Score calculated by technique weight and alignment strength
- Levels: MAJOR (25+), SIGNIFICANT (15-24), NOTABLE (8-14)

---

## Transit Data

**Location**: `/profiles/{name}/output/transit_data_{name}_{start}_to_{end}.json`

**Purpose**: Stores calculated transit data for Mode 3 (Transit Reports).

**Schema**:

### Top Level
```json
{
  "profile": "string",
  "date_range": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD",
    "days": 30
  },
  "current_age": 36,
  "natal_chart": { /* Natal chart snapshot */ },
  "timing_context": { /* Current timing techniques */ },
  "transits": [ /* Array of transit events */ ],
  "daily_scores": [ /* Array of daily score objects */ ],
  "summary": { /* Summary statistics */ }
}
```

### Natal Chart Snapshot
```json
{
  "sect": {
    "type": "night" | "day",
    "determined_by": "Sun below horizon (altitude: -36.72°)"
  },
  "chart_ruler": "Venus" | null,
  "planets": [
    {
      "name": "Sun",
      "symbol": "☉",
      "traditional": true,
      "longitude": 275.939,
      "sign": "Capricorn",
      "degree": 5.939,
      "dms": "5°56'20\"",
      "speed": 1.019,
      "retrograde": false,
      "house": 6,
      "dignities": {
        "essential": {
          "domicile": false,
          "exaltation": false,
          "detriment": false,
          "fall": false,
          "triplicity": "participating" | null,
          "term": "string" | null,
          "face": "string" | null
        },
        "accidental": {
          "angular": false,
          "succedent": false,
          "cadent": true,
          "rejoicing": false
        }
      }
    }
  ],
  "houses": [
    {
      "number": 1,
      "sign": "Leo",
      "degree": 3.456,
      "cusp_longitude": 123.456
    }
  ],
  "lots": {
    "fortune": {
      "sign": "Pisces",
      "degree": 15.234,
      "house": 8
    },
    "spirit": {
      "sign": "Scorpio",
      "degree": 22.567,
      "house": 4
    }
  }
}
```

### Timing Context Object
```json
{
  "profection": {
    "age": 36,
    "house": 1,
    "sign": "Leo",
    "lord_of_year": "Sun"
  },
  "zodiacal_releasing": {
    "fortune": {
      "L1_sign": "Gemini",
      "L1_ruler": "Mercury",
      "L2_sign": "Aquarius",
      "L2_ruler": "Saturn",
      "peak_period": false
    },
    "spirit": {
      "L1_sign": "Capricorn",
      "L1_ruler": "Saturn",
      "L2_sign": "Sagittarius",
      "L2_ruler": "Jupiter",
      "peak_period": false
    }
  },
  "progressions": {
    "sun_sign": "Aquarius",
    "moon_sign": "Capricorn",
    "ascendant_sign": "Virgo"
  },
  "firdaria": {
    "primary_planet": "Jupiter",
    "sub_planet": "Moon"
  }
}
```

### Transit Event Object
```json
{
  "date": "2025-10-15",
  "transit_planet": "Saturn",
  "natal_planet": "Venus",
  "aspect": "square",
  "orb": 2.5,
  "exact_date": "2025-10-16T14:32:18",
  "applying": true,
  "separating": false,
  "retrograde": false,
  "score": 8,
  "dignity_context": {
    "transit_planet_dignity": {
      "sign": "Pisces",
      "domicile": false,
      "exaltation": false,
      "detriment": true,
      "fall": false
    },
    "natal_planet_dignity": {
      "domicile": true,
      "exaltation": false
    }
  }
}
```

**Notes**:
- `score` represents impact strength (0-10)
- `applying` = moving toward exact
- `separating` = moving away from exact
- Retrograde status affects interpretation

### Daily Score Object
```json
{
  "date": "2025-10-15",
  "total_score": 45,
  "transit_count": 8,
  "scores_by_technique": {
    "profection": 12,
    "zodiacal_releasing": 15,
    "progressions": 8,
    "transits": 10
  },
  "major_transits": [
    {
      "transit_planet": "Saturn",
      "natal_planet": "Venus",
      "aspect": "square"
    }
  ]
}
```

**Notes**:
- Daily scores track cumulative astrological significance
- Used to identify high-importance periods
- Threshold: 40+ = highly significant, 25-39 = significant, 15-24 = notable

### Summary Object
```json
{
  "total_transits": 125,
  "by_planet": {
    "Saturn": 15,
    "Jupiter": 22,
    "Mars": 35,
    "Venus": 28,
    "Mercury": 25
  },
  "by_aspect": {
    "conjunction": 25,
    "sextile": 30,
    "square": 28,
    "trine": 27,
    "opposition": 15
  },
  "highest_score_day": {
    "date": "2025-11-03",
    "score": 52
  },
  "average_daily_score": 18.5
}
```

---

## Seed Data (Future)

**Location**: `/profiles/{name}/seed_data/seed_data.json`

**Purpose**: Complete natal chart calculations and interpretations for use by all interpretation agents.

**Status**: Schema to be defined after next seed data regeneration.

**Expected Structure** (based on current usage):
```json
{
  "profile": "string",
  "birth_data": { /* Birth data object */ },
  "planetary_positions": [ /* Array of planet objects */ ],
  "houses": [ /* Array of house objects */ ],
  "aspects": [ /* Array of aspect objects */ ],
  "dignities": { /* Dignity assessments */ },
  "lots": { /* Fortune, Spirit, etc. */ },
  "sect": { /* Day/night chart info */ },
  "profection_year": { /* Current profection */ },
  "chart_patterns": [ /* Grand trines, T-squares, etc. */ ]
}
```

**Note**: Will be documented fully after observing structure from next profile generation.

---

## RAG Database Format

**Location**: `/output/database/astrology_rag_database.jsonl`

**Purpose**: Semantic search database for traditional astrology interpretations (2,472 chunks from 6 reference books).

**Format**: JSON Lines (JSONL) - one JSON object per line

**Schema**:
```json
{
  "chunk_id": "brennan_hellenistic_001",
  "source": "Hellenistic Astrology: The Study of Fate and Fortune",
  "author": "Chris Brennan",
  "page": 125,
  "section": "Essential Dignities",
  "content": "The planet in its domicile...",
  "topics": ["dignities", "domicile", "rulership"],
  "embedding": [0.123, -0.456, 0.789, /* ... 1536 values ... */]
}
```

**Fields**:
- `chunk_id`: Unique identifier (source abbreviation + sequential number)
- `source`: Book title
- `author`: Book author
- `page`: Page number in source book
- `section`: Chapter or section heading
- `content`: Text content (200-1000 characters)
- `topics`: Keywords for filtering
- `embedding`: OpenAI embedding vector (1536 dimensions)

**Notes**:
- Each line is valid JSON (not one big JSON array)
- Load with: `[json.loads(line) for line in file]`
- 2,472 total chunks (as of 2025-10-11)

---

## Agent Communication Formats

### mode-orchestrator → Interpreter Agents

**Format**: Dictionary with interpretation parameters

**Example (Natal Interpretation)**:
```python
{
  "mode": "natal",
  "profile": "darren",
  "seed_data_path": "/profiles/darren/seed_data/seed_data.json",
  "output_path": "/profiles/darren/output/natal_horoscope_darren_2025-10-11.md",
  "settings": {
    "depth": "deep",
    "house_rulers": True,
    "lots": True,
    "psychological_overlay": True
  }
}
```

**Example (Life Arc Interpretation)**:
```python
{
  "mode": "life_arc",
  "profile": "dylan",
  "seed_data_path": "/profiles/dylan/seed_data/seed_data.json",
  "life_arc_data_path": "/profiles/dylan/output/life_arc_timeline_data.json",
  "output_path": "/profiles/dylan/output/life_arc_interpretation_dylan_ages_0-100.md",
  "age_range": {
    "start": 0,
    "end": 100
  }
}
```

**Example (Transit Interpretation - Multi-Movement)**:
```python
{
  "mode": "transit_short",
  "sub_mode": "multi_movement",
  "profile": "darren",
  "seed_data_path": "/profiles/darren/seed_data/seed_data.json",
  "transit_data_path": "/profiles/darren/output/transit_data_darren_2025-10-07_to_2025-11-06.json",
  "output_path": "/profiles/darren/output/transit_report_darren_short_2025-10-07_to_2025-11-06.md",
  "date_range": {
    "start": "2025-10-07",
    "end": "2025-11-06"
  }
}
```

**Example (Transit Interpretation - Period of Interest)**:
```python
{
  "mode": "transit_short",
  "sub_mode": "period_of_interest",
  "profile": "darren",
  "seed_data_path": "/profiles/darren/seed_data/seed_data.json",
  "transit_data_path": "/profiles/darren/output/transit_data_darren_2025-10-07_to_2025-11-06.json",
  "output_path": "/profiles/darren/output/transit_cluster_june2026_darren.md",
  "focus_date": "2026-06-15",
  "cluster_score": 52,
  "context": "Flagged from long-term report as high-convergence period"
}
```

---

## Date and Time Formats

### Standard Date Format
**Format**: ISO 8601 (`YYYY-MM-DD`)
**Examples**: `1992-10-25`, `2025-10-11`

### Standard Time Format
**Format**: 24-hour (`HH:MM:SS`)
**Examples**: `19:00:00`, `14:32:18`

### Datetime Format
**Format**: ISO 8601 with timezone (`YYYY-MM-DDTHH:MM:SS±HH:MM`)
**Examples**: `2025-10-11T14:32:18-04:00`

### Timezone Format
**Format**: IANA timezone identifier
**Examples**: `America/New_York`, `America/Chicago`, `Europe/London`

---

## Coordinate Formats

### Latitude
**Format**: Decimal degrees (-90 to 90)
**Convention**: Positive = North, Negative = South
**Examples**: `40.7128` (New York), `-33.8688` (Sydney)

### Longitude
**Format**: Decimal degrees (-180 to 180)
**Convention**: Positive = East, Negative = West
**Examples**: `-74.0060` (New York), `151.2093` (Sydney)

### Degree-Minute-Second (DMS)
**Format**: `D°M'S"` where D = degrees, M = minutes, S = seconds
**Examples**: `5°56'20"`, `25°27'36"`

---

## Validation Rules

### Profile Validation
- **Name**: Non-empty string
- **Date**: Valid date between 1800-01-01 and 2100-12-31 (Swiss Ephemeris range)
- **Time**: Valid 24-hour time (00:00 to 23:59)
- **Latitude**: -90 to 90
- **Longitude**: -180 to 180
- **Timezone**: Valid IANA timezone identifier

### Transit Data Validation
- **Start date < End date**: Always required
- **Date range**: Within ephemeris range (1800-2100)
- **Transit orb**: 0-10° (typically 6-8° for major aspects)
- **Score**: 0-10 per transit

### Life Arc Data Validation
- **Age range**: 0-100 (or subset)
- **Dates sequential**: Each technique's dates must be chronological
- **Profections**: Exactly 101 entries (ages 0-100)
- **ZR periods**: No gaps in coverage

---

## Common Errors and Fixes

### JSON Parse Errors
**Error**: `json.decoder.JSONDecodeError`
**Cause**: Invalid JSON structure
**Fix**: Validate with `python -m json.tool <file.json>`

### Missing Required Fields
**Error**: `KeyError: 'planetary_positions'`
**Cause**: Incomplete data structure
**Fix**: Regenerate data file with current schema

### Date Format Mismatch
**Error**: `ValueError: time data '10/25/1992' does not match format '%Y-%m-%d'`
**Cause**: Using non-ISO date format
**Fix**: Convert to ISO 8601 (`YYYY-MM-DD`)

### Timezone Issues
**Error**: `pytz.exceptions.UnknownTimeZoneError`
**Cause**: Invalid timezone identifier
**Fix**: Use IANA timezone (e.g., `America/New_York` not `EST`)

---

## Related Documentation

- **TROUBLESHOOTING.md**: Common issues with data files
- **DEVELOPMENT.md**: Profile creation and data generation workflows
- **SCRIPTS_REFERENCE.md**: Scripts that generate these data files
- **AGENTS_REFERENCE.md**: Agents that consume these data formats

---

*This data formats reference will be updated as new schemas are finalized and documented.*
