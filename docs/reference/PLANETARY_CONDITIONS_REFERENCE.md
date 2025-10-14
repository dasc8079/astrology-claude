# Planetary Conditions Reference - Traditional Hellenistic Astrology

**Purpose**: Comprehensive reference for all planetary conditions and special states that should be calculated in natal chart seed data.

**Last Updated**: 2025-10-12
**Version**: 1.0

---

## Table of Contents

1. [Solar Conditions](#solar-conditions)
2. [Visibility & Orientation Conditions](#visibility--orientation-conditions)
3. [Motion & Speed Conditions](#motion--speed-conditions)
4. [Aspect-Based Conditions](#aspect-based-conditions)
5. [Sect-Based Conditions](#sect-based-conditions)
6. [Reception Conditions](#reception-conditions)
7. [Lunar Conditions](#lunar-conditions)
8. [Angularity Conditions](#angularity-conditions)
9. [Dignity-Based Conditions](#dignity-based-conditions)
10. [Calculation Priority & Dependencies](#calculation-priority--dependencies)

---

## I. Solar Conditions

### 1. Combustion
**Definition**: Planet within 8.5° of the Sun
**Traditional Orb**: ±8.5° (some sources use 8° or 8°30')
**Effect**: Planet weakened, "burned up" by solar heat
**Interpretive Significance**:
- Significations obscured or dominated by ego/will
- Planet's independent expression compromised
- Traditional malefic condition
**Sources**: Brennan (Hellenistic Astrology), Hand (Planets in Transit)
**Calculation**: `abs(planet_longitude - sun_longitude) <= 8.5`

### 2. Cazimi
**Definition**: Planet within 17 minutes (0.283°) of the Sun
**Traditional Orb**: ±17' (0.283° or 0.28333°)
**Effect**: Planet empowered, "in the heart of the Sun"
**Interpretive Significance**:
- Blessed by solar radiance
- Rare and highly beneficial
- Overrides combustion weakness
- Planet gains royal favor, empowerment
**Sources**: Brennan, Medieval sources (Bonatti, Al-Biruni)
**Calculation**: `abs(planet_longitude - sun_longitude) <= 0.283`
**Priority**: Check BEFORE combustion (overrides it)

### 3. Under the Beams
**Definition**: Planet within 15° of the Sun
**Traditional Orb**: ±15°
**Effect**: Planet obscured, difficult to express
**Interpretive Significance**:
- Less severe than combustion
- Significations hidden or overshadowed
- Not as debilitating as full combustion
**Sources**: Brennan, traditional Hellenistic sources
**Calculation**: `abs(planet_longitude - sun_longitude) <= 15.0`
**Note**: Overlaps with combustion (combustion is subset of under beams)

---

## II. Visibility & Orientation Conditions

### 4. Oriental (Rising Before Sun)
**Definition**: Planet rises before the Sun (appears in eastern sky before dawn)
**Traditional Name**: "Morning star" for Venus/Mercury
**Determination**:
- For superior planets (Mars, Jupiter, Saturn): Located BEFORE the Sun in zodiacal order
- For inferior planets (Mercury, Venus): Between Sun and western horizon after conjunction
**Interpretive Significance**:
- Independent, assertive expression
- Planet acts with initiative
- Traditional: more masculine, active quality
**Sources**: Brennan, Brady (Predictive Astrology)
**Calculation**: `planet_longitude < sun_longitude` (simplified)
**Note**: Full calculation requires heliacal phase analysis

### 5. Occidental (Rising After Sun)
**Definition**: Planet rises after the Sun (appears in western sky after sunset)
**Traditional Name**: "Evening star" for Venus/Mercury
**Determination**:
- For superior planets: Located AFTER the Sun in zodiacal order
- For inferior planets: Between Sun and eastern horizon before conjunction
**Interpretive Significance**:
- Responsive, reactive expression
- Planet acts in support role
- Traditional: more feminine, receptive quality
**Sources**: Brennan, Brady
**Calculation**: `planet_longitude > sun_longitude` (simplified)
**Note**: Full calculation requires heliacal phase analysis

### 6. Heliacal Rising/Setting
**Definition**: Planet's first/last visibility near the Sun
**Types**:
- **Heliacal Rising**: First visible appearance after conjunction with Sun
- **Heliacal Setting**: Last visible appearance before conjunction with Sun
**Traditional Orbs**:
- Varies by planet (Mercury ~15°, Venus ~15°, Mars ~17°, Jupiter ~14°, Saturn ~15°)
- Ancient sources provide planet-specific values
**Interpretive Significance**:
- Critical phase transitions in planetary cycle
- Heliacal rising marks "rebirth" of planet
- Heliacal setting marks "death" or completion
**Sources**: Brennan (detailed tables), ancient Babylonian/Hellenistic sources
**Calculation**: Complex - requires arcus visionis calculations
**Status**: ADVANCED - May defer to future enhancement

---

## III. Motion & Speed Conditions

### 7. Retrograde Motion
**Definition**: Planet appears to move backward through the zodiac
**Determination**: Daily motion is negative (moving to earlier degrees)
**Interpretive Significance**:
- Internalized expression
- Review, revision, reworking themes
- NOT necessarily negative in traditional astrology
- Can indicate depth, introspection
**Sources**: All traditional sources
**Calculation**: Swiss Ephemeris provides retrograde flag
**Data Source**: `pyswisseph` returns speed value (negative = retrograde)

### 8. Stationary (Station)
**Definition**: Planet appears motionless at turning point
**Types**:
- **Stationary Retrograde**: Turning from direct to retrograde
- **Stationary Direct**: Turning from retrograde to direct
**Traditional Orb**: When daily motion < 0.01° per day (approximate)
**Interpretive Significance**:
- Intensified energy at that degree
- Planet "dwells" at the station point
- Especially powerful for outer planets
**Sources**: Hand, Brady
**Calculation**: Daily speed near zero (< 0.01° or planet-specific threshold)

### 9. Swift in Motion
**Definition**: Planet moving faster than its mean daily motion
**Traditional Assessment**: Considered strengthening condition
**Average Daily Motions** (approximate):
- Moon: 13.2° (swift > 13.2°)
- Sun: 1.0° (fixed)
- Mercury: 1.0° (swift > 1.0°)
- Venus: 1.0° (swift > 1.0°)
- Mars: 0.52° (swift > 0.52°)
- Jupiter: 0.08° (swift > 0.08°)
- Saturn: 0.03° (swift > 0.03°)
**Sources**: Traditional tables, Brennan
**Calculation**: Compare planet's speed to its mean motion

### 10. Slow in Motion
**Definition**: Planet moving slower than its mean daily motion
**Traditional Assessment**: Minor debility (but not as severe as retrograde)
**Interpretive Significance**:
- Delayed manifestation
- Less decisive action
- Requires patience
**Sources**: Medieval sources, Brennan
**Calculation**: Compare planet's speed to its mean motion

---

## IV. Aspect-Based Conditions

### 11. Applying vs. Separating Aspects
**Definition**: Whether aspect is forming or dissolving
**Types**:
- **Applying**: Planets moving toward exactness - STRONGER
- **Separating**: Planets moving past exactness - WEAKER
**Determination**: Compare current orb to orb 24 hours ago
**Traditional Importance**: Applying aspects are active/future; separating are passive/past
**Sources**: All traditional sources
**Calculation**: Track planetary speeds and relative motion
**Status**: Currently calculated in seed data

### 12. Overcoming (Dexter vs. Sinister Aspect)
**Definition**: Aspect direction based on zodiacal order
**Types**:
- **Overcoming/Dexter**: Planet to the right (earlier in zodiac) aspects one to the left
- **Overcome/Sinister**: Planet to the left (later in zodiac) aspects one to the right
**Traditional Significance**:
- Overcoming planet has more power in the relationship
- Especially important for square and opposition
**Example**: Mars at 15° Aries squares Moon at 15° Cancer - Mars overcomes Moon
**Sources**: Brennan (detailed explanation), Hellenistic texts
**Calculation**: Determine which planet is earlier in zodiacal order
**Status**: IMPORTANT - Not yet calculated

### 13. Enclosure
**Definition**: Planet is surrounded by two other planets on both sides
**Traditional Name**: "Besieged" when enclosed by malefics
**Types**:
- **Simple Enclosure**: Any two planets on both sides
- **Benefic Enclosure**: Enclosed by Jupiter and Venus (strengthening)
- **Malefic Enclosure/Besiegement**: Enclosed by Mars and Saturn (weakening)
**Traditional Orbs**: Within ~30° on each side (varies by source)
**Interpretive Significance**:
- Benefic enclosure: Protected, supported
- Malefic enclosure: Trapped, afflicted
**Sources**: Brennan, medieval sources (Bonatti)
**Calculation**: Check if planet has one planet before and one after within orb
**Status**: IMPORTANT - Not yet calculated

### 14. Besiegement
**Definition**: Specific type of enclosure by BOTH malefics (Mars and Saturn)
**Traditional Assessment**: Severe affliction
**Interpretive Significance**:
- Planet trapped between challenging forces
- Significations blocked or frustrated
- Classic malefic testimony
**Sources**: Brennan, medieval sources
**Calculation**: Check if Mars is on one side and Saturn on the other (within ~30°)
**Status**: IMPORTANT - Not yet calculated

### 15. Bonification
**Definition**: Benefic (Venus or Jupiter) supporting a malefic (Mars or Saturn)
**Types**:
1. **Aspect Bonification**: Benefic trines or sextiles malefic
2. **Reception Bonification**: Malefic in benefic's sign (reception)
3. **Angular Bonification**: Benefic on angle supporting malefic
**Sect Consideration**: Bonification stronger when benefic is OF SECT
**Interpretive Significance**: Softens malefic difficulties, provides mitigation
**Sources**: Brennan, George
**Status**: Currently calculated in seed data

---

## V. Sect-Based Conditions

### 16. Hayz (Rejoicing in Sect)
**Definition**: Planet in ideal sect condition - optimally placed
**Requirements** (ALL must be met):
1. Planet in correct sect (diurnal planet in day chart OR nocturnal planet in night chart)
2. Planet in correct gender sign (masculine planet in masculine sign OR feminine in feminine)
3. Planet in correct house sect (diurnal above horizon OR nocturnal below horizon)

**Diurnal Planets**: Sun, Jupiter, Saturn
**Nocturnal Planets**: Moon, Venus, Mars
**Neutral**: Mercury (takes sect of planet it aspects)

**Masculine Signs**: Fire and Air (Aries, Gemini, Leo, Libra, Sagittarius, Aquarius)
**Feminine Signs**: Earth and Water (Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces)

**Interpretive Significance**:
- Maximum planetary strength and joy
- Planet operates at peak efficiency
- All conditions optimal
**Sources**: Brennan (extensive discussion), Hellenistic texts
**Calculation**: Check all three conditions
**Status**: IMPORTANT - Not yet calculated

### 17. Contrary to Sect
**Definition**: Planet operating in opposite type of chart from its nature
**Examples**:
- Jupiter in night chart (less beneficial)
- Venus in day chart (less beneficial)
- Saturn in night chart (harsher malefic)
- Mars in day chart (harsher malefic)
**Interpretive Significance**:
- Benefics less benefic
- Malefics more malefic
**Sources**: Brennan, traditional Hellenistic doctrine
**Calculation**: Compare planet's sect preference to chart sect
**Status**: Partially assessed in dignity scoring

---

## VI. Reception Conditions

### 18. Mutual Reception (By Domicile)
**Definition**: Two planets each in the sign ruled by the other
**Example**: Mars in Libra + Venus in Aries
**Interpretive Significance**:
- Mutual support and exchange of power
- Can mitigate difficult placements
- Traditional form of "translation"
**Sources**: Brennan, George, medieval sources
**Status**: Currently calculated in seed data

### 19. Mixed Reception (By Other Dignities)
**Definition**: Reception by exaltation, triplicity, term, or face
**Types**:
- Reception by exaltation (less strong than domicile)
- Reception by triplicity (minor)
- Reception by term/bound (minor)
- Reception by face/decan (minor)
**Interpretive Significance**: Weaker than mutual reception by domicile
**Sources**: Medieval sources, Brennan
**Status**: ADVANCED - May defer

### 20. No Reception (Aversion)
**Definition**: Two planets in signs that have no aspect relationship
**Traditional Name**: "Aversion" - signs at inconjunct angles (30°, 150°)
**Interpretive Significance**:
- Planets "cannot see" each other
- No natural connection
- Difficulty integrating significations
**Sources**: Brennan (detailed), Hellenistic texts
**Status**: Can be derived from aspect calculations

---

## VII. Lunar Conditions

### 21. Void of Course Moon
**Definition**: Moon makes no major aspects before leaving its current sign
**Traditional Aspects**: Conjunction, sextile, square, trine, opposition
**Orbs**: Apply standard aspect orbs
**Interpretive Significance**:
- "Nothing will come of the matter" (horary)
- In natal: Period of lunar independence
- Less critical in natal than in horary
**Sources**: Traditional horary sources, Hand
**Calculation**:
1. Find Moon's current sign
2. Calculate degrees remaining until next sign
3. Check if any major aspects form before Moon enters next sign
**Status**: Useful for timing - Not yet calculated

### 22. Moon's Nodes
**Definition**: North Node (ascending) and South Node (descending)
**Interpretive Significance**:
- North Node: Evolutionary direction, soul's growth path
- South Node: Past patterns, comfort zone, release point
**Sources**: All modern and some traditional sources
**Status**: Currently calculated in seed data

### 23. Eclipse Proximity
**Definition**: Planet or point near degree of recent/upcoming eclipse
**Traditional Orb**: ±3-5° from eclipse degree
**Interpretive Significance**:
- Activated by eclipse energy
- Major life theme highlighted
- Traditional: powerful timing indicator
**Sources**: Brady (Predictive Astrology), traditional eclipse doctrine
**Calculation**: Compare planet position to eclipse tables
**Status**: ADVANCED - Requires eclipse calculations

---

## VIII. Angularity Conditions

### 24. Angular (On the Angles)
**Definition**: Planet within orb of ASC, MC, DSC, or IC
**Traditional Assessment**: STRONGEST position
**Orbs**:
- Tight conjunction: ±3° (most powerful)
- Wide conjunction: ±8-10° (still strong)
**Interpretive Significance**:
- Direct expression in visible life
- Prominent and powerful manifestation
- Especially powerful for ASC and MC
**Sources**: All traditional sources
**Status**: Currently assessed in seed data (as part of house position)

### 25. Succedent Position
**Definition**: Planet in houses 2, 5, 8, or 11
**Traditional Assessment**: MODERATE strength
**Interpretive Significance**:
- Supportive, stabilizing
- Resources and assets
- More stable than angular, more active than cadent
**Sources**: Traditional house doctrine
**Status**: Currently assessed (part of house classification)

### 26. Cadent Position
**Definition**: Planet in houses 3, 6, 9, or 12
**Traditional Assessment**: WEAKEST position
**Interpretive Significance**:
- Preparatory, learning, behind-the-scenes
- Requires more effort to activate
- Not necessarily negative (6th and 12th have spiritual significance)
**Sources**: Traditional house doctrine
**Status**: Currently assessed (part of house classification)

---

## IX. Dignity-Based Conditions

### 27. Peregrine (No Essential Dignity)
**Definition**: Planet with NO essential dignities in its current sign
**Criteria**: NOT in:
- Domicile
- Exaltation
- Triplicity
- Term/Bound
- Face/Decan
**Interpretive Significance**:
- Planet "wandering" without support
- Must rely entirely on accidental dignities
- Not as severe as detriment or fall
**Sources**: Medieval sources, Brennan
**Calculation**: Check all five dignity types
**Status**: Can be derived from dignity calculations

### 28. Feral Planet
**Definition**: Planet with no major aspects to other planets
**Traditional Names**: "Unbonded," "Wild"
**Determination**: No applying aspects within traditional orbs
**Interpretive Significance**:
- Operates independently, without restraint
- Can be powerful (unbound energy)
- Can be chaotic (no integration)
**Sources**: Modern usage, some traditional precedent
**Calculation**: Check all major aspects to other planets
**Status**: Can be derived from aspect calculations

### 29. Reception Without Aspect
**Definition**: Planet is IN another planet's sign but makes NO aspect to that ruler
**Interpretive Significance**:
- Disconnected from its host
- "Guest without invitation"
- Weaker expression
**Sources**: Medieval doctrine
**Status**: ADVANCED - Requires aspect + dignity integration

---

## X. Calculation Priority & Dependencies

### Essential (Always Calculate)
These conditions are foundational and should always be calculated:

1. **Retrograde/Direct** - Basic motion state
2. **Combustion** - Within 8.5° of Sun
3. **Cazimi** - Within 17' of Sun (CHECK FIRST, overrides combustion)
4. **Under the Beams** - Within 15° of Sun
5. **Applying/Separating** - Aspect dynamics
6. **Sect Alignment** - Day/night chart compatibility
7. **Angularity** - House strength (angular/succedent/cadent)
8. **Mutual Reception** - Planets in each other's signs

### Important (High Priority)
These significantly affect interpretation:

9. **Hayz** - All three conditions optimal
10. **Oriental/Occidental** - Visibility relative to Sun
11. **Stationary** - Near retrograde/direct station
12. **Overcoming** - Dexter vs. sinister aspects
13. **Enclosure/Besiegement** - Trapped by other planets
14. **Bonification** - Benefic support for malefics
15. **Swift/Slow Motion** - Relative to mean speed

### Supplementary (Medium Priority)
Useful additional context:

16. **Void of Course Moon** - Lunar timing
17. **Peregrine** - No essential dignity
18. **Feral** - No aspects
19. **Mixed Reception** - By other dignities

### Advanced (Optional/Future)
Complex calculations for deep analysis:

20. **Heliacal Rising/Setting** - Requires arcus visionis
21. **Eclipse Proximity** - Requires eclipse tables
22. **Reception Without Aspect** - Complex integration
23. **Antiscia/Contra-antiscia** - Mirror degrees

---

## Calculation Order (Dependencies)

### Stage 1: Basic Data
1. Calculate all planetary positions
2. Calculate houses
3. Determine chart sect (day/night)

### Stage 2: Solar Conditions
4. Calculate Sun distance for all planets
5. Check Cazimi FIRST (overrides combustion)
6. Check Combustion
7. Check Under the Beams
8. Determine Oriental/Occidental

### Stage 3: Motion & Speed
9. Extract retrograde flags
10. Calculate speeds
11. Check for stationary (speed near zero)
12. Compare speeds to mean motions (swift/slow)

### Stage 4: Essential Dignities
13. Calculate all five dignity types
14. Identify peregrine planets (no dignities)

### Stage 5: Aspects
15. Calculate all major aspects
16. Determine applying/separating
17. Determine overcoming/overcome
18. Check for enclosure
19. Check for besiegement (malefic enclosure)
20. Identify feral planets (no aspects)

### Stage 6: Integrated Conditions
21. Check mutual receptions
22. Calculate bonification (benefic supporting malefic)
23. Check Hayz (requires sect + sign gender + house position)
24. Check void of course Moon

---

## Sources Summary

### Primary Traditional Sources
- **Chris Brennan**: Hellenistic Astrology: The Study of Fate and Fortune
- **Demetra George**: Astrology and the Authentic Self
- **Robert Hand**: Planets in Transit
- **Bernadette Brady**: Predictive Astrology: The Eagle and the Lark

### Medieval Sources (Referenced)
- Guido Bonatti
- Al-Biruni
- William Lilly (for horary conditions like VOC)

### Modern Synthesis
- Sophia Mason (Progressions)
- Liz Greene (Psychological integration)

---

## Implementation Notes

### Current Status (from SEED_DATA_SPECIFICATION.md)

**Already Calculated**:
- ✅ Retrograde/direct status
- ✅ Combustion (8.5° orb)
- ✅ Cazimi (17' orb)
- ✅ Under the Beams (15° orb)
- ✅ Applying/separating aspects
- ✅ Angularity (house strength)
- ✅ Mutual reception by domicile
- ✅ Bonification (three types)

**Not Yet Calculated**:
- ❌ Oriental/Occidental
- ❌ Stationary (near station)
- ❌ Swift/Slow motion (relative to mean)
- ❌ Hayz (full three-condition check)
- ❌ Overcoming/Overcome aspects
- ❌ Enclosure/Besiegement
- ❌ Void of course Moon
- ❌ Peregrine (explicit flag)
- ❌ Feral (explicit flag)

### Priority for Enhancement

**Phase 1** (Essential Missing Conditions):
1. Hayz calculation (sect + gender + position)
2. Oriental/Occidental determination
3. Stationary detection
4. Swift/Slow motion assessment
5. Overcoming/Overcome aspect direction

**Phase 2** (Important Missing Conditions):
6. Enclosure detection
7. Besiegement detection
8. Void of course Moon
9. Peregrine flag (explicit)
10. Feral flag (explicit)

**Phase 3** (Advanced):
11. Heliacal phases
12. Eclipse proximity
13. Mixed receptions
14. Antiscia

---

## Related Documentation

- [SEED_DATA_SPECIFICATION.md](./SEED_DATA_SPECIFICATION.md) - Complete seed data schema
- [ASTROLOGY_REFERENCE.md](./ASTROLOGY_REFERENCE.md) - Core astrological systems
- [DATA_FORMATS.md](./DATA_FORMATS.md) - Data structure specifications
- [/scripts/seed_data_generator.py](../scripts/seed_data_generator.py) - Current implementation

---

**Last Updated**: 2025-10-12
**Maintained By**: docs-updater-astrology agent
**Version**: 1.0 - Initial compilation from project documentation and traditional sources
