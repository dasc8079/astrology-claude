# Single Event Analysis Design (Mode 3 Level 3)

**Created**: 2025-10-10
**Updated**: 2025-10-11 (Consolidated into transit-analyzer-short)
**Purpose**: Design document for zoomed-in single transit event analysis
**Status**: **CONSOLIDATED** - See transit-analyzer-short Period of Interest Mode

---

## ⚠️ CONSOLIDATION NOTICE

**This functionality has been consolidated into the `transit-analyzer-short` agent as "Period of Interest Mode".**

**Key Change**: Rather than focusing on a single isolated transit, Period of Interest Mode analyzes CLUSTERS of transits flagged by long-term reports as significant. Long-term reports use convergent timing techniques + scoring to identify important periods, then Period of Interest mode provides the complete narrative of what's creating that significance.

**See**:
- **Agent file**: `.claude/agents/transit-analyzer-short.md` (Section: "Period of Interest Mode")
- **Update spec**: `docs/TRANSIT_SHORT_DUAL_MODE_UPDATE.md`
- **User documentation**: `docs/AGENTS_REFERENCE.md` (transit-analyzer-short entry)

**Typical window**: 2-6 weeks showing buildup → peak concentration → resolution

**Example use case**: "Tell me about that June 2026 period" (long-term report showed score: -45) → Shows ALL transits + timing techniques creating that cluster.

---

## Original Design (For Reference)

## Executive Summary

**Single Event Analysis** is Mode 3 Level 3—a deep dive into ONE specific transit event, revealing the full story from past buildup → current moment → future resolution. This complements:
- **Long reports** (1-5 years): Strategic life planning, major narrative arcs
- **Short reports** (1-4 months): Tactical timing, retrograde loop narratives
- **Single event** (Level 3): Microscopic focus on individual transits

**Use Case**: "Tell me everything about Saturn conjunct my Moon on June 8, 2026"

**Output**: 3-8 page focused narrative showing psychological depth, timing context, and practical guidance for this ONE event.

---

## Core Concept

When a user asks about a specific transit event, they want to understand:

1. **What led to this moment?** (Past buildup—earlier transits, timing lord context, natal themes activated)
2. **What IS this moment?** (Current event—exact dates, applying → exact → separating, psychological meaning)
3. **How does this resolve?** (Future arc—what comes after, integration period, next chapter)

This is fundamentally different from long/short reports which show MULTIPLE transits. Single event = ONE transit's complete story.

---

## Structure Overview

### Report Components

**Title Page**:
```markdown
# Single Event Analysis

**[Transit Name]**
Saturn conjunct natal Moon

**[Profile Name]**

**Event Window**: [Applying Date] to [Separating Date]
(e.g., May 15, 2026 - July 10, 2026)

**Exact Date**: June 8, 2026

Born: [Date] at [Time]
[City, Country]

Report Generated: [Date]
```

**Quick Reference**:
- Event timeline (applying → exact → separating with specific dates)
- Timing context summary (Lord of Year, ZR periods, Firdaria, other active transits)
- Convergence score (if high convergence with other techniques)
- Recommended actions/timing (when to act, when to wait)

**Section 1: The Buildup** (1-2 pages):
- Natal context: What does this planet/point mean in your chart?
- Recent history: What transits led to this moment? (past 1-3 months)
- Timing lord context: How does current ZR/profection/Firdaria frame this event?
- Psychological preparation: What themes have been building?

**Section 2: The Event** (2-3 pages):
- Transit description: What IS this transit? (traditional + modern perspectives)
- Exact dates: When does it apply, peak, separate? (include retrograde passes if applicable)
- Psychological depth: What does this mean internally? (emotional, spiritual, relational)
- Practical manifestation: How might this show up in life? (not prediction, but themes)
- Convergent factors: What else is happening simultaneously? (other transits, timing techniques)
- RAG queries: Brennan/George/Hand on this specific transit type

