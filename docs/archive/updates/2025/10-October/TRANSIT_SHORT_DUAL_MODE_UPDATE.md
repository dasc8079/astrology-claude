# Transit-Analyzer-Short: Dual-Mode Update Spec

**Date**: 2025-10-11
**Purpose**: Consolidate single-event deep-dive functionality into transit-analyzer-short agent

---

## Overview

The transit-analyzer-short agent will support TWO modes:

1. **Multi-Movement Mode** (existing): 1-4 month reports with 2-4 thematic movements
2. **Period of Interest Mode** (new): Deep-dive on a concentrated cluster of transits flagged by long-term reports as significant (high positive or negative scores from convergent timing techniques)

---

## Use Cases

### Multi-Movement Mode
- "What's happening next month?"
- "Generate transit report for March-May 2026"
- Standard 1-4 month thematic reports

### Period of Interest Mode
- "Tell me about that June 2026 period" (long-term report flagged June 2026 score: -45)
- "What's happening around June 8, 2026?" (zoom in on high-score cluster)
- "Show me that challenging period in detail" (multiple transits converging)

**Key Insight**: Long-term reports use convergent timing techniques + scoring to flag important periods → Period of Interest mode zooms in to show the complete cluster of transits creating that significance

---

## Period of Interest Mode: How It Works

### Input Parameters
```
--mode period-of-interest
--focus-date 2026-06-08  (the date flagged as significant)
--score -45  (optional: the score from long-term report)
```

### Processing Logic
1. **Identify Cluster Window**: Find the natural window around the focus date containing the transit cluster
   - Look at daily scores around focus date
   - Find boundaries where score concentration begins/ends
   - Typical window: 2-6 weeks around focus date
2. **Gather All Transits**: Find ALL transits active during cluster window
   - Exact transits on/near focus date
   - Applying transits building toward focus date
   - Separating transits resolving after focus date
   - Convergent timing techniques (ZR, Profections, Firdaria) active during period
3. **Identify Primary Themes**: What created the high score?
   - Multiple malefic transits converging?
   - Saturn + Mars both active?
   - Difficult house activation + hard aspects?
4. **Generate Cluster Report**: Show complete story of this concentrated period

### Output Structure (Period of Interest Mode)
```
1. At a Glance
   - Period focus: June 1-20, 2026
   - Score from long-term report: -45 (highly challenging)
   - Key exactness dates: June 8 (Saturn square Moon), June 10 (Mars opposition Sun), June 12 (Mercury square Saturn)
   - Convergent factors: Saturn profection year + ZR L2 Scorpio + Firdaria Mars sub-period

2. Summary Synthesis (200-300 words)
   - Why this period was flagged as significant
   - The cluster of transits creating convergence
   - How timing techniques amplify the transits
   - Complete narrative arc of the concentrated period

3. The Cluster Period: [Title] (800-1200 words)
   - Buildup phase (transits applying, tension building)
   - Peak concentration (multiple exactness dates close together)
   - Resolution phase (transits separating, integration period)
   - ALL transits woven into cohesive narrative
   - Psychological depth showing how themes interact
   - Practical guidance for navigating this intense window

4. Technical Appendix
   - All transits with exact dates and orbs
   - Daily quality scores throughout period
   - Timing technique activations (profection, ZR, Firdaria)
   - Cluster boundary explanation
```

---

## Agent Updates Needed

### 1. Frontmatter Description
**Current**:
```
description: Generate 1-4 month movement-based transit reports...
```

**Updated**:
```
description: Generate transit reports with two modes - (1) Multi-movement for 1-4 month periods showing 2-4 thematic movements, (2) Single-event deep-dive showing one specific transit movement in its entirety including all supporting transits during that period. Perfect for zooming in on important dates flagged in long-term reports or understanding retrograde cycles.
```

### 2. Add Period of Interest Examples
Add after existing examples:

```
<example>
Context: User wants to zoom in on a period flagged by long-term report
user: "Tell me more about that June 2026 period" (long-term report showed score: -45)
assistant: "I'll invoke transit-analyzer-short in period-of-interest mode to show the complete cluster of transits creating that significant score."
<commentary>
Period-of-interest mode: Identifies the natural window around June 2026 containing the transit cluster, finds all transits and timing technique activations during that period, and generates a cohesive narrative showing how these converging factors create the flagged significance.
</commentary>
</example>

<example>
Context: User wants to understand what's creating a concentration
user: "What's going on around June 8, 2026?"
assistant: "I'll use transit-analyzer-short in period-of-interest mode to analyze the transit cluster around that date."
<commentary>
Shows the complete window of converging transits - not just one transit, but the cluster creating concentration. Typical output: 2-6 week window showing buildup → peak concentration → resolution.
</commentary>
</example>
```

