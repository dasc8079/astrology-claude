# Workflows Visual Guide

**Purpose**: Visual flowcharts showing how conversations become interpretations

**Last Updated**: 2025-10-11

**Goal**: Conversational astrology interface where you ask questions and get accurate, high-quality interpretations using specialized agents and tools.

---

## The Vision: Conversational Astrology Interface

```
┌─────────────────────────────────────────────────────────────┐
│  YOU: "What's happening astrologically in March 2026?"      │
│                                                              │
│  SYSTEM: [routes through mode-orchestrator]                 │
│          [detects: transit request, short-term, darren]     │
│          [runs transit calculations]                        │
│          [invokes transit-analyzer-short]                   │
│          [generates movement-based report]                  │
│                                                              │
│  OUTPUT: Professional transit report showing March themes   │
│          (markdown + optional PDF)                          │
└─────────────────────────────────────────────────────────────┘

BENEFIT: Reliable, consistent, high-quality output using
         specialized agents vs. ad-hoc prompting
```

---

## Core Workflow: Conversation → Interpretation

```
┌──────────────────────────────────────────────────────────────┐
│                  YOUR QUESTION / REQUEST                     │
└──────────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│               mode-orchestrator (ALWAYS)                     │
│  • Detects what you need (natal/life arc/transits/timing)   │
│  • Validates profile exists                                  │
│  • Checks seed data availability                             │
└──────────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│              RUNS CALCULATIONS (if needed)                   │
│  • seed_data_generator.py (if missing)                       │
│  • transit_calculator.py (for transits)                      │
│  • life_arc_generator.py (for life arc)                      │
└──────────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│           INVOKES SPECIALIZED AGENT                          │
│  • natal-interpreter (birth chart)                           │
│  • life-arc-interpreter (lifetime timeline)                  │
│  • transit-analyzer-short (1-4 months)                       │
│  • transit-analyzer-long (1-5 years)                         │
└──────────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│          AGENT GENERATES INTERPRETATION                      │
│  • RAG database queries (pulls traditional knowledge)        │
│  • Seed data analysis (chart facts)                          │
│  • Narrative synthesis (psychological depth)                 │
│  • Structured output (following templates)                   │
└──────────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│               SAVES OUTPUT + OFFERS PDF                      │
│  • Markdown: /profiles/{name}/output/{report}.md            │
│  • PDF (optional): {report}.pdf                              │
└──────────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│                  RETURNS TO YOU                              │
│  • File paths                                                │
│  • Success confirmation                                      │
│  • Ready for next question                                   │
└──────────────────────────────────────────────────────────────┘
```

---

## Request Type Detection: What Triggers Which Agent?

```
┌─────────────────────────────────────────────────────────────┐
│                  YOUR REQUEST                                │
└─────────────────────────────────────────────────────────────┘
                          ↓
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        │                 │                 │
   ┌────▼─────┐    ┌──────▼──────┐    ┌────▼─────┐
   │ NATAL?   │    │ LIFE ARC?   │    │ TRANSITS?│
   │          │    │             │    │          │
   │ Keywords:│    │ Keywords:   │    │ Keywords:│
   │ • chart  │    │ • timeline  │    │ • transit│
   │ • birth  │    │ • life story│    │ • what's │
   │ • natal  │    │ • ages X-Y  │    │   happening│
   │ • horoscope│  │ • chapters  │    │ • dates  │
   └──────────┘    └─────────────┘    └──────────┘
        │                 │                 │
        ▼                 ▼                 ▼
  natal-        life-arc-         ┌──────────────┐
  interpreter   interpreter       │ Which type?  │
                                  │              │
                                  │ • Short      │
                                  │   (1-4 mo)   │
                                  │ • Long       │
                                  │   (1-5 yrs)  │
                                  └──────────────┘
                                        │
                         ┌──────────────┴──────────────┐
                         │                             │
                         ▼                             ▼
               transit-analyzer-        transit-analyzer-
                    short                     long
```

---

## Example Workflow 1: "Generate natal horoscope for darren"

