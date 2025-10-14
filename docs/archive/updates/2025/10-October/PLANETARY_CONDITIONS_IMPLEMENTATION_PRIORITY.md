# Planetary Conditions - Implementation Priority Matrix

**Purpose**: Prioritized roadmap for implementing missing planetary conditions in seed data generator

**Last Updated**: 2025-10-12
**Status**: Planning document for enhancement

---

## Current Implementation Status

### ✅ Already Calculated (8 conditions)

| Condition | Orb/Criteria | Location in Seed Data |
|-----------|-------------|----------------------|
| Retrograde/Direct | Speed negative | `planets[planet]['retrograde']` |
| Combustion | ±8.5° from Sun | Special conditions section |
| Cazimi | ±17' from Sun | Special conditions section |
| Under the Beams | ±15° from Sun | Special conditions section |
| Applying/Separating | Aspect dynamics | `aspects[n]['applying']` |
| Angularity | House 1/4/7/10 | House classification |
| Mutual Reception | By domicile | `receptions` section |
| Bonification | 3 types | `bonification` section |

### ❌ Not Yet Calculated (11 high-priority conditions)

| Condition | Traditional Importance | Calculation Complexity |
|-----------|----------------------|----------------------|
| Hayz | HIGH - Peak planetary strength | MODERATE |
| Oriental/Occidental | HIGH - Visibility phase | MODERATE |
| Stationary | MEDIUM - Intensified energy | LOW |
| Swift/Slow Motion | MEDIUM - Accidental dignity | LOW |
| Overcoming/Overcome | MEDIUM - Aspect power | LOW |
| Enclosure | MEDIUM - Protection/affliction | MODERATE |
| Besiegement | HIGH - Severe affliction | MODERATE |
| Void of Course Moon | MEDIUM - Lunar timing | MODERATE |
| Peregrine (explicit) | LOW - Wandering planet | LOW |
| Feral (explicit) | LOW - Unbound energy | LOW |
| Heliacal Phases | HIGH - Cycle phases | VERY HIGH |

---

## Implementation Roadmap

### Phase 1: Simple Additions (1-2 hours)
**Priority**: HIGH - Easy wins with significant value

#### 1.1. Stationary Detection
**Complexity**: LOW
**Traditional Importance**: MEDIUM
**Implementation**:
```python
def is_stationary(speed: float, planet: str) -> bool:
    """Check if planet is stationary (near zero motion)."""
    thresholds = {
        'Mercury': 0.02, 'Venus': 0.02, 'Mars': 0.01,
        'Jupiter': 0.005, 'Saturn': 0.003
    }
    threshold = thresholds.get(planet, 0.01)
    return abs(speed) < threshold

# Add to planetary data
if is_stationary(planet_speed, planet_name):
    planet_data['stationary'] = True
    if planet_speed > 0:
        planet_data['stationary_type'] = 'direct_station'
    else:
        planet_data['stationary_type'] = 'retrograde_station'
```

#### 1.2. Swift/Slow Motion
**Complexity**: LOW
**Traditional Importance**: MEDIUM
**Implementation**:
```python
MEAN_SPEEDS = {
    'Moon': 13.176, 'Sun': 0.9856, 'Mercury': 1.0,
    'Venus': 1.0, 'Mars': 0.524, 'Jupiter': 0.083,
    'Saturn': 0.033, 'Uranus': 0.012, 'Neptune': 0.006,
    'Pluto': 0.004
}

def assess_speed(planet: str, speed: float) -> str:
    """Determine if planet is swift, slow, or average."""
    mean = MEAN_SPEEDS[planet]
    if speed > mean * 1.2:  # 20% faster than mean
        return 'swift'
    elif speed < mean * 0.8:  # 20% slower than mean
        return 'slow'
    else:
        return 'average'

# Add to planetary data
planet_data['speed_assessment'] = assess_speed(planet_name, abs(planet_speed))
```

#### 1.3. Overcoming/Overcome Aspects
**Complexity**: LOW
**Traditional Importance**: MEDIUM
**Implementation**:
```python
def determine_aspect_direction(planet1_long: float, planet2_long: float,
                               aspect_type: str) -> str:
    """
    Determine if aspect is overcoming (dexter) or overcome (sinister).
    Overcoming = planet1 is EARLIER in zodiac than planet2.
    """
    # Normalize to 0-360
    diff = (planet2_long - planet1_long) % 360

    if aspect_type in ['square', 'opposition', 'trine', 'sextile']:
        if diff < 180:
            return 'overcoming'  # planet1 aspects planet2 from earlier position
        else:
            return 'overcome'    # planet1 aspects planet2 from later position
    return 'neutral'  # Conjunctions don't have direction

# Add to aspect data
aspect_data['direction'] = determine_aspect_direction(
    planet1_longitude, planet2_longitude, aspect_type
)
```

