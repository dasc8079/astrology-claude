# Astrology RAG Database & Application Project

**Navigation Hub** - For detailed documentation, see the links below.

---

## Quick Start

**Current Work**: See [CURRENT_WORK.md](CURRENT_WORK.md) for what's happening RIGHT NOW

**Vision & Plans**: See [session_goals.md](docs/session_goals.md) for North Star vision and future plans

**Project History**: See [/history/](history/) for archived completed stages

**Design Documents**: See [/docs/](docs/) for detailed specifications and implementation plans

**Reference Guides**:
- [ASTROLOGY_REFERENCE.md](docs/ASTROLOGY_REFERENCE.md) - Astrology systems and terminology
- [OUTPUT_STYLE_GUIDE.md](docs/OUTPUT_STYLE_GUIDE.md) - Output format standards for all report types
- [DEVELOPMENT_GUIDE.md](docs/DEVELOPMENT_GUIDE.md) - Development workflow and agent creation
- [DATA_FORMATS.md](docs/DATA_FORMATS.md) - Complete JSON schemas and data structures
- [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) - Common issues and debug workflows

**Operational Guides**:
- [AGENT_ORCHESTRATION_GUIDE.md](docs/AGENT_ORCHESTRATION_GUIDE.md) - How to use mode-orchestrator and astrology-output-debugger
- [PROFILES_GUIDE.md](docs/PROFILES_GUIDE.md) - Profile creation and management
- [TRANSITS_GUIDE.md](docs/TRANSITS_GUIDE.md) - Transit concepts and usage
- [LIFE_ARC_GUIDE.md](docs/LIFE_ARC_GUIDE.md) - Life arc timeline generation and interpretation
- [AGENTS_REFERENCE.md](docs/AGENTS_REFERENCE.md) - Complete agent catalog with capabilities
- [SCRIPTS_REFERENCE.md](docs/SCRIPTS_REFERENCE.md) - Script documentation and usage
- [WORKFLOWS_VISUAL.md](docs/WORKFLOWS_VISUAL.md) - Visual workflow diagrams

**Timing Techniques Guides**:
- [PROFECTIONS_GUIDE.md](docs/PROFECTIONS_GUIDE.md) - Annual profections system
- [ZODIACAL_RELEASING_GUIDE.md](docs/ZODIACAL_RELEASING_GUIDE.md) - Zodiacal Releasing (Fortune/Spirit, L1/L2/L3)
- [firdaria_reference.md](docs/firdaria_reference.md) - Firdaria timing system (Persian time-lords)
- [SECONDARY_PROGRESSIONS_GUIDE.md](docs/SECONDARY_PROGRESSIONS_GUIDE.md) - Secondary progressions
- [SOLAR_RETURNS_GUIDE.md](docs/SOLAR_RETURNS_GUIDE.md) - Solar return charts

---

## Project Overview

This project creates a comprehensive traditional/Hellenistic astrology application powered by a RAG (Retrieval-Augmented Generation) database. The system generates birth chart interpretations, life timelines, and transit analysis using authentic astrological methods from authoritative reference sources.

### Core Capabilities

**RAG Database**:
- 2,472 semantic chunks from 6 authoritative traditional astrology sources
- OpenAI embeddings for semantic search
- Source attribution and cross-reference validation
- Query-optimized for chart interpretation, dignities, aspects, and timing techniques

**Application Modes**:
1. **Mode 1: Natal Horoscope Generator** ✅ COMPLETE - Birth chart psychological profiles with PDF output (Opus model)
2. **Mode 2: Life Arc Report Generator** ✅ COMPLETE - Life timeline from birth to age 100 with convergence detection (Opus model)
3. **Mode 3: Transit Report Generator** ✅ COMPLETE - Short-term (1-4 months) and long-term (1-5 years) transit analysis (Opus model)
4. **Mode 4+: Additional Timing Techniques** ⏳ PENDING - Additional predictive techniques

**Rolling Chat Interfaces** (Future):
- Horoscope Inquirer: Deep-dive natal chart questions
- Transit/Advice Chatbot: Transit-specific guidance

---

## Mode Status Table

