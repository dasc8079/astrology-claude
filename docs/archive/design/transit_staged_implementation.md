# Transit Interpretation - Staged Implementation Plan

## Overview

This document contains the step-by-step staged rollout plan for implementing the transit interpretation enhancements. Each stage is independently testable and builds on the previous stage.

**Reference**: See `transit_interpretation_design.md` for complete research findings and methodology.

---

## Stage 1: Basic Personalization (Core Fix)

### Goal
Replace generic RAG paste with personalized synthesis including house, dignity, and strength context.

### Changes Required

**File**: `scripts/interpretation_builder.py`

**Add Methods**:
```python
def extract_core_theme(rag_results: List[Dict]) -> str:
    """
    Extract 1-3 sentence core theme from RAG results.

    Returns:
        Brief archetypal meaning (NOT entire RAG text)
    """
    if not rag_results:
        return "No interpretation found in database."

    # Take primary result
    primary = rag_results[0]
    text = primary['chunk']['text']

    # Extract first 1-3 sentences (max 200 chars)
    sentences = text.split('.')[:3]
    theme = '. '.join(sentences).strip() + '.'

    return theme[:200]  # Hard limit

def apply_natal_context(theme: str, natal_planet_analysis: Dict, house: int) -> str:
    """
    Add house, dignity, strength context to theme.

    Returns:
        "[Theme]. In your chart: [context]"
    """
    dignity = natal_planet_analysis.get('essential_dignities', {}).get('domicile', 'neutral dignity')
    strength = natal_planet_analysis.get('strength_score', 5)
    angularity = natal_planet_analysis.get('accidental_dignities', {}).get('angularity', 'cadent')

    context = f"\n\nIn your chart specifically: This activates your {house}th house "
    context += f"({angularity} placement, "

    # House meanings
    house_meanings = {
        1: "self, body, vitality",
        2: "finances, resources, values",
        3: "communication, siblings, short travel",
        4: "home, family, roots",
        5: "creativity, children, romance",
        6: "work, health, daily routines",
        7: "relationships, partnerships",
        8: "shared resources, transformation",
        9: "philosophy, higher learning, travel",
        10: "career, reputation, public life",
        11: "friends, groups, aspirations",
        12: "spirituality, solitude, hidden matters"
    }
    context += f"{house_meanings.get(house, 'life area')}). "

    # Dignity impact
    if dignity == 'domicile':
        context += f"Your natal planet is in domicile (very strong foundation). "
    elif dignity == 'exaltation':
        context += f"Your natal planet is exalted (honored placement). "
    elif dignity == 'detriment':
        context += f"Your natal planet is in detriment (challenging position). "
    elif dignity == 'fall':
        context += f"Your natal planet is in fall (weakened state). "

    # Strength score
    if strength >= 8:
        context += f"With {strength}/10 strength, you have strong capacity in this area."
    elif strength >= 5:
        context += f"With {strength}/10 strength, you have moderate capacity here."
    else:
        context += f"With {strength}/10 strength, this area may need development."

    return theme + context
```

**Modify Method**:
```python
def synthesize_interpretation(self, query_results: List[Dict],
                              weights: Optional[Dict] = None) -> str:
    """
    OLD: Paste entire RAG results
    NEW: Extract theme only
    """
    return self.extract_core_theme(query_results)
```

**Add to run_transit_analysis.py**:
```python
# After getting RAG results, apply natal context
interpretation_theme = builder.synthesize_interpretation(rag_results)
natal_planet_data = natal_analysis['planets'].get(transit['natal_planet'], {})
house = natal_planet_data.get('house', 0)

interpretation = builder.apply_natal_context(
    interpretation_theme,
    natal_planet_data,
    house
)
transit['interpretation'] = interpretation
```

### Test
1. Run `python3 scripts/run_transit_analysis.py`
2. Check output interpretations:
   - ✓ Brief theme (1-3 sentences, not 300 words)
   - ✓ "In your chart specifically:" section present
   - ✓ House, dignity, strength mentioned
3. Compare to old output - should be MUCH shorter and personalized

### Success Criteria
- No interpretation longer than 400 characters for theme + context
- Every interpretation has house/dignity/strength info
- No more raw RAG dumps

---

## Stage 2: Add Sect Integration

### Goal
Every interpretation includes sect consideration.

### Changes Required

**File**: `scripts/interpretation_builder.py`