### 3. Update "IMPORTANT: Use this agent when" Section
**Add**:
```
**Period of Interest Mode**:
- Long-term report flagged a high-score period needing closer examination
- User asks "What's happening around [date]?" when that date had significant score
- User wants to understand a cluster/concentration of transits
- User says "Tell me about that [month/period]" referencing long-term report findings
```

### 4. Update Purpose Section
Add after existing purpose paragraph:

```
**Dual-Mode Capability**:
- **Multi-Movement Mode**: Standard 1-4 month reports with 2-4 movements (existing functionality)
- **Period of Interest Mode**: Deep-dive on a CLUSTER of transits flagged by long-term reports as significant (high positive or negative scores from convergent timing techniques). This is the "zoom in" feature for examining concentrated periods where multiple transits + timing techniques converge to create important life moments.
```

### 5. Update Scope Boundaries
**Add to IN SCOPE**:
```
- Period of Interest mode (cluster analysis for high-score periods)
- Transit concentration/convergence analysis
- Showing how timing techniques amplify transit clusters
- 2-6 week windows around flagged dates
```

**Add to OUT OF SCOPE**:
```
- Event-analyzer as separate agent (consolidated into this agent's period-of-interest mode)
- Single isolated transit analysis without cluster context
```

### 6. Add Period of Interest Mode Section
Add new section after "Movement-Based Thematic Structure":

```
### 2. Period of Interest Mode (Cluster Analysis)

**When to Use**: User wants to understand a CLUSTER of transits flagged by long-term reports as significant, showing how multiple transits + timing techniques converge to create an important life moment.

**Mode Detection**:
- User references a long-term report finding ("tell me about that June period")
- User asks about a specific date that had high score ("what's happening around June 8?")
- User wants to zoom in on flagged period for complete understanding

**Cluster Period**: The natural window (typically 2-6 weeks) around the focus date containing the transit concentration

**What Creates Significance**:
- **Multiple transits converging** (e.g., Saturn square Moon + Mars opposition Sun + Mercury square Saturn all within 2 weeks)
- **Timing techniques amplifying** (e.g., Saturn profection year + ZR L2 Scorpio + Firdaria Mars sub-period)
- **High daily scores** from convergent scoring system

**Cluster Boundaries**:
- **Start**: When concentration begins building (applying transits, score increases)
- **Peak**: Maximum concentration (multiple exactness dates close together, highest scores)
- **End**: When concentration resolves (separating transits, score decreases)
- **Typical window**: 2-6 weeks depending on transit cluster density

**Report Focus**:
- Single cluster narrative (not multiple movements)
- ALL transits in the cluster as interconnected themes
- Timing techniques as amplification context
- Complete arc: Buildup → Peak Concentration → Resolution
- Deeper psychological analysis showing theme interactions (800-1200 words)

**Output Structure**:
1. At a Glance (cluster period + score + key dates + convergent factors)
2. Summary Synthesis (why this was flagged, what creates significance)
3. The Cluster Period: [Title] (800-1200 words - cohesive narrative)
4. Technical Appendix (all transits + daily scores + timing activations)
```

### 7. Add Algorithm Update Section
After "Finding Natural Movement Boundaries" section, add:

```
### Algorithm: Period of Interest Mode

**Step 1: Identify Cluster Window**
```python
if mode == "period-of-interest":
    focus_date = user_specified_date  # e.g., "2026-06-08"
    score = user_provided_score  # e.g., -45 (from long-term report)

    # Find natural window boundaries around focus date
    cluster_start = find_cluster_start(daily_scores, focus_date)
    cluster_end = find_cluster_end(daily_scores, focus_date)

    # Typical window: 2-6 weeks around focus date
    # Boundaries = where score concentration begins/ends
```

**Step 2: Gather All Transits in Cluster**
```python
# Find ALL transits active during [cluster_start, cluster_end]
cluster_transits = []
for transit in all_transits:
    if transit.overlaps_with(cluster_start, cluster_end):
        cluster_transits.append(transit)