| Mode | Name | Status | Model | Notes |
|------|------|--------|-------|-------|
| 1 | Natal Horoscope | ✅ COMPLETE | Opus | Multi-profile, standardized file structure, PDF output |
| 2 | Life Arc Report | ✅ COMPLETE | Opus | Ages 0-100, convergence detection, narrative chapters |
| 3 | Transit Report | ✅ COMPLETE | Opus | Short-term (1-4 months) and long-term (1-5 years) analysis |
| 4+ | Additional Timing | ⏳ PENDING | TBD | Modular timing techniques (profections, ZR, Firdaria built) |

**Legend**: ✅ Complete | ⏳ Pending

See [CURRENT_WORK.md](CURRENT_WORK.md) for detailed status and next steps.

---

## Technical Stack

**Runtime**: Python 3.x
**Astronomical Calculations**: Swiss Ephemeris (pyswisseph v2.10.3.2)
**Knowledge Base**: RAG database (2,472 chunks from 6 traditional sources)
**Embeddings**: OpenAI API (embeddings only, not for LLM calls)
**Interpretation Agents**: Claude Code agents (natal-interpreter, life-arc-interpreter, transit-analyzer planned)
**House System**: Whole-sign houses (traditional/Hellenistic)
**Planetary Set**: Traditional Seven (Sun through Saturn) primary; modern planets (Uranus, Neptune, Pluto) secondary
**Aspects**: Classical only (conjunction, sextile, square, trine, opposition)
**Storage**: Local files, JSONL vector database
**Output**: Markdown reports + PDF generation (external CSS system with report-type styling)
**PDF System**: WeasyPrint with modular CSS (base.css + type-specific styles)

**Migration Path**: Agent instructions serve as approved "prompts"; can migrate to GPT-5 API later if desired.

---

## Project Agents

**Planning & Documentation**:
- `workflow-planner-2` - Expert advisor for architecture, tools, and technical recommendations
- `feature-designer-astrology` - Conversational feature design and specification creation
- `docs-updater-astrology` - Documentation maintainer (CURRENT_WORK.md, CLAUDE.md, /history/)

**Agent Creation**:
- `astrology-agent-creator` - Creates astrology interpretation agents with OUTPUT_STYLE_GUIDE.md template extraction

**RAG Database**:
- `astrology-rag-builder` - RAG database maintenance, queries, normalization
- `astrology-output-debugger` - Debug interpretation issues, data quality, workflow problems

**Quality Assurance**:
- `accuracy-checker` - Automated quality verification for interpretation outputs

**Orchestration**:
- `mode-orchestrator` - Central coordinator routing all astrology interpretation requests (Mode 1-4+)

**Interpretation & Synthesis**:
- `natal-interpreter` - Natal chart synthesis using traditional Hellenistic methods (Mode 1)
- `life-arc-interpreter` - Life timeline synthesis (Mode 2)
- `transit-analyzer-long` - Long-term transit reports, 1-5 years (Mode 3 Level 1)
- `transit-analyzer-short` - Short-term transit reports, 1-4 months (Mode 3 Level 2)

**Formatting & Output**:
- `pdf-formatter` - Formats plain markdown reports into professional PDFs with report-specific Chart Overview templates

**IMPORTANT**: When creating new interpretation agents, update `mode-orchestrator.md` to add routing logic. astrology-agent-creator automatically invokes docs-updater-astrology. See [AGENT_ORCHESTRATION_GUIDE.md](docs/AGENT_ORCHESTRATION_GUIDE.md) for details.

**Complete Agent Catalog**: See [AGENTS_REFERENCE.md](docs/AGENTS_REFERENCE.md) for detailed agent documentation.

See [.claude/agents/](.claude/agents/) for individual agent configuration files.

---

## Reference Materials

### Authoritative Sources (6 books, 2,472 chunks)

Located in `/References/` folder:

1. **Hellenistic Astrology: The Study of Fate and Fortune** (Chris Brennan) - Foundation text
2. **Astrology and the Authentic Self** (Demetra George) - Integration methods
3. **Planets in Transit: Life Cycles for Living** (Robert Hand) - Predictive techniques
4. **Predictive Astrology: The Eagle and the Lark** (Bernadette Brady) - Timing systems
5. **Delineation of Progressions** (Sophia Mason) - Progression specifics
6. **The Horoscope in Manifestation** (Liz Greene) - Horoscope writing methodology

