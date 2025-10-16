# Agents Reference

**Purpose**: User-facing documentation for all astrology interpretation agents

**Last Updated**: 2025-10-11

**Note**: This is reference documentation explaining WHAT each agent does. The actual agent instructions (prompts) are in `.claude/agents/*.md` files.

---

## Quick Reference

| Agent | Purpose | When to Use | Output |
|-------|---------|-------------|--------|
| mode-orchestrator | Routes all interpretation requests | **Always** - for any astrology question | Coordinates workflow |
| natal-interpreter | Birth chart interpretation | Want complete psychological profile | Natal horoscope (markdown + PDF) |
| life-arc-interpreter | Lifetime timeline (ages 0-100) | Want to see life chapters and major transitions | Life arc report (markdown + PDF) |
| transit-analyzer-short | Dual-mode: (1) 1-4 month transit report (2) Period-of-interest cluster analysis | Need near-term timing OR zoom into high-score periods | Short transit report OR cluster deep-dive |
| transit-analyzer-long | 1-5 year transit report | Need strategic life planning | Long transit report with chapters |
| pdf-formatter | Format markdown to styled PDF | After interpretation completes OR reformatting needed | Professional PDF with cover/TOC/chart overview |
| astrology-output-debugger | Verify interpretation quality | Output seems wrong or inconsistent | Diagnostic report |

---

## Orchestration Agents

### mode-orchestrator

**What It Does**: Central coordinator that routes ALL astrology interpretation requests to the appropriate agents.

**When to Use**:
- Any time you want a chart interpretation, transit analysis, or timing report
- Conversational questions like "What's happening in March 2026?"
- Questions like "When should I apply for this job?"
- Any request requiring seed data, calculations, or interpretations

**How It Works**:
1. Detects which mode you need (Natal/Life Arc/Transits/Timing)
2. Validates your profile exists and has seed data
3. Runs any calculations needed (transits, timing techniques)
4. Invokes the appropriate interpreter agent
5. Saves output to your profile folder
6. Returns file path and offers PDF generation

**Example Requests**:
- "Generate natal horoscope for darren"
- "What's happening astrologically in March 2026?"
- "Analyze my life from ages 35-45"
- "Compare Saturn return to current period"

**Output**: Coordinates the workflow, generates requested report

**See**: [AGENT_ORCHESTRATION_GUIDE.md](AGENT_ORCHESTRATION_GUIDE.md) for detailed usage

---

### astrology-output-debugger

**What It Does**: Systematically investigates interpretation quality issues from seed data through final output.

**When to Use**:
- Output quality seems questionable
- You ask to verify a reading
- Calculations or interpretations appear inconsistent
- New features produce unexpected results
- Comparing outputs reveals discrepancies (e.g., "Saturn return was hardest period but report says positive")

**When NOT to Use**:
- Insufficient context to know what "correct" looks like
- Just asking conceptual questions ("What is a Saturn return?")
- No actual output has been generated yet

**How It Works** (6-phase investigation):
1. **Output Analysis**: Review problematic output in detail
2. **Data Verification**: Check raw seed data, planetary positions, dignities, aspects
3. **Workflow Tracing**: Map complete data flow from input to output
4. **Prompt Review**: Examine agent prompts for completeness
5. **RAG Database Investigation**: Verify retrieved interpretations
6. **Root Cause Report**: Document issues, identify causes, provide fixes

**Output**: Diagnostic report with root cause analysis and specific fixes

**See**: [AGENT_ORCHESTRATION_GUIDE.md](AGENT_ORCHESTRATION_GUIDE.md) for detailed usage

---

## Interpretation Agents

### natal-interpreter

**What It Does**: Generates comprehensive psychological birth chart profiles using traditional Hellenistic astrology.

**When to Use**:
- Want to understand someone's natal chart
- Need complete birth chart interpretation
- Want psychological profile based on chart placements