**Section 3: The Resolution** (1-2 pages):
- What comes after: Next 1-3 months of transits
- Integration period: How long does this take to process?
- Next chapter: Where does the story go from here?
- Long-term significance: How does this fit into bigger life arc?

**Poetic Wrapup** (4-8 sentences, NO heading):
- Visionary, direct second person
- Honor difficulty and grace
- Trust the process

**PDF Generation**:
```bash
python scripts/pdf_generator.py single_event_analysis.md --report-type event
```

---

## Data Requirements

### Input Parameters

**Required**:
- Profile name (for natal chart context)
- Transit specification:
  - Transiting planet (e.g., Saturn)
  - Aspect type (e.g., conjunction)
  - Natal point (e.g., Moon)
- Date range (auto-calculate or user-specified):
  - Start: When transit begins applying (e.g., -1° orb for outer planets)
  - End: When transit finishes separating (e.g., +1° orb for outer planets)
  - Exact date: When aspect becomes exact

**Optional**:
- Retrograde consideration: If transit has multiple exact passes, show all three
- Focus areas: User can request emphasis (e.g., "focus on career implications")

### Data Sources

**From seed_data.json**:
- Natal planetary positions
- Natal house cusps (whole-sign)
- Natal aspects
- Natal dignities
- Lots (if relevant)

**From transit_calculator.py**:
- Transit planetary positions for date range
- Aspect formation dates (applying → exact → separating)
- Retrograde loop dates (if applicable)
- Other simultaneous transits (convergence analysis)

**From timing techniques**:
- Current profection house and Lord of Year
- Current ZR L1/L2/L3 periods (Fortune and Spirit)
- Current Firdaria major and sub-lords
- Planetary returns context (if recent or upcoming)

**From RAG database**:
- Traditional interpretations of this specific transit type
- House ruler context
- Dignity/sect considerations
- Timing lord activation themes

---

## Agent Design: event-analyzer

### Agent Responsibilities

**Phase 1: Data Collection**
1. Load natal chart from seed_data.json
2. Calculate transit dates (applying → exact → separating)
3. Identify retrograde passes (if any)
4. Query timing context (profection, ZR, Firdaria)
5. Find other simultaneous transits (convergence)

**Phase 2: Narrative Planning**
1. Identify natal theme (what does this planet/point mean in chart?)
2. Map recent buildup transits (past 1-3 months)
3. Calculate convergence score
4. Determine psychological arc (initiation → peak → integration)
5. Query RAG for traditional interpretations (~5-8 queries)

**Phase 3: Synthesis**
1. Write Section 1: The Buildup (past context, natal themes, timing lords)
2. Write Section 2: The Event (transit dates, psychological depth, practical themes)
3. Write Section 3: The Resolution (what comes next, integration, long-term view)
4. Write Quick Reference summary
5. Add poetic wrapup (4-8 sentences, NO heading)

**Phase 4: Output Generation**
1. Generate markdown with title page
2. Convert to PDF using `--report-type event`
3. Save to `profiles/{profile}/output/event_analysis_{transit-name}_{exact-date}.pdf`

### Agent Instructions (Draft)

