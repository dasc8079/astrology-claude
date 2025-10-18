# Agent Orchestration Guide

**Purpose**: Guide for when and how to use mode-orchestrator and astrology-output-debugger agents

**Last Updated**: 2025-10-11

---

## Overview

The astrology project uses two key orchestration agents that should be used **proactively** to ensure consistent workflow and quality output:

1. **mode-orchestrator** - Routes all astrology interpretation requests to appropriate agents
2. **astrology-output-debugger** - Verifies and debugs interpretation quality

---

## mode-orchestrator: Central Workflow Coordinator

### Purpose

The mode-orchestrator should handle **all astrology interpretation requests**. It manages the complete workflow from profile loading through calculation and interpretation to final output generation.

### Default Workflow (Standard Process)

When generating astrology reports, follow this standard workflow:

**Step 1: Invoke mode-orchestrator**
```
User: "Generate natal horoscope for Sam_P"
Assistant: Uses Task tool to invoke mode-orchestrator
```

**Step 2: mode-orchestrator manages the pipeline**
- Loads profile from `profiles/{name}/profile.md`
- Checks for `output_mode` setting (standard/custom)
- Loads seed data from `profiles/{name}/seed_data/seed_data.json`
  - **Seed data already exists** from initial profile creation
  - **NO need to regenerate** unless birth data changed
  - Contains all astronomical calculations (planets, houses, aspects, dignities)

**Step 3: mode-orchestrator invokes interpreter agent**
- For Mode 1 (Natal): Invokes `natal-interpreter` or `natal-interpreter-experiential`
- For Mode 2 (Life Arc): Invokes `life-arc-interpreter`
- For Mode 3 (Transits): Invokes `transit-analyzer-short` or `transit-analyzer-long`
- Passes seed data + profile settings to interpreter

**Step 4: Interpreter agent generates output**
- Creates synthesis file (accessible narrative): `natal_synthesis_{name}_{date}.md`
- **NOTE**: Process files no longer generated (removed October 2025 for 30-35% token reduction)
- All technical data resides in `seed_data.json`
- Returns synthesis file to mode-orchestrator

**Step 5: mode-orchestrator saves files**
- Saves to `profiles/{name}/output/` directory
- Returns file paths to user
- Offers PDF generation option

**Key Points**:
- **Always use mode-orchestrator** - Don't manually invoke interpreter agents
- **Seed data persists** - No need to regenerate unless birth data changes
- **Custom mods handled automatically** - Interpreter reads `output_mode` from profile.md
- **Consistent file naming** - Orchestrator ensures standard naming conventions

### When to Use (Proactively)

**Direct Report Requests**:
- "Generate natal for darren"
- "Run the transit report for next month"
- "I want a life arc report"
- "Give me a natal horoscope for [name]"

**Conversational Interpretation Requests**:
- "What's happening astrologically in March 2026?"
- "Analyze the dates around April 1-8"
- "How do transits look for next year?"
- "What does my chart say about ages 35-45?"
- "Tell me about my Saturn return"

**Timing & Predictive Questions**:
- "When should I apply for this job?" (requires transit/timing analysis)
- "What major life changes are coming?" (life arc + transits)
- "How long will this difficult period last?" (transit analysis)
- "When is a good time to [action]?" (transit windows)

**Analysis Comparison Requests**:
- "How many challenging transits in [period]?"
- "Compare Saturn return to current period"
- "Which year was harder astrologically?"

### Key Principle

**If the user's question requires accessing seed data, running calculations, or generating interpretations, route through mode-orchestrator.**

Don't manually invoke interpreter agents (natal-interpreter, life-arc-interpreter, transit-analyzer-short, transit-analyzer-long) directly. Let the orchestrator manage the workflow.

### What mode-orchestrator Does

1. **Detects mode** from user request (Natal/Life Arc/Transits/Timing)
2. **Validates profile** exists and has required data
3. **Loads seed data** from profile directory
4. **Runs calculations** if needed (transit_calculator.py, etc.)
5. **Invokes appropriate interpreter agent** via Task tool
6. **Saves output** to correct location with consistent naming
7. **Returns file path** and offers PDF generation

### Example Usage

```
User: "Run the transit report for next month"
Assistant: "I'll use the mode-orchestrator agent to handle this request."
→ mode-orchestrator detects Mode 3 (Transit), short-term timeframe
→ Validates darren profile exists
→ Runs transit_calculator.py for next 30 days
→ Invokes transit-analyzer-short agent
→ Saves to /profiles/darren/output/transit_report_darren_short_2025-10-10_to_2025-11-10.md
→ Returns file path
```

```
User: "What does my chart say about ages 35-45?"
Assistant: "I'll use the mode-orchestrator agent to generate a life arc analysis."
→ mode-orchestrator detects Mode 2 (Life Arc)
→ Validates darren profile exists
→ Loads seed data
→ Invokes life-arc-interpreter agent with age range 35-45
→ Saves output
→ Returns file path
```

---