```
1. YOU ASK
   ↓
   "Generate natal horoscope for darren"

2. mode-orchestrator DETECTS
   ↓
   • Mode: NATAL (keywords: "natal", "horoscope")
   • Profile: darren
   • Action: Generate birth chart interpretation

3. VALIDATION
   ↓
   • Check: Does /profiles/darren/ exist? ✓
   • Check: Does seed_data.json exist? ✓
   • Ready to proceed

4. INVOKE AGENT
   ↓
   • Launch natal-interpreter agent
   • Pass: seed_data.json content
   • Agent queries RAG database for traditional interpretations
   • Agent synthesizes psychological narrative

5. GENERATE OUTPUT
   ↓
   • Create markdown with chart-based template
   • Sections: Overview, Sect, Ascendant, Planets, Houses, Aspects, Synthesis
   • Save: /profiles/darren/output/natal_horoscope_darren_2025-10-11.md

6. OFFER PDF
   ↓
   • "Would you like a PDF version?"
   • If yes: Run pdf_generator.py --report-type natal

7. RETURN
   ↓
   • "✓ Natal horoscope generated!"
   • File: /profiles/darren/output/natal_horoscope_darren_2025-10-11.md
   • PDF: (if requested)
```

---

## Example Workflow 2: "What's happening in March 2026?"

```
1. YOU ASK
   ↓
   "What's happening in March 2026?"

2. mode-orchestrator DETECTS
   ↓
   • Mode: TRANSITS (keywords: "what's happening", date)
   • Type: SHORT (1 month implied)
   • Profile: darren (default)
   • Date range: March 1-31, 2026

3. VALIDATION
   ↓
   • Check: Does /profiles/darren/ exist? ✓
   • Check: Does seed_data.json exist? ✓
   • Check: Transit data for March 2026? ✗ (needs calculation)

4. RUN CALCULATIONS
   ↓
   • Execute: transit_calculator.py --profile darren
              --start-date 2026-03-01 --end-date 2026-03-31
              --report-type short
   • Calculates: All 10 planets, all tiers, daily scoring
   • Saves: transit_data_darren_2026-03-01_to_2026-03-31.json

5. INVOKE AGENT
   ↓
   • Launch transit-analyzer-short agent
   • Pass: transit data JSON + date range
   • Agent detects movements (typically 2-4 thematic sections)
   • Agent queries RAG for transit interpretations
   • Agent synthesizes movement-based narrative

6. GENERATE OUTPUT
   ↓
   • Create markdown with movement-based template
   • Sections: Summary Synthesis, Movement I, Movement II, etc., Technical Appendix
   • Save: /profiles/darren/output/transit_report_darren_short_2026-03-01_to_2026-03-31.md

7. OFFER PDF
   ↓
   • "Would you like a PDF version?"

8. RETURN
   ↓
   • "✓ Transit report for March 2026 generated!"
   • File path provided
   • Ready for follow-up questions
```

---

## Example Workflow 3: "When should I apply for this job?"

```
1. YOU ASK
   ↓
   "When should I apply for this job?"

2. mode-orchestrator DETECTS
   ↓
   • Mode: TRANSITS (timing question)
   • Type: SHORT (near-term decision implied)
   • Profile: darren (default)
   • Need: Auspicious dates for application

3. CLARIFICATION (if needed)
   ↓
   • "What timeframe are you considering? (e.g., next 3 months)"
   • YOU: "Next 3 months"
   • Date range: Now → 3 months ahead

4. RUN CALCULATIONS
   ↓
   • Execute: transit_calculator.py for 3-month range
   • Identifies most auspicious days
   • Scores each day based on transits

5. INVOKE AGENT
   ↓
   • Launch transit-analyzer-short agent
   • Agent generates full report showing:
     - Most auspicious days (highlighted)
     - Challenging days to avoid
     - Movement narratives explaining themes

6. GENERATE OUTPUT
   ↓
   • Report highlights best application dates
   • Explains why those dates are favorable
   • Shows dates to avoid

7. RETURN ANSWER
   ↓
   • "Based on your transits, the best days to apply are:"
   • Lists top 3-5 dates with brief explanations
   • Provides full report for context
   • "Would you like the full report as PDF?"
```