# Categorize by phase
applying_transits = [t for t in cluster_transits if t.is_applying(focus_date)]
exact_transits = [t for t in cluster_transits if t.is_exact_on(focus_date, orb=1)]
separating_transits = [t for t in cluster_transits if t.is_separating(focus_date)]
```

**Step 3: Identify Convergent Timing Techniques**
```python
# Find timing technique activations during cluster window
timing_factors = {
    "profection": get_profection_year(cluster_start),
    "zr_fortune_l2": get_zr_fortune_l2(cluster_start),
    "zr_spirit_l2": get_zr_spirit_l2(cluster_start),
    "firdaria": get_firdaria_period(cluster_start),
    "major_returns": get_active_returns(cluster_start, cluster_end)
}
```

**Step 4: Identify Primary Themes**
```python
# What created the high score?
primary_themes = analyze_cluster_themes(cluster_transits, timing_factors)
# Examples:
# - Multiple malefic transits converging (Saturn + Mars)
# - Difficult house activation + hard aspects
# - Saturn profection year + ZR L2 malefic period
```

**Step 5: Generate Cluster Report**
```python
# Create report with cluster focus
report = {
    "at_a_glance": generate_cluster_summary(
        cluster_window=(cluster_start, cluster_end),
        score=score,
        key_dates=exact_transits,
        convergent_factors=timing_factors
    ),
    "summary_synthesis": synthesize_cluster_significance(
        why_flagged=score,
        convergence=cluster_transits + timing_factors,
        narrative_arc="buildup → peak → resolution"
    ),
    "the_cluster_period": generate_deep_narrative(
        buildup_phase=applying_transits,
        peak_concentration=exact_transits,
        resolution_phase=separating_transits,
        word_count=800-1200
    ),
    "technical_appendix": list_all_transits_and_scores(
        cluster_transits,
        daily_scores[cluster_start:cluster_end],
        timing_factors
    )
}
```

**Step 6: Query RAG Database**
```python
# RAG queries for period-of-interest mode (8-12 queries)
queries = [
    # Primary transit themes
    f"{transit_1.planet} {transit_1.aspect} {transit_1.natal_planet} in {house}",
    f"{transit_2.planet} {transit_2.aspect} {transit_2.natal_planet} in {house}",
    # Convergence themes
    f"{transit_1.planet} and {transit_2.planet} themes together",
    f"Multiple malefic transits converging",
    # Timing technique amplification
    f"{profection_lord} profection year themes",
    f"ZR {zr_l2_sign} period themes",
    # Cluster navigation
    f"Navigating difficult transit clusters",
    # etc.
]
```
```

---

## Terminal Summary Output

All agents (including both modes of transit-analyzer-short) should output a 3-5 sentence summary to terminal.

**Multi-Movement Mode Terminal Output**:
```
Generated short-term transit report for Darren (March 1 - May 31, 2026).
3 movements detected: "The Catalyst" (Mar 1-Apr 5), "Inner Reckoning" (Apr 6-May 10), "Opening" (May 11-31).
Key themes: Mars-Saturn tension, Jupiter expansion, Venus relationship focus.
Most auspicious day: April 15. Most challenging: March 29.
Report saved to /profiles/darren/output/transit_report_darren_short_2026-03-01_to_2026-05-31.md
```

**Period of Interest Mode Terminal Output**:
```
Generated period-of-interest deep-dive for June 2026 cluster (score: -45).
Cluster period: June 1-20, 2026 (20 days).
Key transits: Saturn square Moon (June 8), Mars opposition Sun (June 10), Mercury square Saturn (June 12).
Convergent factors: Saturn profection year + ZR L2 Scorpio + Firdaria Mars sub-period.
Key theme: Structural pressure under emotional and physical strain.
Report saved to /profiles/darren/output/transit_cluster_june_2026.md
```

---

## Related Documentation Updates Needed

1. **single_event_design.md**: Update to reference transit-analyzer-short in period-of-interest mode (not separate event-analyzer agent)
2. **AGENTS_REFERENCE.md**: Update transit-analyzer-short entry with dual-mode documentation
3. **WORKFLOWS_VISUAL.md**: Add period-of-interest workflow example
4. **mode-orchestrator.md**: Update to detect and route period-of-interest requests
5. **TRANSITS_GUIDE.md**: Add section on period-of-interest deep-dives (cluster analysis)

---

## Benefits of Consolidation

✅ **One agent to maintain** (not two separate agents)
✅ **Consistent methodology** across multi-movement and single-event
✅ **Same RAG database approach**
✅ **Same voice and psychological depth**
✅ **Simpler architecture** for users and maintainers
✅ **Natural workflow**: Long report flags date → Short agent zooms in

---

## Next Steps

1. Update transit-analyzer-short.md agent file (sections listed above)
2. Update single_event_design.md
3. Update AGENTS_REFERENCE.md
4. Update WORKFLOWS_VISUAL.md
5. Update mode-orchestrator.md
6. Add terminal summary output to all agents
7. Test both modes with real data