**Add Method**:
```python
def add_sect_consideration(interpretation: str, sect: str,
                          planet: str, sect_status: str) -> str:
    """
    Append sect-based interpretation.

    Args:
        sect: 'diurnal' or 'nocturnal'
        planet: Planet name
        sect_status: 'of-sect', 'contrary-to-sect', or 'neutral'
    """
    sect_text = f"\n\nSect consideration: In your {sect} chart, {planet} is {sect_status}. "

    if sect_status == 'of-sect':
        sect_text += "This means the energy flows naturally with your chart's fundamental nature."
    elif sect_status == 'contrary-to-sect':
        sect_text += "This means the energy creates some friction, requiring more conscious work."
    else:
        sect_text += "The Sun and Moon are essentially neutral for sect purposes."

    return interpretation + sect_text
```

**Modify run_transit_analysis.py**:
```python
# After apply_natal_context
sect = natal_analysis['sect']
natal_planet = transit['natal_planet']
natal_planet_data = natal_analysis['planets'].get(natal_planet, {})
sect_status = natal_planet_data.get('sect_analysis', {}).get('status', 'neutral')

interpretation = builder.add_sect_consideration(
    interpretation,
    sect,
    natal_planet,
    sect_status
)
```

### Test
1. Run transit analysis
2. Verify EVERY interpretation has sect paragraph
3. Check sect status accuracy (of-sect vs contrary-to-sect)

### Success Criteria
- 100% of interpretations mention sect
- Sect status correctly identified for each planet
- Appropriate explanation for each sect status

---

## Stage 3: Add Natal Aspect Modifier

### Goal
Check if natal chart has aspect between transiting & natal planet, modify interpretation accordingly.

### Changes Required

**File**: `scripts/chart_analyzer.py`

**Add Method**:
```python
def get_natal_aspect_between(planet1: str, planet2: str, natal_data: Dict) -> Optional[str]:
    """
    Find if natal aspect exists between two planets.

    Returns:
        'conjunction', 'sextile', 'square', 'trine', 'opposition', or None
    """
    from scripts.ephemeris_helper import calculate_aspect

    planets = natal_data.get('planets', {})
    p1_data = planets.get(planet1)
    p2_data = planets.get(planet2)

    if not p1_data or not p2_data:
        return None

    p1_long = p1_data.get('longitude')
    p2_long = p2_data.get('longitude')

    if p1_long is None or p2_long is None:
        return None

    aspect = calculate_aspect(p1_long, p2_long, orb=8.0)

    if aspect:
        return aspect.get('aspect')
    return None
```

**File**: `scripts/interpretation_builder.py`

**Add Method**:
```python
def apply_natal_aspect_modifier(interpretation: str, transiting_planet: str,
                                natal_planet: str, natal_aspect: str) -> str:
    """
    Prepend natal aspect modification if exists.

    This is CRITICAL per Robert Hand: "a natal or radical aspect is of primary
    importance and can seriously modify any aspect by transit or progression"
    """
    if not natal_aspect:
        return interpretation

    modifier = f"⚠️ NATAL CONTEXT MODIFIER: Your natal chart has {natal_planet} {natal_aspect} {transiting_planet}. "

    # Explain how this modifies the transit
    if natal_aspect == 'conjunction':
        modifier += "This natal unity means you're familiar with blending these energies. "
    elif natal_aspect == 'trine':
        modifier += "This natal harmony means you have an easy facility with these planets together. "
    elif natal_aspect == 'sextile':
        modifier += "This natal support shows natural cooperation between these planets. "
    elif natal_aspect == 'square':
        modifier += "This natal tension means these planets already challenge each other in your chart. "
    elif natal_aspect == 'opposition':
        modifier += "This natal polarity means you're used to balancing these planetary energies. "

    modifier += "The current transit operates THROUGH this natal relationship.\n\n"

    return modifier + interpretation
```

**Modify run_transit_analysis.py**:
```python
# BEFORE apply_natal_context, check natal aspect
from scripts.chart_analyzer import get_natal_aspect_between

natal_aspect = get_natal_aspect_between(
    transit['transiting_planet'],
    transit['natal_planet'],
    natal_data
)

if natal_aspect:
    interpretation = builder.apply_natal_aspect_modifier(
        interpretation,
        transit['transiting_planet'],
        transit['natal_planet'],
        natal_aspect
    )
```

### Test
1. Find a transit where natal aspect exists (e.g., your natal Saturn trine Neptune, check if transiting Neptune aspects natal Saturn)
2. Run transit analysis
3. Verify interpretation starts with natal aspect modifier
4. Check modifier accurately describes natal relationship

