# Transit Interpretation Enhancement - Design Document

## Overview

This document contains the comprehensive design for enhancing transit interpretation quality from generic RAG excerpts to fully personalized, traditional astrology-compliant delineations.

**Current Problem**: Transit interpretations just paste RAG database excerpts without personalization.

**Solution**: Multi-layered interpretation system using traditional methods (Hephaestio 7-factor analysis, Robert Hand natal context principles, annual profections).

---

## Research Findings

### 1. Robert Hand - Natal Context is Primary

**Source**: *Planets in Transit: Life Cycles for Living* (Foreword by Charles A. Jayne)

> "a natal or radical aspect is of primary importance and can seriously modify any aspect by transit or progression"

**Key Principle**:
- If natal chart has Saturn square Sun, then transiting Saturn trine Sun MUST be interpreted through that natal square lens
- The natal relationship fundamentally alters transit expression
- Example: Natal square creates underlying tension even in beneficial transiting trine

**Application**:
```python
# ALWAYS check natal aspect between transiting & natal planet first
natal_aspect = get_natal_aspect_between(transiting_planet, natal_planet)
if natal_aspect:
    # Modify interpretation based on natal relationship
    interpretation = apply_natal_modification(base_theme, natal_aspect)
```

---

### 2. Hephaestio - 7-Factor Delineation Method

**Source**: Hephaestio's *Apotelesmatika* 2.27.6, via Chris Brennan's *Hellenistic Astrology*

> "Before all, it is necessary to investigate the lord of the year and its **mixture and position and phase**, and the planets that **see it by fixity and by transit**, and **how it was situated at the nativity**, and **how it was found at the time of the transit**"

**The 7 Factors**:

1. **Lord of Year** - Annual profection ruler (time-lord system)
2. **Mixture** - Natal aspects the planet makes
3. **Position** - House & sign placement
4. **Phase** - Relationship to Sun (oriental/occidental, under beams, cazimi)
5. **See by Fixity** - Natal aspects TO the transited planet
6. **See by Transit** - Current transiting aspects
7. **Natal vs Transit Condition** - Compare natal dignity/strength to current state

**Implementation Checklist**:
```
☐ Calculate annual profection (age % 12 = house, get ruler)
☐ Find all natal aspects FROM the planet (mixture)
☐ Determine house (WSH) and sign (position)
☐ Calculate phase to Sun (oriental/occidental/under beams/cazimi)
☐ Find all natal aspects TO the planet (see by fixity)
☐ Check other current transits to/from planet (see by transit)
☐ Compare natal dignity to current transit condition
```

---

### 3. Dorotheus/Anubio - Time-Lord Filtering

**Source**: CCAG 2, p. 198 & 203, trans. Schmidt (*Teachings on Transits*)

> "one need not examine the ingresses of all of the stars, but rather only those of the time-lords"

> "for the indications of the effects are steady at the time when the ingressing planets are also the time-lords"

**Priority System**:

**CRITICAL TIER** (Highest Priority):
- Transits TO lord of year in natal chart
- Transits BY lord of year to other natal planets
- Transits through the profected sign

**NORMAL TIER** (Standard Priority):
- All other transits

**Application**:
- Filter transits by involvement with annual profection
- Massive priority boost if lord of year involved
- Helps distinguish which transits manifest as actual events vs background influences

---

### 4. Brennan - Sign-Based Transit Approach

**Source**: *Hellenistic Astrology*, Chapter 17 (Annual Profections)

**Sign-Based vs Degree-Based**:
- Hellenistic: Transit begins when planet ENTERS configured sign
- Effect intensifies as it approaches exact degree
- Continues until planet LEAVES the sign for final time

**Example**: Saturn at 15° Libra
- Saturn return begins: 0° Libra (sign ingress)
- Intensifies: approaching 15° Libra (exact degree)
- Peak event: at/near 15° Libra
- Ends: 29° Libra (sign egress)

**Retrograde Triple-Hit Pattern**:
1. First Hit (Direct): Initial activation, themes emerge
2. Second Hit (Retrograde): Internalization, review, revision
3. Third Hit (Direct): Resolution, integration, final manifestation

**Application**:
- Always give sign ingress/egress dates
- Note exact degree for peak timing
- Track retrograde periods for extended transits

---

### 5. Robert Hand - Psychological vs Event Manifestation

**Source**: *Planets in Transit*, Introduction

> "Transits do signify events, but only if we expand the conventional notion of an event. An event can occur totally within yourself as a psychological change, or as an interchange between yourself and another, or as a change totally outside yourself in the material and social universe."

