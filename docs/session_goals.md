# Astrology Application - Session Goals

**Last Updated**: 2025-10-07
**Status**: Mode 2 Complete - Ready for Mode 3

---

## Speculative Updates (Future Features)

Features we may implement but haven't fully planned yet:

- **Claude Code API instead of ChatGPT**: Migrate from OpenAI to Claude API
- **Birth data entry in chat interface**: Allow users to enter birth data during chat, automation fetches natal data
- **Transit story/activation timeline**: Expand transit reports to include the totality of a transit's story in the native's life (transits tell stories, not isolated events)
- **Module refinement**: After initial build, go back and refine individual modules
- **Synastry**: Add relationship compatibility analysis
- **Mobile app consideration**: May build over Telegram if we need to adjust settings
- **Different input/output modes**: Various ways to interact with the system
- **Electional astrology**: Add chart selection for optimal timing (doesn't help with transits, so later priority)

---

## North Star Vision

Build a comprehensive astrology application that provides:
1. **Natal Horoscope Generator**: Personalized birth chart interpretation
2. **Transit Report Generator**: Targeted transit analysis by area of life and timeframe
3. **Additional Timing Techniques**: Zodiacal releasing, annual profections, and other traditional methods
4. **Interactive Chat Interfaces**: Two rolling conversation modes
   - **Horoscope Inquirer**: Chat about natal chart, personality, ideal vocation
   - **Transit/Advice Chatbot**: Chat about current situation, transits, and advice

**Ultimate Goal**: Make traditional/Hellenistic astrology insights accessible through natural conversation, grounded in authoritative sources (Brennan, Hand, George, Brady, Greene).

**User Context**: Deep astrology expertise, limited coding experience. Need expert technical guidance to implement vision.

**Workflow**: Start in Claude Code → migrate to web/Telegram if successful

---

## Current State Assessment

### What We Already Have ✅

**Infrastructure (Production-Ready)**:
- **RAG Database**: 2,249 chunks from traditional sources (104MB)
  - Sources: Brennan, Hand, George, Brady, Mason
  - **New source to add**: "The Horoscope in Manifestation" (Stage -1)
- **Chart Analyzer**: Complete natal analysis with dignities, sect, strength scores
- **Transit Calculator**: Verified astronomical calculations via Swiss Ephemeris
- **Interpretation Builder**: RAG query system for traditional delineations
- **Helper Scripts**: ephemeris_helper.py, astrology_reference.py, chart_analyzer.py

**Tech Stack**:
- Python 3.x
- OpenAI API (embeddings only for RAG database)
- **Interpretation/Synthesis**: Claude Code agents (natal-interpreter, transit-analyzer)
  - No external API calls needed for MVP
  - Agent instructions serve as approved "prompts"
  - Can migrate to GPT-5 API later if desired
- pyswisseph (Swiss Ephemeris)
- Local file-based storage
- Traditional/Hellenistic compliance

**Documentation**:
- Working agents (natal-interpreter, transit-analyzer workflows documented)
- Design documents for transit interpretation enhancement
- Comprehensive CLAUDE.md with all systems cataloged

### What We Need to Build 🔨

**Orchestration Layer**:
- Session manager to tie existing pieces together
- Multiple mode handlers (horoscope, transits, timing techniques)
- Prompt engineering for quality output
- CLI interface (initially)
- Two separate rolling chat interfaces

**Additional Components**:
- Process new reference book into RAG database
- Assess existing references for redundancy
- Research and implement additional timing techniques
- Generate reports to `/reports/` folder

---

## Recommended Technical Approach

### Architecture: Session-Based Command System

**Mental Model**: Like a doctor's appointment
- Doctor reviews your file at start (loads natal chart + base analysis)
- You tell them what you need (horoscope, transit report, timing analysis, or ask questions)
- They pull relevant info and give you specific answers
- Your file stays loaded the whole visit (session persists)

### System Components

```
Session Manager (Orchestrator)
├── Loads natal chart at session start
├── Maintains session context
└── Routes commands to appropriate modules
    ├── Mode 1: Natal Horoscope Generator
    ├── Mode 2: Transit Report Generator
    ├── Mode 3+: Additional Timing Techniques (zodiacal releasing, profections, etc.)
    ├── Chat Mode A: Horoscope Inquirer (chat about natal chart)
    └── Chat Mode B: Transit/Advice Chatbot (chat about transits + current situation)
        └── All modules use:
            ├── chart_analyzer.py
            ├── transit_calculator.py
            ├── interpretation_builder.py (RAG)
            ├── ephemeris_helper.py
            └── astrology_reference.py
```

### Mode Breakdown

**Mode 1: Natal Horoscope Generator**
- Input: Birth data file path
- Process:
  1. Generate seed info (natal analysis with dignities, sect, strength)
  2. Query RAG for each planet's interpretation
  3. Synthesize narrative with LLM (GPT-5)
- Output: Comprehensive natal horoscope
  - Format: Plain language, moderate astrology terminology
  - Best practices: Use Brennan and Liz Greene methods
  - Include: Planetary strength table
  - No chart diagram needed
  - **Length**: To be researched during implementation
  - Save to `/reports/`
- Research during build: Tone, length, sections, depth

**Mode 2: Personalized Transit Report**
- Input: Area of life + timeframe (days)
- Process:
  1. Generate seed info (current transits, aspects to natal)
  2. Filter transits by area of life (map to houses)
  3. Query RAG for each relevant transit
  4. Synthesize targeted report with advice
- Output: Transit report scaled to important information
  - Save to `/reports/`
- **Design to be researched**: Format, prioritization, advice style

**Mode 3+: Traditional Timing Techniques** (CLI commands)
- Based on Stage 0 research (see findings above)
- **Core Techniques** (Must implement):
  1. Annual Profections - Time-lord activation (essential for transit filtering)
  2. Zodiacal Releasing - Major life chapter periods
  3. Secondary Progressions - Inner development timeline
- **Optional Techniques** (Post-MVP):
  4. Solar Returns - Annual forecast chart
  5. Planetary Returns - Jupiter/Saturn cycles
- Each technique becomes a CLI command
- All contribute context for Transit/Advice Chatbot

**Chat Mode A: Horoscope Inquirer**
- Rolling conversation about natal chart
- User asks: personality, ideal vocation, chart placements
- AI assesses question, retrieves relevant data, answers directly
- **Chat history length**: To be researched
- Session-aware (natal chart loaded)

**Chat Mode B: Transit/Advice Chatbot**
- Generate transit report first
- Then rolling conversation about report + current situation
- User asks: current transits, timing, advice for specific situations
- AI pulls from transit report + timing techniques + RAG database
- Gives advice based on traditional literature
- Session-aware (natal chart + transit report loaded)

**Future**: Combine both chat modes once they work independently

---

## Staged Implementation Plan

### Stage -1: RAG Database Enhancement
**Timeline**: 2-3 days
**Goal**: Process new reference and optimize database

**Tasks**:
1. **Process "The Horoscope in Manifestation"**:
   - Use astrology-rag-builder agent
   - Extract text from PDF
   - Create semantic chunks (200-800 tokens)
   - Generate embeddings
   - Add to RAG database
   - Tag with metadata (source, author, tradition, content_type)

2. **Assess All References for Redundancy**:
   - Current references:
     1. Hellenistic Astrology (Chris Brennan)
     2. Astrology and the Authentic Self (Demetra George)
     3. Planets in Transit (Robert Hand)
     4. Predictive Astrology (Bernadette Brady)
     5. Delineation of Progressions (Sophia Mason)
     6. **NEW**: The Horoscope in Manifestation
   - Question: Can we remove any redundant sources to lighten the load?
   - Evaluate:
     - Coverage overlap
     - Quality of content
     - Tradition alignment
     - Usage in queries
   - Document findings
   - Remove or archive low-value sources

**Success Criteria**:
- New book successfully added to RAG database
- Redundancy assessment complete
- Database optimized for performance
- Documentation updated

**Deliverables**:
- Updated RAG database (JSONL file)
- Redundancy assessment report
- Recommendations for which sources to keep/remove

---

### Stage 0: Research Timing Techniques ✅
**Timeline**: 1-2 days
**Status**: COMPLETE (2025-10-04)
**Goal**: Identify which traditional timing techniques to implement as CLI modes

**Research Findings**:

**MUST IMPLEMENT** (Core Mode 3+ Techniques):
1. **Annual Profections** ⭐⭐⭐⭐⭐ - ESSENTIAL
   - Time-lord activation system (1 house per year of life)
   - Required for Hephaestio's 7-factor transit analysis
   - Lord of year determines CRITICAL vs NORMAL tier transits
   - Well-documented: Brennan Ch. 17 (17 pages)
   - Complexity: LOW (~100 lines, no ephemeris needed)
   - Implement FIRST in Stage 1.4

2. **Zodiacal Releasing** ⭐⭐⭐⭐⭐ - HIGH PRIORITY
   - Major life chapter periods from Lot of Fortune/Spirit
   - Peak periods (angular triads) for opportunities
   - Well-documented: Brennan Ch. 18 (38 pages)
   - Complexity: MEDIUM-HIGH (~300 lines, ephemeris needed)
   - Implement SECOND in Stage 1.4

3. **Secondary Progressions** ⭐⭐⭐⭐ - MEDIUM PRIORITY
   - Inner development timeline (1 day = 1 year)
   - Progressed Moon shows emotional focus
   - Well-documented: Entire Mason book, Brennan mentions
   - Complexity: MEDIUM (~200 lines, ephemeris needed)
   - Implement THIRD in Stage 1.4

**NICE-TO-HAVE** (Post-MVP Enhancements):
4. **Solar Returns** ⭐⭐⭐ - Annual forecast chart
   - Documented: George Ch. 12
   - Complexity: MEDIUM (~200 lines)
   - Implement FOURTH or later

5. **Planetary Returns** ⭐⭐ - Jupiter/Saturn major cycles
   - Limited specific coverage in RAG
   - Complexity: MEDIUM (~150 lines)
   - Implement FIFTH or skip for MVP

**NOT RECOMMENDED** (Redundant or Poorly Documented):
- ❌ Lunar phases/returns - Redundant with Mode 2 transits
- ❌ Firdaria - Poor RAG coverage (1 mention only)
- ❌ Primary directions - Extreme complexity, minimal RAG coverage

**Key Insight**: Annual profections is REQUIRED, not optional, because:
- Dorotheus/Anubio state only lord of year transits manifest as events
- Transit interpretation enhancement (design doc) requires it
- Foundation for entire transit priority system

**Deliverables**: ✅
- `/docs/timing_techniques_plan.md` created (comprehensive research)
- Priority implementation order defined
- Integration with Transit/Advice Chatbot designed
- CLI command structure planned
- This update to session_goals.md

**Success Criteria**: ✅
- Clear understanding of which techniques add value
- Implementation roadmap defined
- Ready to proceed to Stage 1

---

### Stage 1: Build Natal Horoscope System (Mode 1) ✅
**Timeline**: COMPLETE
**Goal**: Working natal horoscope generator with PDF output
**Status**: ✅ COMPLETE - Multi-profile support, automated generation, PDF output working

**IMPORTANT**: All agent instructions (for horoscope generation, transit reports, chat responses) must be shown to user for approval before agents are created. Agent instructions serve as the "prompts" that control output quality and style.

**Sub-stages**:

### Stage 2: Build Life Arc Report System (Mode 2) ✅
**Timeline**: COMPLETE
**Goal**: Working life arc timeline generator (ages 0-100) with narrative interpretation
**Status**: ✅ COMPLETE - Enhanced with convergence detection and narrative chapter structure

**Major Accomplishments**:
1. ✅ **Timing Technique Calculators Built**:
   - Annual profections (12-year cycles)
   - Zodiacal Releasing Fortune/Spirit L1 (skip L2 for noise reduction)
   - Firdaria (75-year Persian time-lord system, major + sub-periods)
   - Planetary returns (Jupiter, Saturn, Uranus opposition)
   - Progressed Sun sign changes (every ~30 years)

2. ✅ **Unified Timeline Generator**:
   - `life_arc_generator.py` integrates 5 core timing techniques
   - Returns unified timeline data with all techniques synchronized
   - Includes convergence detection (point-based scoring)

3. ✅ **Convergence Detection System**:
   - TIER 1 (20pts): ZR L1 transitions, Progressed Sun sign changes
   - TIER 2 (10-15pts): Saturn return, Uranus opposition, Firdaria major
   - TIER 3 (1-5pts): Jupiter return, Firdaria sub, annual profection
   - Thresholds: 25+ = MAJOR, 15-24 = SIGNIFICANT, 8-14 = NOTABLE
   - Tested: 6 major, 11 significant, 7 notable events in 100-year lifespan

4. ✅ **Narrative Interpretation Agent**:
   - life-arc-interpreter agent rewritten for storytelling approach
   - Chapter structure: Each ZR L1 period = one chapter
   - Convergent events = subheadings within chapters
   - "Current Situation: Age X" sub-chapter for present moment
   - Ages 0-100 treated equally (past and future both narrative)
   - RAG-integrated for traditional grounding

5. ✅ **Profile Settings Simplified**:
   - Single-line format: `variable: true|false // description`
   - Easier scanning and modification
   - Lives in profile.md file

6. ✅ **10 Lots Integrated**:
   - All calculated lots accessible in timeline
   - 3 new lots added: Exaltation, Marriage, Children
   - 7 existing lots: Fortune, Spirit, Eros, Necessity, Courage, Victory, Basis

7. ✅ **Complete Testing**:
   - Full 0-100 report generated for darren profile
   - 6 chapters organized by ZR L1 periods
   - PDF output working (157.9 KB)
   - Output directory structure corrected: `profiles/{profile}/output/`

**Files Created**:
- `/scripts/profections_calculator.py`
- `/scripts/zodiacal_releasing.py`
- `/scripts/firdaria_calculator.py`
- `/scripts/life_arc_generator.py` (enhanced)
- `/scripts/life_arc_synthesis_simplified.py`
- `/scripts/test_convergence.py`
- `/scripts/seed_data_generator.py` (enhanced with 3 new lots)
- `/.claude/agents/life-arc-interpreter.md` (rewritten for narrative structure)
- `/docs/PROFECTIONS_GUIDE.md`
- `/docs/ZODIACAL_RELEASING_GUIDE.md`
- `/docs/LIFE_ARC_GUIDE.md`

### Stage 3: Build Transit Report System (Mode 3) ⏳
**Timeline**: PENDING
**Goal**: Working transit report generator with current and future transit analysis
**Status**: ⏳ PENDING - Ready to begin after Mode 2 completion
**Design Documents Available**:
- `/docs/transit_interpretation_design.md` - Transit enhancement research
- `/docs/transit_staged_implementation.md` - Transit rollout plan

**Transit Report Requirements**:
- **First**: Create transit-analyzer agent using agent-creator
  - Define agent role, advice style, prioritization approach → User approves agent instructions
  - Agent instructions control how transits are synthesized and advice is given
- **Then**: Build `transit_report.py` (~200 lines)
  - Script calculates transits to natal
  - Script filters by importance and timeframe
  - Script uses annual profections for transit priority (lord of year = critical tier)
  - Script queries RAG for transit interpretations
  - Script calls transit-analyzer agent to synthesize
  - Script formats and saves report
- **Research during build**:
  - **Format**: How to structure transit report?
  - **Prioritization**: Use Hephaestio's 7-factor system + lord of year
  - **Timeframe handling**: Current transits + upcoming (30-90 days)
  - **Advice format**: Actionable guidance grounded in traditional texts
  - **Output**: Save to `profiles/{profile}/output/transit_report_[date].md`
- **Testing phase**: Generate test reports, evaluate quality, refine agent instructions if needed
- **Status**: PENDING - Design documents complete, ready for implementation

### Stage 4: Build Interactive Chat Modes ⏳
**Timeline**: PENDING
**Goal**: Rolling conversation interfaces for natal chart and transit questions
**Status**: ⏳ PENDING - To be implemented after Mode 3 complete

---

### Stage 5: Build Two Separate Rolling Chats
**Timeline**: 1-2 weeks
**Goal**: Interactive conversation modes for natal chart and transits

**IMPORTANT**: All chat agent instructions and function calling configurations must be shown to user for approval before agents are created. These agents will handle interactive conversations about natal charts and transits.

**Why two separate chats?**
- Different contexts and purposes
- Easier to build and test independently
- Can combine later once both work

#### 3.1: Chat Mode A - Horoscope Inquirer
- Build `horoscope_chat.py` (~200 lines)
- **Purpose**: Rolling conversation about natal chart
- **User questions**:
  - "What does Mars in Aries in 9th house mean for me?"
  - "What's my ideal vocation based on my chart?"
  - "How do I work with Saturn in my 10th house?"
  - "What are my chart's dominant themes?"
- **Architecture**: OpenAI function calling + session state
- **Functions AI can call**:
  - `get_planet_analysis(planet)` - Get planet position, dignity, strength
  - `get_aspect_between(planet1, planet2)` - Calculate aspect
  - `query_rag(query_string)` - Search traditional texts
  - `get_house_topics(house_num)` - House significations
  - `calculate_dignity(planet, sign)` - Dignity status
- **Chat history**: To be researched - reasonable number of messages to keep?
- **Session state**: Natal chart stays loaded
- **Output**: Conversational, cites sources

#### 3.2: Chat Mode B - Transit/Advice Chatbot
- Build `transit_chat.py` (~200 lines)
- **Purpose**: Rolling conversation about current situation and transits
- **Workflow**:
  1. Generate transit report first (Mode 2)
  2. User can then ask questions about report + current situation
- **User questions**:
  - "What transits are affecting my career right now?"
  - "When will this difficult period end?"
  - "How should I approach this Saturn transit?"
  - "What opportunities are coming up in the next 3 months?"
- **Context available**:
  - Pre-generated transit report
  - All timing technique data (zodiacal releasing, profections, etc.)
  - Natal chart analysis
  - RAG database for traditional advice
- **Functions AI can call**:
  - `get_transit_details(planet, aspect, natal_planet)` - Detailed transit info
  - `get_timing_technique(technique_name)` - Zodiacal releasing, profections, etc.
  - `query_rag_advice(situation)` - Traditional advice for situations
  - `calculate_future_transits(planet, days)` - Upcoming transits
- **Chat history**: Research needed
- **Output**: Advice based on traditional literature, grounded in transits

#### 3.3: Integration
**CLI Interface with Chats**:
```bash
Commands:
  horoscope - Generate full natal horoscope
  transits <area> <days> - Transit report
  [timing techniques...]
  chat-horoscope - Start horoscope chat session
  chat-transits - Start transit chat session (generates report first)
  exit - End session

> chat-horoscope
Starting horoscope chat...
Ask me anything about your natal chart.

You: What does Mars in Aries mean for me?
AI: Mars in Aries in your 9th house represents Mars in its domicile...
[Conversation continues]

You: exit
Exiting horoscope chat.

> chat-transits
Generating current transit report...
Report saved to /reports/transit_report_2025-10-04.md
Starting transit chat...
Ask me about your current transits or situation.

You: What's happening with Saturn right now?
AI: Saturn is currently transiting...
[Conversation continues with context from report + timing techniques]
```

**Success Criteria**:
- Both chat modes working independently
- AI retrieves correct data via function calling
- Answers are accurate, well-cited, traditional
- Conversation flows naturally
- Can maintain context across multiple questions
- No hallucinations or made-up aspects

**Testing Phase**:
- Test each chat mode extensively
- Evaluate answer quality and accuracy
- Test conversation memory and context
- Iterate on function calling prompts
- Adjust chat history length as needed

---

### Stage 4: Refinement & Iteration
**Timeline**: Ongoing (1-2 weeks minimum)
**Goal**: Improve output quality through real-world use

**Process**:
1. **Use CLI yourself daily** for 1-2 weeks
2. **Document feedback**:
   - What works well?
   - What's confusing or inaccurate?
   - What features are missing?
   - What prompts need improvement?
3. **Iterate on**:
   - Prompt engineering (tone, depth, citations)
   - RAG query relevance
   - Output formatting
   - Error handling
   - GPT-5 settings (if needed)
4. **Add features** as needs emerge:
   - Save reports to PDF
   - Export chat transcripts
   - Multiple birth chart support
   - Historical transit lookups
5. **Validate** each improvement before moving on

**Success Criteria**:
- Output quality matches your standards
- Comfortable using it regularly
- Interpretations are accurate and traditional
- Chat modes provide useful advice
- Documented refinements in `/docs/refinement_log.md`

---

## Future Stages (Post-MVP)

### Stage 5: Web Interface (Optional)
**Timeline**: 1-2 weeks
**Goal**: User-friendly GUI for non-CLI users

**Recommended Framework**: Streamlit or Gradio
- Built for Python, zero HTML/CSS/JS required
- Quick to build and deploy

**Features**:
- File upload for birth data
- Buttons for each mode
- Text areas for chat
- Download buttons for reports (Markdown/PDF)
- Session persistence

**Deployment Options**:
- Local only (run on your machine)
- Cloud hosting (Streamlit Cloud, Hugging Face Spaces)
- Share with others for testing

### Stage 6: Telegram Bot (Optional)
**Timeline**: 1 week
**Goal**: Mobile-friendly interface with notifications

**Why Telegram?**:
- Mobile-friendly
- No app store approval needed
- Easy to share with friends/clients
- Can add scheduled notifications later
- Good for adjusting settings on mobile

**Features**:
- Same commands as CLI
- Persistent chat sessions
- Push notifications (future)
- Same backend logic, different interface layer

---

## Technology Stack (Detailed)

### Core Technologies
- **Runtime**: Python 3.x
- **Interpretation/Synthesis**: Claude Code agents
  - **natal-interpreter**: Synthesizes natal horoscopes from RAG data
  - **transit-analyzer**: Synthesizes transit reports and advice
  - **Chat agents** (Stage 3): Interactive conversation modes
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
- **(Stage 5)** streamlit or gradio: Web interface
- **(Stage 6)** python-telegram-bot: Telegram interface

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
  - agent-creator: Conversational agent creation
- **Interpretation agents** (to be created in Stage 1):
  - natal-interpreter: Natal horoscope synthesis
  - transit-analyzer: Transit report synthesis
- **Chat agents** (to be created in Stage 3):
  - horoscope-chat: Interactive natal chart conversations
  - transit-chat: Interactive transit/advice conversations

---

## Output Specifications

### Horoscope Output Design

**Research during Stage 1 build**:
1. **Tone**: Plain language, moderate astrology terminology
2. **Style**: Use best practices from Chris Brennan and Liz Greene (query RAG database)
3. **Length**: To be researched during implementation (don't pre-specify)
4. **Structure**: TBD during research
   - Suggested: Overview → Planets (by strength) → Major aspects → House emphasis → Synthesis
5. **Citations**: Source attribution for all interpretations
6. **Visuals**:
   - Planetary strength table (yes)
   - Chart diagram (not needed)

**Example strength table**:
```
Planet Strength Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Planet    Sign      House  Dignity    Strength
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mars      Aries     9      Domicile   9.75/10
Jupiter   Pisces    7      Domicile   8.50/10
Sun       Libra     2      Detriment  4.25/10
[...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Transit Report Design

**Research during Stage 1 build**:
- Format and structure
- Prioritization methodology
- How many transits to include
- Advice format (actionable vs. general)
- Timeframe presentation
- Citation style

### Chat Interface Design

**Research needed**:
1. **Function Calling**: Which functions should AI have access to?
   - Horoscope chat: planet analysis, aspects, dignities, RAG queries
   - Transit chat: transit details, timing techniques, advice, future transits
2. **Conversation Memory**: How many messages to retain?
   - Start with 10 messages?
   - Test and adjust
3. **Error Handling**: What if question is unanswerable from chart?
   - Graceful fallback: "I don't have enough information to answer that accurately. Can you rephrase?"

---

## Success Factors

### What Will Make This Succeed?

1. **Quality Output**: Interpretations must be accurate, well-cited, traditional
2. **Ease of Use**: Even non-technical users can generate reports
3. **Your Daily Use**: If you use it regularly, it's working
4. **Incremental Validation**: Test each stage before moving to next
5. **Traditional Compliance**: All interpretations grounded in sources
6. **Good Prompts**: Well-engineered prompts for GPT-5
7. **Comprehensive Timing**: Multiple techniques give fuller picture
8. **Separate Chat Modes**: Focused contexts prevent confusion

### What Could Derail This?

1. **Prompt Engineering**: If LLM output is poor quality, need to iterate
2. **RAG Coverage Gaps**: If database lacks key interpretations, need to expand
3. **Over-Engineering**: Building complex features before validating basics
4. **Scope Creep**: Adding features instead of perfecting core modes
5. **Settings Issues**: Wrong GPT-5 settings could degrade output

**Mitigation**:
- Start simple (Stage -1, 0, 1)
- Validate quality at each stage
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

## Current Status

**Stage**: Mode 2 Complete - Ready for Mode 3
**Completed Stages**:
- Stage -1 ✅ (RAG Database Enhancement)
- Stage 0 ✅ (Research Timing Techniques)
- Stage 1 ✅ (Build Natal Horoscope System - Mode 1)
- Stage 2 ✅ (Build Life Arc Report System - Mode 2)
**Current Work**: Documentation updates complete
**Next Action**: Begin Mode 3 (Transit Report System) when ready
**Recent Infrastructure Improvements** (2025-10-04):
- Strengthened documentation automation system
- Added proactive triggers to docs-updater-astrology agent ✅
- Added proactive triggers to astrology-rag-builder agent ✅
- Created agent-creator meta-agent ✅
  - Helps user create new custom agents conversationally (instead of /agents command)
  - Gathers requirements, drafts definitions, iterates, ensures quality
  - Automatically triggers docs-updater-astrology after creating agents
  - File: `.claude/agents/agent-creator.md`
  - Makes agent creation collaborative and template-matched
- All docs now update automatically after major steps
- All critical agents now trigger automatically (no manual prompts needed)
- Clear division of labor between workflow-planner-2 and docs-updater-astrology
- This ensures session_goals.md, CLAUDE.md, and agent READMEs stay synchronized

---

## Questions for Workflow Planner (Ongoing)

As we build, consult workflow-planner-2 agent for:
- Architecture decisions
- Framework/library recommendations
- Prompt engineering strategies
- Error handling patterns
- Testing approaches
- Deployment options
- GPT-5 settings optimization

---

## Documentation Strategy

- **This file (session_goals.md)**: High-level vision, strategic direction, simple
- **/docs/**: Detailed design docs (horoscope_design.md, timing_techniques_plan.md, chat_design.md, etc.)
- **CLAUDE.md**: Current state, completed work, system catalog
- **/reports/**: All generated horoscopes, transit reports, timing analyses

**Ownership**:
- **workflow-planner-2**: Creates session_goals.md structure, defines stages, makes recommendations (does NOT mark progress)
- **docs-updater-astrology**: Marks progress in session_goals.md, updates CLAUDE.md, maintains current state (does NOT change plan)
- **Implementation agents**: Document detailed specs in /docs/

**Automatic Updates**: After every major step, docs-updater-astrology automatically updates all three documentation types (session_goals.md progress + CLAUDE.md + READMEs). No manual prompts needed.

---

*This is a living document. Update as we learn and iterate.*