#### 1.4. Peregrine Flag (Explicit)
**Complexity**: LOW
**Traditional Importance**: LOW
**Implementation**:
```python
def is_peregrine(planet_dignities: Dict) -> bool:
    """Check if planet has NO essential dignities."""
    return all([
        not planet_dignities.get('domicile'),
        not planet_dignities.get('exaltation'),
        not planet_dignities.get('triplicity'),
        not planet_dignities.get('term'),
        not planet_dignities.get('face')
    ])

# Add to planetary data
planet_data['peregrine'] = is_peregrine(planet_data['dignities'])
```

#### 1.5. Feral Flag (Explicit)
**Complexity**: LOW
**Traditional Importance**: LOW
**Implementation**:
```python
def is_feral(planet: str, all_aspects: List[Dict]) -> bool:
    """Check if planet has no major applying aspects."""
    planet_aspects = [a for a in all_aspects
                     if planet in [a['planet1'], a['planet2']]
                     and a['applying']]
    return len(planet_aspects) == 0

# Add to planetary data
planet_data['feral'] = is_feral(planet_name, all_aspects)
```

**Phase 1 Total**: ~2 hours implementation + testing

---

### Phase 2: Moderate Complexity (3-5 hours)
**Priority**: HIGH - Important traditional conditions

#### 2.1. Hayz (Rejoicing in Sect)
**Complexity**: MODERATE
**Traditional Importance**: HIGH
**Implementation**:
```python
def check_hayz(planet: str, chart_sect: str, planet_sign: str,
               planet_house: int) -> bool:
    """
    Check if planet is in hayz (rejoicing in sect).

    Requirements:
    1. Planet in correct sect (diurnal in day chart OR nocturnal in night)
    2. Planet in correct gender sign (masculine planet in masculine sign)
    3. Planet in correct hemisphere (diurnal above horizon OR nocturnal below)
    """
    # Define planet sects
    diurnal_planets = ['Sun', 'Jupiter', 'Saturn']
    nocturnal_planets = ['Moon', 'Venus', 'Mars']
    # Mercury is neutral - takes sect of planet it aspects (defer for now)

    # Define sign genders (masculine = fire/air, feminine = earth/water)
    masculine_signs = ['Aries', 'Gemini', 'Leo', 'Libra', 'Sagittarius', 'Aquarius']
    feminine_signs = ['Taurus', 'Cancer', 'Virgo', 'Scorpio', 'Capricorn', 'Pisces']

    # Check condition 1: Planet in correct sect
    if chart_sect == 'day' and planet not in diurnal_planets:
        return False
    if chart_sect == 'night' and planet not in nocturnal_planets:
        return False

    # Check condition 2: Planet in correct gender sign
    if planet in diurnal_planets and planet_sign not in masculine_signs:
        return False
    if planet in nocturnal_planets and planet_sign not in feminine_signs:
        return False

    # Check condition 3: Planet in correct hemisphere
    # Above horizon = houses 7-12, Below horizon = houses 1-6
    if chart_sect == 'day':
        if planet_house not in [7, 8, 9, 10, 11, 12]:  # Diurnal should be above
            return False
    else:  # night chart
        if planet_house not in [1, 2, 3, 4, 5, 6]:  # Nocturnal should be below
            return False

    return True  # All three conditions met!

# Add to planetary data
planet_data['hayz'] = check_hayz(
    planet_name, chart_data['sect'],
    planet_data['sign'], planet_data['house']
)
```

#### 2.2. Oriental/Occidental
**Complexity**: MODERATE (simplified) to HIGH (full heliacal phase)
**Traditional Importance**: HIGH
**Implementation** (Simplified version):
```python
def determine_orientation(planet: str, planet_long: float,
                         sun_long: float) -> str:
    """
    Determine if planet is oriental or occidental.
    Simplified: Based on zodiacal position relative to Sun.
    """
    # Skip for Sun and Moon
    if planet in ['Sun', 'Moon']:
        return 'N/A'

    # Check if under beams, combust, or cazimi first
    diff = abs(planet_long - sun_long)
    if diff <= 0.283:
        return 'cazimi'
    elif diff <= 8.5:
        return 'combust'
    elif diff <= 15:
        return 'under_beams'

    # Determine orientation (simplified)
    # Oriental = planet rises before Sun (earlier in zodiac)
    # Occidental = planet rises after Sun (later in zodiac)
    if planet_long < sun_long:
        return 'oriental'
    else:
        return 'occidental'

# Add to planetary data
planet_data['orientation'] = determine_orientation(
    planet_name, planet_longitude, sun_longitude
)
```

**Note**: Full heliacal phase calculation requires arcus visionis and is deferred to Phase 4.