```markdown
You are the **Single Event Analyzer**, providing deep psychological analysis of individual transit events.

## Your Role

Reveal the complete story of ONE transit event: what led to this moment (buildup), what this moment means (event), and how it resolves (aftermath).

**See ASTROLOGY_REFERENCE.md for complete systems, planets, aspects, and techniques.**

## Core Responsibilities

### 1. Accept Event Specification

**Required Input**:
- Profile name
- Transit specification (e.g., "Saturn conjunct natal Moon")
- Exact date (or date range if retrograde loop)

**Auto-calculate**:
- Applying date (when orb begins, ~-1° for outer planets)
- Exact date (0° orb)
- Separating date (when orb ends, ~+1° for outer planets)
- Retrograde passes (if applicable—show all three exact dates)

### 2. Gather Context

**Natal Context**:
- What does the natal planet/point mean in this chart?
- House position, sign, aspects, dignities, sect
- How does house ruler context amplify this?

**Recent History** (past 1-3 months):
- What transits led to this moment?
- What timing lord periods were active?
- What themes have been building?

**Current Timing** (at exact date):
- Profection Lord of Year
- ZR Fortune L1/L2/L3 periods
- ZR Spirit L1/L2/L3 periods
- Firdaria major/sub-lords
- Convergence score (calculate using standard system)

**Simultaneous Transits**:
- What other transits are happening within ±7 days?
- Do they reinforce or counterbalance this event?

### 3. Query RAG Database

**Query strategically** (~5-8 queries):
- "[Transit type] traditional interpretation" (e.g., "Saturn conjunct Moon Hellenistic")
- "[Planet] to natal [planet/point] meaning"
- "[Planet] in [sign] transit interpretation"
- "Lord of Year [planet] transit activation"
- "ZR period [sign] [planet] themes"

**Citation Format**:
"Traditional sources describe Saturn transits to the Moon as... (Brennan, *Hellenistic Astrology*)"

### 4. Write Three-Part Narrative

**Section 1: The Buildup** (1-2 pages):
- Natal theme: "Your Moon in [sign] in the [house] house..."
- Recent transits: "Over the past three months, you've experienced..."
- Timing lord context: "You're currently in a [ZR period], making this transit especially significant because..."
- Psychological preparation: "This transit doesn't arrive in isolation—it's the culmination of..."

**Section 2: The Event** (2-3 pages):
- Transit dates: "Saturn begins applying to your natal Moon on **May 15, 2026**, reaches exactitude on **June 8**, and separates by **July 10**"
- Traditional interpretation: "[RAG query results]"
- Modern psychological depth: "This is a moment when emotional life feels..."
- Practical themes: "You might notice themes of..."
- Convergence: "This transit converges with [other factors] (score: X points), amplifying..."

**Section 3: The Resolution** (1-2 pages):
- What comes next: "After Saturn separates in mid-July, the next significant transit is..."
- Integration period: "Allow 2-3 months for this theme to integrate..."
- Next chapter: "This transit is part of Saturn's larger journey through [sign/house], which continues until..."
- Long-term view: "In the context of your whole-life arc, this moment represents..."

**Poetic Wrapup** (4-8 sentences, NO heading):
- Direct second person, visionary tone
- "You stand at [metaphor]. There is within you..."
- NO astrological jargon

### 5. Format Output

**Title Page** (use Template C2 format):
```markdown
# Single Event Analysis

**Saturn Conjunct Natal Moon**

**[Profile Name]**

**Event Window**: May 15, 2026 - July 10, 2026
**Exact Date**: June 8, 2026

Born: [Date] at [Time]
[City, Country]

Report Generated: [Date]
```

**Quick Reference**:
| Element | Details |
|---------|---------|
| Transit | Saturn conjunct natal Moon |
| Applying | May 15, 2026 |
| Exact | June 8, 2026 |
| Separating | July 10, 2026 |
| Retrograde Passes | N/A (or list all three dates) |
| Lord of Year | [Planet] |
| ZR Fortune Period | [Sign] (ages X-Y) |
| ZR Spirit Period | [Sign] (ages X-Y) |
| Convergence Score | [N] points ([tier]) |
| Simultaneous Transits | [List 2-3 major transits ±7 days] |

**Recommended Timing**:
- Best days to engage: [dates with supportive transits]
- Days to exercise caution: [dates with challenging transits]
- Integration period: [date range after separation]

### 6. Voice & Style

**Psychological Depth** (matches natal-interpreter):
- Poetic, intimate second-person address
- Evocative language, metaphor, imagery
- Long flowing paragraphs
- Compassionate witnessing of shadow and light
- Translate all jargon to psychological meaning

**Examples**:
- ❌ "Saturn conjunct Moon"
- ✅ "Saturn presses against your Moon, and emotional life feels suddenly bounded, tested, real"
- ❌ "This activates your 4th house"
- ✅ "This touches the foundation of your life—home, family, emotional roots"

**Balance**:
- Traditional seven (Sun-Saturn) = PRIMARY narrative
- Modern planets (Uranus-Pluto) = SECONDARY psychological context
- Timing techniques provide context, not determinism
- Focus on MEANING, not prediction

### 7. Generate PDF

```bash
python scripts/pdf_generator.py event_analysis.md --report-type event
```

**CSS Files Loaded**:
- `base.css` (universal styles)
- `movement_based.css` (event-specific: prominent Quick Reference, date emphasis, timing boxes)

**Output Path**:
- `profiles/{profile}/output/event_analysis_{transit-name}_{exact-date}.pdf`
- `profiles/{profile}/output/event_analysis_{transit-name}_{exact-date}_process.md` (technical data)
```

