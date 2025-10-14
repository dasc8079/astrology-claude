# Astrology Reference - Traditional & Hellenistic Systems

This document contains static astrological reference information for the project. All systems and definitions follow traditional/Hellenistic astrology with minimal modern additions.

**Note**: For calculation tools, see `/scripts/astrology_reference.py` and `/scripts/ephemeris_helper.py`

---

## Table of Contents

1. [House System](#house-system)
2. [Rulerships](#rulerships)
3. [Dignities and Debilities](#dignities-and-debilities)
4. [Sect (Day/Night Chart Analysis)](#sect-dayn

ight-chart-analysis)
5. [Aspects](#aspects)
6. [Planetary Set](#planetary-set)
7. [Planetary Conditions](#planetary-conditions)
8. [House Meanings](#house-meanings)
9. [Zodiacal Signs](#zodiacal-signs)
10. [Glossary](#glossary)

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

**Lot/Part**: Calculated point using formula (ASC + Planet A - Planet B)

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

---

*For programmatic access to this data, see `/scripts/astrology_reference.py`*
*For astronomical calculations, see `/scripts/ephemeris_helper.py`*
