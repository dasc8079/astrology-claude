# Development Guide

This guide explains how to contribute to the astrology application project.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment activated
- Dependencies installed: `pip install -r requirements.txt`

### Key Dependencies

- `pyswisseph` (Swiss Ephemeris for astronomical calculations)
- `PyYAML` (YAML data handling)
- `pytz` (Timezone support)
- OpenAI API key (for RAG database embeddings)

### Environment Setup

1. Clone/access project at working directory
2. Activate virtual environment: `source venv/bin/activate`
3. Copy `.env.example` to `.env` and add your OpenAI API key
4. Verify installation: `python scripts/ephemeris_helper.py`

---

## Project Structure

```
/Users/darrenschaeffer/Documents/Claude/Astrogy_Claude/
├── CURRENT_WORK.md          # Current focus and active work
├── REFERENCE.md             # Static astrology knowledge
├── DEVELOPMENT.md           # This file - how to contribute
├── README.md                # Project overview
├── CLAUDE.md                # Complete system documentation (legacy)
├── docs/                    # Design documents and specifications
│   ├── session_goals.md     # North Star vision (workflow-planner-2)
│   ├── life_arc_report_design.md
│   └── seed_data_schema.yaml
├── history/                 # Archived completed stages
│   ├── STAGE_-1_RAG_Enhancement.md
│   ├── STAGE_0_Research_Timing.md
│   └── STAGE_1_Natal_Horoscope.md
├── scripts/                 # Python scripts
│   ├── astrology_reference.py    # Static reference data
│   ├── ephemeris_helper.py       # Swiss Ephemeris wrapper
│   ├── profile_loader.py         # Multi-profile support
│   ├── seed_data_generator.py    # Unified seed generator
│   ├── create_profile.py         # Profile creation
│   └── natal_interpreter.py      # Natal seed data
├── profiles/                # User profiles
│   ├── [name]/
│   │   ├── profile.md       # Birth data + settings
│   │   ├── seed_data/       # Generated seed data
│   │   └── output/          # Final outputs (PDF, markdown)
│   └── README.md
├── output/                  # RAG database and processing
│   └── database/
│       └── astrology_rag_database.jsonl
└── Referendces/             # Source PDFs (6 books)
```

---

## Documentation Hierarchy

**CURRENT_WORK.md** (30-50 lines)
- What's happening RIGHT NOW
- Current focus and active work
- Next immediate steps
- Files in progress

**REFERENCE.md** (Static knowledge)
- House systems, rulerships, dignities
- Aspects, sect, planetary conditions
- Immutable astrology reference

**DEVELOPMENT.md** (This file)
- How to contribute
- Project structure
- Development workflow
- Agent usage

**README.md** (Project overview)
- High-level description
- Installation instructions
- Quick start guide

**session_goals.md** (North Star)
- Long-term vision
- Strategic direction
- Technical approach
- Maintained by workflow-planner-2

