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

Generates: `/profiles/darren/seed_data/master_seed_data.yaml` or `seed_data.json`

**IMPORTANT WORKFLOW NOTE**:
- **seed_data_generator.py should be called EVERY TIME new birth data is entered**
- This ensures all astronomical calculations are fresh and accurate
- Interpretation agents (natal, life-arc, transit) require ONLY seed_data.json
- Agents do NOT require natal-interpreter or other interpreters to have run first
- Seed data is the single source of truth for all downstream interpretation

**Current Capabilities**:
- Basic natal chart data (planets, houses, aspects, sect)
- (Life arc calculations coming in next iteration)

**Data Formats**: See **[DATA_FORMATS.md](DATA_FORMATS.md)** for complete schemas:
- Profile formats (profile.txt and profile.md)
- Life arc timeline data structure
- Transit data structure
- Seed data structure (coming soon)
- RAG database format
- Agent communication formats

### 3. Agent-Based Synthesis

**Available Agents** (`.claude/agents/`):

For complete agent documentation, see **[AGENTS_REFERENCE.md](AGENTS_REFERENCE.md)** which includes:
- Complete agent catalog with capabilities and triggers
- Coordination patterns and handoffs
- When to use each agent
- Agent-to-agent communication protocols

**Key Interpretation Agents**:

**natal-interpreter**:
- Purpose: Generate natal horoscope synthesis
- Input: Seed data from `natal_interpretation_enhanced.md`
- Output: Markdown + PDF synthesis
- Style: Narrative prose, plain language

**life-arc-interpreter**:
- Purpose: Generate life timeline narratives
- Input: Life arc timeline data
- Output: Decades-long life story (ages 0-100)

**transit-analyzer-short**:
- Purpose: 1-4 month transit reports (multi-movement OR period-of-interest)
- Dual mode: Standard date range OR cluster analysis

**transit-analyzer-long**:
- Purpose: 1-5 year detailed transit analysis
- Structure: Chapter-based with convergence tracking

**Infrastructure Agents**:

**mode-orchestrator**:
- Purpose: Central routing for ALL interpretation requests
- Routes: Natal, Life Arc, Transit, Timing requests
- Validates: Profile and seed data before invoking interpreters

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

**astrology-output-debugger**:
- Purpose: Debug interpretation quality issues
- Investigates: Data inconsistency, missing sections, logic errors

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
4. Create PDF: `python scripts/pdf_generator.py input.md --report-type natal`

**All automated with**: "Create a natal horoscope for [person]"

### Generate PDF from Markdown

All astrology reports use the **external CSS system** for consistent formatting:

```bash
# Natal report (chart-based styling)
python scripts/pdf_generator.py profiles/name/output/natal_synthesis.md --report-type natal

# Life arc report (timeline-based styling)
python scripts/pdf_generator.py profiles/name/output/life_arc_synthesis.md --report-type life_arc

# Transit report (movement-based styling)
python scripts/pdf_generator.py profiles/name/output/transit_report.md --report-type transit
```

**Report Types**:
- `natal` - Loads base.css + chart_based.css
- `life_arc` - Loads base.css + timeline_based.css
- `transit` - Loads base.css + movement_based.css
- `event` - Loads base.css + movement_based.css (same as transit)

**CSS Files** (in `scripts/css/`):
- `base.css` - Universal styles (page setup, title pages, typography)
- `chart_based.css` - Natal horoscope specific styles
- `timeline_based.css` - Life arc specific styles
- `movement_based.css` - Transit/event specific styles

**See**: [OUTPUT_STYLE_GUIDE.md](OUTPUT_STYLE_GUIDE.md) for complete formatting standards

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

For complete agent workflows and coordination patterns, see **[WORKFLOWS_VISUAL.md](WORKFLOWS_VISUAL.md)** and **[AGENTS_REFERENCE.md](AGENTS_REFERENCE.md)**.

**When to use agents**:

1. **mode-orchestrator**: ALL interpretation requests (natal, life arc, transit)
2. **workflow-planner-2**: Planning features, architecture decisions, tool selection
3. **docs-updater-astrology**: After completing work, when docs need updating
4. **natal-interpreter**: Synthesizing natal horoscope from seed data (via mode-orchestrator)
5. **life-arc-interpreter**: Synthesizing life arc timeline narratives (via mode-orchestrator)
6. **transit-analyzer-short**: 1-4 month transit reports (via mode-orchestrator)
7. **transit-analyzer-long**: 1-5 year transit reports (via mode-orchestrator)
8. **astrology-rag-builder**: RAG database work, adding sources, quality control
9. **astrology-output-debugger**: Debug interpretation quality issues

**Agent invocation**: Use Task tool to launch agents (mode-orchestrator handles routing)

**Agent modification**: Synthesis agents (natal-interpreter, life-arc-interpreter, transit-analyzer) require user approval before changes

**Complete workflows**: See [WORKFLOWS_VISUAL.md](WORKFLOWS_VISUAL.md) for visual workflow diagrams

---

## Creating New Interpretation Agents

When creating new astrology interpretation agents, follow these standards:

### Required Agent Instructions

All interpretation agents MUST include these sections in their instructions:

