# Life Arc V3 Significance System Specification

**Version**: 3.0
**Created**: 2025-10-12
**Status**: Draft - Ready for Implementation
**Author**: Collaborative design session (User + Claude)

---

## Overview

### Problem Statement

The current Life Arc significance detection system (V1/V2) fails to capture multi-year difficult periods that are experientially significant to users. Specifically:

1. **Saturn Return Aftermath Missed**: Ages 29-35 was user's most difficult life period, but only age 29 scored as SIGNIFICANT (15pts). The 3-5 year rebuilding period scored below threshold (8-13pts), creating no narrative coverage despite being extremely difficult.

2. **Traditional Periods Ignored**: Traditional Hellenistic concepts like "Loosing of the Bond" (final years before major L1 transitions) and "Peak Periods" (bonification when L2 matches L1) are not scored, despite being traditionally significant.

3. **Noise from Granular Periods**: V2 attempted to reduce noise by removing L2/Firdaria subs from convergence, but this was too aggressive - it removed meaningful patterns along with noise.

4. **Good Periods Underweighted**: System emphasizes difficult periods but doesn't equivalently highlight traditionally fortunate periods (11H profection years, peak periods, benefic-ruled years).

### Goals

1. **Capture Multi-Year Difficult Periods**: Saturn Returns should score the return moment AND assess whether the aftermath period needs extended coverage (ages 29-35 style).

2. **Integrate Traditional Significance**: Loosing of the Bond, Peak Periods, and other traditional Hellenistic concepts should receive scoring bonuses regardless of mechanical convergence.

3. **Balance Good and Bad**: Highlight traditionally fortunate periods (peak periods, 11H years, benefic activations) with equal weight to difficult periods.

4. **Maintain Clarity**: ~15 major events across 100 years (not 40+), organized around chapter-level transitions.

5. **Contextual Assessment**: Saturn Return difficulty should be assessed based on natal chart (6H/8H/12H placement, malefic of sect, afflictions) to determine whether 1-2 year or 3-5 year coverage is appropriate.

### Non-Goals

- Daily transit timing precision
- Complete algorithm redesign (keep convergence foundation)
- Predictive event forecasting
- Removing L2 data entirely (V2 mistake - keep data, just score selectively)

---

## Requirements

### Functional Requirements

1. **System MUST assess Saturn Return contextually**:
   - Check natal Saturn: house placement (6/8/12 = difficult), sect (malefic contrary = difficult), dignity (detriment/fall = challenged), aspects (afflicted = difficult)
   - IF 2+ difficulty indicators: Score return year 15pts, add +8pts/year for next 3-5 years "rebuilding period"
   - IF Saturn well-placed: Score return year 15pts, add +3pts/year for next 1-2 years only

2. **System MUST detect Loosing of the Bond**:
   - Identify final L2 period before each L1 transition
   - Add +10pts to ages within that final L2 period
   - Traditional significance: preparatory/intense phase before major chapter shift

3. **System MUST detect Peak Periods (bonification)**:
   - When ZR Fortune L2 matches L1 sign (e.g., Capricorn L2 within Capricorn L1)
   - Add +10pts to ages within that peak period
   - Traditional significance: empowered phase, smooth expression of chapter themes