### Success Criteria
- Natal aspect check runs for every transit
- When natal aspect exists, modifier appears FIRST
- Modifier accurately describes how natal aspect changes transit meaning
- No false positives (aspect detected when none exists)

---

## Stage 4: Add Annual Profections

### Goal
Calculate lord of year, prioritize transits involving it, add profection context.

### Changes Required

**File**: `scripts/chart_analyzer.py`

**Add Method**:
```python
def calculate_profection(birth_date: datetime, current_date: datetime) -> Dict:
    """
    Calculate annual profection.

    Returns:
        {
            'age': int,
            'profected_house': int (1-12),
            'profected_sign': str,
            'lord_of_year': str  # Traditional planet only
        }
    """
    # Calculate age
    age = current_date.year - birth_date.year
    if current_date < birth_date.replace(year=current_date.year):
        age -= 1

    # Profected house = (age % 12) + 1
    # Age 0 = 1st house, Age 1 = 2nd house, etc.
    profected_house = (age % 12) + 1

    # Get profected sign (from birth data ASC + profection)
    # This requires natal chart - implement based on your ASC
    # For now, simplified version:

    from scripts.astrology_reference import HOUSES

    # Map house to sign based on natal ASC
    # This is placeholder - actual implementation needs natal ASC

    return {
        'age': age,
        'profected_house': profected_house,
        'profected_sign': 'TBD',  # Calculate from natal ASC
        'lord_of_year': 'TBD'  # Get ruler of profected sign
    }
```

**File**: `scripts/transit_calculator.py`

**Modify prioritize_transits**:
```python
def prioritize_transits(self, transits: List[Dict], natal_analysis: Dict,
                       profection: Dict = None) -> List[Dict]:
    """
    Add profection parameter, boost priority if lord of year involved.
    """
    # Existing prioritization...

    if profection:
        lord = profection.get('lord_of_year')
        for transit in scored_transits:
            # Check if transit involves lord of year
            if (transit['transiting_planet'] == lord or
                transit['natal_planet'] == lord):
                transit['priority_score'] += 20  # Massive boost
                transit['lord_involvement'] = True

    # Sort and return
```

**File**: `scripts/interpretation_builder.py`

**Add Method**:
```python
def add_profection_context(interpretation: str, profection: Dict,
                          transiting_planet: str, natal_planet: str) -> str:
    """Add lord of year context if relevant."""

    lord = profection.get('lord_of_year')
    house = profection.get('profected_house')
    age = profection.get('age')

    if transiting_planet == lord or natal_planet == lord:
        context = f"\n\n🎯 LORD OF YEAR ACTIVATION: At age {age}, you're in a {house}th house profection year, "
        context += f"making {lord} the lord of the year. This transit involving {lord} is CRITICALLY important "
        context += f"for your annual themes and likely to manifest as significant events."
    else:
        context = f"\n\nProfection context: Age {age} activates the {house}th house with {lord} as lord. "
        context += f"This transit is secondary to themes involving {lord}."

    return interpretation + context
```

**Modify run_transit_analysis.py**:
```python
# At start of workflow
from scripts.chart_analyzer import calculate_profection
from datetime import datetime

birth_date = datetime(1987, 7, 30)  # From natal data
current_date = datetime.utcnow()

profection = calculate_profection(birth_date, current_date)
print(f"Current profection: Age {profection['age']}, {profection['profected_house']}th house")

# Pass to prioritization
prioritized = calc.prioritize_transits(current_transits, natal_analysis, profection)

# Add to interpretation
interpretation = builder.add_profection_context(
    interpretation,
    profection,
    transit['transiting_planet'],
    transit['natal_planet']
)
```

### Test
1. Calculate your current profection manually (age % 12)
2. Run transit analysis
3. Verify profection calculated correctly
4. Check transits involving lord of year are ranked higher
5. Verify profection context in interpretations

### Success Criteria
- Profection calculation accurate
- Lord of year identified correctly
- Transits involving lord have +20 priority boost
- Every interpretation mentions profection context

---

## Stage 5: Add Timing Dynamics

### Goal
Include orb tightness, applying/separating, retrograde meaning in interpretations.

### Changes Required

**File**: `scripts/interpretation_builder.py`