---

## Implementation Phases

### Phase 1: Calculator Enhancement (FIRST)
**Deliverables**:
- `scripts/event_calculator.py` - New script that:
  - Accepts transit specification (planet, aspect, natal point)
  - Calculates applying/exact/separating dates with proper orbs
  - Detects retrograde loops (if any) with all three exact passes
  - Identifies simultaneous transits within ±7 days
  - Calculates convergence score
  - Outputs JSON with all context data

**Test Case**:
```bash
python scripts/event_calculator.py \
  --profile darren \
  --transit "Saturn conjunct Moon" \
  --date 2026-06-08
```

**Output**:
```json
{
  "profile": "darren",
  "transit": {
    "type": "conjunction",
    "transiting_planet": "Saturn",
    "natal_point": "Moon",
    "applying_date": "2026-05-15",
    "exact_date": "2026-06-08",
    "separating_date": "2026-07-10",
    "orb_degrees": 1.0,
    "retrograde_loop": null
  },
  "natal_context": {
    "moon_sign": "Pisces",
    "moon_house": 7,
    "moon_aspects": [...],
    "moon_dignities": {...}
  },
  "timing_context": {
    "lord_of_year": "Saturn",
    "profection_house": 11,
    "zr_fortune_l1": "Capricorn",
    "zr_fortune_l2": "Sagittarius",
    "zr_fortune_l3": "Aquarius",
    "zr_spirit_l1": "Gemini",
    "zr_spirit_l2": "Virgo",
    "firdaria_major": "Sun",
    "firdaria_sub": "Jupiter"
  },
  "convergence": {
    "score": 18,
    "tier": "SIGNIFICANT",
    "factors": [
      "Transit to Lord of Year (+10 points)",
      "Transit during ZR L3 period (+6 points)",
      "Transit to Firdaria sub-lord (+2 points)"
    ]
  },
  "simultaneous_transits": [
    {
      "transit": "Jupiter trine Sun",
      "exact_date": "2026-06-05",
      "quality": "supportive"
    },
    {
      "transit": "Mars square Mercury",
      "exact_date": "2026-06-12",
      "quality": "challenging"
    }
  ],
  "recent_history": [
    {
      "transit": "Saturn sextile Venus",
      "exact_date": "2026-04-20",
      "relevance": "Builds toward emotional maturation theme"
    }
  ]
}
```

### Phase 2: Agent Creation (SECOND)
**Deliverables**:
- `.claude/agents/event-analyzer.md` - New agent following instructions above
- Agent uses event_calculator.py JSON as input
- Agent queries RAG database (~5-8 queries)
- Agent writes 3-section narrative (buildup → event → resolution)
- Agent generates Quick Reference summary

**Agent Metadata**:
```yaml
name: event-analyzer
description: Analyzes individual transit events with full story arc (buildup → event → resolution). Traditional planets PRIMARY, modern SECONDARY. Queries RAG for interpretations. 3-8 page focused narrative.
model: sonnet
color: red
```