**RAG Database**: `/output/database/astrology_rag_database.jsonl`

See [/docs/ASTROLOGY_REFERENCE.md](docs/ASTROLOGY_REFERENCE.md) for detailed astrology systems reference.

---

## User Profiles & Data

**Location**: `/profiles/` directory with multi-profile support

**Standardized Profile Structure** (v1.0 - Oct 2025):
```
profiles/
├── FirstName_LastInitial/         # Capitalized, underscore separator
│   ├── profile.md                 # Birth data + interpretation settings
│   ├── seed_data/
│   │   └── seed_data.json         # Complete astronomical calculations
│   └── output/                    # ALL generated reports
│       ├── natal_process_*.md     # Technical analysis
│       ├── natal_synthesis_*.md   # Accessible narrative (markdown)
│       ├── natal_synthesis_*.pdf  # Professional PDF (primary deliverable)
│       ├── life_arc_*             # Life timeline reports
│       └── transit_*              # Transit analysis reports
```

**Active Profiles**:
- `Darren_S/` - Complete: natal, life arc (0-100), transits
- `Sam_P/` - Natal horoscope
- Additional profiles available

**Naming Convention**:
- Format: `FirstName_LastInitial` (e.g., `Darren_S`, `Sam_P`, `Elizabeth_M`)
- Capitalized first name and last initial
- Underscore separator (no spaces)
- Consistent across all file names within profile

**Settings System**: Each `profile.md` contains customizable interpretation settings:
- Traditional techniques (house rulers, lots, nodes, receptions, bonification)
- Modern methods (Lilith, Chiron, psychological overlays - optional)
- Timing techniques (firdaria, progressions, solar returns)
- Output preferences (depth, citations, technical sections)

**Complete Documentation**: See [docs/PROFILE_STRUCTURE.md](docs/PROFILE_STRUCTURE.md) for detailed standards, migration guide, and validation checklist.

---

## Swiss Ephemeris Integration

**Helper Script**: `/scripts/ephemeris_helper.py`
**Library**: pyswisseph v2.10.3.2 (installed in project venv)

**Capabilities**:
- Planetary positions (traditional seven + modern planets)
- House calculations (whole-sign primary, multiple systems supported)
- Aspect calculations (classical aspects only)
- Transit calculations
- Eclipse dates
- Date/time conversions (Julian day, UTC handling)

**Key Functions**:
```python
get_planetary_positions(dt, utc=True, include_modern=True)
calculate_houses(dt, latitude, longitude, house_system='W', utc=True)
calculate_aspect(long1, long2, orb=8.0)
calculate_transit(natal_position, transit_date, planet, utc=True)
get_eclipse_dates(start_date, num_eclipses=5, eclipse_type='lunar')
```

See `/scripts/ephemeris_helper.py` for complete API reference and examples.

---

## Output Structure

**Reports Folder**: `/reports/` (not tracked in git - local output only)

**Generated Files**:
- Natal horoscopes: `/reports/natal/`
- Life arc reports: `/reports/life_arc/` (in development)
- Transit reports: `/reports/transits/` (planned)

**Format**: Markdown + PDF with professional typography

---

## Astrological Systems

This project adheres strictly to traditional/Hellenistic astrological systems:

**House System**: Whole-sign houses (WSH) - each house spans one complete zodiacal sign
**Rulerships**: Traditional only (no modern rulerships)
**Dignities**: Domicile, exaltation, detriment, fall, triplicity, bounds/terms, decans/faces
**Sect**: Day/night chart analysis with sect light and benefic/malefic of sect
**Aspects**: Classical only - conjunction (0°), sextile (60°), square (90°), trine (120°), opposition (180°)
**Planetary Set**: Traditional Seven primary (Sun through Saturn); modern planets (Uranus, Neptune, Pluto) secondary context only

See [/docs/ASTROLOGY_REFERENCE.md](docs/ASTROLOGY_REFERENCE.md) for complete astrological systems reference.

---

## Navigation Index