**What You Get**:
- **Title Page**: Profile name, birth data, date generated
- **Overview**: 2-3 paragraph synthesis of chart's main themes
- **Core Sections**:
  - Sect (Day/Night chart)
  - Ascendant & Chart Ruler
  - Sun, Moon, Mercury, Venus, Mars
  - Jupiter, Saturn
  - Modern Planets (Uranus, Neptune, Pluto) - secondary context
  - Houses
  - Major aspects
- **Synthesis**: Poetic wrap-up integrating themes
- **Format**: Markdown + PDF (chart-based CSS styling)

**Technical Details**:
- Uses whole-sign houses (traditional/Hellenistic)
- Traditional Seven (Sun-Saturn) PRIMARY
- Modern planets (Uranus-Pluto) SECONDARY
- Classical aspects only (conjunction, sextile, square, trine, opposition)
- RAG-integrated (queries astrology reference database)
- Psychological depth voice (intimate, witnessing, poetic)

**Requirements**:
- Profile must exist with birth data
- Seed data must be generated (`seed_data.json`)

**Output Location**: `/profiles/{name}/output/natal_horoscope_{name}_{date}.md` (and PDF)

**Example**: See `/profiles/darren/output/` for sample natal horoscope

---

### life-arc-interpreter

**What It Does**: Generates narrative lifetime timeline showing life chapters and major transitions from birth to age 100.

**When to Use**:
- Want to see your entire life story arc
- Understand major life chapter boundaries
- Identify significant transition points
- See when different life themes are active

**What You Get**:
- **Title Page**: "Life Arc Report 0-100", name, birth data
- **Overview**: High-level life story synthesis (2-3 pages)
- **Chapters** (organized by Zodiacal Releasing L1 periods):
  - Each major life chapter (8-30 year periods)
  - Convergence points (when multiple timing techniques align)
  - "Current Situation" sub-chapter for present age
- **Major Events**: Automatically flagged significant transitions
- **Format**: Markdown + PDF (timeline-based CSS styling)

**Technical Details**:
- **5 Core Timing Techniques**:
  - Annual Profections (12-year cycles)
  - Zodiacal Releasing Fortune L1 (major life chapters)
  - Zodiacal Releasing Spirit L1 (identity chapters)
  - Firdaria (Persian 75-year cycle)
  - Planetary Returns (Jupiter ~12y, Saturn ~29.5y, Uranus opposition ~42y)
- **Convergence Detection**: Point-based scoring (25+ = MAJOR event)
- **Narrative Structure**: Story chapters, not technique-by-technique listing
- **Voice**: Psychological depth, life-story narrative

**Requirements**:
- Profile must exist with birth data
- Seed data must be generated

**Output Location**: `/profiles/{name}/output/life_arc_interpretation_{name}_ages_{start}-{end}.md` (and PDF)

**Example**: See `/profiles/darren/output/` for sample life arc report

**See**: [LIFE_ARC_GUIDE.md](LIFE_ARC_GUIDE.md) for detailed usage

---

### transit-analyzer-short

**What It Does**: Generates transit reports with TWO modes - (1) Multi-movement reports for 1-4 month periods, (2) Period-of-interest deep-dives showing transit clusters flagged by long-term reports.

**When to Use**:

**Multi-Movement Mode**:
- Need tactical timing for near-term (next 1-4 months)
- Want to understand upcoming transit themes
- Planning specific events or decisions
- Need detailed day-by-day or week-by-week timing

**Period of Interest Mode**:
- Long-term report flagged a high-score period needing closer examination
- User asks "What's happening around [date]?" when that date had significant score
- Want to understand a cluster/concentration of transits
- User says "Tell me about that [month/period]" referencing long-term report findings

**What You Get**:

**Multi-Movement Mode**:
- **Summary Synthesis**: Overview connecting all movements
- **Movements** (2-4 thematic sections):
  - Evocative titles ("The Catalyst", "Inner Reckoning")
  - Narrative weaving all transits in that timeframe
  - Key dates highlighted in bold within text