### Phase 3: Testing & Refinement (THIRD)
**Test Cases**:
1. **Outer planet conjunction**: Saturn conjunct Moon (slow, weighty, 2-month window)
2. **Inner planet conjunction**: Mars conjunct Sun (fast, direct, 1-week window)
3. **Retrograde loop**: Jupiter trine Mercury with 3 passes (5-month arc)
4. **Hard aspect**: Pluto square Venus (transformative, long-duration)
5. **High convergence**: Transit during ZR peak period with Lord of Year activation

**Success Criteria**:
- ✅ Dates calculated accurately (applying → exact → separating)
- ✅ Retrograde loops handled correctly (all three passes shown)
- ✅ Convergence score meaningful (aligns with other techniques)
- ✅ Narrative has psychological depth (not just technical description)
- ✅ RAG citations appropriate and well-integrated
- ✅ Voice matches natal-interpreter (poetic, intimate, flowing)
- ✅ PDF generates correctly with movement_based.css
- ✅ Output length appropriate (3-8 pages, not bloated)

---

## CLI Integration

### Command Structure

```bash
# Basic usage
python scripts/analyze_event.py \
  --profile darren \
  --transit "Saturn conjunct Moon" \
  --date 2026-06-08

# Retrograde loop (auto-detects three passes)
python scripts/analyze_event.py \
  --profile darren \
  --transit "Jupiter trine Mercury" \
  --date 2026-08-15

# Custom date range (override auto-calculation)
python scripts/analyze_event.py \
  --profile darren \
  --transit "Mars square Sun" \
  --start-date 2026-03-10 \
  --end-date 2026-03-20

# Focus on specific area (optional emphasis)
python scripts/analyze_event.py \
  --profile darren \
  --transit "Pluto square Venus" \
  --date 2027-05-20 \
  --focus "relationships"
```

### Output Files

**Generated Files**:
- `profiles/{profile}/output/event_analysis_{transit-name}_{exact-date}.md` (interpretation markdown)
- `profiles/{profile}/output/event_analysis_{transit-name}_{exact-date}.pdf` (final report)
- `profiles/{profile}/output/event_analysis_{transit-name}_{exact-date}_process.md` (technical data)
- `profiles/{profile}/output/event_data_{transit-name}_{exact-date}.json` (calculator output)

**Example**:
```
profiles/darren/output/
├── event_analysis_saturn-conj-moon_2026-06-08.md
├── event_analysis_saturn-conj-moon_2026-06-08.pdf
├── event_analysis_saturn-conj-moon_2026-06-08_process.md
└── event_data_saturn-conj-moon_2026-06-08.json
```

---

## Relationship to Other Modes

**Mode 3 Hierarchy**:

| Level | Type | Scope | Purpose | Example |
|-------|------|-------|---------|---------|
| **Level 1** | Long Report | 1-5 years | Strategic planning, major arcs | "Show me next 5 years" |
| **Level 2** | Short Report | 1-4 months | Tactical timing, retrogrades | "Show me this spring" |
| **Level 3** | Single Event | ONE transit | Deep dive, full story arc | "Tell me about Saturn conjunct Moon" |

**How they work together**:
1. User runs **long report** (5 years) → sees Saturn conjunct Moon on June 8, 2026 flagged as challenging
2. User runs **short report** (Spring 2026) → sees more context around that period
3. User runs **single event analysis** (Saturn-Moon) → gets complete psychological depth and guidance

**Data Flow**:
- Long/short reports identify WHICH transits are significant
- Single event analysis dives deep into ONE transit's complete story
- All three use same calculator (transit_calculator.py) but filter differently

---

## Technical Considerations

### Orb Calculations

**Standard Orbs** (applying → separating):
- Sun, Moon, Mercury, Venus, Mars: ±1° (tight)
- Jupiter, Saturn: ±1° (moderate)
- Uranus, Neptune, Pluto: ±1° (wide, slow-moving)

**Why tight orbs for events**:
- Single event analysis focuses on PEAK moment
- Wider orbs dilute narrative focus
- User wants to know "when is this EXACT?"

### Retrograde Detection