**Three Manifestation Levels**:

1. **Internal/Psychological**: Change within consciousness, intention, emotional state
2. **Interpersonal**: Relationship dynamics, exchanges with others
3. **External/Material**: Events in physical world, circumstances

**Projection Mechanism**:
- If unwilling to deal with inner dilemma → energy projects outward
- Experienced as "happening to you" rather than "coming from you"
- Unconscious operation = not in control

**Application**:
```
For each transit, describe:
1. Core psychological dynamic (what inner pattern activates)
2. Potential interpersonal expression (relationship manifestations)
3. Possible external events (if energy projects outward)
4. How natal planet condition affects manifestation level
```

**"Difficult" Transits**:
- Test weak points in life structure
- If area weak: purification/renewal process
- If area strong: catapult to new success
- Destructive only if "resolutely continue on wrong course"

**"Easy" Transits**:
- Flow with existing direction (reinforces patterns)
- Opportunity for voluntary change
- Risk: doing nothing, becoming lethargic
- Can cause more long-term damage than "difficult" transits if wasted

---

### 6. Robert Hand - Integration Without Overemphasis

**Source**: *Planets in Transit*, Foreword

> "Perhaps the main challenge in the art of interpretation is integrating a number of factors. Overemphasis on any one factor gives a lopsided picture"

**Integration Formula**:
```
General Theme (from RAG)
    ↓
Natal Aspect Modification (fundamental alteration)
    ↓
Dignity Modulation (expression quality)
    ↓
House Activation (life area)
    ↓
Sect Lens (flow vs friction)
    ↓
Solar Conditions (special modulation)
    ↓
Timing Dynamics (orb, applying/separating, retrograde)
    ↓
Lord of Year Weight (massive boost if involved)
    ↓
Synthesis (practical guidance)
```

**Anti-Pattern**: Don't overemphasize any single factor
- Not just "Saturn square = bad"
- Not just "5th house = creativity"
- Not just "applying = growing stronger"

**Pattern**: Balanced synthesis of ALL factors

---

## Traditional Compliance Requirements

### Must Maintain:
- ✅ Whole-sign houses (no quadrant/cusp calculations)
- ✅ Traditional seven planets as primary
- ✅ Classical aspects only (0°, 60°, 90°, 120°, 180°)
- ✅ Sect fundamental to all analysis
- ✅ Essential dignities (domicile, exaltation, triplicity, bounds, decans)
- ✅ Profections as primary time-lord system

### Modern Planets (Uranus, Neptune, Pluto):
**Status**: SECONDARY context only

**When Transiting**:
1. Interpret through traditional ruler of sign first
   - Neptune → Jupiter (traditional Pisces ruler)
   - Uranus → Saturn (traditional Aquarius ruler)
   - Pluto → Mars (traditional Scorpio ruler)
2. Add modern archetypal nuance as supplementary flavor
3. Primary meaning = traditional ruler dynamics

**When Natal**:
- Interpret through sign's traditional ruler
- Modern planet adds characteristic, not primary signification

---

## Interpretation Template Structure

### Full Template (All Factors):

```markdown
## [Transit Name: e.g., Saturn Square Natal Mars]

### General Theme
[1-2 sentences from RAG - core archetypal meaning]

### Natal Relationship Modifier ⚠️
**Natal aspect between these planets**: [aspect type or "none"]
**How this modifies transit**: [Explanation of fundamental alteration]

### Natal Planet Analysis
**[Planet] in [Sign]** (House [X]):
- Essential dignity: [domicile/exaltation/triplicity/bounds/decan]
- Accidental dignity: [angular/succedent/cadent]
- Phase to Sun: [oriental/occidental/under beams/combust/cazimi]
- Sect status: [of-sect/contrary-to-sect/neutral]
- Strength score: [X/10]

### Natal Configuration ("See by Fixity")
**Aspects from other natal planets**:
- [Planet] [aspect] [Planet]: [significance]
- [Synthesis of natal web around this planet]

### Transit Dynamics
**Current transiting aspects** ("See by Transit"):
- [Other transiting planets aspecting either body]
- Orb: [X.XX°] ([applying/separating])
- Retrograde: [Yes/No - traditional interpretation]
- Sign-based timeline: Ingress [date] → Exact [date] → Egress [date]

### Lord of Year Context 🎯
**Current profection**: Age [X] → House [X] → Ruler = [Planet]
**Involvement**: [CRITICAL if involving lord / Normal if not]

### Manifestation Analysis
Based on natal planet strength ([X]/10):

**Psychological Core**:
[Inner dynamic, pattern, intention being activated]

**Interpersonal Potential**:
[Relationship dynamics, exchanges with others]

**External Events** (if energy projects):
[Specific manifestations based on house + condition]

### House & Sect Integration
**House [X] ([angular/succedent/cadent])**:
- Life area: [specific house significations]
- Angularity: [visibility/manifestation level]

**[Diurnal/Nocturnal] Chart**:
- [Planet] is [of-sect/contrary-to-sect]
- [Interpretation of sect impact]

### Timing Guidance
- Orb tightness: [immediate/active/building]
- Motion: [applying = growing / separating = waning]
- Retrograde: [internalization/review if applicable]

### Integration Practice
**Working WITH this energy**:
[Practical steps for conscious engagement]
[How to avoid projection/victimhood]
[Voluntary changes to make]

**If lord of year involved**:
[Connection to annual theme]
[Profected house topic integration]
```