- **Technical Appendix**:
  - Transit list by date
  - Most auspicious/challenging days
  - Movement boundary explanations
- **Format**: Markdown + PDF (movement-based CSS styling)

**Period of Interest Mode**:
- **At a Glance**: Cluster period + score + key dates + convergent factors
- **Summary Synthesis**: Why this period was flagged, what creates significance (200-300 words)
- **The Cluster Period**: Complete narrative arc (800-1200 words)
  - Buildup phase (applying transits, tension building)
  - Peak concentration (multiple exactness dates close together)
  - Resolution phase (separating transits, integration period)
- **Technical Appendix**: All transits + daily scores + timing activations
- **Format**: Markdown + PDF (movement-based CSS styling)

**Technical Details**:
- **Planets**: ALL 10 (Sun through Pluto)
- **Tiers**: CRITICAL + IMPORTANT + NOTABLE
- **Structure**: Dynamic movement detection (not fixed time divisions) OR cluster window detection (2-6 weeks)
- **Movement Extension**: First/last movements extend to natural boundaries
- **Cluster Analysis**: Shows ALL transits + timing techniques creating high scores
- **Voice**: Accessible psychological depth, no unexplained jargon

**Requirements**:
- Profile must exist
- Transit data calculated for date range (1-4 months) OR cluster period
- For period-of-interest mode: Focus date and score from long-term report

**Output Location**:
- Multi-movement: `/profiles/{name}/output/transit_report_{name}_short_{start}_to_{end}.md` (and PDF)
- Period of interest: `/profiles/{name}/output/transit_cluster_{identifier}.md` (and PDF)

**See**: [TRANSITS_GUIDE.md](TRANSITS_GUIDE.md) for transit concepts, [TRANSIT_SHORT_DUAL_MODE_UPDATE.md](TRANSIT_SHORT_DUAL_MODE_UPDATE.md) for dual-mode spec

---

### transit-analyzer-long

**What It Does**: Generates 1-5 year strategic transit reports with chapter structure organized by Zodiacal Releasing L2 periods.

**When to Use**:
- Need strategic life planning (1-5 years ahead)
- Want to understand major life transitions
- Planning long-term goals or major decisions
- Want to see big-picture timing patterns

**What You Get**:
- **Title Page**: Date range, name, birth data
- **Quick Reference Tables**:
  - Most auspicious days (top dates)
  - Most challenging days (top dates)
  - Peak/low periods
- **Section 1** (3-page overview): High-level synthesis of entire period
- **Section 2** (Detailed chapters):
  - **Chapters** (H1): Zodiacal Releasing L2 periods (1-3 years each)
  - **Sub-chapters** (H2): Zodiacal Releasing L3 periods (1-5 months)
  - Narrative synthesis weaving transits into story
  - Bold dates integrated naturally
- **Format**: Markdown + PDF (movement-based CSS styling)

**Technical Details**:
- **Planets**: 6 slower planets only (Mars through Pluto)
- **Tiers**: CRITICAL only (filters ~70% of transits)
- **Structure**: ZR L2 chapters (Fortune periods), L3 sub-periods
- **Voice**: Psychological depth, life-story narrative (matches life-arc-interpreter)
- **Traditional PRIMARY**, modern SECONDARY

**Requirements**:
- Profile must exist
- Transit data calculated for date range (1-5 years)
- Zodiacal Releasing data available

**Output Location**: `/profiles/{name}/output/transit_report_{name}_long_{start}_to_{end}.md` (and PDF)

**Example**: See `/profiles/darren/output/` for sample long transit report

**See**: [TRANSITS_GUIDE.md](TRANSITS_GUIDE.md) for transit concepts

---

## Support Agents

### pdf-formatter

**What It Does**: Formats plain markdown astrology reports into professionally styled PDFs with cover pages, table of contents, report-specific chart overview, and proper page layout. Separates presentation logic from interpretation logic.