---

## Example Workflow 4: "Tell me about my life from ages 35-45"

```
1. YOU ASK
   ↓
   "Tell me about my life from ages 35-45"

2. mode-orchestrator DETECTS
   ↓
   • Mode: LIFE ARC (keywords: "life", age range)
   • Profile: darren (default)
   • Ages: 35-45 (10-year span)

3. VALIDATION
   ↓
   • Check: Does /profiles/darren/ exist? ✓
   • Check: Does seed_data.json exist? ✓
   • Check: Life arc data for ages 35-45? ✗ (needs calculation)

4. RUN CALCULATIONS
   ↓
   • Execute: life_arc_generator.py --profile darren
              --start-age 35 --end-age 45
   • Calculates: All 5 timing techniques
   • Detects: Convergence points (major events)
   • Saves: life_arc_data_darren_ages_35-45.json

5. INVOKE AGENT
   ↓
   • Launch life-arc-interpreter agent
   • Pass: life arc data JSON + age range
   • Agent identifies: ZR L1 chapters in this range
   • Agent detects: Major transitions/convergences
   • Agent queries: RAG for timing technique interpretations
   • Agent synthesizes: Narrative life story

6. GENERATE OUTPUT
   ↓
   • Create markdown with timeline-based template
   • Structure: Chapter-based (by ZR L1 periods)
   • Sections: Overview, Chapters (with convergence sub-sections), Current Situation
   • Save: /profiles/darren/output/life_arc_interpretation_darren_ages_35-45.md

7. OFFER PDF
   ↓
   • "Would you like a PDF version?"

8. RETURN
   ↓
   • "✓ Life arc report for ages 35-45 generated!"
   • Summary: "You experience TWO major life chapter changes in this period..."
   • File path provided
```

---

## Example Workflow 5: "Tell me about that June 2026 period" (Period of Interest Mode)

```
1. YOU ASK
   ↓
   "Tell me about that June 2026 period"
   (User has already run long-term report which flagged June 2026 with score: -45)

2. mode-orchestrator DETECTS
   ↓
   • Mode: TRANSIT (keywords: "June 2026", "that period")
   • Sub-mode: PERIOD OF INTEREST (user references flagged period)
   • Profile: darren (default)
   • Focus date: 2026-06-08 (approximate center of flagged period)
   • Score: -45 (from long-term report)

3. VALIDATION
   ↓
   • Check: Does /profiles/darren/ exist? ✓
   • Check: Does seed_data.json exist? ✓
   • Check: Transit data around June 2026? ✗ (needs calculation)

4. IDENTIFY CLUSTER WINDOW
   ↓
   • Load daily quality scores from long-term report
   • Find cluster boundaries:
     - Start: When score concentration begins (June 1, 2026)
     - Peak: Multiple exactness dates close together (June 8, 10, 12)
     - End: When concentration resolves (June 20, 2026)
   • Typical window: 2-6 weeks (in this case: 20 days)

5. RUN CALCULATIONS
   ↓
   • Execute: transit_calculator.py --profile darren
              --start-date 2026-06-01 --end-date 2026-06-20
              --report-type short
   • Calculates: ALL transits during cluster window
   • Categorizes: Applying (building), Exact (peak), Separating (resolving)
   • Gathers: Timing technique activations (profection, ZR, Firdaria)
   • Saves: transit_data_darren_cluster_june_2026.json

6. INVOKE AGENT
   ↓
   • Launch transit-analyzer-short agent in PERIOD OF INTEREST MODE
   • Pass: Transit data JSON + focus date + score + cluster boundaries
   • Agent identifies: ALL transits in cluster (not just one primary)
   • Agent identifies: Convergent timing techniques amplifying
   • Agent queries: RAG for cluster themes (8-12 queries)
     - "Saturn square Moon traditional interpretation"
     - "Mars opposition Sun overlapping themes"
     - "Multiple malefic transits converging"
     - "Navigating difficult transit clusters"
     - etc.
   • Agent synthesizes: Complete cluster narrative (800-1200 words)

7. GENERATE OUTPUT
   ↓
   • Create markdown with period-of-interest template
   • Structure:
     - At a Glance (cluster period, score, key dates, convergent factors)
     - Summary Synthesis (why flagged, what creates significance)
     - The Cluster Period (buildup → peak → resolution narrative)
     - Technical Appendix (all transits, daily scores, timing activations)
   • Save: /profiles/darren/output/transit_cluster_june_2026.md

8. OUTPUT TERMINAL SUMMARY
   ↓
   Generated period-of-interest deep-dive for June 2026 cluster (score: -45).
   Cluster period: June 1-20, 2026 (20 days).
   Key transits: Saturn square Moon (June 8), Mars opposition Sun (June 10), Mercury square Saturn (June 12).
   Convergent factors: Saturn profection year + ZR L2 Scorpio + Firdaria Mars sub-period.
   Key theme: Structural pressure under emotional and physical strain.

9. OFFER PDF
   ↓
   • "Would you like a PDF version?"

10. RETURN
    ↓
    • "✓ Period-of-interest report for June 2026 cluster generated!"
    • Summary: "This 20-day period shows THREE major transits converging..."
    • File path provided
```

