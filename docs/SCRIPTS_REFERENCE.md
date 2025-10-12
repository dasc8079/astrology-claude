# Scripts Reference

**Purpose**: Complete reference for all Python scripts in the project

**Last Updated**: 2025-10-11

**Location**: `/scripts/` directory

---

## Quick Reference Table

| Script | Purpose | When to Use | Agent Alternative |
|--------|---------|-------------|-------------------|
| seed_data_generator.py | Generate natal chart calculations | **Always first** - before any interpretation | None - required |
| transit_calculator.py | Calculate transits for date range | Need transit data | mode-orchestrator does this |
| life_arc_generator.py | Generate lifetime timeline data | Need life arc data | mode-orchestrator does this |
| pdf_generator.py | Convert markdown to PDF | Want professional PDF output | Agents offer this |
| profile_loader.py | Load profile data | Testing/debugging | Agents use this |

---

## Core Data Generation Scripts

### seed_data_generator.py

**Purpose**: Generate complete natal chart calculations (the single source of truth for all interpretations)

**When to Use**:
- **EVERY TIME** new birth data is entered
- Before any natal, life arc, or transit analysis
- When updating profile settings

**What It Generates**:
- Planetary positions (longitude, latitude, speed, retrograde status)
- House cusps (whole-sign + other systems)
- Dignities (domicile, exaltation, triplicity, bounds, decans)
- Aspects (classical aspects with orbs)
- Sect determination (day/night chart)
- Lots (Fortune, Spirit, + 8 others)
- House rulers

**Usage**:
```bash
python scripts/seed_data_generator.py --profile darren
```

**Output**: `/profiles/darren/seed_data/seed_data.json`

**Dependencies**: pyswisseph, profile data

**Note**: This is the FIRST step for any new profile. Everything else depends on this file.

---

### transit_calculator.py

**Purpose**: Calculate all transits for a specified date range with quality scoring

**When to Use**:
- Need transit data for transit reports
- Want to analyze specific time period
- Comparing different date ranges

**What It Calculates**:
- All planetary transits to natal planets (applying → exact → separating)
- Transit aspects (conjunction, sextile, square, trine, opposition)
- Retrograde loops and stations
- Daily quality scoring (summation of all active transits)
- Peak/low period detection
- Most auspicious/challenging days
- Timing lord integration (Profections, ZR, Firdaria)

**Usage**:
```bash
# Short report (1-4 months): All planets, all tiers
python scripts/transit_calculator.py --profile darren --start-date 2025-10-01 --end-date 2026-01-31 --report-type short

# Long report (1-5 years): Slower planets, CRITICAL tier only
python scripts/transit_calculator.py --profile darren --start-date 2025-10-01 --end-date 2030-10-01 --report-type long
```

**Output**: `/profiles/darren/output/transit_data_darren_{start}_to_{end}.json`

**Dependencies**: seed_data.json, pyswisseph, timing technique data

**Note**: mode-orchestrator runs this automatically when you request transit reports.

---

### life_arc_generator.py

**Purpose**: Generate unified lifetime timeline combining all timing techniques with convergence detection

**When to Use**:
- Need life arc timeline data
- Want to see all timing techniques combined
- Analyzing specific age range

**What It Generates**:
- **5 Core Timing Techniques**:
  - Annual Profections (12-year cycles)
  - Zodiacal Releasing Fortune & Spirit L1 (major chapters)
  - Firdaria (75-year Persian cycle)
  - Planetary Returns (Jupiter, Saturn, Uranus opposition)
  - Progressed Sun Sign Changes (every ~30 years)
- **Convergence Detection**: Flags when multiple techniques align (MAJOR = 25+ points)
- **Timeline Events**: Every significant timing activation from birth to age 100

**Usage**:
```bash
python scripts/life_arc_generator.py --profile darren --start-age 0 --end-age 100
```

**Output**: `/profiles/darren/output/life_arc_data_darren_ages_{start}-{end}.json`

**Dependencies**: seed_data.json, pyswisseph

**Note**: mode-orchestrator runs this automatically when you request life arc reports.

---

## Timing Technique Scripts

### profections_calculator.py

**Purpose**: Calculate annual profections (12-year house activation cycle)

**When to Use**:
- Want to see profection years
- Need Lord of Year for specific age
- Understanding which house is activated each year

**What It Calculates**:
- Profection house for each age
- Lord of Year (ruler of profection house)
- Time Lord periods

**Usage**:
```bash
python scripts/profections_calculator.py --profile darren --start-age 0 --end-age 100
```