**Three-Pass Story**:
1. **Direct pass** (initiation): Planet moving forward, first exact aspect
2. **Retrograde pass** (deepening): Planet moving backward, second exact aspect
3. **Direct pass** (integration): Planet moving forward again, third exact aspect

**Station Dates**:
- Station retrograde: Planet "stops" before going backward (maximum intensity)
- Station direct: Planet "stops" before going forward again (turning point)

**Include in narrative**:
- All three exact dates
- Both station dates
- Total duration of loop (e.g., "5-month Jupiter retrograde arc")
- Psychological arc: initiation → review → integration

### Convergence Scoring

**Use existing system** (from transit_calculator.py):
- Transit to Lord of Year: +10 points
- Transit to ZR L2 lord: +8 points
- Transit to ZR L3 lord: +6 points
- Transit to ZR L1 lord: +5 points
- Exact transit during ZR L3 peak (L3=L2 or L3=L1): +10 points
- Multiple transits to same planet within 7 days: +5 points

**Convergence Tiers**:
- **MAJOR** (20+ points): Always highlight prominently
- **SIGNIFICANT** (12-19 points): Note and explain
- **NOTABLE** (8-11 points): Mention in context
- **MINIMAL** (<8 points): Single transit, no special emphasis

### RAG Query Strategy

**Query Types**:
1. **Transit interpretation**: "[Planet] [aspect] natal [planet] traditional meaning"
2. **Sign-based context**: "[Planet] in [sign] transit themes"
3. **House activation**: "[Planet] transiting [house] traditional interpretation"
4. **Timing lord activation**: "Lord of Year [planet] transit significance"
5. **Dignity considerations**: "[Planet] in [dignity state] transit effects"

**Query Count**: 5-8 total (not more—keep narrative focused)

**Citation Style**:
"Traditional sources describe Saturn transits to the Moon as times of emotional sobering, when boundaries between inner and outer life become more defined (Brennan, *Hellenistic Astrology*, p. 342)."

---

## Example Output Structure

```markdown
# Single Event Analysis

**Saturn Conjunct Natal Moon**

**Darren Schaeffer**

**Event Window**: May 15, 2026 - July 10, 2026
**Exact Date**: June 8, 2026

Born: December 27, 1988, 8:25 PM
Masan, South Korea

Report Generated: October 10, 2025

---

## Quick Reference: Event Timeline

| Element | Details |
|---------|---------|
| Transit | Saturn conjunct natal Moon |
| Transiting Sign | Pisces |
| Natal Position | Moon in Pisces, 7th house |
| Applying | May 15, 2026 |
| Exact | **June 8, 2026** |
| Separating | July 10, 2026 |
| Retrograde | No (single pass) |
| Orb | ±1° |
| Duration | ~8 weeks |

**Timing Context**:
- **Lord of Year**: Saturn (age 37)
- **ZR Fortune**: Sagittarius L2 period (ages 35.5-37.4)
- **ZR Spirit**: Virgo L2 period
- **Convergence Score**: 18 points (SIGNIFICANT)
  - Transit to Lord of Year (+10)
  - Transit to ZR L3 lord (+6)
  - Transit to Firdaria sub-lord (+2)

**Simultaneous Transits** (±7 days):
- June 5: Jupiter trine Sun (supportive)
- June 12: Mars square Mercury (challenging)

**Recommended Actions**:
- Best days to engage: June 1-4 (Jupiter support)
- Days requiring care: June 8-14 (Saturn exact + Mars friction)
- Integration period: July 11 - September 11 (2-3 months)

---

## Section 1: The Buildup

Your Moon rests in Pisces in the 7th house—a placement that speaks to emotional attunement in relationships, to feeling the boundaries between self and other as permeable, sometimes too permeable. You've spent your life learning how to be close without dissolving...

[1-2 pages of narrative showing natal context, recent transits, timing lord themes, psychological preparation]

---

## Section 2: The Event

Saturn begins applying to your natal Moon on **May 15, 2026**. At first, you may not notice—Saturn moves slowly, and its effects accumulate rather than announce themselves. But by late May, something shifts...

[2-3 pages showing transit dates, traditional interpretation, psychological depth, practical themes, convergence factors, RAG citations]

Traditional sources describe Saturn transits to the Moon as periods of emotional consolidation, when the boundary between inner feeling life and outer responsibility becomes more defined, when emotional expression faces reality testing (Brennan, *Hellenistic Astrology*).

The exact conjunction occurs on **June 8, 2026**. This is the peak moment—Saturn at 0° from your natal Moon...

[Continue narrative through separation on July 10]

---

## Section 3: The Resolution

After Saturn separates from your Moon in mid-July, the immediate intensity eases. But this transit doesn't end abruptly—it integrates slowly over the following 2-3 months...

[1-2 pages showing what comes next, integration period, next chapter, long-term significance]

---

You stand at the threshold of a profound emotional maturation. There is within you the capacity to meet what Saturn asks—to build boundaries without building walls, to accept limitation without accepting defeat. The difficulty of this moment is also its gift: you're learning what emotional adulthood actually means. Trust the process, honor the timeline, and remember that what feels heavy now is teaching you what you're made of.

*Generated by event-analyzer agent*
*Mode 3 Level 3: Single Event Analysis*
*Traditional Hellenistic Foundation + Modern Psychological Context*
```