**When to Use** (triggers automatically or manually):
- After any interpretation agent completes markdown output
- mode-orchestrator completes interpretation and needs PDF generation
- User requests PDF formatting for existing markdown report
- Reformatting needed after style changes

**How It Works**:
1. Reads plain markdown synthesis file + seed data
2. Builds HTML title page structure
3. Generates Table of Contents from markdown headings
4. Creates report-specific Chart Overview:
   - **Template A (natal)**: Astrological data bullets (sect, ruler, dignities, auto-fill to ~12 items)
   - **Template B (life_arc)**: Major Life Events Timeline table with accessible descriptions
   - **Template C (transit)**: Current timing context (L1, L2, profections, active transits)
5. Formats Introduction section (~300 words with page break)
6. Formats main content (converts headings, adds strategic page breaks)
7. Formats Reflection section (poetic wrapup with ## Reflection heading)
8. Generates PDF using pdf_generator.py with appropriate --report-type

**Key Features**:
- **Separation of Concerns**: Interpreters focus on content, pdf-formatter handles presentation
- **Report-Type Specific**: Different Chart Overview templates for natal/life_arc/transit reports
- **Auto-Fill Intelligence**: Natal Chart Overview fills to ~12 bullets (fixed stars, lots, receptions, etc.)
- **Accessible Language**: Life arc timeline uses NO jargon (translates "Saturn return" to "major crisis and reckoning")
- **L1 Context**: Transit reports ALWAYS include L1 chapter for framing

**Technical Details**:
- Model: Sonnet (fast, efficient for formatting tasks)
- Extended Thinking: false (straightforward formatting logic)
- Color: Cyan (utility/infrastructure agent)
- CSS Loading: base.css + report-specific CSS (chart_based/timeline_based/movement_based)

**Output**: Formatted markdown + professional PDF with:
- Title page with birth data
- Hierarchical Table of Contents
- Report-specific Chart Overview
- ~300 word Introduction
- Main content with strategic page breaks
- Reflection section with proper heading

**Coordination**:
```
interpreter completes → passes to pdf-formatter:
  - markdown_file path
  - seed_data_file path
  - report_type (natal/life_arc/transit_short/transit_long)
  - profile info

pdf-formatter generates → confirms success:
  - formatted markdown path
  - final PDF path
```

**Benefits**:
- Reduces interpreter token count by ~80-100 lines (17-18% reduction)
- Single source of truth for PDF formatting
- Easy style changes without touching interpreters
- Consistent output across all report types

**See**: `docs/pdf_formatter_design.md` for complete specification

---

### feature-designer-astrology

**What It Does**: Translates feature vision into comprehensive technical specifications through conversational requirement gathering.

**When to Use**:
- Designing complex new features or components
- Requirements are unclear and need discovery
- Want to explore edge cases before implementation
- Need formal specification document for complex work

**How It Works**:
1. **Requirements Discovery**: Asks clarifying questions, explores examples
2. **Design Proposal**: Recommends technical approach with tradeoffs
3. **Spec Creation**: Documents comprehensive feature specification at `docs/[feature]_specification.md`
4. **Agent Coordination**: Automatically triggers astrology-agent-creator if spec involves new agents

**What You Get**:
- Specification document with:
  - Problem statement and goals
  - Functional and non-functional requirements
  - Edge cases and design decisions
  - Implementation plan
  - Testing strategy

**Workflow**:
```
User vision → feature-designer (conversational) → spec document → astrology-agent-creator (if needed)
```

**Output**: Comprehensive feature specification document at `docs/[feature]_specification.md`

**See**: [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md) for feature design workflow

---

### astrology-agent-creator

**What It Does**: Creates new astrology interpretation agents with proper template extraction and documentation integration.

**When to Use**:
- Creating new interpretation agents (natal, transit, timing techniques)
- Need agent that follows OUTPUT_STYLE_GUIDE.md templates
- Want conversational agent design and refinement

**How It Works**:
1. **Spec Acceptance** (optional): Reads spec from feature-designer-astrology
2. **Requirements Discovery**: Conversational exploration of agent purpose
3. **Template Extraction**: Parses OUTPUT_STYLE_GUIDE.md for required sections
4. **Agent Creation**: Builds agent with proper coordination and tool access
5. **Auto-Documentation**: Automatically invokes docs-updater-astrology to catalog new agent

**Coordination**:
- Accepts specification documents from feature-designer-astrology
- Auto-invokes docs-updater-astrology after creating agents
- Updates AGENTS_REFERENCE.md and CLAUDE.md automatically

**Output**: New agent file at `.claude/agents/[name].md` + updated documentation

---

### astrology-rag-builder

**What It Does**: Maintains the RAG (Retrieval-Augmented Generation) database of traditional astrology knowledge.

**When to Use**:
- Adding new reference books to database
- Querying astrology concepts for interpretation
- Normalizing terminology across sources
- Quality control on database content

**What It Can Do**:
- Extract and structure knowledge from PDFs
- Create semantic embeddings for search
- Query database for specific concepts
- Cross-reference multiple sources
- Identify terminology conflicts

**Database Stats**:
- 2,472 semantic chunks
- 6 authoritative traditional sources
- OpenAI embeddings for semantic search

**Output**: Updated RAG database, query results, coverage assessments

---

### docs-updater-astrology

**What It Does**: Maintains project documentation (CURRENT_WORK.md, history archives, agent catalogs, etc.)

**When to Use** (triggers automatically):
- After completing any implementation stage
- Current focus or task changes
- Files in progress change
- Major milestones reached
- After astrology-agent-creator creates new agents

**What It Updates**:
1. **CURRENT_WORK.md**: Current focus, files in progress, next steps (30-50 lines)
2. **AGENTS_REFERENCE.md**: Complete agent catalog with capabilities
3. **CLAUDE.md**: Navigation hub with agent list
4. **/history/**: Archive completed stages with full documentation
5. **/history/index.md**: Update with stage summary
6. **session_goals.md**: Mark progress (✅ complete stages, update status)

**Agent Maintenance** (expanded capability):
- Scans all `.claude/agents/*.md` files for outdated tool/doc references
- Updates agent instructions when new tools or docs are added
- Cross-reference validation (ensures referenced docs exist)

**Output**: Updated documentation files, agent instruction updates

---

### accuracy-checker

**What It Does**: Automated quality verification for interpretation outputs using systematic cross-validation. **STATUS: Specification complete, implementation pending**

**When to Use** (will auto-trigger):
- After any natal-interpreter, life-arc-interpreter, or transit-analyzer completes
- User requests verification of interpretation quality
- Comparing interpretations reveals discrepancies

**How It Will Work**:
1. **Data Cross-Validation**: Verify astronomical data against Swiss Ephemeris
2. **Traditional Compliance**: Check adherence to traditional/Hellenistic methods
3. **RAG Query Validation**: Verify interpretations match retrieved knowledge
4. **Template Adherence**: Confirm OUTPUT_STYLE_GUIDE.md structure followed
5. **Consistency Check**: Compare similar chart elements for coherence
6. **Quality Report**: Document findings, flag issues, recommend fixes

**Output**: Quality report with pass/fail status and specific fixes needed

**Status**: Specification document exists at `docs/accuracy_checker_specification.md`, implementation pending

---

### workflow-planner-2

**What It Does**: Provides expert technical recommendations for architecture, tools, and implementation approaches.

**When to Use**:
- Planning new features
- Unsure which library or approach to use
- Need architectural guidance
- Want technical recommendations for implementation

**What It Provides**:
- Framework/library recommendations
- Architecture design guidance
- Technical approach options with pros/cons
- Implementation roadmaps

**Output**: Technical recommendations, architecture designs, implementation plans

---

## Agent Coordination Flow

### Standard Report Generation

```
User: "Run transit report for next month"
   ↓
mode-orchestrator (detects Mode 3, short timeframe)
   ↓
Validates darren profile exists
   ↓
Runs transit_calculator.py (30 days)
   ↓
Invokes transit-analyzer-short agent
   ↓
Agent generates report
   ↓
Saves to /profiles/darren/output/transit_report_darren_short_{dates}.md
   ↓
Offers PDF generation
   ↓
Returns file path to user
```

### Feature Design Flow (Complex Features)

```
User: "I want to redesign the life arc scoring system"
   ↓
feature-designer-astrology (triggered)
   ↓
Conversational requirements discovery
   ↓
Design proposal with tradeoffs
   ↓
Creates docs/[feature]_specification.md
   ↓
If spec involves new agents:
   ↓
Automatically triggers astrology-agent-creator
   ↓
Agent created at .claude/agents/[name].md
   ↓
Automatically triggers docs-updater-astrology
   ↓
AGENTS_REFERENCE.md + CLAUDE.md updated
```

### Simple Agent Creation Flow

```
User: "Create agent for secondary progressions interpretation"
   ↓
astrology-agent-creator (triggered directly)
   ↓
Conversational requirements discovery
   ↓
Template extraction from OUTPUT_STYLE_GUIDE.md
   ↓
Agent created at .claude/agents/[name].md
   ↓
Automatically triggers docs-updater-astrology
   ↓
AGENTS_REFERENCE.md + CLAUDE.md updated
```

### Verification Flow

```
User: "The Saturn return interpretation seems wrong"
   ↓
astrology-output-debugger (triggered)
   ↓
Phase 1: Reviews output
Phase 2: Verifies data (seed data, calculations)
Phase 3: Traces workflow
Phase 4: Reviews prompts
Phase 5: Checks RAG queries
Phase 6: Identifies root cause
   ↓
Returns diagnostic report with fixes
   ↓
docs-updater-astrology (documents issue in TROUBLESHOOTING.md)
```

---

## Agent Maintenance

**AUTOMATED**: docs-updater-astrology now handles most agent maintenance automatically:

**When astrology-agent-creator creates new agent**:
1. ✅ **docs-updater-astrology automatically updates**:
   - AGENTS_REFERENCE.md - Document what the new agent does
   - CLAUDE.md - Add to Project Agents section
   - CURRENT_WORK.md - Document the new agent creation

2. ⚠️ **Manual updates still required**:
   - **mode-orchestrator.md** - Add routing logic for new interpretation agents (if applicable)
   - **Agent-specific handoffs** - Update coordination in related agents

**When new tools/docs are added**:
- docs-updater-astrology scans all `.claude/agents/*.md` files for outdated references
- Updates agent instructions with new tool/doc references
- Cross-reference validation (ensures referenced docs exist)

**See**: [AGENT_ORCHESTRATION_GUIDE.md](AGENT_ORCHESTRATION_GUIDE.md) for detailed update checklist

---

## Related Documentation

- **Agent instructions (prompts)**: `.claude/agents/*.md`
- **Agent orchestration guide**: [AGENT_ORCHESTRATION_GUIDE.md](AGENT_ORCHESTRATION_GUIDE.md)
- **Timing techniques guides**: [PROFECTIONS_GUIDE.md](PROFECTIONS_GUIDE.md), [ZODIACAL_RELEASING_GUIDE.md](ZODIACAL_RELEASING_GUIDE.md), [LIFE_ARC_GUIDE.md](LIFE_ARC_GUIDE.md)
- **Transit concepts**: [TRANSITS_GUIDE.md](TRANSITS_GUIDE.md)
- **Output formats**: [OUTPUT_STYLE_GUIDE.md](OUTPUT_STYLE_GUIDE.md)
- **Astrology reference**: [ASTROLOGY_REFERENCE.md](ASTROLOGY_REFERENCE.md)

---

**Remember**: Use mode-orchestrator for ALL astrology interpretation requests. It will route you to the right agent automatically.