4. **System MUST highlight good periods**:
   - 11H profection years: +3pts (traditionally fortunate - friends, hopes, benefactors)
   - 5H profection years: +2pts (creativity, pleasure, joy)
   - Benefic-ruled profection years (Jupiter/Venus): +2pts
   - Peak periods: +10pts (see #3 above)

5. **System MUST maintain L2 data** but score selectively:
   - Keep L2 periods in timeline data structure
   - Only score L2 transitions that are traditionally significant (peak, loosing, climax)
   - Regular L2 transitions score 0pts

6. **System SHOULD detect other traditional periods**:
   - Climax/culmination: Midpoint of L1 period → +5pts
   - Opening phase: First 2 years of new L1 → +5pts

### Non-Functional Requirements

- **Performance**: Scoring calculation should complete in <1 second per 100-year timeline
- **Backward Compatibility**: V1/V2 agents should continue working (don't break existing function signatures)
- **Testing**: All changes must be validated against Darren's profile ages 29-39 to confirm ages 29-35 period is captured

### Edge Cases

1. **Well-placed Saturn Returns**: User with Saturn exalted in Libra in 10H (day chart, benefic of sect) → Brief coverage (1-2 years), not extended
2. **Multiple malefic indicators**: Saturn in Cancer in 12H, malefic contrary to sect, square Mars → Maximum difficulty, 5-year aftermath coverage
3. **Peak periods during difficult chapters**: Capricorn Peak Period (L2=L1) during ages 12-15 within overall difficult Capricorn chapter → Both +10pts for peak AND context of challenging chapter
4. **Loosing of Bond + Saturn Return convergence**: Age 37-39 has both Loosing of Bond (+10) AND approaches major L1 shift (+15) → Scores stack appropriately
5. **Jupiter Return during Peak Period**: Age 12 has both Jupiter Return (+8) and Peak Period (+10) → Correctly highlights fortunate transition
6. **11H profection year + Peak Period**: Age where both occur → Bonuses stack (+3 + +10 = +13), creates NOTABLE event

---

## Design

### Architecture

**Hybrid Scoring System**: Mechanical convergence PLUS traditional significance overlays

```
Total Score = Base Convergence Score + Traditional Overlays + Contextual Bonuses
```

**Components**:

1. **Base Convergence** (existing V2 system):
   - L1 transitions: 15pts (Fortune), 10pts (Spirit)
   - Major planetary returns: 15pts (Saturn), 8pts (Jupiter)
   - Profection cycles: varies
   - Firdaria major periods: 5pts

2. **Traditional Overlays** (NEW):
   - Loosing of Bond detection: +10pts
   - Peak Period detection: +10pts
   - Climax detection: +5pts
   - Opening Phase detection: +5pts
   - Good house profections: +2-3pts

3. **Contextual Bonuses** (NEW):
   - Saturn Return aftermath: +8pts/year (if difficult) or +3pts/year (if well-placed)
   - Difficult house profections (6H/8H/12H) + malefic activation: +3pts
   - Multiple malefic convergence: +5pts

### Data Structures

**Scoring Configuration**:
```python
SCORING_RULES_V3 = {
    # Base convergence (existing)
    'l1_fortune_transition': 15,
    'l1_spirit_transition': 10,
    'saturn_return': 15,
    'jupiter_return': 8,
    'uranus_opposition': 10,
    'progressed_sun_sign_change': 12,
    'firdaria_major_transition': 5,

    # Traditional overlays (NEW)
    'loosing_of_bond': 10,
    'peak_period': 10,
    'climax_period': 5,
    'opening_phase': 5,

    # Profection overlays (NEW)
    'profection_11h': 3,  # fortunate house
    'profection_5h': 2,   # joyful house
    'profection_10h': 2,  # career house
    'profection_difficult': 3,  # 6H/8H/12H
    'profection_benefic_ruled': 2,  # Jupiter/Venus year
    'profection_malefic_ruled': 2,  # IF malefic of sect

    # Contextual bonuses (NEW)
    'saturn_return_difficult_aftermath': 8,  # per year for 3-5 years
    'saturn_return_easy_aftermath': 3,       # per year for 1-2 years
    'multiple_malefic_convergence': 5,
    'multiple_benefic_convergence': 5,
}

THRESHOLDS = {
    'major': 25,        # Chapter-defining
    'significant': 15,  # Major milestones
    'notable': 8        # Worth mentioning
}
```

**Saturn Return Assessment**:
```python
def assess_saturn_return_difficulty(natal_data: dict) -> dict:
    """
    Assess whether Saturn return will be difficult based on natal condition.

    Returns:
        {
            'difficulty_level': 'extreme' | 'difficult' | 'moderate' | 'easy',
            'indicators': [list of difficulty factors],
            'aftermath_years': int (1-5),
            'aftermath_bonus': int (3-8 per year)
        }
    """
    saturn = natal_data['planets']['Saturn']
    difficulty_score = 0
    indicators = []

    # Check house placement
    if saturn['house'] in [6, 8, 12]:
        difficulty_score += 2
        indicators.append(f"{saturn['house']}H placement (difficult house)")

    # Check sect
    if natal_data['sect'] == 'night' and not saturn.get('sect_benefic'):
        difficulty_score += 2
        indicators.append("Malefic contrary to sect")

    # Check dignity
    if saturn['dignities']['essential']['detriment']:
        difficulty_score += 1
        indicators.append("Detriment (Cancer)")
    elif saturn['dignities']['essential']['fall']:
        difficulty_score += 1
        indicators.append("Fall (Aries)")

    # Check afflictions
    difficult_aspects = [a for a in saturn['aspects']
                        if a['aspect_type'] in ['square', 'opposition']
                        and a['planet_2'] in ['Mars', 'Saturn']]
    if len(difficult_aspects) >= 2:
        difficulty_score += 1
        indicators.append(f"{len(difficult_aspects)} difficult aspects")

    # Determine level and aftermath
    if difficulty_score >= 4:
        level = 'extreme'
        aftermath_years = 5
        aftermath_bonus = 8
    elif difficulty_score >= 2:
        level = 'difficult'
        aftermath_years = 3
        aftermath_bonus = 8
    elif difficulty_score == 1:
        level = 'moderate'
        aftermath_years = 2
        aftermath_bonus = 5
    else:
        level = 'easy'
        aftermath_years = 1
        aftermath_bonus = 3

    return {
        'difficulty_level': level,
        'indicators': indicators,
        'aftermath_years': aftermath_years,
        'aftermath_bonus': aftermath_bonus,
        'difficulty_score': difficulty_score
    }
```

**Traditional Period Detection**:
```python
def detect_traditional_periods(timeline: dict) -> dict:
    """
    Detect traditional Hellenistic significant periods.

    Returns:
        {
            'loosing_of_bond': [
                {'ages': (37, 39), 'l1_sign': 'Capricorn', 'l2_sign': 'Sagittarius'},
                ...
            ],
            'peak_periods': [
                {'ages': (12, 15), 'sign': 'Capricorn'},
                ...
            ],
            'climax_periods': [
                {'age': 25, 'l1_sign': 'Capricorn', 'midpoint': True},
                ...
            ],
            'opening_phases': [
                {'ages': (39, 41), 'l1_sign': 'Aquarius'},
                ...
            ]
        }
    """
    periods = {
        'loosing_of_bond': [],
        'peak_periods': [],
        'climax_periods': [],
        'opening_phases': []
    }

    # Detect Loosing of Bond (final L2 before L1 transition)
    for i, l1_period in enumerate(timeline['zr_fortune']['l1_periods']):
        if i < len(timeline['zr_fortune']['l1_periods']) - 1:
            # Get final L2 period before this L1 ends
            l2_periods_in_l1 = [l2 for l2 in timeline['zr_fortune']['l2_periods']
                               if l1_period['start_age'] <= l2['start_age'] < l1_period['end_age']]
            if l2_periods_in_l1:
                final_l2 = l2_periods_in_l1[-1]
                periods['loosing_of_bond'].append({
                    'ages': (int(final_l2['start_age']), int(l1_period['end_age'])),
                    'l1_sign': l1_period['sign'],
                    'l2_sign': final_l2['sign']
                })

    # Detect Peak Periods (L2 matches L1 sign)
    for l1_period in timeline['zr_fortune']['l1_periods']:
        l2_periods_in_l1 = [l2 for l2 in timeline['zr_fortune']['l2_periods']
                           if l1_period['start_age'] <= l2['start_age'] < l1_period['end_age']]
        for l2 in l2_periods_in_l1:
            if l2['sign'] == l1_period['sign']:
                periods['peak_periods'].append({
                    'ages': (int(l2['start_age']), int(l2['end_age'])),
                    'sign': l1_period['sign']
                })

    # Detect Climax (midpoint of L1 period)
    for l1_period in timeline['zr_fortune']['l1_periods']:
        midpoint = (l1_period['start_age'] + l1_period['end_age']) / 2
        periods['climax_periods'].append({
            'age': int(midpoint),
            'l1_sign': l1_period['sign'],
            'midpoint': True
        })

    # Detect Opening Phases (first 2 years of L1)
    for l1_period in timeline['zr_fortune']['l1_periods']:
        periods['opening_phases'].append({
            'ages': (int(l1_period['start_age']), int(l1_period['start_age'] + 2)),
            'l1_sign': l1_period['sign']
        })

    return periods
```

### Algorithms

**V3 Convergence Scoring Algorithm**:

```python
def calculate_convergence_score_v3(age: int, snapshot: dict, timeline: dict,
                                   traditional_periods: dict,
                                   saturn_assessment: dict) -> tuple[int, List[str]]:
    """
    Calculate convergence score with traditional overlays and contextual bonuses.

    Args:
        age: Current age being scored
        snapshot: Data snapshot for this age
        timeline: Full timeline data
        traditional_periods: Traditional period detections
        saturn_assessment: Saturn return difficulty assessment

    Returns:
        (score, reasons) tuple
    """
    score = 0
    reasons = []

    # === BASE CONVERGENCE (existing) ===

    # L1 transitions
    if snapshot['fortune_l1_transition']:
        score += 15
        reasons.append(f"Fortune L1 → {snapshot['fortune_l1']['sign']}")

    if snapshot['spirit_l1_transition']:
        score += 10
        reasons.append(f"Spirit L1 → {snapshot['spirit_l1']['sign']}")

    # Planetary returns
    if snapshot.get('saturn_return'):
        score += 15
        reasons.append("Saturn Return")

    if snapshot.get('jupiter_return'):
        score += 8
        reasons.append("Jupiter Return")

    if snapshot.get('uranus_opposition'):
        score += 10
        reasons.append("Uranus Opposition")

    # Progressed Sun sign change
    if snapshot.get('progressed_sun_change'):
        score += 12
        reasons.append(f"Progressed Sun → {snapshot['progressed_sun']['new_sign']}")

    # Firdaria major period change
    if snapshot.get('firdaria_major_transition'):
        score += 5
        reasons.append(f"Firdaria → {snapshot['firdaria']['planet']}")

    # === TRADITIONAL OVERLAYS (NEW) ===

    # Loosing of Bond
    for period in traditional_periods['loosing_of_bond']:
        if period['ages'][0] <= age <= period['ages'][1]:
            score += 10
            reasons.append(f"Loosing of Bond ({period['l1_sign']} ending)")
            break

    # Peak Period
    for period in traditional_periods['peak_periods']:
        if period['ages'][0] <= age <= period['ages'][1]:
            score += 10
            reasons.append(f"Peak Period ({period['sign']} empowered)")
            break

    # Climax
    for period in traditional_periods['climax_periods']:
        if abs(age - period['age']) <= 0.5:
            score += 5
            reasons.append(f"Climax ({period['l1_sign']} midpoint)")
            break

    # Opening Phase
    for period in traditional_periods['opening_phases']:
        if period['ages'][0] <= age <= period['ages'][1]:
            score += 5
            reasons.append(f"Opening Phase ({period['l1_sign']} begins)")
            break

    # Profection overlays
    profection_house = snapshot['profection']['house']
    profection_lord = snapshot['profection']['lord']

    if profection_house == 11:
        score += 3
        reasons.append("11H profection (fortunate)")
    elif profection_house == 5:
        score += 2
        reasons.append("5H profection (joyful)")
    elif profection_house == 10:
        score += 2
        reasons.append("10H profection (career)")
    elif profection_house in [6, 8, 12]:
        score += 3
        reasons.append(f"{profection_house}H profection (difficult)")

    if profection_lord in ['Jupiter', 'Venus']:
        score += 2
        reasons.append(f"{profection_lord} year (benefic)")

    # === CONTEXTUAL BONUSES (NEW) ===

    # Saturn Return aftermath
    saturn_return_age = snapshot.get('saturn_return_age')
    if saturn_return_age:
        years_since = age - saturn_return_age
        if 0 < years_since <= saturn_assessment['aftermath_years']:
            score += saturn_assessment['aftermath_bonus']
            reasons.append(f"Saturn Return aftermath year {int(years_since)}")

    # Multiple malefic convergence
    malefic_count = sum([
        snapshot.get('saturn_activation', False),
        snapshot.get('mars_activation', False),
        profection_house in [6, 8, 12],
        any('Saturn' in r or 'Mars' in r for r in reasons)
    ])
    if malefic_count >= 3:
        score += 5
        reasons.append("Multiple malefic convergence")

    # Multiple benefic convergence
    benefic_count = sum([
        snapshot.get('jupiter_activation', False),
        snapshot.get('venus_activation', False),
        profection_house in [5, 11],
        any('Jupiter' in r or 'Venus' in r for r in reasons),
        any('Peak Period' in r for r in reasons)
    ])
    if benefic_count >= 3:
        score += 5
        reasons.append("Multiple benefic convergence")

    return score, reasons
```

### Integration Points

**life_arc_generator.py modifications**:
1. Add `assess_saturn_return_difficulty()` function
2. Add `detect_traditional_periods()` function
3. Modify `calculate_convergence_score()` to accept `traditional_periods` and `saturn_assessment`
4. Add `mode='v3'` parameter to `generate_life_arc_timeline()` function
5. Keep backward compatibility: `mode='v2'` uses old scoring

**life-arc-interpreter agent**:
- Create new `life-arc-interpreter-v3.md` agent
- Agent calls `generate_life_arc_timeline()` with `mode='v3'`
- Agent interprets traditional periods narratively
- Agent provides context for Saturn Return aftermath periods
- Agent highlights good periods equivalently to difficult ones

---

## Implementation Plan

### Phase 1: Core Contextual Rules (Estimated: 4-6 hours)

**Tasks**:
1. Implement `assess_saturn_return_difficulty()` function in life_arc_generator.py
   - Validation: Test with Darren's chart (Saturn in Capricorn 6H, malefic contrary to sect)
   - Expected: difficulty_level='difficult', aftermath_years=3-5, aftermath_bonus=8

2. Implement `detect_traditional_periods()` function
   - Validation: Test with Darren's timeline ages 0-100
   - Expected: Loosing of Bond detected at ages 37-39 (Capricorn→Aquarius)
   - Expected: Peak Period detected at ages 12-15 (Capricorn L2 in Capricorn L1)

3. Modify `calculate_convergence_score()` to use traditional overlays
   - Add traditional_periods parameter
   - Add saturn_assessment parameter
   - Keep backward compatibility with mode parameter

4. Add Saturn Return aftermath scoring loop
   - For each age 1-5 years after Saturn Return, add aftermath bonus
   - Validation: Ages 30-35 should score +8pts each year for Darren

**Validation Criteria**:
- ✅ Darren ages 29-35 all score NOTABLE or higher (8+ points)
- ✅ Age 29 scores SIGNIFICANT (15+ points)
- ✅ Ages 37-39 score SIGNIFICANT (Loosing of Bond + approaching L1 shift)
- ✅ Ages 12-15 score NOTABLE (Peak Period)

### Phase 2: Traditional Overlays & Good Periods (Estimated: 3-4 hours)

**Tasks**:
1. Implement profection house overlays (11H, 5H, 10H bonuses)
2. Implement profection lord overlays (benefic-ruled years)
3. Implement climax detection (midpoint of L1)
4. Implement opening phase detection (first 2 years of L1)
5. Test good period detection with multiple profiles

**Validation Criteria**:
- ✅ 11H profection years score +3pts bonus
- ✅ Peak periods score +10pts
- ✅ Benefic-ruled years score appropriately
- ✅ Good periods are narratively highlighted equivalently to difficult periods

### Phase 3: Agent Creation & Testing (Estimated: 2-3 hours)

**Tasks**:
1. Create life-arc-interpreter-v3.md agent
   - Copy from v2 agent
   - Update to call `generate_life_arc_timeline(mode='v3')`
   - Update narrative instructions to cover traditional periods
   - Update to provide Saturn Return context

2. Generate test report for Darren ages 0-100
   - Compare against V1 output (if available)
   - Compare against V2 output
   - Validate ages 29-35 coverage

3. Create comparison document showing V2→V3 changes
   - Document in docs/life_arc_interpreter_v2_to_v3_changes.md
   - Show sample output differences

4. Update version tracker
   - Update docs/life_arc_interpreter_versions.md with V3 entry

**Validation Criteria**:
- ✅ V3 report covers ages 29-35 difficult period narratively
- ✅ Loosing of Bond periods are described
- ✅ Peak periods are highlighted
- ✅ Saturn Return includes aftermath context
- ✅ Good periods receive equivalent emphasis to difficult periods

---

## Testing Strategy

### Unit Tests

**Test 1: Saturn Return Assessment**
```python
def test_saturn_return_assessment_difficult():
    """Test Saturn in difficult condition"""
    natal_data = {
        'sect': 'night',
        'planets': {
            'Saturn': {
                'house': 6,
                'dignities': {'essential': {'domicile': True}},
                'aspects': []
            }
        }
    }
    result = assess_saturn_return_difficulty(natal_data)
    assert result['difficulty_level'] in ['difficult', 'extreme']
    assert result['aftermath_years'] >= 3
    assert result['aftermath_bonus'] >= 8

def test_saturn_return_assessment_easy():
    """Test Saturn in favorable condition"""
    natal_data = {
        'sect': 'day',
        'planets': {
            'Saturn': {
                'house': 10,
                'dignities': {'essential': {'exaltation': True}},
                'aspects': []
            }
        }
    }
    result = assess_saturn_return_difficulty(natal_data)
    assert result['difficulty_level'] in ['easy', 'moderate']
    assert result['aftermath_years'] <= 2
```

**Test 2: Traditional Period Detection**
```python
def test_loosing_of_bond_detection():
    """Test Loosing of Bond detection"""
    timeline = generate_test_timeline()
    periods = detect_traditional_periods(timeline)

    # Should detect final L2 before each L1 transition
    assert len(periods['loosing_of_bond']) > 0

    # Check specific case: Capricorn→Aquarius at age 39
    capricorn_loosing = [p for p in periods['loosing_of_bond']
                         if p['l1_sign'] == 'Capricorn']
    assert len(capricorn_loosing) == 1
    assert 37 <= capricorn_loosing[0]['ages'][0] <= 38
    assert 38 <= capricorn_loosing[0]['ages'][1] <= 39

def test_peak_period_detection():
    """Test Peak Period detection"""
    timeline = generate_test_timeline()
    periods = detect_traditional_periods(timeline)

    # Should detect L2=L1 matches
    assert len(periods['peak_periods']) > 0

    # Check specific case: Capricorn L2 in Capricorn L1
    capricorn_peak = [p for p in periods['peak_periods']
                      if p['sign'] == 'Capricorn']
    assert len(capricorn_peak) >= 1
```

**Test 3: V3 Convergence Scoring**
```python
def test_v3_scoring_darren_age_29():
    """Test age 29 scores correctly with Saturn Return"""
    snapshot = get_darren_snapshot(age=29)
    timeline = generate_darren_timeline()
    traditional = detect_traditional_periods(timeline)
    saturn_assessment = assess_saturn_return_difficulty(get_darren_natal())

    score, reasons = calculate_convergence_score_v3(
        29, snapshot, timeline, traditional, saturn_assessment
    )

    assert score >= 15  # SIGNIFICANT threshold
    assert any('Saturn Return' in r for r in reasons)

def test_v3_scoring_darren_age_32():
    """Test age 32 scores with aftermath bonus"""
    snapshot = get_darren_snapshot(age=32)
    timeline = generate_darren_timeline()
    traditional = detect_traditional_periods(timeline)
    saturn_assessment = assess_saturn_return_difficulty(get_darren_natal())

    score, reasons = calculate_convergence_score_v3(
        32, snapshot, timeline, traditional, saturn_assessment
    )

    assert score >= 8  # NOTABLE threshold (was 13 in V2, failed threshold)
    assert any('aftermath' in r.lower() for r in reasons)

def test_v3_scoring_darren_age_38():
    """Test age 38 scores with Loosing of Bond"""
    snapshot = get_darren_snapshot(age=38)
    timeline = generate_darren_timeline()
    traditional = detect_traditional_periods(timeline)
    saturn_assessment = assess_saturn_return_difficulty(get_darren_natal())

    score, reasons = calculate_convergence_score_v3(
        38, snapshot, timeline, traditional, saturn_assessment
    )

    assert score >= 8  # Should have Loosing of Bond bonus
    assert any('Loosing of Bond' in r for r in reasons)
```

### Integration Tests

**Integration Test 1: Full Timeline Generation**
```python
def test_full_v3_timeline_darren():
    """Test complete V3 timeline for Darren profile"""
    timeline = generate_life_arc_timeline(
        profile_name='darren',
        start_age=0,
        end_age=100,
        mode='v3'
    )

    # Check V3-specific fields exist
    assert 'traditional_periods' in timeline
    assert 'saturn_assessment' in timeline
    assert 'mode' in timeline
    assert timeline['mode'] == 'v3'

    # Check convergence events
    convergence = timeline['convergence']

    # Validate ages 29-35 are captured
    ages_29_35 = [e for e in convergence['significant'] + convergence['notable']
                  if 29 <= e['age'] <= 35]
    assert len(ages_29_35) >= 5  # At least 5 of these years should be notable+
```

**Integration Test 2: Agent Invocation**
```python
def test_life_arc_interpreter_v3_agent():
    """Test V3 agent generates report correctly"""
    # Invoke agent (via Task tool or direct call)
    result = invoke_agent(
        'life-arc-interpreter-v3',
        profile='darren',
        start_age=0,
        end_age=100
    )

    # Check output files exist
    assert os.path.exists('profiles/darren/output/life_arc_interpretation_darren_ages_0-100_v3.md')

    # Check content includes traditional periods
    content = open('profiles/darren/output/life_arc_interpretation_darren_ages_0-100_v3.md').read()
    assert 'ages 29' in content.lower() or 'saturn return' in content.lower()
    assert 'ages 31' in content.lower() or 'ages 32' in content.lower()  # Aftermath coverage
```

### User Acceptance Criteria

**UAT 1: Ages 29-35 Coverage**
- ✅ User can read report and see narrative coverage of ages 29-35 difficult period
- ✅ Report explains WHY this period was difficult (Saturn Return + aftermath)
- ✅ Report provides context (natal Saturn condition, when relief comes)

**UAT 2: Traditional Periods Highlighted**
- ✅ Loosing of Bond periods are described narratively (not just scored)
- ✅ Peak periods are highlighted as empowered/smooth phases
- ✅ Reader understands traditional astrological concepts without jargon

**UAT 3: Good Periods Balanced**
- ✅ Fortunate periods (11H years, peak periods) receive equivalent narrative weight
- ✅ Report doesn't feel like "doom and gloom" - shows opportunities too

**UAT 4: Clarity Maintained**
- ✅ ~15 major events across 100 years (not overwhelming)
- ✅ Clear chapter structure around L1 periods
- ✅ Current age position clearly marked

---

## Open Questions

- [ ] Should climax periods receive more weight than +5pts? (Currently midpoint of L1 gets +5pts)
- [ ] Should we detect "void" periods (no significant scoring) and mention them as "quieter times"?
- [ ] How to handle multiple Saturn Returns (ages 29, 58, 87)? Same contextual assessment each time?
- [ ] Should Jupiter Returns also get contextual assessment (though less intense than Saturn)?

---

## Decision Log

| Decision | Rationale | Alternatives Considered | Date |
|----------|-----------|------------------------|------|
| Contextual Saturn Return scoring | Captures multi-year aftermath based on natal condition, addressing core user pain point | Fixed 15pts for all returns, ignoring aftermath | 2025-10-12 |
| Keep L2 data, score selectively | Allows peak period and loosing detection while reducing noise | Remove L2 entirely (V2 approach - too aggressive) | 2025-10-12 |
| +10pts for Loosing of Bond | Traditional significance warrants high bonus regardless of convergence | Lower bonus (5pts), or no bonus | 2025-10-12 |
| +10pts for Peak Periods | Balances difficult period emphasis with traditional fortunate periods | Different bonus values, or omit entirely | 2025-10-12 |
| Thresholds unchanged (25/15/8) | Raising would require all profiles to be re-scored; better to increase event scores | Lower thresholds to 20/12/6 | 2025-10-12 |
| Saturn aftermath 3-5 years if difficult | Matches user experience (ages 29-35 = 6 years including return) | Fixed 3 years for all, or no aftermath at all | 2025-10-12 |
| mode='v3' parameter for backward compat | V1/V2 agents continue working during transition | Break existing function signature | 2025-10-12 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0-draft | 2025-10-12 | Initial V3 specification created from collaborative design session |

---

## Appendices

### Appendix A: Test Case - Darren's Chart Ages 29-39

**Natal Saturn Assessment**:
- Position: Capricorn 5° (domicile)
- House: 6H (health/service - traditionally difficult)
- Sect: Night chart → Saturn is malefic contrary to sect (PRIMARY challenge)
- Aspects: Conjunct Sun 0.88° orb (very tight)
- Assessment: difficulty_level='difficult', aftermath_years=3-5, aftermath_bonus=8

**Expected V3 Scores**:

| Age | V2 Score | V3 Score | V3 Bonuses | Tier |
|-----|----------|----------|------------|------|
| 29 | 15 | 28 | Saturn Return (15) + 6H profection (3) + malefic ruled (2) + convergence (8) | MAJOR |
| 30 | 5 | 13 | Aftermath year 1 (8) + profection (5) | NOTABLE |
| 31 | 8 | 16 | Aftermath year 2 (8) + profection (8) | SIGNIFICANT |
| 32 | 13 | 21 | Aftermath year 3 (8) + profection (13) | SIGNIFICANT |
| 33 | 8 | 16 | Aftermath year 4 (8) + profection (8) | SIGNIFICANT |
| 34 | 5 | 13 | Aftermath year 5 (8) + profection (5) | NOTABLE |
| 35 | 8 | 18 | 12H profection (3) + Loosing starts (10) + other (5) | SIGNIFICANT |
| 37 | 5 | 15 | Loosing of Bond (10) + profection (5) | SIGNIFICANT |
| 38 | 8 | 18 | Loosing of Bond (10) + profection (8) | SIGNIFICANT |
| 39 | 33 | 43+ | L1 transition (15) + Loosing ends (10) + Peak begins (10) + profection (8) | MAJOR |

**Narrative Impact**:
- Ages 29-35: "Saturn Return and Rebuilding (Ages 29-35)" becomes dedicated narrative section
- Ages 37-39: "Preparation for Major Shift (Ages 37-39)" - Loosing of Bond coverage
- Age 39: "Profound Relief - The Aquarius Chapter Begins" - major transition with peak period

### Appendix B: Implementation Checklist

**Pre-Implementation**:
- [ ] Review specification with user for final approval
- [ ] Create feature branch: `feature/life-arc-v3-significance`
- [ ] Set up test fixtures (Darren profile data)

**Phase 1 Implementation**:
- [ ] Implement assess_saturn_return_difficulty()
- [ ] Write unit tests for Saturn assessment
- [ ] Implement detect_traditional_periods()
- [ ] Write unit tests for period detection
- [ ] Modify calculate_convergence_score() with v3 logic
- [ ] Write unit tests for v3 scoring
- [ ] Test with Darren ages 29-39
- [ ] Validate all Phase 1 criteria pass

**Phase 2 Implementation**:
- [ ] Implement profection overlays
- [ ] Implement climax/opening detection
- [ ] Test good period scoring
- [ ] Validate all Phase 2 criteria pass

**Phase 3 Implementation**:
- [ ] Create life-arc-interpreter-v3.md agent
- [ ] Generate test report for Darren
- [ ] Compare V2 vs V3 outputs
- [ ] Create comparison document
- [ ] Update version tracker
- [ ] Validate all Phase 3 criteria pass

**Post-Implementation**:
- [ ] Code review
- [ ] User acceptance testing
- [ ] Documentation updates (if other instance complete)
- [ ] Merge feature branch
- [ ] Deploy to production

---

**End of Specification**

This document captures the complete design for Life Arc V3 Significance System. Implementation can proceed from this specification using the feature-designer-astrology agent workflow.