#### 2.3. Enclosure Detection
**Complexity**: MODERATE
**Traditional Importance**: MEDIUM
**Implementation**:
```python
def check_enclosure(planet_long: float, all_planets: Dict,
                   orb: float = 30.0) -> Dict:
    """
    Check if planet is enclosed (surrounded) by other planets.

    Returns dict with enclosure info:
    - enclosed: bool
    - before_planet: str (planet earlier in zodiac)
    - after_planet: str (planet later in zodiac)
    - type: 'benefic' | 'malefic' | 'mixed' | 'neutral'
    """
    benefics = ['Venus', 'Jupiter']
    malefics = ['Mars', 'Saturn']

    # Find nearest planet before and after
    before_planet = None
    before_distance = 360  # Maximum
    after_planet = None
    after_distance = 360

    for p_name, p_data in all_planets.items():
        p_long = p_data['longitude']

        # Check if before (earlier in zodiac, within orb)
        diff_before = (planet_long - p_long) % 360
        if 0 < diff_before < orb and diff_before < before_distance:
            before_planet = p_name
            before_distance = diff_before

        # Check if after (later in zodiac, within orb)
        diff_after = (p_long - planet_long) % 360
        if 0 < diff_after < orb and diff_after < after_distance:
            after_planet = p_name
            after_distance = diff_after

    # Determine enclosure
    if before_planet and after_planet:
        # Determine type
        enclosed_type = 'neutral'
        if before_planet in benefics and after_planet in benefics:
            enclosed_type = 'benefic'
        elif before_planet in malefics and after_planet in malefics:
            enclosed_type = 'malefic'  # Besiegement
        elif (before_planet in benefics and after_planet in malefics) or \
             (before_planet in malefics and after_planet in benefics):
            enclosed_type = 'mixed'

        return {
            'enclosed': True,
            'before_planet': before_planet,
            'after_planet': after_planet,
            'type': enclosed_type
        }

    return {'enclosed': False}

# Add to planetary data
planet_data['enclosure'] = check_enclosure(
    planet_longitude, all_planet_data
)
```

#### 2.4. Besiegement Detection
**Complexity**: MODERATE (derived from enclosure)
**Traditional Importance**: HIGH
**Implementation**:
```python
def check_besiegement(enclosure_data: Dict) -> bool:
    """
    Check if planet is besieged (enclosed by BOTH malefics).
    """
    if not enclosure_data.get('enclosed'):
        return False

    return enclosure_data.get('type') == 'malefic'

# Add to planetary data
planet_data['besieged'] = check_besiegement(planet_data['enclosure'])
```

#### 2.5. Void of Course Moon
**Complexity**: MODERATE
**Traditional Importance**: MEDIUM (for timing techniques)
**Implementation**:
```python
def check_void_of_course(moon_data: Dict, all_planets: Dict) -> Dict:
    """
    Check if Moon is void of course (no major aspects before sign change).

    Returns:
    - void: bool
    - next_aspect: str (if not void)
    - degrees_to_sign_change: float
    """
    import swisseph as swe

    moon_long = moon_data['longitude']
    moon_speed = moon_data['speed']  # degrees per day

    # Calculate degrees to next sign
    current_sign_number = int(moon_long / 30)
    next_sign_start = (current_sign_number + 1) * 30
    degrees_to_sign_change = next_sign_start - moon_long

    # Calculate time to sign change in days
    time_to_sign_change = degrees_to_sign_change / moon_speed

    # Project Moon's position and check for aspects
    major_aspects = [0, 60, 90, 120, 180]  # Conjunction, sextile, square, trine, opposition
    aspect_orb = 8.0

    next_aspect = None

    for planet_name, planet_data in all_planets.items():
        if planet_name == 'Moon':
            continue

        planet_long = planet_data['longitude']

        # Check each major aspect
        for aspect_angle in major_aspects:
            # Calculate where Moon would be when aspect is exact
            aspect_target = (planet_long + aspect_angle) % 360

            # Check if Moon will reach this aspect before sign change
            diff = (aspect_target - moon_long) % 360

            if diff < degrees_to_sign_change and diff < aspect_orb:
                next_aspect = {
                    'planet': planet_name,
                    'aspect': aspect_angle,
                    'degrees_away': diff
                }
                break

        if next_aspect:
            break

    return {
        'void': next_aspect is None,
        'next_aspect': next_aspect,
        'degrees_to_sign_change': degrees_to_sign_change
    }

# Add to lunar data (only for Moon)
if planet_name == 'Moon':
    planet_data['void_of_course'] = check_void_of_course(
        planet_data, all_planet_data
    )
```

**Phase 2 Total**: ~5 hours implementation + testing

---

### Phase 3: Advanced Calculations (Optional/Future)
**Priority**: MEDIUM - Valuable but complex