---

## Code Architecture

### Existing Components:

**scripts/chart_analyzer.py**:
- `parse_birth_data()` - Parse natal chart file
- `analyze_all_planets()` - Complete natal analysis
- `determine_sect()` - Calculate diurnal/nocturnal
- `parse_degree()` - ✓ FIXED (handles Unicode quotes)

**scripts/transit_calculator.py**:
- `TransitCalculator.calculate_transits()` - Get all active transits
- `TransitCalculator.prioritize_transits()` - Sort by importance
- `TransitCalculator.calculate_exact_date()` - When transit exact
- ✓ All calculations verified accurate

**scripts/interpretation_builder.py**:
- `InterpretationBuilder.query_rag_transit()` - Get RAG results
- `InterpretationBuilder.synthesize_interpretation()` - ❌ BROKEN (just pastes RAG)

**scripts/run_transit_analysis.py**:
- Main workflow execution
- Calls all components
- Generates final report

### Required Enhancements:

**NEW: chart_analyzer.py additions**:
```python
def get_natal_aspect_between(planet1: str, planet2: str, natal_data: Dict) -> Optional[str]:
    """Find if natal aspect exists between two planets."""

def calculate_profection(birth_date: datetime, current_date: datetime) -> Dict:
    """Calculate annual profection."""

def calculate_phase_to_sun(planet_long: float, sun_long: float) -> str:
    """Determine oriental/occidental/under beams/cazimi."""

def get_natal_aspects_to_planet(planet: str, natal_data: Dict) -> List[Dict]:
    """Find all natal aspects TO this planet (see by fixity)."""
```

**MODIFY: interpretation_builder.py**:
```python
def extract_core_theme(rag_results: List[Dict]) -> str:
    """Extract 1-2 sentence core theme from RAG (not entire text)."""

def apply_natal_context(theme: str, natal_planet_analysis: Dict, house: int) -> str:
    """Add house, dignity, strength context to theme."""

def apply_natal_aspect_modifier(interpretation: str, natal_aspect: str) -> str:
    """Prepend natal aspect modification if exists."""

def add_sect_consideration(interpretation: str, sect: str, planet: str, sect_status: str) -> str:
    """Append sect-based interpretation."""

def add_timing_dynamics(interpretation: str, orb: float, applying: bool, retrograde: bool) -> str:
    """Add timing interpretation."""

def build_comprehensive_interpretation(transit: Dict, natal_analysis: Dict,
                                       profection: Dict, rag_results: List[Dict]) -> str:
    """Main method - applies all layers in order."""
```

**MODIFY: run_transit_analysis.py**:
```python
def generate_executive_summary(top_transits: List[Dict], natal_analysis: Dict) -> str:
    """Create plain-language 2-3 sentence summary."""

# Add at start of workflow:
profection = calculate_profection(birth_date, current_date)

# Modify transit prioritization:
prioritized = calc.prioritize_transits(transits, natal_analysis, profection)

# Use comprehensive interpretation:
interpretation = builder.build_comprehensive_interpretation(
    transit, natal_analysis, profection, rag_results
)
```

---

## Testing Strategy

### Unit Tests (per function):
- `get_natal_aspect_between()`: Test various planet combinations
- `calculate_profection()`: Verify age → house → ruler calculation
- `extract_core_theme()`: Ensure 1-2 sentences max, not full RAG text
- `apply_natal_context()`: Check house/dignity/strength added correctly

