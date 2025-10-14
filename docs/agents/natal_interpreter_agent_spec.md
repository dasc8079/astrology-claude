# Natal Interpreter Agent Specification

**Version**: 1.1
**Created**: 2025-10-13
**Updated**: 2025-10-14 (Added Chiron toggleability via profile settings)
**Purpose**: Define hierarchical interpretation framework for natal horoscope generation
**Applies To**: natal-interpreter.md (psychological sections) and natal-interpreter-experiential.md (experiential domains)

---

## Executive Summary

### Problem Statement

Current natal horoscope interpretations treat all 14 astrological factors equally, resulting in unfocused, scattered interpretations that list multiple possibilities without identifying PRIMARY patterns. This produces horoscopes that feel accurate but lack clarity about the central life themes.

**Example**: Sam_P (professional artist) received career section focused on "counseling, therapy, social work, teaching, healthcare" when chart clearly indicates creative professional work (Venus chart ruler in Gemini 9th, Jupiter exalted in Cancer 10th stellium with Sun-Mercury).

### Solution

Implement hierarchical testimony framework with three tiers:
- **PRIMARY factors** (70-80% of content): Most important indicators based on traditional astrological hierarchies
- **SECONDARY factors** (15-20% of content): Supporting/modifying factors
- **TERTIARY factors** (5-10% of content): Minor considerations

### Success Criteria

1. **Clarity**: Identify PRIMARY life pattern first, then show HOW secondary factors modify it
2. **Accuracy**: Work for any chart type (artist, designer, engineer, therapist, etc.) without being prescriptive
3. **Generalizability**: Based on traditional astrological principles, not specific profiles
4. **Testability**: Sam_P chart identifies creative professional career; Darren_S chart identifies creative system builder

---

## Foundation Principles

### Planetary Strength = Essential Dignity + Accidental Dignity

**CRITICAL**: Essential and accidental dignity work TOGETHER to determine a planet's overall strength and effectiveness as a PRIMARY factor. They are not separate considerations.

**Essential Dignity** (Planetary Strength) answers: "How strong is this planet inherently?"
**Accidental Dignity** (Planetary Effectiveness) answers: "How well can this planet express its strength?"

### Essential Dignity Hierarchy

**From highest to lowest**:
1. Domicile (e.g., Mars in Aries) - Maximum strength
2. Exaltation (e.g., Jupiter in Cancer) - Empowered strength
3. Triplicity ruler - Moderate strength
4. Term/bound ruler - Minor strength
5. Decan/face ruler - Minor strength
6. Peregrine (no essential dignity) - Neutral/challenged
7. Detriment (e.g., Mars in Libra) - Weakened
8. Fall (e.g., Jupiter in Capricorn) - Debilitated

### Accidental Dignity Hierarchy (Modifies Essential Dignity)

**From highest to lowest**:
1. Angular houses (1st, 10th, 7th, 4th) - Maximum effectiveness
2. Succedent houses (2nd, 11th, 8th, 5th) - Moderate effectiveness
3. Cadent houses (3rd, 12th, 9th, 6th) - Minimum effectiveness
4. **Planetary Joys** (planet in its joy house) - Dignity boost
   - Mercury in 1st (joy of communication at forefront)
   - Moon in 3rd (joy in movement, siblings, environment)
   - Venus in 5th (joy in pleasure, creativity, romance)
   - Mars in 6th (joy in labor, conflict, service)
   - Sun in 9th (joy in meaning, philosophy, god)
   - Jupiter in 11th (joy in community, good spirit, hopes)
   - Saturn in 12th (joy in solitude, bad spirit, confinement)

### Combined Dignity Assessment (for PRIMARY Factor Evaluation)

**Maximum PRIMARY Strength**:
- Strong essential dignity (domicile/exaltation) + Angular placement + Planetary joy (if applicable)
- Example: Jupiter in Cancer (exaltation) in 11th house (angular + joy) = MAXIMUM PRIMARY strength

**Strong PRIMARY (but less effective)**:
- Strong essential dignity (domicile/exaltation) + Cadent placement
- Example: Mars in Aries (domicile) in 12th house (cadent) = Strong but poorly placed to act

**Challenged PRIMARY (but visible)**:
- Weak essential dignity (detriment/fall) + Angular placement
- Example: Mars in Libra (detriment) in 10th house (angular) = Weak but publicly visible

**Maximum Challenge**:
- Weak essential dignity (detriment/fall) + Cadent placement
- Example: Saturn in Cancer (detriment) in 12th house (cadent) = Weak and hidden

