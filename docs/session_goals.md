# Astrology Application - Session Goals

**Last Updated**: 2025-10-12
**Status**: Stage 4 - Natal Horoscope Optimization (extended-thinking + antiscia/fixed stars implementation)

---

## Speculative Updates (Future Features)

Features we may implement but haven't fully planned yet:

-  add scoring system to natal interpreter?
- update agents/orchistrator so the agetns outpout the final files
- make poetic wrap up more poetic and 3-5 sentences
- refactor docs folder for current spec, future plans, and archive
- are there multiople scripts that run for a horoscope? can we consolidate?
- check that the planning agents use context7 when appropriate.
- setting to allow for uncertain birth times, just use houses/signs, no asc, mc, etc.
- **Angle interpretations**: Add specific interpretations for chart angles (ASC/MC/DSC/IC sign rulers, aspects TO the angles)
- **Electional astrology**: Add chart selection for optimal timing (doesn't help with transits, so later priority)
- Daily report - runs automatically to genereate a daily report. Maybe make a whole workflwo to generate a horoscope and summarize my day/find any news sources I'm interested in.
- **Module refinement**: After initial build, go back and refine individual modules - alreadY in progress
- **Synastry**: Add relationship compatibility analysis
- **Mobile app consideration**: May build over Telegram if we need to adjust settings
- **Different input/output modes**: Various ways to interact with the system
- optimize system with rag

- **Claude Code API instead of ChatGPT**: Migrate from OpenAI to Claude API


### Natal Horoscope Enhancement - Deeper Nuanced Synthesis (20 pages)

**Goal**: Transform natal horoscopes from high-level summaries to deeply nuanced personality portraits where astrological techniques weave together naturally rather than being listed separately.

**Key Changes**:

1. **Seed Data Enhancements** (add missing calculations):

   **Priority 1** (critical for nuanced interpretation):
   - Stelliums: Calculate 3+ traditional planets in same sign OR house, identify ruler
   - Hayz: Optimal sect condition (diurnal planet above horizon by day, nocturnal below by night, in appropriate sign)
   - Terms/Bounds: Fix null values (Swiss Ephemeris should provide these)
   - Decans/Faces: Fix null values

   **Priority 2** (adds significant color):
   - Stationary: Planets within 1-2° of retrograde/direct stations
   - Swift/Slow motion: Relative to mean speed (>110% = swift, <90% = slow)
   - Oriental/Occidental: Rising before/after Sun
   - Peregrine flag: Explicitly mark planets with NO essential dignities
   - Feral flag: Explicitly mark planets with NO major aspects

   **Priority 3** (advanced, less critical):
   - Overcoming: Planet in superior square/opposition position
   - Enclosure/Besiegement: Surrounded by benefics (helped) or malefics (burdened)

2. **Structure Changes**:
   - Page 1: Title page only
   - Page 2: Chart Overview (8-12 sparse bullets) - technical quick reference, NO narrative prose
   - Page 3: Synthesis Introduction (600-800 words) - essential you overview, flowing narrative
   - Pages 4-19: Main Synthesis (~4,800 words) - woven narrative
   - Page 20: Synthesis & Integration (300 words) - poetic wrapup at END of document
   - Remove all technical sections (goes to separate process file)
   - Target: 5,700-6,000 words = 19-20 pages

3. **Content Enhancements** (weaving techniques together):

   **Life-Area Section Structure** (KEEP EXISTING):
   - Core Personality & Character
   - Psychological Makeup (subsections: Ideal Self, Emotional Nature, Mental Style, Love & Relating)
   - Life Path & Purpose
   - Strengths & Natural Gifts
   - Challenges & Growth Areas
   - Career & Vocation
   - Synthesis & Integration
   - Optional additions: Relationships & Intimacy, Creative Expression, Spiritual Path, Daily Rhythms

   **Integration Formula** (weave into EACH life-area section):
   1. Essential Dignities (domicile, exaltation, triplicity, terms, decans) - shows strength
   2. Accidental Dignities (angularity, speed, hayz, oriental/occidental) - shows effectiveness
   3. House Ruler Analysis - ruler's placement shows HOW life area unfolds
   4. Planets in House - show WHAT energies are active
   5. Aspects to Ruler and Planets - show SUPPORT or CHALLENGE
   6. Aspect Patterns (T-squares, grand trines) - larger stories
   7. Lot Placements - shows WHERE themes manifest
   8. Sect Layering - colors EVERY planet's expression
   9. Receptions & Bonification - hidden support networks
   10. Stellium Influence - gravitational center (not separate section)
   11. Planetary Conditions (combustion, cazimi, stationary, oriental/occidental, swift/slow, overcoming, enclosure, peregrine, feral)
   12. Antiscia Connections - hidden symmetries
   13. Chart Ruler Emphasis - overall life expression

4. **Writing Style Shift**:
   - Before: "You have Sun conjunct Saturn. This creates discipline. You also have Moon square Jupiter."
   - After: "Your Sun-Saturn conjunction demands discipline, but because Saturn rules both your 6th house of work AND 7th house of partnership, this shows up in both how you approach craft and how you relate to others. Your Leo Moon wants playful warmth, creating tension—but your Lot of Eros in the 5th house suggests that creative play in both domains resolves the conflict..."

**Implementation Steps**:
1. **Seed Data Updates** (scripts/seed_data_generator.py):
   - Add 11 new calculations (priorities 1-3)
   - Fix terms/bounds null values
   - Fix decans/faces null values
   - Total: ~200-300 lines of code

2. **Agent Updates** (.claude/agents/natal-interpreter.md):
   - Keep existing life-area section structure
   - Add complete 13-point integration formula
   - Add word count targets per section (total 5,700-6,000 words)
   - Add weaving examples for each section type
   - Remove instructions to generate technical sections III-VIII (goes to separate process file)

3. **Optional Section Expansion** (if needed for 20 pages):
   - Add "Relationships & Intimacy" (separate from Love & Relating)
   - Add "Creative Expression"
   - Add "Spiritual Path & Inner Life"
   - Add "Daily Rhythms & Health"
   - Each ~400-600 words

4. **Test & Iterate**:
   - Generate test horoscope with Darren's chart
   - Verify 19-20 page output
   - Check that techniques are woven together, not listed separately
   - Verify accuracy with accuracy-checker agent

**Expected Result**: Horoscopes that read like cohesive personality portraits where every technique adds nuance to a unified narrative, not separate observations listed one after another.

---

## North Star Vision

Build a comprehensive astrology application that provides:
1. **Natal Horoscope Generator**: Personalized birth chart interpretation
2. **Life Arc Report Generator**: Decades-long life timeline with convergence detection
3. **Transit Report Generator**: Targeted transit analysis by area of life and timeframe
4. **Additional Timing Techniques**: Zodiacal releasing, annual profections, and other traditional methods
5. **Conversational Orchestrator** (Planned): Transform mode-orchestrator into rolling astrology assistant
   - Quick question answering (without full reports)
   - Full report generation when appropriate
   - RAG integration for traditional interpretations
   - Multi-turn conversational memory
   - **See**: [orchestrator_conversational_upgrade_spec.md](orchestrator_conversational_upgrade_spec.md) for complete 5-phase plan

**Ultimate Goal**: Make traditional/Hellenistic astrology insights accessible through natural conversation, grounded in authoritative sources (Brennan, Hand, George, Brady, Greene, Mason).

**User Context**: Deep astrology expertise, limited coding experience. Need expert technical guidance to implement vision.

**Workflow**: Start in Claude Code → migrate to web/Telegram if successful

---

## Current State Assessment

### What We Already Have ✅

**Completed Modes**:
- ✅ **Mode 1: Natal Horoscope** - Multi-profile system, PDF output, RAG-integrated synthesis
- ✅ **Mode 2: Life Arc Report** - Decades-long timeline with convergence detection, narrative chapters, 5 core timing techniques
- ✅ **Mode 3: Transit Report** - Dual-level reporting (short 1-4 months, long 1-5 years), ZR L2/L3 chapters, convergence scoring, psychological narrative

**Infrastructure (Production-Ready)**:
- **RAG Database**: 2,472 chunks from 6 traditional sources
  - Sources: Brennan, Hand, George, Brady, Mason, Greene
- **Chart Analyzer**: Complete natal analysis with dignities, sect, strength scores
- **Swiss Ephemeris Integration**: Verified astronomical calculations
- **Timing Calculators**: Profections, Zodiacal Releasing, Firdaria, planetary returns, progressions
- **Convergence Detection**: Point-based scoring system for major life events
- **Profile System**: Multi-profile support with settings customization

**Tech Stack**:
- Python 3.x
- OpenAI API (embeddings only for RAG database)
- **Interpretation/Synthesis**: Claude Code agents (natal-interpreter, life-arc-interpreter)
  - No external API calls needed for MVP
  - Agent instructions serve as approved "prompts"
  - Can migrate to GPT-5 API later if desired
- pyswisseph (Swiss Ephemeris)
- Local file-based storage
- Traditional/Hellenistic compliance

### What We Need to Build 🔨

**Next Priorities**:
- **Mode 1 Enhancements**: Antiscia and fixed stars implementation, profile settings loader
- **Mode 4: Additional Timing CLI** - Core techniques already built, just need wrappers
- **Chat Modes** (Future) - Rolling conversations for natal and transit questions

**Orchestration Layer**:
- Session manager to tie existing pieces together
- Multiple mode handlers (horoscope, transits, timing techniques)
- CLI interface (initially)
- Two separate rolling chat interfaces (future)

---

## System Architecture

### Mental Model: Like a Doctor's Appointment
- Doctor reviews your file at start (loads natal chart + base analysis)
- You tell them what you need (horoscope, transit report, timing analysis, or ask questions)
- They pull relevant info and give you specific answers
- Your file stays loaded the whole visit (session persists)

### Mode Structure

**Mode 1: Natal Horoscope Generator** ✅ COMPLETE
- Input: Birth data file path
- Process: Generate seed data → Query RAG → Synthesize narrative
- Output: Comprehensive natal horoscope (markdown + PDF)
- Length: ~6,900 words with planetary strength table

**Mode 2: Life Arc Report Generator** ✅ COMPLETE
- Input: Profile + age range (default 0-100)
- Process: Calculate 5 timing techniques → Detect convergence → Generate narrative chapters
- Output: Decades-long life timeline (markdown + PDF)
- Structure: ZR L1 periods as chapters, convergences as subheadings

**Mode 3: Transit Report Generator** ✅ COMPLETE
- Input: Profile + timeframe (1-4 months short, 1-5 years long)
- Process: Calculate transits → Filter by report type → Query RAG → Synthesize narrative
- Output: Dual-level reports (short with movements, long with ZR L2/L3 chapters)
- Features: Convergence scoring, period-of-interest clusters, psychological depth voice

**Mode 4+: Traditional Timing Techniques** ⏳ READY TO BUILD
- Core techniques already implemented (profections, ZR, Firdaria, returns, progressions)
- Need: CLI command wrappers for each technique
- Each technique becomes a CLI command

**Chat Mode A: Horoscope Inquirer** (Future)
- Rolling conversation about natal chart
- User asks: personality, ideal vocation, chart placements
- AI assesses question, retrieves relevant data, answers directly
- Session-aware (natal chart loaded)

**Chat Mode B: Transit/Advice Chatbot** (Future)
- Generate transit report first
- Then rolling conversation about report + current situation
- User asks: current transits, timing, advice for specific situations
- AI pulls from transit report + timing techniques + RAG database
- Gives advice based on traditional literature
- Session-aware (natal chart + transit report loaded)

---

## Implementation Priorities

### Completed ✅
- ✅ Stage -1: RAG Database Enhancement (2,472 chunks from 6 sources) - [Archive](../history/STAGE_-1_RAG_Enhancement.md)
- ✅ Stage 0: Research Timing Techniques (profections, ZR, Firdaria identified) - [Archive](../history/STAGE_0_Research_Timing.md)
- ✅ Stage 1: Natal Horoscope System (multi-profile, automated, PDF output) - [Archive](../history/STAGE_1_Natal_Horoscope.md)
- ✅ Stage 2: Life Arc Report System (5 techniques, convergence detection, narrative structure) - [Archive](../history/STAGE_2_Life_Arc_Report.md)
- ✅ Stage 3: Transit Report System (dual-level reporting, ZR L2/L3, convergence scoring) - [Archive](../history/STAGE_3_Transit_Reports.md)

### Next: Stage 4 (Natal Horoscope Optimization) 🔨
**Goal**: Enhance natal horoscope with antiscia, fixed stars, extended-thinking, and optimized technique selection

**Requirements**:
- ✅ Extended-thinking integration (all 4 interpretation agents)
- ✅ Meta-agent enhancement (agent-creator, prompt-improver, astrology-agent-creator)
- ✅ Technique selection finalized (sect PRIMARY, angles, 4 lots, antiscia, fixed stars)
- ✅ Profile structure standardized (FirstName_LastInitial/ format)
- ✅ Documentation created (NATAL_DATA_MODEL_OPTIMIZATION.md, SEED_DATA_SPECIFICATION.md, PROFILE_STRUCTURE.md)
- ⏳ Implement antiscia calculation in seed_data_generator.py
- ⏳ Implement fixed stars calculation (5 major stars: Regulus, Spica, Algol, Aldebaran, Antares)
- ⏳ Create profile_settings_loader.py (read settings from profile.md)
- ⏳ Test regenerated natal horoscopes with new enhancements

**Design Documents Available**:
- `/docs/NATAL_DATA_MODEL_OPTIMIZATION.md`
- `/docs/SEED_DATA_SPECIFICATION.md`
- `/docs/PROFILE_STRUCTURE.md`

### Future: Mode 4 (CLI Commands) ⏳
- Wrap existing timing calculators (profections, ZR, Firdaria, returns, progressions)
- Each becomes a CLI command
- Simple formatting or agent synthesis per technique

### Future: Chat Modes (Stages 5-6) ⏳
- Build two separate rolling chat interfaces
- Function calling for retrieving chart data
- RAG queries for traditional interpretations
- Session persistence

---

## Success Factors

### What Will Make This Succeed?

1. **Quality Output**: Interpretations must be accurate, well-cited, traditional
2. **Ease of Use**: Even non-technical users can generate reports
3. **Your Daily Use**: If you use it regularly, it's working
4. **Incremental Validation**: Test each stage before moving to next
5. **Traditional Compliance**: All interpretations grounded in sources
6. **Good Prompts**: Well-engineered agent instructions for synthesis
7. **Comprehensive Timing**: Multiple techniques give fuller picture
8. **Separate Chat Modes**: Focused contexts prevent confusion

### What Could Derail This?

1. **Prompt Engineering**: If agent output is poor quality, need to iterate
2. **RAG Coverage Gaps**: If database lacks key interpretations, need to expand
3. **Over-Engineering**: Building complex features before validating basics
4. **Scope Creep**: Adding features instead of perfecting core modes
5. **Settings Issues**: Wrong agent settings could degrade output

**Mitigation**:
- Start simple, validate quality at each stage
- Research before building
- Test with your own chart continuously
- Expand only when ready

---

## Non-Goals (What We're NOT Doing)

1. **Not building for scale initially**: Focus on single-user (you) first
2. **Not building a business/marketplace**: Just a tool for your use
3. **Not adding modern astrology**: Strict traditional/Hellenistic only
4. **Not building chart calculation from scratch**: Use Swiss Ephemeris
5. **Not building mobile apps**: Web/Telegram sufficient for mobile access
6. **Not adding social features**: No sharing, comments, or community (yet)
7. **Not monetizing initially**: Focus on quality and personal use
8. **Not using Claude API yet**: That's a speculative future update

---

## Technology Stack (Detailed)

### Core Technologies
- **Runtime**: Python 3.x
- **Interpretation/Synthesis**: Claude Code agents
  - **natal-interpreter**: Synthesizes natal horoscopes from RAG data
  - **life-arc-interpreter**: Synthesizes life arc reports with narrative structure
  - **transit-analyzer** (planned): Synthesizes transit reports and advice
  - **Chat agents** (future): Interactive conversation modes
  - **Advantages**: No API calls, faster, better quality, easier to iterate
  - **Migration path**: Can switch to GPT-5 API later if desired
- **Embeddings**: OpenAI text-embedding-3-large (for RAG database only)
- **Astronomical Calculations**: pyswisseph (Swiss Ephemeris)
- **Storage**: Local files (JSONL for RAG database)
- **Interface Progression**: CLI → Streamlit → Telegram

### Key Libraries
- **openai**: Embeddings only (for RAG database)
- **pyswisseph**: Ephemeris calculations
- **numpy**: Data processing
- **datetime**: Date/time handling
- **json**: Data serialization
- **pathlib**: File path handling
- **(Future)** streamlit or gradio: Web interface
- **(Future)** python-telegram-bot: Telegram interface

### MCP Servers & Tools
- **OpenAI API**: Required for RAG embeddings only
- **context7**: Optional (for library research)
- **filesystem**: Default (file operations)
- **github**: Not needed for MVP

### Agents Required
- **Infrastructure agents** (existing):
  - workflow-planner-2: Strategic planning and architecture
  - docs-updater-astrology: Documentation maintenance
  - astrology-rag-builder: RAG database management
  - agent-creator: Conversational agent creation (global)
- **Interpretation agents** (Mode 1-3 complete):
  - natal-interpreter ✅: Natal horoscope synthesis
  - life-arc-interpreter ✅: Life arc timeline synthesis
  - transit-analyzer-long ✅: Long-term transit reports (1-5 years)
  - transit-analyzer-short ✅: Short-term transit reports (1-4 months, dual-mode)
- **Orchestration agents**:
  - mode-orchestrator ✅: Routes requests to appropriate interpretation agents
  - astrology-output-debugger ✅: Verifies output quality and planetary positions
- **Chat agents** (future):
  - horoscope-chat: Interactive natal chart conversations
  - transit-chat: Interactive transit/advice conversations

---

## Documentation Strategy

### File Structure
- **CLAUDE.md**: Navigation hub pointing to all other files (~500-800 lines)
- **CURRENT_WORK.md**: What's happening RIGHT NOW (200 lines, frequently updated)
- **session_goals.md** (this file): High-level vision and future plans (rarely changes)
- **/docs/**: Design documents, usage guides, reference materials
- **/history/**: Archived completed stages

### Ownership
- **workflow-planner-2**: Creates plans, defines stages, makes technical recommendations (does NOT mark progress)
- **docs-updater-astrology**: Marks progress, updates status, archives finished stages (does NOT change plan)
- **Implementation agents**: Document detailed specs in /docs/

### Automatic Updates
After every major step, docs-updater-astrology automatically updates:
1. CURRENT_WORK.md (current focus, files in progress, next steps)
2. session_goals.md (mark stages complete ✅, update status)
3. CLAUDE.md (mode status table, last updated date)

No manual prompts needed.

---

## Current Status

**Stage**: Stage 4 - Natal Horoscope Optimization
**Completed Stages**:
- ✅ Stage -1: RAG Database Enhancement
- ✅ Stage 0: Research Timing Techniques
- ✅ Stage 1: Natal Horoscope System (Mode 1)
- ✅ Stage 2: Life Arc Report System (Mode 2)
- ✅ Stage 3: Transit Report System (Mode 3)
**Current Work**: Implementing antiscia + fixed stars calculations, testing enhanced natal horoscopes
**Next Action**: Complete antiscia calculation, then fixed stars, then test regenerated horoscopes

**Recent Infrastructure Improvements** (2025-10-04 - 2025-10-12):
- ✅ Extended-thinking integration (all 4 interpretation agents + 3 meta-agents)
- ✅ Transit report system complete (dual-level, ZR L2/L3, convergence scoring)
- ✅ Agent orchestration system (mode-orchestrator + astrology-output-debugger)
- ✅ Output format standardization (external CSS, hardcoded templates, 70% token savings)
- ✅ Profile structure standardized (FirstName_LastInitial/ format)
- ✅ Documentation cleanup (CURRENT_WORK.md down to 106 lines from 703)
- ✅ Stage archiving system working (detailed milestones archived to /history/)
- ✅ Natal optimization planned (antiscia, fixed stars, optimized technique selection)

---

## Questions for Workflow Planner (Ongoing)

As we build, consult workflow-planner-2 agent for:
- Architecture decisions
- Framework/library recommendations
- Prompt engineering strategies
- Error handling patterns
- Testing approaches
- Deployment options
- Agent settings optimization

---

*This is a living document tracking the long-term vision. For current tactical work, see CURRENT_WORK.md.*