### Integration Tests (per stage):
- Stage 1: Verify personalization replaces RAG paste
- Stage 2: Verify sect appears in every interpretation
- Stage 3: Verify natal aspect modifier when applicable
- Stage 4: Verify lord of year priority boost
- Stage 5: Verify timing dynamics included
- Stage 6: Verify all 7 Hephaestio factors present

### End-to-End Test:
```python
# Run full transit analysis
report = run_full_transit_analysis(birth_data_path)

# Check quality metrics:
assert "In your chart specifically" in report  # Personalization
assert all(sect_mentioned for transit in top_10)  # Sect always present
assert no_rag_dumps(report)  # No 300-word excerpts
assert executive_summary_present(report)  # Plain-language summary
assert lord_of_year_highlighted(report)  # Profection integrated
```

### Manual Validation:
- Pick one transit
- Manually calculate all 7 Hephaestio factors
- Compare to automated interpretation
- Verify astrological accuracy

---

## Plain-Language Translation Guidelines

### Avoid Jargon in Executive Summary:
❌ "Saturn square Mars with applying orb in 10th house cadent placement"
✅ "Career frustrations peak mid-month, requiring patience with obstacles"

❌ "Lord of year activates natal Venus in domicile with sect benefic status"
✅ "Relationship and creative themes are unusually prominent this year"

### Keep Technical Details in Full Analysis:
- Executive summary: Plain language for non-astrologers
- Full interpretation: Technical terms OK, explained in context
- Integration guidance: Practical actions, minimal jargon

### Translation Patterns:
```
Technical → Plain Language

"Angular placement" → "Publicly visible, affects reputation"
"Cadent house" → "Behind-the-scenes, mental preparation"
"Of sect" → "Flows naturally with your chart's energy"
"Contrary to sect" → "Creates friction, requires conscious work"
"Applying aspect" → "Building in intensity over coming weeks"
"Separating aspect" → "Influence fading, integration phase"
```

---

## Future Enhancements (Stages 7-8)

### Executive Summary Feature:

**Two Modes**:

1. **General Report**:
```
KEY THEMES FOR [DATE RANGE]

The next 30 days emphasize [theme 1], [theme 2], and [theme 3].
[Most important timing]. [Key actionable insight].
```

2. **Question-Driven Report**:
```
RESPONSE TO: "[user's question]"

[Direct answer in 2-3 sentences using transit data]
[Most relevant timing window]
```

### Conversational Input Feature:

**Intent Patterns**:
- Timing: "when should I", "good time for", "best time to"
- Current state: "what's going on with", "why is", "happening"
- Advice: "how can I", "what should I do about"
- Prediction: "will", "is going to", "future"

**Topic → House Mapping**:
```python
{
    'relationship': 7, 'partner': 7, 'marriage': 7,
    'career': 10, 'job': 10, 'business': 10,
    'money': 2, 'finances': 2,
    'home': 4, 'family': 4, 'moving': 4,
    'health': 6, 'work': 6,
    'creative': 5, 'children': 5, 'romance': 5,
    'friends': 11, 'learning': 9, 'travel': 9
}
```

**Question Flow**:
```
User input → Intent parse → Parameter check →
  [Complete? → Generate report]
  [Incomplete? → Ask questions → Get answers → Generate report]
```

---

## References

1. **Chris Brennan** - *Hellenistic Astrology: The Study of Fate and Fortune*
   - Annual profections (Chapter 17)
   - Sign-based transits
   - 7-factor Hephaestio method

2. **Robert Hand** - *Planets in Transit: Life Cycles for Living*
   - Natal aspect modification principle
   - Psychological vs event manifestation
   - Integration methodology

3. **Dorotheus/Anubio** - *Teachings on Transits* (CCAG translations)
   - Time-lord filtering
   - Lord of year priority

4. **Hephaestio** - *Apotelesmatika* 2.27.6
   - 7-factor delineation method

5. **Vettius Valens** - *Anthology*
   - Activation of planets in profected sign
   - Sect-based interpretation

---

## Implementation Timeline

### Quick Win (1 Week):
- Stage 0: Design doc ✓
- Stage 1: Basic personalization (2 days)
- Stage 2: Sect integration (1 day)
- Stage 3: Natal aspect modifier (1 day)

### Complete Traditional (2-3 Weeks):
- Stages 4-6: Profections + full Hephaestio method

### Full Feature (4-6 Weeks):
- Stages 7-8: Executive summary + conversational input

---

*Document Version: 1.0*
*Last Updated: 2025-10-04*
*Author: Transit Interpretation Enhancement Project*