---

## Success Metrics

**Qualitative Metrics**:
- ✅ Narrative has psychological depth (not just technical description)
- ✅ Voice matches natal-interpreter (poetic, intimate, flowing paragraphs)
- ✅ Dates are accurate and clearly explained
- ✅ Retrograde loops handled elegantly (all three passes as story arc)
- ✅ Convergence score adds meaningful context
- ✅ RAG citations well-integrated and relevant
- ✅ Practical guidance provided without determinism
- ✅ Poetic wrapup is visionary and grounded

**Quantitative Metrics**:
- Output length: 3-8 pages (proportional to transit complexity)
- RAG queries: 5-8 total
- Quick Reference table: Complete and scannable
- PDF generation: Clean, professional, movement_based.css applied
- Processing time: <2 minutes per event

---

## Future Enhancements

**Phase 2 (After Initial Implementation)**:
1. **Comparative Analysis**: Compare multiple events (e.g., "Saturn conjunct Moon" vs "Saturn square Moon")
2. **Historical Review**: Analyze past transits to understand patterns
3. **Synthesis Feature**: Combine multiple simultaneous events into one report
4. **Custom Focus Areas**: Allow user to emphasize specific life areas (career, relationships, health)
5. **Remedial Measures**: Suggest traditional remediation practices if desired

**Phase 3 (Advanced Features)**:
1. **Interactive Timeline**: Visual representation of applying → exact → separating
2. **Email Notifications**: Alert user N days before exact transit
3. **Journal Integration**: Track user's actual experience vs predicted themes
4. **Pattern Recognition**: Identify recurring transit themes across years

---

## Conclusion

**Single Event Analysis (Mode 3 Level 3)** fills a critical gap in the astrology application suite. While long reports show strategic arcs and short reports show tactical timing, single event analysis provides the psychological depth and narrative completeness needed to truly understand ONE transit's full story.

**Implementation Priority**: MEDIUM
- Depends on: transit_calculator.py (already built)
- Enables: Deep user engagement with specific life moments
- Complexity: Moderate (new agent + calculator enhancement)

**Next Steps**:
1. Review and approve this design document
2. Implement Phase 1 (event_calculator.py)
3. Test calculator with 5 diverse transit types
4. Implement Phase 2 (event-analyzer agent)
5. Generate test reports for quality assessment
6. Refine voice and structure based on feedback
7. Document in TRANSITS_GUIDE.md
8. Archive this design to /docs/archive/design/

---

*Design Document v1.0*
*Created: 2025-10-10*
*Status: Awaiting Approval*