## astrology-output-debugger: Quality Verification Agent

### Purpose

The astrology-output-debugger systematically investigates interpretation quality issues, from seed data accuracy through calculation correctness to interpretation consistency.

### When to Use (Proactively)

**Trigger automatically when**:
1. **Output quality seems questionable** - Interpretations don't match expected traditional principles
2. **User asks to verify a reading** - "Can you verify this interpretation?", "Does this look right?"
3. **Calculations or interpretations appear inconsistent** - Discrepancies between different reports or sections
4. **New features produce unexpected results** - After implementing new calculation or interpretation logic
5. **Comparing outputs reveals discrepancies** - Saturn return scored as positive when user says it was hardest period

### When NOT to Use

**Do NOT trigger when**:
- There's insufficient context to know what "correct" looks like
- User is just asking conceptual questions ("What is a Saturn return?")
- No actual output has been generated yet
- Request is about methodology, not output quality

### What astrology-output-debugger Does

The debugger follows a systematic 6-phase investigation:

1. **Output Analysis** - Review problematic output in detail
2. **Data Verification** - Check raw seed data, planetary positions, dignities, aspects
   - For transit reports: Extract planetary position timeline from JSON and compare against narrative statements
3. **Workflow Tracing** - Map complete data flow from input to output
4. **Prompt Review** - Examine agent system prompts for completeness and alignment
5. **RAG Database Investigation** - Verify retrieved interpretations are relevant and accurate
6. **Root Cause Report** - Document issues, identify primary causes, provide concrete fixes

### Example Usage: Saturn Return Scoring Bug

```
Context: User corrected Saturn return analysis
User: "The saturn return at 29 was the hardest thing I've ever experienced"
[But report showed positive average score +11.9]
Assistant: "This discrepancy indicates a possible scoring bug. Let me use the astrology-output-debugger agent."
→ Debugger Phase 1: Reviews comparison report output
→ Debugger Phase 2: Extracts transit data from 2017-2019 period
→ Debugger Phase 2: Discovers Saturn conjunction rated as score 0 (neutral)
→ Debugger Phase 3: Traces scoring algorithm logic
→ Debugger Phase 6: ROOT CAUSE FOUND
   - Scoring logic: conjunction + dignified planet = neutral (0)
   - Problem: Saturn conjunctions are challenging regardless of dignity
   - Impact: All Saturn return data invalid, comparative analysis unreliable
→ Debugger recommends fix or acknowledges quantitative limitations

```

---

## Agent Maintenance Requirements

### When Creating New Interpreter Agents

**IMPORTANT**: The mode-orchestrator agent must be updated every time a new astrology interpretation agent is created.

**Required Updates to mode-orchestrator.md**:

1. **Update "Existing Agents" section** (around line 261):
   ```
   **Existing Agents** (update when new interpreters created):
   - Add new agent to list with status
   ```

2. **Update Mode Detection routing** (around line 84-103):
   ```
   - Add keywords that should trigger the new agent
   - Document output format
   - Specify which handler to use
   ```

3. **Update Workflow section** (around line 122-156):
   ```
   - Add workflow steps for new mode
   - Document calculator scripts needed
   - Specify how to invoke new interpreter
   ```

4. **Update "Invokes (via Task tool)" section** (around line 272-287):
   ```
   - Add new agent with:
     - What data to pass
     - What output to receive
   ```

### Verification After Updates

After updating mode-orchestrator, verify:

1. ✓ New agent listed in "Existing Agents"
2. ✓ Mode keywords updated
3. ✓ Workflow documented
4. ✓ Invocation pattern specified
5. ✓ Test with conversational request matching new agent's purpose

---

## Quick Reference

### mode-orchestrator Triggers

✅ **USE** for:
- Any astrology interpretation request (natal, life arc, transits, timing)
- Conversational questions requiring chart analysis
- Comparative analysis requests
- Questions needing seed data or calculations

❌ **DON'T USE** for:
- Conceptual astrology questions
- Documentation updates
- RAG database queries
- General planning or discussion

### astrology-output-debugger Triggers

✅ **USE** for:
- Questionable output quality
- User asks to verify reading
- Inconsistent calculations/interpretations
- New feature produces unexpected results
- Comparative analysis reveals discrepancies

❌ **DON'T USE** for:
- Insufficient context scenarios
- Conceptual questions only
- No output generated yet
- Methodology discussions

---

## Related Documentation

- **mode-orchestrator agent definition**: `.claude/agents/mode-orchestrator.md`
- **astrology-output-debugger agent definition**: `.claude/agents/astrology-output-debugger.md`
- **Interpreter agents**: `.claude/agents/natal-interpreter.md`, `life-arc-interpreter.md`, `transit-analyzer-short.md`, `transit-analyzer-long.md`
- **Project documentation**: `CLAUDE.md`, `CURRENT_WORK.md`, `session_goals.md`

---

**Remember**: Route through mode-orchestrator, verify with astrology-output-debugger, update mode-orchestrator when creating new interpreters.
