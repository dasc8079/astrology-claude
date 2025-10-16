# Astrology Reference - Traditional & Hellenistic Systems

This document contains static astrological reference information for the project. All systems and definitions follow traditional/Hellenistic astrology with minimal modern additions.

**Note**: For calculation tools, see `/scripts/astrology_reference.py` and `/scripts/ephemeris_helper.py`

---

## Table of Contents

1. [House System](#house-system)
2. [Rulerships](#rulerships)
3. [Dignities and Debilities](#dignities-and-debilities)
4. [Sect (Day/Night Chart Analysis)](#sect-daynight-chart-analysis)
5. [Aspects](#aspects)
6. [Planetary Set](#planetary-set)
7. [Planetary Conditions](#planetary-conditions)
8. [Lots (Hermetic Parts)](#lots-hermetic-parts)
9. [Antiscia and Contra-Antiscia](#antiscia-and-contra-antiscia)
10. [Fixed Stars](#fixed-stars)
11. [Stelliums](#stelliums)
12. [Hayz](#hayz)
13. [Aspect Dynamics](#aspect-dynamics)
14. [House Meanings](#house-meanings)
15. [Zodiacal Signs](#zodiacal-signs)
16. [Glossary](#glossary)

---

## House System

### Whole-Sign Houses (WSH)
**Primary system used throughout this project**

- Each house spans one complete zodiacal sign (30°)
- Rising sign becomes the entire 1st house
- No complex house cusp calculations required
- Traditional Hellenistic practice

**Example**:
- Ascendant at 15° Leo → Entire sign of Leo = 1st house
- 2nd house = Virgo (all 30° of Virgo)
- 3rd house = Libra (all 30° of Libra)
- etc.

**Supported systems** (via Swiss Ephemeris):
- Whole-Sign ('W') - PRIMARY
- Placidus ('P'), Koch ('K'), Equal ('E'), Campanus ('C'), Regiomontanus ('R'), Porphyry ('O')

---

## Rulerships

**Traditional rulerships only** - No modern rulerships used:

| Planet | Domicile Sign(s) | Day/Night |
|--------|------------------|-----------|
| ☉ Sun | ♌ Leo | Day |
| ☽ Moon | ♋ Cancer | Night |
| ☿ Mercury | ♊ Gemini, ♍ Virgo | Neutral |
| ♀ Venus | ♉ Taurus, ♎ Libra | Night |
| ♂ Mars | ♈ Aries, ♏ Scorpio | Night |
| ♃ Jupiter | ♐ Sagittarius, ♓ Pisces | Day |
| ♄ Saturn | ♑ Capricorn, ♒ Aquarius | Day |

**Modern planets** (Uranus, Neptune, Pluto) are **NOT assigned traditional rulerships** in this system.

---

## Dignities and Debilities

### Essential Dignities

Dignities are zodiacal positions that strengthen a planet's expression.

**1. Domicile (Rulership)** - Strongest dignity
- Planet in its own sign
- Example: Mars in Aries, Venus in Taurus

**2. Exaltation** - Second-strongest dignity
- Planet in sign of exaltation

| Planet | Exaltation Sign | Degree |
|--------|----------------|--------|
| ☉ Sun | ♈ Aries | 19° |
| ☽ Moon | ♉ Taurus | 3° |
| ☿ Mercury | ♍ Virgo | 15° |
| ♀ Venus | ♓ Pisces | 27° |
| ♂ Mars | ♑ Capricorn | 28° |
| ♃ Jupiter | ♋ Cancer | 15° |
| ♄ Saturn | ♎ Libra | 21° |

**3. Triplicity** - Elemental dignity
- Day, night, and participating rulers for each element

| Element | Day Ruler | Night Ruler | Participating |
|---------|-----------|-------------|---------------|
| Fire (♈♌♐) | Sun | Jupiter | Saturn |
| Earth (♉♍♑) | Venus | Moon | Mars |
| Air (♊♎♒) | Saturn | Mercury | Jupiter |
| Water (♋♏♓) | Venus | Mars | Moon |

**4. Bounds/Terms** - Egyptian system
- Signs divided into 5 unequal segments, each ruled by a planet
- See `/scripts/astrology_reference.py` for complete tables

**5. Decans/Faces** - Chaldean order
- Signs divided into three 10° segments
- See `/scripts/astrology_reference.py` for complete tables

### Essential Debilities

**1. Detriment** - Planet opposite its domicile
- Example: Mars in Libra (opposite Aries), Venus in Scorpio (opposite Taurus)

**2. Fall** - Planet opposite its exaltation
- Example: Sun in Libra (opposite Aries), Moon in Scorpio (opposite Taurus)

---

## Sect (Day/Night Chart Analysis)

Sect determines which planets are strengthened or weakened based on whether the chart is diurnal (day) or nocturnal (night).

### Determination
- **Diurnal**: Sun above horizon at birth
- **Nocturnal**: Sun below horizon at birth

### Sect Light
- **Day chart**: Sun is the sect light (primary luminary)
- **Night chart**: Moon is the sect light (primary luminary)

### Benefics by Sect
- **Diurnal charts**: Jupiter is benefic of sect (stronger)
- **Nocturnal charts**: Venus is benefic of sect (stronger)

### Malefics by Sect
- **Diurnal charts**: Saturn is malefic of sect (gentler)
- **Nocturnal charts**: Mars is malefic of sect (gentler)

### Contrary to Sect
Planets operating contrary to sect are either:
- Benefics that are less beneficial (Jupiter in night chart, Venus in day chart)
- Malefics that are harsher (Saturn in night chart, Mars in day chart)

---

## Aspects

**Classical aspects only** - No modern harmonic aspects (quintile, septile, etc.)

| Aspect | Angle | Nature | Traditional Orb | Symbol |
|--------|-------|--------|-----------------|--------|
| Conjunction | 0° | Neutral* | 8-10° | ☌ |
| Sextile | 60° | Harmonious | 6-8° | ⚹ |
| Square | 90° | Challenging | 7-8° | □ |
| Trine | 120° | Harmonious | 7-8° | △ |
| Opposition | 180° | Separating | 8-10° | ☍ |

*Conjunction nature depends on planets involved

### Applying vs. Separating
- **Applying**: Aspect forming (planets moving toward exactness) - Stronger
- **Separating**: Aspect moving past exactness - Weaker

### Orb Variations
- Luminaries (Sun/Moon) may use larger orbs (up to 10°)
- Faster planets typically use tighter orbs
- Aspect to angles (ASC/MC/DSC/IC): Similar orbs apply

---

## Planetary Set

### Traditional Seven (Primary)
- ☉ Sun, ☽ Moon, ☿ Mercury, ♀ Venus, ♂ Mars, ♃ Jupiter, ♄ Saturn
- Used for all traditional dignities, rulerships, and primary interpretation

### Modern Planets (Secondary, Context Only)
- ♅ Uranus, ♆ Neptune, ♇ Pluto
- Supplementary interpretation only
- **Never** primary rulers or dignity holders
- Not integrated into traditional dignity system

### Special Points
- North Node (☊) / South Node (☋) - Lunar nodes
- Chiron (⚷) - Wounded healer archetype (modern, toggleable)
- Lilith (⚸) - Black Moon Lilith mean position (modern, toggleable)

**Chiron Interpretation** (when `include_chiron: true`):
- Represents core wound and healing gifts
- Shows where one experienced early rejection or inadequacy that becomes source of wisdom
- Indicates areas of deep teaching ability born from personal wounding
- By house: WHERE the wound manifests and WHERE healing gifts emerge
- By sign: HOW the wound manifests and the NATURE of healing gifts
- By aspects: Challenging aspects show areas where wound is activated; harmonious aspects show easier access to healing gifts
- Integration: TERTIARY or SECONDARY depending on prominence (angular placement or major aspects = SECONDARY)
- Tone: Frame as wound-to-wisdom transformation, teaching others what you had to learn the hard way

**Example Interpretations**:
- Chiron in 1st house: Identity wound, learning to embody authentic self, teaching others about self-acceptance
- Chiron in 6th house: Health/service wound, becoming healer through own health crisis or service challenges
- Chiron in 10th house: Career/authority wound, teaching others about authentic vocation and leadership
- Chiron-Sun square: Father wound or core identity rejection, teaching others about authentic self-worth
- Chiron-Moon trine: Emotional healing gifts flow naturally, intuitive understanding of others' pain

**Lilith Interpretation** (when `include_lilith: true`):
- Represents shadow feminine, repressed desires, primal instincts
- Shows WHERE one confronts societal taboos and experiences alienation
- Indicates areas where authentic primal self was rejected/suppressed
- By house: WHERE shadow material emerges and WHERE rejection occurred
- By sign: HOW shadow manifests and the NATURE of repressed qualities
- By aspects: Challenging aspects show internal shadow conflicts; harmonious aspects show easier integration
- Integration: TERTIARY or SECONDARY depending on prominence (angular placement or major aspects = SECONDARY)
- Tone: Frame as reclamation of power and authenticity, not pathology

**Example Interpretations**:
- Lilith in 1st house: Shadow self visible to others, identity formed through confronting rejection
- Lilith in 7th house: Projection of shadow onto partners, relationships trigger primal instincts
- Lilith in 10th house: Public role involves taboo subjects or confronting societal norms
- Lilith-Moon square: Emotional needs conflict with primal instincts, maternal rejection themes
- Lilith-Venus trine: Easier integration of shadow feminine with love/beauty expression

---

## Planetary Conditions

### Combustion and Solar Proximity

**Combust**: Within 8.5° of Sun
- Planet weakened, "burned up" by solar heat
- Significations obscured or dominated by ego/will

**Under the Beams**: Within 15° of Sun
- Planet obscured, difficult to express
- Less severe than combustion

**Cazimi**: Within 17 minutes (0.283°) of Sun
- "In the heart of the Sun"
- Planet empowered, blessed by solar radiance
- Rare and highly beneficial

### Motion

**Direct**: Normal forward motion through zodiac

**Retrograde**: Apparent backward motion
- Internalized expression
- Review, revision, reworking themes
- Not necessarily negative

**Stationary**: Turning point (direct→retrograde or retrograde→direct)
- Planet appears motionless
- Intensified energy at that degree

### Angularity (House Position Strength)

**Angular** (Houses 1, 4, 7, 10): Strongest
- Direct expression in visible, active life areas
- Planets here are prominent and powerful

**Succedent** (Houses 2, 5, 8, 11): Moderate
- Supportive, stabilizing positions
- Resources and assets

**Cadent** (Houses 3, 6, 9, 12): Weakest
- Preparatory, learning, behind-the-scenes
- Requires more effort to activate

### Additional Planetary Conditions

**Swift vs Slow Motion**:
- Swift: Planet moving faster than mean daily motion (> 110% of mean speed)
- Slow: Planet moving slower than mean daily motion (< 90% of mean speed but > 0)
- Mean daily motions: Sun 0.99°, Moon 13.18°, Mercury 1.38°, Venus 1.60°, Mars 0.52°, Jupiter 0.08°, Saturn 0.03°

**Oriental vs Occidental**:
- Oriental: Planet rises before Sun (ahead in zodiacal order, eastern position)
- Occidental: Planet rises after Sun (behind in zodiacal order, western position)
- Applies to Mercury, Venus, Mars, Jupiter, Saturn (not Sun or Moon)

**Peregrine**:
- Planet with no essential dignities (no domicile, exaltation, triplicity, term, or face)
- Weakened position, "wandering" without strength

**Feral**:
- Planet making no major aspects to any other planet
- Isolated, acting independently without connection to chart themes

---

## Lots (Hermetic Parts)

Hermetic lots are calculated points using the formula: **ASC + Planet A - Planet B**

Many lots use different formulas for day vs night charts to maintain sect alignment.

### Primary Lots

**Lot of Fortune (⊗)**:
- Day formula: ASC + Moon - Sun
- Night formula: ASC + Sun - Moon
- Signifies: Material resources, body, health, fortune

**Lot of Spirit (⊙)**:
- Day formula: ASC + Sun - Moon
- Night formula: ASC + Moon - Sun
- Signifies: Character, soul, life purpose, vocation

**Lot of Eros (♡)**:
- Day formula: ASC + Venus - Spirit
- Night formula: ASC + Spirit - Venus
- Signifies: Desires, love, passionate attachment

**Lot of Necessity (⚙)**:
- Day formula: ASC + Fortune - Mercury
- Night formula: ASC + Mercury - Fortune
- Signifies: Fate, constraint, compulsion, unavoidable circumstances

### Secondary Lots

**Lot of Courage (⚔)**:
- Day formula: ASC + Fortune - Mars
- Night formula: ASC + Mars - Fortune
- Signifies: Bravery, assertion, martial activity

**Lot of Victory (🏆)**:
- Day formula: ASC + Spirit - Jupiter
- Night formula: ASC + Jupiter - Spirit
- Signifies: Success, expansion, recognition, triumph

**Lot of Saturn (Basis/Nemesis) (⚓)**:
- Day formula: ASC + Fortune - Saturn
- Night formula: ASC + Saturn - Fortune
- **Dual Interpretation** (same formula, context-dependent):
  - When Saturn is dignified (domicile, exaltation, strong triplicity): Interpreted as **"Lot of Basis"** - Foundation, structure, stability, long-term building
  - When Saturn is debilitated (detriment, fall, peregrine, afflicted): Interpreted as **"Lot of Nemesis"** - Retribution, enemies, downfall, consequences, karmic debt

**Lot of Marriage (💍)**:
- Formula: ASC + Venus - Saturn (same for day and night)
- Signifies: Partnership, committed relationships

**Lot of Children (👶)**:
- Day formula: ASC + Jupiter - Saturn
- Night formula: ASC + Saturn - Jupiter
- Signifies: Offspring, generativity, legacy

### Relational & Life Domain Lots

**Lot of Father (👨)**:
- Day formula: ASC + Sun - Saturn
- Night formula: ASC + Saturn - Sun
- Signifies: Paternal relationships, authority figures, inheritance from father

**Lot of Mother (👩)**:
- Day formula: ASC + Moon - Venus
- Night formula: ASC + Venus - Moon
- Signifies: Maternal relationships, nurturing, emotional foundation

**Lot of Siblings (👥)**:
- Day formula: ASC + Jupiter - Saturn
- Night formula: ASC + Saturn - Jupiter
- Signifies: Peer relationships, siblings, equals, collaborators

**Lot of Accusation (⚖️)**:
- Day formula: ASC + Mars - Saturn
- Night formula: ASC + Saturn - Mars
- Signifies: Legal issues, conflicts, accusations, disputes

**Lot of Friends (🤝)**:
- Day formula: ASC + Moon - Mercury
- Night formula: ASC + Mercury - Moon
- Signifies: Social networks, beneficial connections, community

### Excluded Lots

**Lot of Exaltation** (ASC + Mars - Sun):
- ❌ **EXCLUDED** - Formula doesn't match traditional Hellenistic sources
- Cannot verify authenticity from primary sources (Chris Brennan, Demetra George, Robert Hand)
- Possibly modern invention or miscalculation
- **Status**: Kept in implementation but marked for review/verification

**Lot of Commerce** (ASC + Fortune - Spirit):
- ❌ **EXCLUDED** - Cannot verify this is traditional Hellenistic
- Possibly Renaissance or modern invention
- Insufficient source documentation
- **Replacement**: Lot of Friends serves similar social/network function

---

## Antiscia and Contra-Antiscia

Antiscia are mirror points across the 0° Cancer/Capricorn axis (solstice points), revealing hidden connections and symmetries between chart placements.

### Calculation Method

**Antiscion Formula**: `180° - longitude`

**Contra-Antiscion Formula**: `antiscion + 180°`

### Example
- Planet at Aries 15° (longitude 15°)
- Antiscion: 180° - 15° = 165° = Virgo 15°
- Contra-antiscion: 165° + 180° = 345° = Pisces 15°

### Interpretation Guidelines

**Integration Level**: TERTIARY testimony (supportive evidence)

**Orb**: 3° for antiscia connections to planets or angles

**Significance**:
- Antiscia reveal hidden connections between planets/angles at mirror degrees
- Like a "shadow aspect" - planets at antiscia points share subtle resonance
- Traditional technique showing equal power/equal darkness relationships
- Only mentioned in interpretation when within 3° threshold

---

## Fixed Stars

Five major fixed stars with traditional significance. Only conjunctions within 1° orb are considered.

### Calculation Method

Uses Swiss Ephemeris `fixstar_ut()` function for precise fixed star positions at birth time.

**Orb**: 1.0° for conjunctions (traditional standard)

**Checked Against**: All planets AND all angles (ASC, MC, DSC, IC)

### The Five Major Stars

**1. Regulus (Cor Leonis - Heart of the Lion)**:
- Nature: Success, royalty, honor, leadership
- Magnitude: 1.4
- Traditional: Royal star of kings and nobility

**2. Spica (Spica Virginis - Ear of Wheat)**:
- Nature: Gifts, protection, success through skill
- Magnitude: 1.0
- Traditional: Benefic star of harvest and abundance

**3. Algol (Caput Medusae - Medusa's Head)**:
- Nature: Violence, danger, challenges (use with caution)
- Magnitude: 2.1
- Traditional: Most notorious malefic star

**4. Antares (Cor Scorpii - Heart of Scorpion)**:
- Nature: Conflict, courage, obsession
- Magnitude: 1.0
- Traditional: Rival of Mars, associated with war

**5. Aldebaran (Oculus Tauri - Eye of the Bull)**:
- Nature: Honor, integrity, achievement
- Magnitude: 0.9
- Traditional: Royal star of success

### Integration Level

**TERTIARY testimony** when conjunct natal planet/angle within 1°

**NOTE**: Requires `sefstars.txt` ephemeris file for Regulus, Algol, Antares, Aldebaran. Spica calculates without additional files.

---

## Stelliums

A stellium occurs when 3 or more traditional planets occupy the same sign OR the same house.

### Calculation Method

**Sign Stellium**: 3+ traditional planets in same zodiacal sign
**House Stellium**: 3+ traditional planets in same house (by whole-sign system)

### Interpretation Guidelines

- Stellium ruler: The planet ruling the sign containing the stellium
- Intensity: Concentrated energy in that sign/house's themes
- Significance: Major life emphasis in that area
- Count: Number of planets involved (3-planet minimum, 4+ = very strong stellium)

### Example
- Sun, Mercury, Venus all in Virgo = Virgo stellium (ruled by Mercury)
- Emphasis on Virgoan themes: analysis, service, refinement, craft

---

## Hayz

Hayz is a condition where a planet is in its optimal sect position, combining three factors: chart sect, horizon position, and sign gender.

### Conditions for Hayz

**Diurnal Planets** (Sun, Jupiter, Saturn) in hayz when:
- Day chart (Sun above horizon at birth)
- AND planet above horizon (houses 7-12)
- AND planet in masculine sign (Aries, Gemini, Leo, Libra, Sagittarius, Aquarius)

**Nocturnal Planets** (Moon, Venus, Mars) in hayz when:
- Night chart (Sun below horizon at birth)
- AND planet below horizon (houses 1-6)
- AND planet in feminine sign (Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces)

**Mercury**: Neutral - does not have hayz condition (adapts to chart sect)

### Significance

Planets in hayz have optimal expression - all three sect factors aligned for maximum effectiveness and ease of function.

---

## Aspect Dynamics

### Overcoming

**Definition**: In square or opposition aspects, the planet later in zodiacal order "overcomes" the earlier planet.

**Calculation**: Planet ahead in zodiacal order (within the aspect) has superior position.

**Significance**:
- Overcoming planet has dominance in the dynamic
- Applies to challenging aspects (square, opposition)
- Shows which planet has upper hand in the relationship

**Example**: Mars at Aries 10° square Saturn at Cancer 12° → Saturn overcomes Mars (Saturn is ahead in zodiacal order from Aries to Cancer)

### Enclosure and Besiegement

**Definition**: Planet positioned between two other planets within ~15° on each side.

**Types**:
- **Benefic Enclosure**: Planet between Venus and Jupiter (supportive, protective)
- **Malefic Besiegement**: Planet between Mars and Saturn (challenging, restrictive)
- **Mixed Enclosure**: Planet between benefic and malefic (mixed influence)

**Calculation**:
1. Sort traditional planets by longitude
2. Check if any planet has another planet within 15° on both sides
3. Determine enclosure type based on nature of enclosing planets

**Significance**:
- Benefic enclosure: Protection, support, ease
- Malefic besiegement: Restriction, challenge, difficulty
- Shows whether planet operates with help or hindrance

---

## House Meanings

Traditional significations for each of the 12 houses:

### Angular Houses

**1st House** - Self, Body, Appearance
- Physical body, vitality, appearance
- Character, temperament, approach to life
- Life direction and personal identity

**4th House** - Home, Family, Roots
- Home, family, parents (especially father in Hellenistic)
- Private life, foundations, ancestry
- Real estate, land, endings

**7th House** - Partnerships, Others
- Marriage, partnerships, committed relationships
- Open enemies, rivals, opponents
- What we project onto others

**10th House** - Career, Reputation, Public Life
- Career, vocation, profession
- Public standing, reputation, honors
- Calling, life purpose

### Succedent Houses

**2nd House** - Resources, Values, Possessions
- Money, possessions, movable property
- Personal values, self-worth
- What we value and how we earn

**5th House** - Creativity, Children, Pleasure
- Children, offspring, progeny
- Creativity, creative expression, play
- Romance, pleasure, joy, good fortune

**8th House** - Death, Transformation, Shared Resources
- Death, endings, transformation
- Shared resources, inheritance, other people's money
- Taxes, debts, sex, deep intimacy

**11th House** - Friends, Hopes, Community
- Friends, allies, social networks
- Hopes, wishes, aspirations
- Groups, communities, beneficial connections

### Cadent Houses

**3rd House** - Communication, Siblings, Short Travel
- Siblings, neighbors, extended family
- Communication, learning, early education
- Short journeys, local travel
- Writing, teaching (in local context)

**6th House** - Work, Health, Service
- Work, daily labor, employment
- Health, illness, injuries
- Service, servants, subordinates
- Small animals, pets

**9th House** - Philosophy, Religion, Long Travel
- Philosophy, religion, higher learning
- Long journeys, foreign lands, foreign people
- Publishing, higher education
- Wisdom, beliefs, worldview

**12th House** - Hidden, Undoing, Isolation
- Hidden enemies, self-undoing
- Isolation, confinement, retreat
- Spirituality, mysticism, the unconscious
- Hospitals, prisons, monasteries
- Large animals (traditionally)

---

## Zodiacal Signs

### Fire Signs (♈♌♐)
**Element**: Hot & Dry
**Qualities**: Active, initiating, creative, enthusiastic
- **♈ Aries** - Cardinal Fire (initiating action)
- **♌ Leo** - Fixed Fire (sustained creative expression)
- **♐ Sagittarius** - Mutable Fire (adaptable enthusiasm)

### Earth Signs (♉♍♑)
**Element**: Cold & Dry
**Qualities**: Practical, grounded, material, stable
- **♉ Taurus** - Fixed Earth (stable resources)
- **♍ Virgo** - Mutable Earth (adaptable service)
- **♑ Capricorn** - Cardinal Earth (initiating structure)

### Air Signs (♊♎♒)
**Element**: Hot & Moist
**Qualities**: Intellectual, social, communicative, relational
- **♊ Gemini** - Mutable Air (adaptable communication)
- **♎ Libra** - Cardinal Air (initiating relationships)
- **♒ Aquarius** - Fixed Air (sustained ideas/community)

### Water Signs (♋♏♓)
**Element**: Cold & Moist
**Qualities**: Emotional, intuitive, receptive, deep
- **♋ Cancer** - Cardinal Water (initiating care/nurture)
- **♏ Scorpio** - Fixed Water (sustained depth/intensity)
- **♓ Pisces** - Mutable Water (adaptable compassion)

### Modalities

**Cardinal** (♈♋♎♑): Initiating, beginning, action-oriented
**Fixed** (♉♌♏♒): Sustaining, maintaining, stabilizing
**Mutable** (♊♍♐♓): Adapting, changing, flexible

### Polarities

**Masculine/Yang** (♈♊♌♎♐♒): Active, outward, expressive
**Feminine/Yin** (♉♋♍♏♑♓): Receptive, inward, reflective

---

## Glossary

**Accidental Dignity**: Strength from house position, aspects, or planetary conditions

**Applying**: Aspect forming as planets move toward exactness

**Benefic**: Jupiter and Venus (bringers of ease and fortune)

**Cadent**: Houses 3, 6, 9, 12 (weak positions)

**Cazimi**: Within 17' of Sun (empowered)

**Combust**: Within 8.5° of Sun (weakened)

**Contrary to Sect**: Planet operating in opposite type of chart from its nature

**Decan**: 10° division of sign (3 per sign)

**Detriment**: Planet in sign opposite its domicile

**Domicile**: Planet in its own sign (strongest essential dignity)

**Essential Dignity**: Strength from zodiacal position

**Exaltation**: Planet in sign of exaltation

**Fall**: Planet in sign opposite its exaltation

**Lot/Part**: Calculated point using formula (ASC + Planet A - Planet B). See [Lots section](#lots-hermetic-parts) for complete formulas.

**Malefic**: Mars and Saturn (bringers of challenge and difficulty)

**Nocturnal**: Night chart (Sun below horizon)

**Reception**: Planet in sign ruled by another planet

**Retrograde**: Apparent backward motion

**Sect**: Day/night division determining planetary strength

**Separating**: Aspect moving past exactness

**Succedent**: Houses 2, 5, 8, 11 (moderate positions)

**Triplicity**: Elemental dignity (fire, earth, air, water rulers)

**Under the Beams**: Within 15° of Sun (obscured)

**Whole-Sign Houses**: House system where each house = one complete sign

**Antiscia**: Mirror point across 0° Cancer/Capricorn axis (formula: 180° - longitude). See [Antiscia section](#antiscia-and-contra-antiscia).

**Contra-Antiscia**: Point 180° from antiscion (formula: antiscion + 180°)

**Stellium**: 3 or more traditional planets in same sign or house. See [Stelliums section](#stelliums).

**Hayz**: Planet in optimal sect condition (chart sect + horizon position + sign gender aligned). See [Hayz section](#hayz).

**Overcoming**: Planet ahead in zodiacal order dominates in square/opposition. See [Aspect Dynamics section](#aspect-dynamics).

**Enclosure**: Planet between two others within ~15°. See [Aspect Dynamics section](#aspect-dynamics).

---

**IMPORTANT NOTE**: This document describes the calculation methods used in this project. Any time calculation methods change in `seed_data_generator.py` or other calculation scripts, this reference document MUST be updated accordingly to maintain accuracy.

---

*For astronomical calculations implementation, see `/scripts/seed_data_generator.py`*
*For ephemeris helper functions, see `/scripts/ephemeris_helper.py`*
