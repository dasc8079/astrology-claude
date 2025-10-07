# Astrology RAG Database & Application Project

**Navigation Hub** - For detailed documentation, see the links below.

---

## Quick Start

**Current Work**: See [CURRENT_WORK.md](CURRENT_WORK.md) for what's happening RIGHT NOW

**Vision & Plans**: See [session_goals.md](docs/session_goals.md) for North Star vision and future plans

**Project History**: See [/history/](history/) for archived completed stages

**Design Documents**: See [/docs/](docs/) for detailed specifications and implementation plans

**Static References**: See [REFERENCE.md](REFERENCE.md), [DEVELOPMENT.md](DEVELOPMENT.md), [README.md](README.md)

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
1. **Mode 1: Natal Horoscope Generator** ✅ COMPLETE - Birth chart psychological profiles with PDF output
2. **Mode 2: Life Arc Report Generator** ✅ COMPLETE - Life timeline from birth to age 100 with convergence detection
3. **Mode 3: Transit Report Generator** ⏳ PENDING - Current and upcoming transit analysis
4. **Mode 4+: Additional Timing Techniques** ⏳ PENDING - Additional predictive techniques

**Rolling Chat Interfaces** (Future):
- Horoscope Inquirer: Deep-dive natal chart questions
- Transit/Advice Chatbot: Transit-specific guidance

---

## Mode Status Table

| Mode | Name | Status | Stage | Notes |
|------|------|--------|-------|-------|
| 1 | Natal Horoscope | ✅ COMPLETE | Production | Multi-profile, PDF output, fully functional |
| 2 | Life Arc Report | ✅ COMPLETE | Production | Enhanced with convergence detection, narrative chapters, 5 core timing techniques |
| 3 | Transit Report | ⏳ PENDING | Design ready | Design documents complete, ready to implement |
| 4+ | Additional Timing | ⏳ PENDING | Research done | Core techniques built (profections, ZR, Firdaria) |

**Legend**: ✅ Complete | 🔄 In Progress | ⏳ Pending

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
**Output**: Markdown reports + PDF generation

**Migration Path**: Agent instructions serve as approved "prompts"; can migrate to GPT-5 API later if desired.

---

## Project Agents

**Planning & Documentation**:
- `workflow-planner-2` - Expert advisor for architecture, tools, and technical recommendations
- `docs-updater-astrology` - Documentation maintainer (CURRENT_WORK.md, CLAUDE.md, /history/)

**RAG Database**:
- `astrology-rag-builder` - RAG database maintenance, queries, normalization
- `astrology-output-debugger` - Debug interpretation issues, data quality, workflow problems

**Interpretation & Synthesis**:
- `natal-interpreter` - Natal chart synthesis using traditional Hellenistic methods (Mode 1) ✅
- `life-arc-interpreter` - Life timeline synthesis (Mode 2) ✅ WORKING (fixed 2025-10-07)
- `transit-analyzer` - Transit analysis and timing (Mode 3) ⏳ Planned

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

See [REFERENCE.md](REFERENCE.md) for detailed astrology systems reference.

---

## User Birth Data

**Location**: `/profiles/` directory with multi-profile support

**Profiles Available**:
- `darren/` - Complete natal horoscope (technical + synthesis + PDF)
- `mom/` - Synthesis PDF only
- `sister/` - Synthesis PDF only

**Profile Structure**:
```
profiles/
├── darren/
│   ├── profile.txt          # Birth data
│   ├── seed_data.json       # Astronomical calculations
│   ├── natal_technical.md   # Technical analysis
│   ├── natal_synthesis.md   # Accessible synthesis
│   └── natal_synthesis.pdf  # Professional PDF output
```

**Settings Block System**: Each profile.txt contains customizable interpretation settings (depth, house rulers, lots, psychological overlay, modern methods, etc.)

See [DEVELOPMENT.md](DEVELOPMENT.md) for profile creation and management.

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

See [REFERENCE.md](REFERENCE.md) for complete astrological systems reference.

---

## Navigation Index

**Current Work & Status**:
- [CURRENT_WORK.md](CURRENT_WORK.md) - What's happening RIGHT NOW (30-50 lines)
- [session_goals.md](docs/session_goals.md) - North Star vision and future plans (150-500 lines)

**Project History**:
- [/history/](history/) - Archived completed stages
- [/history/index.md](history/index.md) - History index with stage summaries

**Design & Specifications**:
- [/docs/life_arc_report_design.md](docs/life_arc_report_design.md) - Life Arc Report design (105+ pages)
- [/docs/timing_techniques_plan.md](docs/timing_techniques_plan.md) - Timing techniques plan (25+ pages)
- [/docs/transit_interpretation_design.md](docs/transit_interpretation_design.md) - Transit design
- [/docs/transit_staged_implementation.md](docs/transit_staged_implementation.md) - Transit implementation plan
- [/docs/session_goals_COMPARISON.md](docs/session_goals_COMPARISON.md) - Documentation structure comparison

**Static Documentation**:
- [REFERENCE.md](REFERENCE.md) - Astrological systems and terminology (rarely updated)
- [DEVELOPMENT.md](DEVELOPMENT.md) - Contributor guide and development workflow (rarely updated)
- [README.md](README.md) - Project overview and installation (rarely updated)

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

See [DEVELOPMENT.md](DEVELOPMENT.md) for setup instructions and development workflow.

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

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed workflow documentation.

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