**Priority Rule**: When evaluating planets as PRIMARY factors, assess BOTH essential and accidental dignity together. A planet in domicile but cadent is still PRIMARY (strong planet) but mention effectiveness is reduced. A planet in detriment but angular is still a PRIMARY challenge (weak planet) but at least has visibility.

### Sect Hierarchy

**Day Chart** (Sun above horizon):
- Sect light: Sun (PRIMARY)
- Benefic of sect: Jupiter (PRIMARY for benefic matters)
- Malefic of sect: Saturn (SECONDARY for challenges)
- Malefic contrary to sect: Mars (PRIMARY for challenges)

**Night Chart** (Sun below horizon):
- Sect light: Moon (PRIMARY)
- Benefic of sect: Venus (PRIMARY for benefic matters)
- Malefic of sect: Mars (SECONDARY for challenges)
- Malefic contrary to sect: Saturn (PRIMARY for challenges)

**Priority Rule**: Sect light and malefic contrary to sect are PRIMARY factors. Benefic of sect is PRIMARY for talents/gifts.

### House Analysis Hierarchy

**For any life area (e.g., career = 10th house)**:
1. **PRIMARY**: WHERE does the house ruler go? (10th ruler placement)
2. **PRIMARY**: WHAT is in the house? (planets in 10th)
3. **SECONDARY**: HOW is it modified? (aspects to 10th ruler, aspects to planets in 10th, aspects to MC)
4. **TERTIARY**: Additional context (MC sign, minor dignities, decan rulers)

**Priority Rule**: House ruler placement (WHERE) always comes before planets in house (WHAT). Aspects (HOW) are SECONDARY unless they radically change the testimony.

### Aspect Hierarchy

**By type**:
1. Conjunction (0°) - Merging, blending, intensification
2. Opposition (180°) - Tension, polarity, integration challenge
3. Square (90°) - Dynamic friction, growth pressure
4. Trine (120°) - Harmony, ease, natural flow
5. Sextile (60°) - Opportunity, support, cooperation

**By target**:
1. Aspects to house ruler (HIGH priority - modify PRIMARY pattern)
2. Aspects to planets in house (MEDIUM priority - modify WHAT)
3. Aspects to angles (ASC/MC/DSC/IC) (MEDIUM priority - affect overall chart expression)
4. Major aspect patterns (stellium, T-square, grand trine) (HIGH priority if present)

**Priority Rule**: Aspects to house ruler are SECONDARY factors that modify PRIMARY testimony. Harmonious aspects (trine/sextile) ease expression; dynamic aspects (square/opposition) create friction or growth pressure.

---

## Priority Tables by Life Area

### 1. Career & Vocation (10th House)

**PRIMARY FACTORS (70-80%)**:
- 10th house ruler placement (WHERE career unfolds)
- Planets in 10th house (WHAT career involves)
- Lot of Spirit placement (PURPOSE alignment)
- Essential dignities of 10th ruler (strength/weakness)
- Aspects to 10th house ruler (HOW career is modified)

**SECONDARY FACTORS (15-20%)**:
- MC sign and its ruler
- Aspects to MC
- 6th house analysis (daily work conditions)
- Sect considerations (day vs night chart)
- Accidental dignities (angular/succedent/cadent)

**TERTIARY FACTORS (5-10%)**:
- 2nd house (income from career)
- Decan rulers
- Minor dignities
- Creative factors (5th house connections)

**Decision Rules**:
- IF 10th ruler in 5th house → Creative professional career (not prescriptive about being "artist")
- IF 10th ruler in 9th house → Teaching, publishing, philosophy, travel-related work
- IF 10th ruler in 6th house → Service-oriented work, health/healing, detailed technical work
- IF 10th ruler angular + well-dignified → Public prominence in career
- IF 10th ruler cadent + afflicted → Behind-the-scenes work or career challenges

### 2. Love & Intimate Relating (7th House)

**PRIMARY FACTORS (70-80%)**:
- 7th house ruler placement (WHERE partnerships form)
- Venus placement, dignity, condition (universal relationship significator)
- Mars placement, dignity, condition (desire nature)
- Planets in 7th house (WHAT partnerships involve)
- Aspects to 7th house ruler (HOW relationships are modified)

**SECONDARY FACTORS (15-20%)**:
- Descendant sign
- Sect considerations (benefic of sect for ease in relating)
- Mutual reception between relationship planets
- Aspects to Venus and Mars
- Moon placement (emotional needs)