---

## Decision Tree: Which Report Type?

```
                        "I want to understand..."
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
           MY BIRTH            MY LIFE          WHAT'S
            CHART             STORY            HAPPENING
                │                 │                 │
                ▼                 ▼                 ▼
        ┌───────────────┐  ┌───────────────┐  ┌────────────┐
        │ NATAL         │  │ LIFE ARC      │  │ TRANSITS   │
        │ HOROSCOPE     │  │ REPORT        │  │            │
        └───────────────┘  └───────────────┘  └────────────┘
                │                 │                 │
                │                 │          ┌──────┴──────┐
                │                 │          │             │
                │                 │     NEAR-TERM      FAR-TERM
                │                 │     (1-4 mo)      (1-5 yrs)
                │                 │          │             │
                ▼                 ▼          ▼             ▼
         natal-          life-arc-   transit-      transit-
         interpreter     interpreter  analyzer-    analyzer-
                                      short        long
                │                 │          │             │
                ▼                 ▼          ▼             ▼
          ┌─────────┐      ┌──────────┐  ┌────────┐  ┌─────────┐
          │ Chart   │      │ Timeline │  │Movement│  │ Chapter │
          │ Sections│      │ Chapters │  │ Based  │  │ Based   │
          └─────────┘      └──────────┘  └────────┘  └─────────┘
                │                 │          │             │
                └─────────────────┴──────────┴─────────────┘
                                  │
                                  ▼
                        MARKDOWN + PDF OUTPUT
```

---

## Verification Workflow: When Output Seems Wrong

```
1. YOU NOTICE ISSUE
   ↓
   "The Saturn return interpretation seems wrong -
    it says positive but it was the hardest period"

2. astrology-output-debugger TRIGGERED
   ↓
   • Proactive verification mode activated
   • Issue: Discrepancy between output and lived experience

3. PHASE 1: Output Analysis
   ↓
   • Reviews the problematic report
   • Identifies claim: "Saturn return average +11.9 (positive)"
   • Flags: Contradicts user statement

4. PHASE 2: Data Verification
   ↓
   • Loads raw transit data from 2017-2019
   • Extracts all Saturn transit scores
   • Finds: All Saturn conjunctions scored as 0 (neutral)
   • Red flag: Should be challenging, not neutral

5. PHASE 3: Workflow Tracing
   ↓
   • Traces through transit_calculator.py logic
   • Finds scoring algorithm: conjunction + dignified = neutral
   • Identifies bug: Saturn conjunctions challenging regardless of dignity

6. PHASE 4: Prompt Review
   ↓
   • Checks agent instructions for scoring guidance
   • Verifies: No explicit Saturn conjunction handling

7. PHASE 5: RAG Database Investigation
   ↓
   • Queries RAG for Saturn return interpretations
   • Confirms: Traditional sources say Saturn returns are challenging
   • Data supports user experience, not scoring

8. PHASE 6: Root Cause Report
   ↓
   FINDING: Scoring algorithm flaw
   - Saturn conjunctions rated neutral (0) when should be challenging
   - Logic: conjunction + dignified planet = neutral
   - Impact: All Saturn period comparisons invalid

   FIX OPTIONS:
   1. Update scoring to treat Saturn conjunctions as challenging
   2. Acknowledge quantitative scoring limitations
   3. Use user's lived experience as primary data

9. DOCUMENT ISSUE
   ↓
   • docs-updater-astrology adds to TROUBLESHOOTING.md
   • Issue documented for future reference

10. RETURN TO USER
    ↓
    • "Found the issue: Scoring algorithm bug..."
    • Explains root cause
    • Provides fix options
    • Validates user's experience
```