**Output**: JSON data with profection info

**See**: [PROFECTIONS_GUIDE.md](PROFECTIONS_GUIDE.md)

---

### zodiacal_releasing.py

**Purpose**: Calculate Zodiacal Releasing (ZR) periods for Fortune and Spirit

**When to Use**:
- Need ZR Fortune periods (external life chapters)
- Need ZR Spirit periods (internal identity chapters)
- Want to see L1/L2/L3 sub-periods

**What It Calculates**:
- Fortune L1 (8-30 year periods)
- Fortune L2 (1-3 year sub-periods)
- Fortune L3 (1-5 month sub-periods)
- Spirit L1, L2, L3 (same structure)
- Peak periods (when L2=L1 or L3=L1)
- Loosing of the bond events

**Usage**:
```bash
python scripts/zodiacal_releasing.py --profile darren --start-date 1988-12-27 --end-date 2088-12-27
```

**Output**: JSON data with ZR periods

**See**: [ZODIACAL_RELEASING_GUIDE.md](ZODIACAL_RELEASING_GUIDE.md)

---

### firdaria_calculator.py

**Purpose**: Calculate Firdaria (Persian 75-year planetary period system)

**When to Use**:
- Want to see Firdaria major periods
- Need sub-period timing
- Understanding planetary time-lord rulerships

**What It Calculates**:
- Major periods (7-10 years each)
- Sub-periods within major periods
- Sect-based ordering (day/night charts have different sequences)

**Usage**:
```bash
python scripts/firdaria_calculator.py --profile darren --start-age 0 --end-age 75
```

**Output**: JSON data with Firdaria periods

**See**: [firdaria_reference.md](firdaria_reference.md)

---

### secondary_progressions.py

**Purpose**: Calculate secondary progressions (day-for-year technique)

**When to Use**:
- Want progressed planetary positions
- Need progressed aspects
- Optional timing technique (not emphasized in reports)

**What It Calculates**:
- Progressed Sun, Moon, Mercury, Venus, Mars positions
- Progressed aspects to natal chart
- Progressed house cusps

**Usage**:
```bash
python scripts/secondary_progressions.py --profile darren --target-age 36
```

**Output**: JSON data with progression info

**See**: [SECONDARY_PROGRESSIONS_GUIDE.md](SECONDARY_PROGRESSIONS_GUIDE.md)

---

### solar_returns.py

**Purpose**: Calculate solar return charts (annual charts when Sun returns to natal position)

**When to Use**:
- Want annual solar return charts
- Analyzing specific year's themes
- Optional timing technique (not emphasized in reports)

**What It Calculates**:
- Complete chart for moment Sun returns to natal degree
- Return chart planetary positions
- Return chart houses

**Usage**:
```bash
python scripts/solar_returns.py --profile darren --year 2025
```

**Output**: JSON data with solar return chart

**See**: [SOLAR_RETURNS_GUIDE.md](SOLAR_RETURNS_GUIDE.md)

---

## Output Generation Scripts

### pdf_generator.py

**Purpose**: Convert markdown reports to professionally styled PDFs

**When to Use**:
- After generating markdown report
- Want print-ready output
- Need professional presentation

**What It Does**:
- Loads appropriate CSS based on report type
- Converts markdown to HTML
- Generates PDF with proper typography
- Handles page breaks, title pages, table formatting

**Usage**:
```bash
# Natal report (chart-based styling)
python scripts/pdf_generator.py input.md --report-type natal

# Life arc report (timeline-based styling)
python scripts/pdf_generator.py input.md --report-type life_arc

# Transit report (movement-based styling)
python scripts/pdf_generator.py input.md --report-type transit

# Auto-detect output filename
python scripts/pdf_generator.py input.md --report-type natal --output auto
```

**CSS Files Used**:
- `scripts/css/base.css` - Universal styles (always loaded)
- `scripts/css/chart_based.css` - Natal horoscopes
- `scripts/css/timeline_based.css` - Life arc reports
- `scripts/css/movement_based.css` - Transit/event reports

**Output**: PDF file with `.pdf` extension

**Dependencies**: WeasyPrint, markdown library

**See**: [OUTPUT_STYLE_GUIDE.md](OUTPUT_STYLE_GUIDE.md)

---

## Utility Scripts

### profile_loader.py

**Purpose**: Load and validate profile data (used by other scripts and agents)

**When to Use**:
- Testing profile data loading
- Debugging profile issues
- Validating profile structure