**Add Method**:
```python
def add_timing_dynamics(interpretation: str, orb: float,
                       applying: bool, retrograde: bool) -> str:
    """Add timing interpretation."""

    timing = "\n\nTiming dynamics: "

    # Orb tightness
    if orb < 1.0:
        timing += f"At {orb:.2f}° orb, this is VERY TIGHT and highly active. "
    elif orb < 3.0:
        timing += f"At {orb:.2f}° orb, this is active and significant. "
    elif orb < 5.0:
        timing += f"At {orb:.2f}° orb, this is building in strength. "
    else:
        timing += f"At {orb:.2f}° orb, this is in background, not yet peak. "

    # Applying/separating
    if applying:
        timing += "The aspect is APPLYING (approaching exact), meaning influence is growing stronger. "
    else:
        timing += "The aspect is SEPARATING (moving past exact), meaning influence is waning and integration phase. "

    # Retrograde
    if retrograde:
        timing += "The transiting planet is RETROGRADE, emphasizing internal processing, review, and revision rather than external action."

    return interpretation + timing
```

**Modify run_transit_analysis.py**:
```python
interpretation = builder.add_timing_dynamics(
    interpretation,
    transit['exact_orb'],
    transit['applying'],
    transit['retrograde']
)
```

### Test
1. Run transit analysis
2. Check each interpretation has timing section
3. Verify orb, applying/separating, retrograde status accurate

### Success Criteria
- Every interpretation has timing paragraph
- Orb interpretation matches actual orb
- Applying/separating correctly identified
- Retrograde noted when applicable

---

## Stage 6: Full Hephaestio Method (Advanced)

### Goal
Complete 7-factor analysis (mixture, position, phase, see by fixity, see by transit).

### Changes Required

**File**: `scripts/chart_analyzer.py`

**Add Methods**:
```python
def calculate_phase_to_sun(planet_long: float, sun_long: float) -> str:
    """
    Determine oriental/occidental/under beams/cazimi.

    Returns:
        'oriental' (rising before Sun)
        'occidental' (rising after Sun)
        'under beams' (within 15° of Sun)
        'combust' (within 8.5° of Sun)
        'cazimi' (within 17' of Sun)
    """
    diff = abs(planet_long - sun_long)
    if diff > 180:
        diff = 360 - diff

    if diff <= (17/60):  # 17 arc minutes
        return 'cazimi'
    elif diff <= 8.5:
        return 'combust'
    elif diff <= 15:
        return 'under beams'
    elif planet_long < sun_long:
        return 'oriental'
    else:
        return 'occidental'

def get_natal_aspects_to_planet(planet: str, natal_data: Dict) -> List[Dict]:
    """
    Find all natal aspects TO this planet ("see by fixity").

    Returns:
        [{'planet': 'Mars', 'aspect': 'trine'}, ...]
    """
    from scripts.ephemeris_helper import calculate_aspect

    aspects = []
    planets = natal_data.get('planets', {})
    target = planets.get(planet)

    if not target:
        return []

    for other_planet, other_data in planets.items():
        if other_planet == planet:
            continue

        aspect = calculate_aspect(
            target.get('longitude'),
            other_data.get('longitude'),
            orb=8.0
        )

        if aspect:
            aspects.append({
                'planet': other_planet,
                'aspect': aspect.get('aspect')
            })

    return aspects
```

**File**: `scripts/interpretation_builder.py`

**Add Comprehensive Method**:
```python
def build_hephaestio_interpretation(self, transit: Dict, natal_analysis: Dict,
                                   profection: Dict, rag_results: List[Dict]) -> str:
    """
    Apply complete 7-factor Hephaestio method:
    1. Lord of year
    2. Mixture (natal aspects FROM planet)
    3. Position (house & sign)
    4. Phase (relationship to Sun)
    5. See by fixity (natal aspects TO planet)
    6. See by transit (current transiting aspects)
    7. Natal vs transit condition
    """
    # Start with core theme
    interpretation = self.extract_core_theme(rag_results)

    # Factor 1: Lord of year
    interpretation = self.add_profection_context(
        interpretation, profection,
        transit['transiting_planet'], transit['natal_planet']
    )

    # Factor 2: Mixture (natal aspects FROM)
    # Factor 3: Position (house & sign)
    natal_planet_data = natal_analysis['planets'].get(transit['natal_planet'], {})
    interpretation = self.apply_natal_context(
        interpretation,
        natal_planet_data,
        natal_planet_data.get('house', 0)
    )

    # Factor 4: Phase
    # Factor 5: See by fixity
    # Factor 6: See by transit
    # (Implement these...)

    # Factor 7: Natal vs transit condition
    # (Compare dignities)

    # Add sect
    sect = natal_analysis['sect']
    sect_status = natal_planet_data.get('sect_analysis', {}).get('status')
    interpretation = self.add_sect_consideration(
        interpretation, sect,
        transit['natal_planet'], sect_status
    )

    # Add timing
    interpretation = self.add_timing_dynamics(
        interpretation,
        transit['exact_orb'],
        transit['applying'],
        transit['retrograde']
    )

    return interpretation
```