---

## Maintenance Workflow: Creating New Agents

```
1. YOU IDENTIFY NEED
   ↓
   "We need an agent for single-event deep-dives"

2. AGENT CREATION
   ↓
   • Use agent-creator OR manually create
   • Define: Purpose, scope, methodology, output format
   • Write: Agent instructions (.claude/agents/event-analyzer.md)

3. TESTING
   ↓
   • Test with sample data
   • Verify output quality
   • Refine agent instructions

4. INTEGRATION
   ↓
   MUST UPDATE (critical):
   • mode-orchestrator.md - Add routing logic
   • AGENTS_REFERENCE.md - Add agent documentation
   • CLAUDE.md - Add to Project Agents section

5. DOCUMENTATION
   ↓
   • Document in CURRENT_WORK.md
   • Add examples to WORKFLOWS_VISUAL.md (this file)
   • Update any relevant guides

6. VERIFICATION
   ↓
   • Test via mode-orchestrator
   • Ensure proactive triggering works
   • Verify output quality with astrology-output-debugger
```

---

## Quick Reference: Common Questions → Actions

| Your Question | What Happens | Output |
|---------------|--------------|--------|
| "Generate natal for darren" | mode-orchestrator → natal-interpreter | Natal horoscope (md + pdf) |
| "Show me ages 30-40" | mode-orchestrator → life-arc-interpreter | Life arc report (md + pdf) |
| "What's happening next month?" | mode-orchestrator → transit-analyzer-short (multi-movement) | Short transit report (md + pdf) |
| "Tell me about that June 2026 period" | mode-orchestrator → transit-analyzer-short (period-of-interest) | Cluster deep-dive (md + pdf) |
| "What's happening around June 8?" | mode-orchestrator → transit-analyzer-short (period-of-interest) | Cluster deep-dive (md + pdf) |
| "Analyze 2025-2030" | mode-orchestrator → transit-analyzer-long | Long transit report (md + pdf) |
| "When should I apply?" | mode-orchestrator → transit-analyzer-short | Report with best dates highlighted |
| "This seems wrong" | astrology-output-debugger | Diagnostic report with fixes |
| "How do I create a profile?" | Direct guidance (no agent) | Instructions + profile template |
| "What is a Saturn return?" | Direct explanation (no agent) | Conceptual answer |

---

## Related Documentation

- **Agent details**: [AGENTS_REFERENCE.md](AGENTS_REFERENCE.md)
- **Script details**: [SCRIPTS_REFERENCE.md](SCRIPTS_REFERENCE.md)
- **Agent coordination**: [AGENT_ORCHESTRATION_GUIDE.md](AGENT_ORCHESTRATION_GUIDE.md)
- **Timing techniques**: [LIFE_ARC_GUIDE.md](LIFE_ARC_GUIDE.md), [TRANSITS_GUIDE.md](TRANSITS_GUIDE.md), [ZODIACAL_RELEASING_GUIDE.md](ZODIACAL_RELEASING_GUIDE.md)

---

**Remember**: The goal is conversational astrology. You ask, mode-orchestrator routes, specialized agents deliver accurate interpretations. This is more reliable than ad-hoc prompting.