**Current Work & Status**:
- [CURRENT_WORK.md](CURRENT_WORK.md) - What's happening RIGHT NOW (30-50 lines)
- [session_goals.md](docs/session_goals.md) - North Star vision and future plans (150-500 lines)

**Project History**:
- [/history/](history/) - Archived completed stages
- [/history/index.md](history/index.md) - History index with stage summaries

**Design & Specifications**:
- [/docs/single_event_design.md](docs/single_event_design.md) - Single Event Analysis design (Mode 3 Level 3)
- [/docs/FUTURE_ENHANCEMENTS.md](docs/FUTURE_ENHANCEMENTS.md) - Deferred features and future improvements

**Archived Design Documents** (see /docs/archive/design/):
- life_arc_report_design.md - Life Arc Report design (105+ pages)
- timing_techniques_plan.md - Timing techniques plan (25+ pages)
- transit_interpretation_design.md - Transit design
- transit_staged_implementation.md - Transit implementation plan

**Static Documentation**:
- [ASTROLOGY_REFERENCE.md](docs/ASTROLOGY_REFERENCE.md) - Astrological systems and terminology (rarely updated)
- [DEVELOPMENT_GUIDE.md](docs/DEVELOPMENT_GUIDE.md) - Contributor guide and development workflow (rarely updated)
- [OUTPUT_STRUCTURE.md](docs/OUTPUT_STRUCTURE.md) - File organization and naming conventions
- [README.md](README.md) - Project overview and installation

**Agents**:
- [.claude/agents/](.claude/agents/) - Individual agent configuration files

**Scripts & Tools**:
- [/scripts/](scripts/) - Automation scripts (profile creation, PDF generation, ephemeris helper)

**Output** (local only):
- [/reports/](reports/) - Generated horoscopes and reports (not in git)
- [/output/](output/) - RAG database and assessments

---

## Environment & Configuration

**Python Environment**: Virtual environment with pyswisseph, openai, reportlab, markdown
**MCP Servers**: context7 (library docs), filesystem (file operations), github (repo operations)
**Allowed Directories**: Project root, /Users/darrenschaeffer/.claude/agents/, iCloud sync paths

See [/docs/DEVELOPMENT_GUIDE.md](docs/DEVELOPMENT_GUIDE.md) for setup instructions and development workflow.

---

## Automated Horoscope Workflow

**Command**: `python scripts/horoscope_generator.py --profile <name>`

**Steps**:
1. Load profile from `/profiles/<name>/profile.txt`
2. Generate astronomical seed data (`seed_data.json`)
3. Invoke natal-interpreter agent for synthesis
4. Extract synthesis to markdown
5. Generate professional PDF output

**Modes**:
- Mode 1: Natal horoscope ✅ (complete)
- Mode 2: Life arc report ✅ (complete - enhanced with convergence detection)
- Mode 3: Transit report ⏳ (ready to implement)

See [/docs/DEVELOPMENT_GUIDE.md](docs/DEVELOPMENT_GUIDE.md) for detailed workflow documentation.

---

## Archive Notice

**Previous CLAUDE.md**: The original 89KB (2,705 lines) detailed documentation has been archived to [/history/CLAUDE_ARCHIVE_2025_10_06.md](history/CLAUDE_ARCHIVE_2025_10_06.md).

**New Structure**: This file is now a navigation hub (~10KB) pointing to current work, design documents, and project history. Detailed technical content has been relocated to appropriate documentation files.

---

## Version & Updates

**Last Updated**: 2025-10-07
**Framework**: Global Claude Code documentation structure (CLAUDE.md as navigation hub)
**Maintained By**: docs-updater-astrology agent

**Update Triggers**:
- New modes added
- New agents created
- Major architectural changes
- File exceeds 10KB (archive old content to /history/)

---

## Contact & Support

For questions about this project or to report issues, see the project repository or contact the project owner.

**Documentation Issues**: Update [CURRENT_WORK.md](CURRENT_WORK.md), [session_goals.md](docs/session_goals.md), or specific design documents as needed.

---

*This is a living navigation hub. For detailed implementation status, see [CURRENT_WORK.md](CURRENT_WORK.md).*