**What It Does**:
- Loads profile.md
- Parses birth data
- Validates settings
- Returns structured profile object

**Usage**:
```python
from profile_loader import load_profile
profile = load_profile("darren")
```

**Output**: Python dictionary with profile data

**Note**: This is primarily used internally by other scripts/agents.

---

## Analysis & Testing Scripts

### test_convergence.py

**Purpose**: Test convergence detection algorithm with sample data

**When to Use**:
- Testing convergence scoring logic
- Debugging convergence detection
- Understanding point-based scoring

**What It Does**:
- Runs convergence detection on test timeline
- Shows which events are flagged as MAJOR/SIGNIFICANT/NOTABLE
- Validates scoring algorithm

**Usage**:
```bash
python scripts/test_convergence.py
```

**Output**: Console output showing convergence test results

---

### saturn_periods_comparison.py

**Purpose**: Compare transit data across different Saturn periods (return, square, etc.)

**When to Use**:
- Comparing different life periods
- Analyzing Saturn cycle phases
- Research/testing purposes

**What It Does**:
- Generates transit data for multiple periods
- Compares statistical measures
- Identifies patterns across periods

**Usage**:
```bash
python scripts/saturn_periods_comparison.py --profile darren
```

**Output**: Comparison analysis report

**Note**: This was created for specific comparative analysis. General transit comparison should use transit_calculator.py with different date ranges.

---

## Synthesis Scripts (Simplified Versions)

### transit_synthesis_simplified.py

**Purpose**: Generate simplified transit synthesis without full agent invocation (testing)

**When to Use**:
- Testing transit synthesis logic
- Quick transit report without RAG database
- Debugging transit interpretation flow

**What It Does**:
- Loads transit data JSON
- Generates basic narrative synthesis
- No RAG queries (template-based only)

**Usage**:
```bash
python scripts/transit_synthesis_simplified.py --profile darren --transit-file transit_data.json
```

**Output**: Basic transit synthesis markdown

**Note**: For production use, use transit-analyzer agents through mode-orchestrator instead.

---

## Legacy/Deprecated Scripts

### generate_dylan_synthesis.py

**Purpose**: Legacy profile-specific script (archived)

**Status**: Deprecated - use seed_data_generator.py + agents instead

---

### transit_report_long.py

**Purpose**: Legacy transit report generator (archived)

**Status**: Deprecated - use transit_calculator.py + transit-analyzer-long agent instead

---

### transits.py

**Purpose**: Old transit calculation script (archived)

**Status**: Deprecated - use transit_calculator.py instead

---

### analyze_long_transit_report.py

**Purpose**: Legacy analysis script (archived)

**Status**: Deprecated - use astrology-output-debugger agent instead

---

## Script Execution Order

### For New Profile:
```
1. Create profile: manual or create_profile.py (if that script exists)
2. Generate seed data: seed_data_generator.py --profile {name}
3. Request interpretation via mode-orchestrator
```

### For Transit Report:
```
1. Ensure seed data exists
2. Ask mode-orchestrator for transit report
   → It runs transit_calculator.py automatically
   → It invokes appropriate transit analyzer agent
   → It offers PDF generation
```

### For Life Arc Report:
```
1. Ensure seed data exists
2. Ask mode-orchestrator for life arc report
   → It runs life_arc_generator.py automatically
   → It invokes life-arc-interpreter agent
   → It offers PDF generation
```

---

## When to Use Scripts vs. Agents

**Use Scripts Directly When**:
- Generating seed data (seed_data_generator.py) - always required first step
- Testing/debugging data generation
- Researching specific calculations
- Batch processing multiple profiles

**Use Agents (via mode-orchestrator) When**:
- Want interpretations/narratives
- Need complete reports
- Having conversational interaction
- Want quality-assured output with RAG integration

**Golden Rule**: For interpretations, always use mode-orchestrator. It will run the necessary scripts automatically.

---

## Related Documentation

- **Agent reference**: [AGENTS_REFERENCE.md](AGENTS_REFERENCE.md)
- **Agent orchestration**: [AGENT_ORCHESTRATION_GUIDE.md](AGENT_ORCHESTRATION_GUIDE.md)
- **Data formats**: [DATA_FORMATS.md](DATA_FORMATS.md) (see JSON structures)
- **Development workflow**: [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md)
- **Output styling**: [OUTPUT_STYLE_GUIDE.md](OUTPUT_STYLE_GUIDE.md)

---

**Remember**: mode-orchestrator is your interface for interpretations. It manages script execution automatically.