**/history/** (Completed work)
- Archived stages
- Lessons learned
- Historical context

---

## Astrological Systems

**Traditional Foundation**:
- Whole-sign houses (each house = 30° sign)
- Traditional seven planets (Sun through Saturn)
- Classical aspects only (conjunction, sextile, square, trine, opposition)
- Hellenistic dignities (domicile, exaltation, triplicity, bounds, decans)
- Sect (day/night chart analysis)

**Modern Additions** (Secondary):
- Uranus, Neptune, Pluto (context only, never primary rulers)
- Chiron, Lilith (toggleable)
- Psychological analysis (Jungian depth)

**House System**: Whole-sign houses (WSH) exclusively

**Dignity Hierarchy**: Traditional only - no modern rulerships

---

## Development Workflow

### 1. Profile-Based System

All work centers on user profiles in `/profiles/[name]/`:

**Create New Profile**:
```bash
python scripts/create_profile.py --name "person" \
    --date "MM/DD/YYYY" \
    --time "HH:MM AM/PM" \
    --location "City, State" \
    --lat 40.7128 \
    --lon -74.0060 \
    --timezone "EST"
```

**Profile Settings** (in `profile.md`):
- `depth`: minimal | standard | deep | comprehensive
- `house_rulers`: true/false
- `lots`: basic | extended | full | false
- `technical_sections`: true/false (show technical analysis or synthesis only)

### 2. Seed Data Generation

**Unified Generator** (`scripts/seed_data_generator.py`):
```bash
python scripts/seed_data_generator.py --profile darren
```

Generates: `/profiles/darren/seed_data/master_seed_data.yaml`

**Current Capabilities**:
- Basic natal chart data (planets, houses, aspects, sect)
- (Life arc calculations coming in next iteration)

**Seed Data Structure**: See `/docs/seed_data_schema.yaml`

### 3. Agent-Based Synthesis

**Available Agents** (`.claude/agents/`):

**natal-interpreter**:
- Purpose: Generate natal horoscope synthesis
- Input: Seed data from `natal_interpretation_enhanced.md`
- Output: Markdown + PDF synthesis
- Style: Narrative prose, plain language

**workflow-planner-2**:
- Purpose: Technical advisor and architect
- Maintains: `session_goals.md`
- Role: Recommendations, not implementation

**docs-updater-astrology**:
- Purpose: Documentation maintenance
- Maintains: CURRENT_WORK.md, references to /docs/
- Updates: After major work, stage completion

**astrology-rag-builder**:
- Purpose: RAG database maintenance
- Database: 2,472 chunks from 6 sources
- Queries: Semantic search for interpretations

### 4. Testing

**Test Ephemeris Helper**:
```bash
python scripts/ephemeris_helper.py
```

**Test Astrology Reference**:
```bash
python scripts/astrology_reference.py
```

**Test Profile Loader**:
```bash
python -c "from scripts.profile_loader import get_default_profile; print(get_default_profile())"
```

---

## Common Tasks

### Generate Natal Horoscope

1. Create profile (if new): `create_profile.py`
2. Generate seed data: `natal_interpreter.py`
3. Invoke natal-interpreter agent for synthesis
4. Create PDF: `create_synthesis_pdf.py`

**All automated with**: "Create a natal horoscope for [person]"

### Query RAG Database

```bash
python scripts/query_rag_database.py "Mars square Saturn"
```

### Add New Reference Book

1. Place PDF in `/Referendces/`
2. Extract and chunk text (200-800 tokens)
3. Generate embeddings via OpenAI API
4. Add to `/output/database/astrology_rag_database.jsonl`
5. Use astrology-rag-builder agent

### Update Documentation

**Current work**: Update CURRENT_WORK.md manually or trigger docs-updater-astrology

**Static reference**: Update REFERENCE.md for astrology system changes

**Completed stages**: Archive to `/history/STAGE_N_Name.md`

---

## Agent Coordination

**When to use agents**:

1. **workflow-planner-2**: Planning features, architecture decisions, tool selection
2. **docs-updater-astrology**: After completing work, when docs need updating
3. **natal-interpreter**: Synthesizing natal horoscope from seed data
4. **astrology-rag-builder**: RAG database work, adding sources, quality control

**Agent invocation**: Use Task tool to launch agents

**Agent modification**: Synthesis agents (natal-interpreter, future life-arc agent) require user approval before changes

---

## Data Architecture

### Hybrid Approach

**Structured Seed Data** (YAML/JSON):
- Precise astronomical calculations
- Chart positions, aspects, dignities
- Deterministic lookups
- Location: `/profiles/[name]/seed_data/`

**RAG Database** (JSONL):
- Traditional interpretations
- Delineations from 6 reference books
- Semantic search for synthesis
- Location: `/output/database/`

**Chat Interface** (Future):
- Queries BOTH structured seed + RAG interpretations
- Combines facts with traditional wisdom

### Incremental Integration

As new modes are added (natal → life arc → transits), the unified seed generator expands:

1. **Stage 1** (DONE): Basic natal seed
2. **Stage 2** (IN PROGRESS): Life arc calculations
3. **Stage 3** (FUTURE): Transit data
4. **Stage 4** (FUTURE): Additional timing techniques

All data consolidated in `master_seed_data.yaml` per profile.

---

## Code Style

### Python

- Use type hints
- Follow PEP 8
- Document functions with docstrings
- Use `Optional[Type]` for nullable parameters
- Prefer explicit over implicit
- Use helper modules: `astrology_reference.py`, `ephemeris_helper.py`, `profile_loader.py`

### Astrology Notation

**Standard forms** (use controlled vocabulary):
- Planets: Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn
- Signs: Aries, Taurus, ..., Pisces
- Houses: 1-12 (integers)
- Aspects: conjunction, sextile, square, trine, opposition
- Dignities: domicile, exaltation, detriment, fall, triplicity, bounds, decans

**Symbols converted to text**:
- ☉ → Sun, ☽ → Moon, ♂ → Mars, ♀ → Venus, etc.
- ♈ → Aries, ♉ → Taurus, ♊ → Gemini, etc.
- △ → trine, □ → square, ☍ → opposition

---

## Quality Control

### Validation Checklist

- [ ] Birth data accurate (date, time, location, coordinates)
- [ ] Planetary positions verified against ephemeris
- [ ] Dignities calculated correctly (domicile, exaltation, triplicity, bounds, decans)
- [ ] Aspects computed with correct orbs
- [ ] Sect determination correct (Sun above/below horizon)
- [ ] House rulers identified accurately
- [ ] Lots calculated using correct formulas (day vs night chart)
- [ ] Interpretations grounded in RAG database sources
- [ ] Citations include source, author, page numbers
- [ ] Output format matches template (markdown + PDF)

### Testing New Features

1. Test with Darren's profile first (default profile)
2. Verify calculations against known chart data
3. Cross-reference interpretations with source books
4. Check PDF generation and formatting
5. Validate YAML/JSON output structure

---

## Troubleshooting

### Common Issues

**ModuleNotFoundError**:
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**KeyError in chart data**:
- Check chart_analyzer output structure
- Verify keys exist before access
- Use `get()` method with defaults

**Ephemeris calculation errors**:
- Verify date is within ephemeris range (1800-2400 CE typically)
- Check coordinates are valid (lat: -90 to 90, lon: -180 to 180)
- Ensure timezone is correct

**RAG database not found**:
- Verify `/output/database/astrology_rag_database.jsonl` exists
- Check OpenAI API key in `.env` file
- Rebuild database if corrupted

### Debug Mode

Set environment variables:
```bash
export DEBUG=1
python scripts/seed_data_generator.py --profile darren
```

---

## Contributing Guidelines

1. **Check CURRENT_WORK.md** for active focus
2. **Read session_goals.md** for strategic direction
3. **Test with default profile** (Darren) first
4. **Use helper modules** (don't reinvent the wheel)
5. **Document as you go** (update CURRENT_WORK.md)
6. **Archive completed stages** to `/history/`
7. **Ground interpretations in sources** (cite book, page)
8. **Respect traditional foundation** (modern additions clearly marked)
9. **Get approval for agent changes** (especially synthesis agents)
10. **Update docs-updater-astrology** when major work completes

---

## Resources

**Key Scripts**:
- `astrology_reference.py` - Static reference data module
- `ephemeris_helper.py` - Swiss Ephemeris wrapper
- `profile_loader.py` - Multi-profile utilities
- `query_rag_database.py` - RAG database search

**Key Documents**:
- `session_goals.md` - North Star vision
- `REFERENCE.md` - Astrology systems used
- `/docs/seed_data_schema.yaml` - Complete data structure
- `/docs/life_arc_report_design.md` - Life arc system design

**Reference Books** (in `/Referendces/`):
1. Hellenistic Astrology (Chris Brennan) - PRIMARY
2. Astrology and the Authentic Self (Demetra George)
3. Planets in Transit (Robert Hand)
4. Predictive Astrology (Bernadette Brady)
5. Delineation of Progressions (Sophia Mason)
6. The Horoscope in Manifestation (Liz Greene)

---

*For current work status, see CURRENT_WORK.md*
*For astrology reference, see REFERENCE.md*
*For project overview, see README.md*