**TERTIARY FACTORS (5-10%)**:
- 5th house (romance, dating, creative self-expression in love)
- 11th house (friendship element in partnership)
- Lot of Eros (erotic connection)

**Decision Rules**:
- IF 7th ruler in 1st → Partnerships deeply affect identity
- IF 7th ruler in 5th → Romance-focused, creative partnerships
- IF 7th ruler in 10th → Partnerships tied to career/public life
- IF Venus/Mars in mutual reception → Strong attraction and compatibility

### 3. Core Personality (Ascendant)

**PRIMARY FACTORS (70-80%)**:
- Ascendant sign (mask, persona, approach to life)
- Chart ruler placement and dignity (core identity, WHERE energy goes)
- Planets in 1st house (WHAT defines self-presentation)
- Aspects to Ascendant (HOW personality is modified)
- Aspects to chart ruler (HOW core identity is shaped)

**SECONDARY FACTORS (15-20%)**:
- Sect light (Sun for day chart, Moon for night chart)
- Planets closely conjunct ASC
- Chart ruler's house placement
- Aspects to planets in 1st house

**TERTIARY FACTORS (5-10%)**:
- Rising decan
- Fixed stars on Ascendant
- Antiscia to Ascendant

**Decision Rules**:
- IF chart ruler angular + well-dignified → Strong sense of self, clear direction
- IF chart ruler cadent + afflicted → Identity formation through challenges
- IF chart ruler in 10th → Public identity, career-focused personality
- IF chart ruler in 4th → Private, family-oriented, inward personality

### 4. Psychological Makeup

**4a. Emotional Nature (Moon)**

**PRIMARY FACTORS (70-80%)**:
- Moon placement by house (WHERE emotions are experienced)
- Moon's essential dignities (emotional strength/challenge)
- Aspects to Moon (HOW emotions are triggered)
- Sect considerations (Moon as sect light in night chart = PRIMARY)

**SECONDARY FACTORS (15-20%)**:
- Moon phase (relationship to Sun)
- Planets in 4th house (emotional foundation)
- 4th house ruler (roots, security needs)
- Aspects to 4th house ruler

**TERTIARY FACTORS (5-10%)**:
- Lot of Fortune (material/physical well-being)
- Moon's antiscia

**4b. Mental Tendencies (Mercury)**

**PRIMARY FACTORS (70-80%)**:
- Mercury placement by house (WHERE mind engages)
- Mercury's essential dignities (mental clarity/challenge)
- Aspects to Mercury (HOW thinking is shaped)
- Mercury's condition (retrograde, combust, cazimi)

**SECONDARY FACTORS (15-20%)**:
- 3rd house ruler (communication style)
- Planets in 3rd house
- 9th house connections (higher mind, beliefs)

**TERTIARY FACTORS (5-10%)**:
- Mercury's speed (swift or slow)
- Minor aspects to Mercury

**4c. Will & Vitality (Sun)**

**PRIMARY FACTORS (70-80%)**:
- Sun placement by house (WHERE vitality shines)
- Sun's essential dignities (strength of will)
- Aspects to Sun (HOW vitality is expressed)
- Sect considerations (Sun as sect light in day chart = PRIMARY)

**SECONDARY FACTORS (15-20%)**:
- Planets in 5th house (creative expression)
- 5th house ruler (joy, creativity)
- Sun-Moon phase relationship

**TERTIARY FACTORS (5-10%)**:
- Solar eclipses near birth
- Sun's antiscia

**4d. Desire & Drive (Mars)**

**PRIMARY FACTORS (70-80%)**:
- Mars placement by house (WHERE action is taken)
- Mars's essential dignities (strength/challenge of drive)
- Aspects to Mars (HOW desire is expressed)
- Sect considerations (Mars contrary to sect in day chart = intensified)

**SECONDARY FACTORS (15-20%)**:
- Mars condition (retrograde, swift/slow)
- Planets Mars aspects
- 1st house connections (assertiveness in personality)

**TERTIARY FACTORS (5-10%)**:
- Mars's antiscia
- Minor aspects to Mars

### 5. Life Path & Purpose (North Node, Lot of Spirit)

**PRIMARY FACTORS (70-80%)**:
- Lot of Spirit placement (purpose, calling, spiritual path)
- North Node placement (evolutionary direction)
- 9th house ruler (philosophy, meaning, higher learning)
- Sun placement (core identity, vitality, will)