### Test
1. Pick one transit
2. Manually calculate all 7 factors
3. Run analysis
4. Compare automated output to manual calculation
5. Verify all factors present and accurate

### Success Criteria
- All 7 Hephaestio factors present
- Astrologically accurate
- Properly synthesized (not list of disconnected facts)

---

## Stage 7: Executive Summary

### Goal
Plain-language summary at top of report.

### Changes Required

**File**: `scripts/run_transit_analysis.py`

**Add Method**:
```python
def generate_executive_summary(top_transits: List[Dict], natal_analysis: Dict) -> str:
    """
    Create 2-3 sentence plain-language summary.

    Focus on:
    - Top 3 themes from transits
    - Key timing
    - Actionable insight
    """
    # Analyze top 3-5 transits
    themes = []
    key_dates = []

    for transit in top_transits[:3]:
        # Extract theme
        house = natal_analysis['planets'][transit['natal_planet']]['house']

        # Map house to life area (plain language)
        area_map = {
            1: "personal vitality", 2: "financial matters",
            3: "communication", 4: "home and family",
            5: "creative expression", 6: "work and health",
            7: "relationships", 8: "shared resources",
            9: "learning and travel", 10: "career",
            11: "friendships", 12: "spirituality"
        }

        themes.append(area_map.get(house, f"{house}th house matters"))

        # Track timing
        if transit.get('exact_date'):
            key_dates.append(transit['exact_date'])

    # Build summary
    summary = "## KEY THEMES FOR NEXT 30 DAYS\n\n"

    if len(themes) >= 2:
        summary += f"The upcoming period emphasizes {themes[0]} and {themes[1]}. "

    if key_dates:
        earliest = min(key_dates)
        summary += f"Key developments peak around {earliest.strftime('%B %d')}. "

    # Actionable insight based on applying vs separating
    applying_count = sum(1 for t in top_transits[:3] if t['applying'])
    if applying_count >= 2:
        summary += "Focus energy on initiating rather than concluding, as influences are building."
    else:
        summary += "Focus on integration and completion of recent developments."

    summary += "\n\n---\n\n"

    return summary
```

**Modify main workflow**:
```python
# After getting top transits, generate summary
summary = generate_executive_summary(top_transits, natal_analysis)

# Prepend to report
report = summary + report
```

### Test
1. Run transit analysis
2. Read executive summary WITHOUT looking at technical report
3. Ask: "Can a non-astrologer understand this?"
4. Ask: "Is it actionable?"
5. Verify summary accurately reflects top transits

### Success Criteria
- Summary is 2-3 sentences max
- Plain language (minimal jargon)
- Actionable (not just descriptive)
- Accurately reflects top transits

---

## Stage 8: Conversational Input (Future Phase)

### Goal
Natural language questions → targeted reports.

### Architecture

**New File**: `scripts/conversational_transit.py`

**Components**:
1. Intent parser
2. Parameter validator
3. Question generator
4. Targeted report generator
5. Conversational entry point

### Implementation (Detailed in design doc)

See `transit_interpretation_design.md` section "Future Enhancements" for full specifications.

---

## Testing Protocol

### Before Each Stage:
1. Run `python3 scripts/run_transit_analysis.py`
2. Save output as `baseline_stageX.txt`
3. Note what's missing/broken

### After Each Stage:
1. Run transit analysis
2. Compare to baseline
3. Verify new feature works
4. Check nothing broke
5. Git commit if successful

### Rollback:
```bash
# If stage fails
git log --oneline  # Find last working commit
git revert <commit-hash>
```

---

## Progress Tracking

### Stage 0: ✅ COMPLETE
- Design document created
- Research compiled
- Implementation plan documented

### Stage 1: ⏳ PENDING
- Basic personalization

### Stage 2: ⏳ PENDING
- Sect integration

### Stage 3: ⏳ PENDING
- Natal aspect modifier

### Stage 4: ⏳ PENDING
- Annual profections

### Stage 5: ⏳ PENDING
- Timing dynamics

### Stage 6: ⏳ PENDING
- Full Hephaestio method

### Stage 7: ⏳ PENDING
- Executive summary

### Stage 8: ⏳ PENDING
- Conversational input

---

*Document Version: 1.0*
*Last Updated: 2025-10-04*
*Implementation Status: Planning Complete, Ready for Execution*