#### 3.1. Heliacal Rising/Setting (Full Phase Cycle)
**Complexity**: VERY HIGH
**Traditional Importance**: HIGH
**Requirements**:
- Arcus visionis calculations
- Altitude/azimuth conversions
- Planet-specific visibility thresholds
- Geographic latitude considerations
**Status**: Defer to specialized timing techniques module

#### 3.2. Eclipse Proximity
**Complexity**: HIGH
**Traditional Importance**: HIGH
**Requirements**:
- Eclipse date calculations
- Saros cycle tracking
- Degree proximity assessment
**Status**: Defer to eclipse module or timing techniques

#### 3.3. Antiscia/Contra-antiscia
**Complexity**: MODERATE
**Traditional Importance**: LOW-MEDIUM
**Requirements**:
- Mirror degree calculations
- Aspect-like behavior assessment
**Status**: Lower priority

---

## Implementation Schedule

### Week 1: Phase 1 (Simple Additions)
**Duration**: 1-2 days
**Tasks**:
- [ ] Implement stationary detection
- [ ] Implement swift/slow motion assessment
- [ ] Implement overcoming/overcome aspect direction
- [ ] Implement peregrine flag
- [ ] Implement feral flag
- [ ] Update seed data schema
- [ ] Test with existing profiles

### Week 2: Phase 2 (Moderate Complexity)
**Duration**: 3-5 days
**Tasks**:
- [ ] Implement hayz calculation
- [ ] Implement oriental/occidental (simplified)
- [ ] Implement enclosure detection
- [ ] Implement besiegement detection
- [ ] Implement void of course Moon
- [ ] Update seed data schema
- [ ] Test with existing profiles

### Week 3: Integration & Testing
**Duration**: 2-3 days
**Tasks**:
- [ ] Update seed_data_generator.py
- [ ] Update natal-interpreter agent to use new conditions
- [ ] Update SEED_DATA_SPECIFICATION.md
- [ ] Create test cases for all new conditions
- [ ] Generate updated seed data for all profiles
- [ ] Verify interpretation quality improvements

### Future: Phase 3 (Advanced)
**Duration**: TBD
**Tasks**:
- [ ] Research heliacal phase calculation methods
- [ ] Implement eclipse proximity module
- [ ] Consider antiscia if prioritized by user

---

## Testing Strategy

### Unit Tests
Create test cases for each new condition with known examples:

```python
# Test stationary
assert is_stationary(0.005, 'Jupiter') == True
assert is_stationary(0.05, 'Jupiter') == False

# Test hayz
assert check_hayz('Jupiter', 'day', 'Sagittarius', 10) == True
assert check_hayz('Mars', 'day', 'Aries', 1) == False

# Test enclosure
# (Mars at 15° Aries, enclosed by Venus at 10° Pisces and Saturn at 20° Taurus)
assert check_enclosure(15.0, {
    'Venus': {'longitude': 340.0},
    'Saturn': {'longitude': 50.0}
})['enclosed'] == True
```

### Integration Tests
Test with real birth charts:
- Darren's chart
- Historical charts with known conditions
- Edge cases (planets near sign boundaries, exact stations, etc.)

### Interpretation Impact Tests
Verify that new conditions enhance interpretation quality:
- Generate before/after reports
- Check that hayz planets are highlighted as especially strong
- Verify besiegement warnings appear for afflicted planets
- Confirm void of course Moon timing implications

---

## Success Metrics

### Coverage
- ✅ 100% of essential traditional conditions calculated
- ✅ 90%+ of important traditional conditions calculated
- ✅ 50%+ of supplementary conditions calculated

### Quality
- All conditions match traditional definitions from sources
- No false positives/negatives in test cases
- Interpretations accurately reflect condition meanings

### Performance
- Seed data generation time increases < 20%
- All calculations complete in < 2 seconds per chart

### User Value
- natal-interpreter agent produces richer, more nuanced readings
- Special conditions (hayz, besiegement) are highlighted appropriately
- Users report increased accuracy and depth in interpretations

---

## Related Documentation

- [PLANETARY_CONDITIONS_REFERENCE.md](./PLANETARY_CONDITIONS_REFERENCE.md) - Complete condition definitions
- [SEED_DATA_SPECIFICATION.md](./SEED_DATA_SPECIFICATION.md) - Current seed data schema
- [ASTROLOGY_REFERENCE.md](./ASTROLOGY_REFERENCE.md) - Core traditional systems
- [/scripts/seed_data_generator.py](../scripts/seed_data_generator.py) - Implementation target

---

**Last Updated**: 2025-10-12
**Status**: Ready for implementation approval
**Estimated Total Time**: 2-3 weeks for Phases 1-2 + integration