1. **Output Format Standards**:
```
Follow OUTPUT_STYLE_GUIDE.md for all output:
- Two-file system: process.md (technical) + synthesis.pdf (narrative)
- Report structure templates based on type (Chart-Based, Timeline-Based, Movement-Based)
- Title page with metadata
- Voice standards (psychological depth, second-person, minimal jargon)
```

2. **PDF Generation**:
```
Generate PDF using external CSS system:
python scripts/pdf_generator.py output.md --report-type [natal|life_arc|transit|event]

Report types:
- natal: Chart-based reports (natal horoscopes)
- life_arc: Timeline-based reports (life arc timelines)
- transit: Movement-based reports (transit analysis)
- event: Movement-based reports (single event analysis)
```

3. **Astrological Systems Reference**:
```
See ASTROLOGY_REFERENCE.md for:
- Traditional systems (houses, dignities, aspects)
- Planetary meanings and conditions
- Timing techniques
Do NOT duplicate this content in agent instructions.
```

4. **Report Structure Template**:
Specify which template from OUTPUT_STYLE_GUIDE.md:
- **Template A**: Chart-Based (for natal/chart-focused reports)
- **Template B**: Timeline-Based (for life arc/decades reports)
- **Template C1**: Movement-Based with Chapters (for long transit reports)
- **Template C2**: Pure Movement-Based (for short transit/event reports)

### Agent Creation Checklist

- [ ] References OUTPUT_STYLE_GUIDE.md for formatting
- [ ] Specifies correct report type for PDF generation
- [ ] References ASTROLOGY_REFERENCE.md (not duplicating content)
- [ ] Includes title page generation instructions
- [ ] Specifies voice standards (psychological depth, therapeutic tone)
- [ ] Defines two-file output (process.md + synthesis.pdf)
- [ ] Uses appropriate report structure template

### Example Agent Instruction Block

```markdown
## Output Format

Follow [OUTPUT_STYLE_GUIDE.md](docs/OUTPUT_STYLE_GUIDE.md) standards:

**Report Type**: Timeline-Based (Template B)
**Structure**: ZR L1 chapters → H2 headings, convergence events → H3 subheadings
**Voice**: Psychological depth, second-person, minimal jargon
**Files**: life_arc_process.md (technical) + life_arc_synthesis.pdf (narrative)

## PDF Generation

Generate PDF with timeline-based styling:
```bash
python scripts/pdf_generator.py output.md --report-type life_arc
```

## Astrological Systems

See [ASTROLOGY_REFERENCE.md](docs/ASTROLOGY_REFERENCE.md) for:
- Traditional systems and dignities
- Timing techniques (profections, ZR, Firdaria)
- Planetary meanings
```

**For complete standards**: See [OUTPUT_STYLE_GUIDE.md](OUTPUT_STYLE_GUIDE.md)

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

For comprehensive troubleshooting, see **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** which covers:
- Profile issues (not found, missing fields)
- Seed data problems (missing, incomplete, schema mismatch)
- Calculation errors (Swiss Ephemeris, transits)
- Interpretation quality issues (data inconsistency, missing sections, jargon)
- RAG database problems (empty results, corruption)
- Output generation failures (reports not saved, terminal summary issues)
- Agent coordination issues (routing, triggering)
- PDF generation problems (missing title page, formatting)
- Complete debug workflows

### Quick Fixes

**ModuleNotFoundError**:
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**Profile not found**:
- Create with: `python scripts/create_profile.py --name <name> --date ... --time ... --location ...`

**Seed data not found**:
- Generate with: `python scripts/seed_data_generator.py --profile <name>`

**RAG database not found**:
- Verify `/output/database/astrology_rag_database.jsonl` exists
- Rebuild if needed: `python scripts/build_rag_database.py`

### Debug Mode

Set environment variables:
```bash
export DEBUG=1
python scripts/seed_data_generator.py --profile darren
```

For detailed troubleshooting procedures, consult [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

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
- `/docs/DATA_FORMATS.md` - Complete JSON schemas and data structures
- `/docs/TROUBLESHOOTING.md` - Common issues and debug workflows
- `/docs/AGENTS_REFERENCE.md` - Complete agent catalog with capabilities
- `/docs/SCRIPTS_REFERENCE.md` - Script documentation and usage
- `/docs/WORKFLOWS_VISUAL.md` - Visual workflow diagrams

**Reference Books** (in `/Referendces/`):
1. Hellenistic Astrology (Chris Brennan) - PRIMARY
2. Astrology and the Authentic Self (Demetra George)
3. Planets in Transit (Robert Hand)
4. Predictive Astrology (Bernadette Brady)
5. Delineation of Progressions (Sophia Mason)
6. The Horoscope in Manifestation (Liz Greene)

---

**Documentation Index**:
- **CURRENT_WORK.md** - Current focus and active work
- **REFERENCE.md** - Astrology systems and terminology
- **AGENTS_REFERENCE.md** - Complete agent catalog
- **SCRIPTS_REFERENCE.md** - Script documentation
- **DATA_FORMATS.md** - JSON schemas and data structures
- **TROUBLESHOOTING.md** - Common issues and fixes
- **WORKFLOWS_VISUAL.md** - Visual workflow diagrams
- **OUTPUT_STYLE_GUIDE.md** - Output format standards
- **README.md** - Project overview