**SECONDARY FACTORS (15-20%)**:
- 9th house planets
- Aspects to Lot of Spirit
- South Node placement (past patterns to release)
- 12th house connections (spiritual development)

**TERTIARY FACTORS (5-10%)**:
- Jupiter placement (growth, expansion, wisdom)
- Saturn placement (structure, discipline, mastery)

**Decision Rules**:
- IF Lot of Spirit in angular house → Public purpose, visible calling
- IF Lot of Spirit in cadent house → Behind-the-scenes purpose, teaching, healing
- IF North Node in 10th → Purpose through career, public contribution

### 6. Strengths & Gifts

**PRIMARY FACTORS (70-80%)**:
- Planets in domicile (e.g., Venus in Taurus, Mars in Scorpio)
- Planets in exaltation (e.g., Venus in Pisces, Jupiter in Cancer)
- Benefic of sect (Jupiter for day chart, Venus for night chart)
- Chart ruler if well-dignified and well-placed

**SECONDARY FACTORS (15-20%)**:
- Triplicity rulers
- Planets in angular houses
- Harmonious aspects (trines, sextiles) from benefics
- Mutual receptions between benefics

**TERTIARY FACTORS (5-10%)**:
- Term/bound rulers
- Fixed stars of benefic nature
- Cazimi planets (within 0°17' of Sun)

**Priority Rule**: Domicile/exaltation placements are PRIMARY strengths. Benefic of sect shows WHERE ease and support naturally flow.

### 7. Challenges & Growth Edges

**PRIMARY FACTORS (70-80%)**:
- Planets in detriment (e.g., Venus in Aries, Mars in Libra)
- Planets in fall (e.g., Sun in Libra, Moon in Scorpio)
- Malefic contrary to sect (Mars in day chart, Saturn in night chart)
- Saturn placement (structure, limitation, fear, mastery through discipline)

**SECONDARY FACTORS (15-20%)**:
- Malefic of sect (Saturn in day chart, Mars in night chart)
- Planets in cadent houses
- Difficult aspects (squares, oppositions) from malefics
- Combust planets (within 8° of Sun, NOT cazimi)

**TERTIARY FACTORS (5-10%)**:
- 12th house planets (unconscious challenges)
- 8th house planets (crisis, transformation)
- Retrograde planets (internalized expression)

**Priority Rule**: Detriment/fall placements are PRIMARY challenges. Malefic contrary to sect shows WHERE friction and growth occur.

### 8. Relationships & Social Bonds (11th House)

**PRIMARY FACTORS (70-80%)**:
- 11th house ruler placement (WHERE friendships form)
- Planets in 11th house (WHAT friendships involve)
- Moon placement (emotional connection, community)
- 3rd house ruler (siblings, neighbors, local community)
- Aspects to 11th house ruler (HOW friendships are modified)

**SECONDARY FACTORS (15-20%)**:
- Aspects to planets in 11th house
- Venus placement (social harmony)
- Mercury placement (communication with friends)
- 7th house connections (one-on-one vs group relating)

**TERTIARY FACTORS (5-10%)**:
- Jupiter placement (expansion through community)
- Saturn placement (long-term friendships, boundaries)

**Decision Rules**:
- IF 11th ruler in 1st → Friendships deeply affect identity
- IF 11th ruler in 10th → Friendships tied to career/goals
- IF 11th ruler in 5th → Creative, playful friendships

### 9. Creative Expression (5th House)

**PRIMARY FACTORS (70-80%)**:
- 5th house ruler placement (WHERE creativity flows)
- Planets in 5th house (WHAT creative expression involves)
- Venus placement (beauty, art, aesthetic)
- Sun placement (radiant self-expression, joy)
- Aspects to 5th house ruler (HOW creativity is modified)

**SECONDARY FACTORS (15-20%)**:
- Aspects to planets in 5th house
- 3rd house connections (communication of ideas)
- Moon placement (emotional creativity)
- Mercury placement (mental creativity)

**TERTIARY FACTORS (5-10%)**:
- Mars placement (creative drive, passion)
- Jupiter placement (expansive creativity)

**Decision Rules**:
- IF 5th ruler in 10th → Professional creative work
- IF 5th ruler in 9th → Teaching, publishing, philosophical creativity
- IF 5th ruler well-dignified + Venus strong → Natural creative talent

### 10. Synthesis & Integration

**PRIMARY FACTORS (70-80%)**:
- Central pattern identified across all life areas (e.g., "Creative professional building structures")
- Sun-Moon relationship (core identity + emotional nature)
- Chart ruler's final disposition chain
- Sect light emphasis

**SECONDARY FACTORS (15-20%)**:
- Major aspect patterns (T-square, grand trine, stellium)
- Convergence points (multiple techniques pointing to same theme)
- Mutual receptions creating strong bonds

**TERTIARY FACTORS (5-10%)**:
- Antiscia connections
- Fixed star influences
- Eclipse points

**Decision Rules**:
- Synthesis MUST synthesize PRIMARY factors from all sections into coherent narrative
- Avoid listing secondary factors unless they radically modify primary pattern
- Focus on HOW primary factors work together, not individual details

---

## Synthesis Guidelines

### Four-Part Synthesis Structure

**1. Opening (PRIMARY pattern) - 30% of section**:
- State the PRIMARY life theme/pattern clearly
- Use most dignified planets, sect light, chart ruler
- Example: "Your life centers on creative professional work that builds lasting structures..."

**2. Development (HOW it unfolds) - 30% of section**:
- Show HOW the primary pattern manifests across life areas
- Use house ruler placements, angular planets
- Example: "This creative building impulse appears through [10th ruler in 5th]..."

**3. Supporting (ALSO true) - 25% of section**:
- Add SECONDARY factors that support or modify the pattern
- Use aspects, secondary dignities, sect considerations
- Example: "Additionally, [Venus square Saturn] adds discipline to your aesthetic..."

**4. Integration (bringing it together) - 15% of section**:
- Synthesize PRIMARY + SECONDARY into unified picture
- Show convergence of multiple techniques
- Example: "The convergence of [Sun-Saturn conjunction + Mars in 9th + 10th ruler in 5th] creates..."

### Word Allocation by Tier

**PRIMARY factors**: 70-80% of word count
**SECONDARY factors**: 15-20% of word count
**TERTIARY factors**: 5-10% of word count (or omit entirely if space limited)

### Language Patterns by Tier

**PRIMARY tier language**:
- "Your life centers on..."
- "The core pattern is..."
- "Most fundamentally..."
- "At the heart of your chart..."

**SECONDARY tier language**:
- "This is modified by..."
- "Additionally..."
- "Supporting this pattern..."
- "This tendency is shaped by..."

**TERTIARY tier language**:
- "As a minor note..."
- "Also present..."
- "In a subtler way..."
- "Worth mentioning..."

---

## Output Structure

### Universal 3-Page Standard

**Page 1**: Title page
- Full name
- Birth date, time, location
- Chart image (if available)
- Title: "Natal Horoscope"

**Page 2**: Chart Overview (8-12 sparse bullets, NO narrative prose)
- Essential dignities (domicile, exaltation)
- Angular planets
- Major aspect patterns (stellium, T-square, grand trine)
- Sect light
- Chart ruler placement
- Notable lots (Fortune, Spirit)
- Key mutual receptions
- Significant combustion/cazimi

**Page 3**: Synthesis Introduction (600-800 words prose, NO heading)
- Opens directly with synthesis
- Identifies central life theme/pattern
- Uses PRIMARY factors only
- Written in flowing, accessible prose
- NO section heading visible

**Pages 4-19**: Main Synthesis (~4,800 words total)
- **Variant A (Psychological Sections)**: 11 sections
  1. Core Personality (450 words)
  2. Psychological Makeup (800 words) - 4 subsections
  3. Love & Intimate Relating (450 words)
  4. Relationships & Social Bonds (400 words)
  5. Life Path & Purpose (450 words)
  6. Strengths & Gifts (450 words)
  7. Challenges & Growth Edges (450 words)
  8. Career & Vocation (450 words)
  9. Creative Expression (450 words)
  10. Synthesis & Integration (450 words)

- **Variant B (Experiential Domains)**: 4 domains
  1. Inner Life (1,200 words) - 3 subsections
  2. Outer Expression (1,200 words) - 3 subsections
  3. Relational Life (1,200 words) - 3 subsections
  4. Purpose & Calling (1,200 words) - 3 subsections

**Page 20**: Poetic Wrapup (300 words, NO heading)
- Closes with synthesized, poetic reflection
- References PRIMARY pattern from introduction
- Written in flowing, accessible prose
- NO section heading visible

### Three Output Files Required

1. **process.md**: Technical analysis with all 14 astrological factors documented
   - Dignities table
   - House analysis
   - Aspect tables
   - Lot calculations
   - Stellium identification
   - Combustion/cazimi notes
   - Mutual receptions
   - Antiscia
   - Angle aspects
   - Complete technical data for reference

2. **synthesis.md**: Accessible prose synthesis following universal 3-page standard
   - Page 1: Title page
   - Page 2: Chart overview (8-12 bullets)
   - Page 3: Introduction (600-800 words)
   - Pages 4-19: Main synthesis (4,800 words)
   - Page 20: Poetic wrapup (300 words)

3. **synthesis.pdf**: Professional PDF generated from synthesis.md
   - Professional typography (Garamond/Georgia serif)
   - Justified text with hyphenation
   - Elegant heading hierarchy
   - Decorative elements (✦ bullets, drop caps)
   - Print-ready format

### Agent Output Format Ownership

**The agent produces final formatted markdown files. The orchestrator does NOT reformat.**

Agent must:
- Generate correctly structured synthesis.md with page breaks
- Include proper heading hierarchy
- Apply word count targets to each section
- Format Page 2 as 8-12 sparse bullets (NO narrative)
- Format Page 3 and Page 20 as prose without section headings
- Generate technical process.md with complete data
- Provide clear file naming: `natal_synthesis_{profile_name}_{date}.md` and `natal_process_{profile_name}_{date}.md`

---

## Aspect Integration Guidelines

### How to Interpret Aspects

**Harmonious Aspects (Trine 120°, Sextile 60°)**:
- Ease, flow, natural talent
- Support, opportunity, cooperation
- "X flows easily into Y"
- "X supports Y naturally"

**Dynamic Aspects (Square 90°, Opposition 180°)**:
- Friction, tension, growth pressure
- Integration challenge, polarity
- "X creates friction with Y, pushing growth in Z direction"
- "X and Y create tension that must be integrated through..."

**Conjunction (0°)**:
- Merging, blending, intensification
- Cannot separate the two energies
- "X and Y blend into unified expression"
- "X intensifies Y"

### Aspects to House Rulers (SECONDARY factors)

**Modify PRIMARY testimony of WHERE house ruler goes**:
- 10th ruler in 5th trine Venus → Creative career with EASE, aesthetic flow
- 10th ruler in 5th square Saturn → Creative career with DISCIPLINE, structure, obstacles
- 7th ruler in 10th opposite Mars → Partnerships tied to career but WITH TENSION around independence

### Aspects to Planets in House (SECONDARY factors)

**Modify WHAT planets in house indicate**:
- Sun in 10th trine Jupiter → Public success with EXPANSION, opportunity
- Sun in 10th square Saturn → Public success with DISCIPLINE, obstacles, mastery through effort
- Venus in 7th opposite Mars → Relationships with POLARITY between harmony (Venus) and independence (Mars)

### Aspects to Angles (MEDIUM priority)

**Modify overall chart expression**:
- Jupiter trine Ascendant → Optimistic, expansive persona
- Saturn square Ascendant → Reserved, serious, disciplined persona
- Venus conjunct MC → Public image tied to beauty, harmony, relationships
- Mars opposite IC → Family dynamics involve conflict, independence, assertion

### Major Aspect Patterns (HIGH priority if present)

**Stellium** (3+ planets in same sign/house):
- Creates intensity, focus, emphasis
- Treat as PRIMARY factor in that life area
- Example: Sun-Mercury-Jupiter stellium in 10th → Career is CENTRAL life focus

**T-Square** (two planets in opposition, both square a third):
- Creates dynamic tension requiring integration
- Treat as SECONDARY factor affecting multiple life areas
- Example: Moon-Saturn opposition both square Mars → Emotional security vs structure creates drive for independence

**Grand Trine** (three planets in trine, forming triangle):
- Creates ease, natural talent, flow
- Treat as SECONDARY factor showing WHERE ease occurs
- Example: Sun-Moon-Jupiter grand trine → Emotional harmony, optimism, ease with self

---

## All Techniques Included

### Profile Settings Integration

**IMPORTANT**: Agents must read profile settings from `profiles/{profile_name}/profile.md` before interpretation.

**Toggleable Techniques** (as of v1.1):
- **Chiron** (`include_chiron: true/false`) - Wounded healer archetype
  - If `true`: Interpret Chiron placement, aspects, and themes throughout synthesis
  - If `false`: Do NOT mention or interpret Chiron anywhere in synthesis or process files

**Non-Toggleable Techniques** (always included):
- Traditional seven planets (Sun through Saturn)
- Modern outer planets (Uranus, Neptune, Pluto) - always included as secondary psychological context
- Four core lots (Fortune, Spirit, Eros, Necessity)
- House rulers, angles, aspects, dignities
- Antiscia (if within 3° orb)
- Fixed stars (if within 1° orb)

**Implementation**:
- Agents read `include_chiron` setting in **Step 3.5** of workflow
- Only calculate and interpret Chiron if setting is `true`
- Seed data generator respects this setting and only calculates Chiron position when enabled
- See agent workflow sections for implementation details

### Four Lots (PRIMARY/SECONDARY depending on context)

**Lot of Fortune** (material well-being, body, health):
- PRIMARY for physical health, material security
- Placement by house shows WHERE fortune manifests
- Ruler of Lot shows HOW fortune develops

**Lot of Spirit** (purpose, calling, spiritual path):
- PRIMARY for life path, career purpose, calling
- Placement by house shows WHERE purpose is found
- Ruler of Lot shows HOW purpose unfolds

**Lot of Eros** (erotic connection, passion, desire):
- SECONDARY for love relationships
- Shows WHERE passion is experienced
- Adds nuance to Venus/Mars testimony

**Lot of Necessity** (fate, constraint, obligation):
- SECONDARY for challenges, obligations
- Shows WHERE constraints exist
- Adds nuance to Saturn/South Node testimony

### Mutual Reception (SECONDARY factor)

**Definition**: Two planets in each other's domicile (e.g., Venus in Aries, Mars in Taurus)

**Effect**: Creates strong bond, cooperation, exchange of energy between the two planets

**Interpretation**:
- "Venus and Mars are in mutual reception, creating natural cooperation between [Venus themes] and [Mars themes]"
- If involves house rulers, strengthens connection between those life areas

### Stelliums (PRIMARY factor when present)

**Definition**: 3+ planets in same sign or same house

**Effect**: Intensifies, focuses, emphasizes that sign/house

**Interpretation**:
- Treat stellium as PRIMARY factor in that life area
- "The stellium of [planets] in [house] creates intense focus on [life area]"
- Often shows WHERE most life energy goes

### Combustion & Cazimi (SECONDARY/TERTIARY factor)

**Combustion** (planet within 8° of Sun, but NOT cazimi):
- Planet is "burned up", weakened, hidden, internalized
- SECONDARY challenge factor
- "Mercury combust suggests communication style is internalized, less visible"

**Cazimi** (planet within 0°17' of Sun):
- Planet is "in the heart of the Sun", empowered, clarified
- SECONDARY strength factor
- "Venus cazimi suggests relationships are central to identity, empowered by will"

### Angle Aspects (MEDIUM priority)

**Planets aspecting Ascendant** (affect personality, self-presentation):
- Jupiter trine ASC → Optimistic, expansive persona
- Saturn square ASC → Reserved, serious, disciplined persona

**Planets aspecting Midheaven** (affect career, public image):
- Venus conjunct MC → Public image tied to beauty, harmony
- Mars square MC → Public image involves assertion, conflict, independence

**Planets aspecting Descendant** (affect partnerships):
- Jupiter opposite ASC (conjunct DSC) → Partnerships bring expansion, optimism
- Saturn opposite ASC (conjunct DSC) → Partnerships involve commitment, structure

**Planets aspecting IC** (affect home, roots, family):
- Moon conjunct IC → Deep emotional connection to home, family
- Mars square IC → Family dynamics involve conflict, assertion

### Antiscia (TERTIARY factor)

**Definition**: Mirror points across 0° Cancer-Capricorn axis (e.g., 15° Gemini = antiscion 15° Cancer)

**Effect**: Hidden connection, shadow side, unconscious link

**Interpretation**: Usually TERTIARY unless connecting major chart factors

### Under the Beams (SECONDARY/TERTIARY factor)

**Definition**: Planet within 15° of Sun (but beyond 8° combustion range)

**Effect**: Planet is weakened, less visible, operating in Sun's shadow

**Interpretation**:
- SECONDARY challenge factor (less severe than combustion)
- "Mercury under the beams suggests communication style operates in shadow of identity/will"
- Planet's natural expression is diminished but not destroyed

### Final Dispositor (SECONDARY factor)

**Definition**: Planet that rules the chain of dispositions (the planet that no other planet disposes)

**Effect**: Shows ultimate authority and integration point in chart

**Interpretation**:
- SECONDARY factor for overall chart synthesis
- "All planetary energy ultimately flows through [final dispositor]"
- If no final dispositor, note mutual reception chain as integration mechanism
- Example: Moon in Aries → Mars in Taurus → Venus in Pisces → Jupiter in Cancer → Moon (mutual reception chain, no final dispositor)
- Example: Moon in Aries → Mars in Scorpio (Mars is final dispositor in domicile)

---

## Quality Standards

### Good Hierarchical Interpretation

✅ Opens with PRIMARY pattern clearly stated
✅ Shows HOW primary pattern manifests across life areas
✅ Adds SECONDARY factors only when they modify the primary pattern
✅ Uses traditional astrological hierarchies (dignity, accidental placement, sect)
✅ Feels focused, clear, purposeful (reader can answer "What is this person's PRIMARY life theme?")
✅ Works for any chart type without being prescriptive about specific careers/paths

### Poor Hierarchical Interpretation

❌ Lists multiple possibilities equally ("You could be X or Y or Z")
❌ Treats all factors as equally important
❌ Feels scattered, unfocused
❌ Reader cannot identify PRIMARY life pattern
❌ Prescriptive about specific careers ("You are an artist")
❌ Ignores traditional astrological hierarchies

---

## Testing Criteria

### Test Case 1: Sam_P (Professional Artist)

**Chart Features**:
- Libra Ascendant, Venus chart ruler in Gemini 9th
- Sun-Mercury-Jupiter stellium in Cancer 10th (Jupiter exalted)
- Moon in Pisces 6th
- Day chart

**Expected Interpretation**:
- **Career PRIMARY**: "Your career centers on creative professional work..." (10th ruler Moon in Pisces 6th suggests service-oriented creative work; Jupiter exalted in 10th stellium suggests teaching/publishing; Venus in Gemini 9th suggests communication/ideas)
- **NOT prescriptive**: Doesn't say "You are an artist" but DOES identify creative professional field
- **NOT scattered**: Doesn't list "counseling, therapy, social work, teaching, healthcare" equally

**Success Metric**: Career section identifies creative professional work as PRIMARY, with teaching/communication/ideas as modifiers.

### Test Case 2: Darren_S (Creative System Builder)

**Chart Features**:
- Leo Ascendant, Sun chart ruler in Capricorn 6th conjunct Saturn
- Venus in Sagittarius 5th
- Mars in Aries 9th (domicile)
- Moon in Leo 1st
- Night chart

**Expected Interpretation**:
- **Career PRIMARY**: "Your career centers on building creative structures/systems..." (Sun-Saturn conjunction in Capricorn 6th suggests structured, disciplined work; Venus in 5th suggests creative element; Mars in Aries 9th suggests innovation/ideas)
- **Personality PRIMARY**: "Your core identity involves creative leadership..." (Moon in Leo 1st, Sun in Capricorn suggests disciplined creativity)
- **NOT scattered**: Identifies "creative system builder" as central theme, not "you could do therapy OR teaching OR engineering OR art"

**Success Metric**: Career section identifies structured creative work as PRIMARY, with leadership and innovation as modifiers.

---

## Phase 2 Future Enhancements (NOT for v1)

### RAG Database for Chart Interpretation Patterns

**Purpose**: Query past chart interpretations to find similar patterns
**Use Case**: "Show me charts with 10th ruler in 5th" → Learn from past interpretations
**Status**: Future enhancement, not implemented in v1

### Scoring System for Hierarchical Weighting

**Purpose**: Numerical weights for each factor (e.g., domicile = 10 points, triplicity = 3 points)
**Use Case**: Automated calculation of PRIMARY vs SECONDARY vs TERTIARY
**Status**: Future enhancement, not implemented in v1

### Cross-Chart Pattern Recognition

**Purpose**: Identify recurring patterns across multiple charts
**Use Case**: "What do all charts with 10th ruler in 5th have in common?"
**Status**: Future enhancement, not implemented in v1

---

## Implementation Notes

### Applies to Both Agent Variants

This specification applies to:
1. **natal-interpreter.md** (11 psychological sections)
2. **natal-interpreter-experiential.md** (4 experiential domains)

Both agents must implement the same hierarchical framework with the same priority tables.

### Agent Owns Output Format

The agent produces final formatted markdown files. The mode-orchestrator does NOT reformat or restructure the output.

Agent responsibilities:
- Generate synthesis.md with correct page structure
- Generate process.md with complete technical analysis
- Apply hierarchical framework to all sections
- Meet word count targets
- Format Page 2 as bullets, Page 3 and Page 20 as prose without headings
- Provide correct file naming and paths

---

**End of Specification**

*This document serves as the source of truth for natal horoscope interpretation. All agent updates should reference this spec.*
