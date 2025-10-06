# Transits Guide

## Overview

**Transits** are the current positions of planets in the sky and their aspects to your natal chart. They represent the most immediate and concrete timing technique - showing when natal chart themes get triggered by real-time planetary movements.

Think of transits as **weather** passing through your natal chart: some days are sunny (Jupiter trine natal Venus), some days are stormy (Mars square natal Moon), but the underlying landscape (natal chart) remains constant.

## Key Principle

**Transiting planets activate natal planets when they aspect them**.

- **Transiting Jupiter conjunct natal Sun** = Expansion and opportunity activating your core identity
- **Transiting Saturn square natal Moon** = Restriction and maturity challenging your emotional nature
- **Transiting Mars trine natal Mercury** = Energy and drive flowing harmoniously with your mind/communication

The natal chart shows **what you have**, transits show **when it activates**.

## How It Works

### Real-Time Sky Positions

Calculate where planets are **right now** (or any date):
- Transiting Sun at 13° Libra
- Transiting Moon at 4° Aries
- Transiting Saturn at 27° Pisces Retrograde
- etc.

### Aspects to Natal Chart

Compare these positions to your natal planets:
- If transiting Mars (current sky) is at 10° Scorpio
- And natal Neptune is at 9° Capricorn
- They form a **sextile** (60°) with orb 1°
- = **Transiting Mars sextile natal Neptune**

### Orbs (Allowable Distance)

**Tight orbs** (most powerful):
- 0-1° = **Exact** (maximum effect)
- 1-3° = **Strong** (clearly felt)

**Wide orbs** (background influence):
- 3-5° = **Moderate** (subtle)
- 5°+ = **Weak** (minimal effect)

Use tight orbs (1-3°) for practical timing.

### Applying vs Separating

**Applying**: Transit approaching exact aspect
- Builds intensity
- "Coming events cast their shadows before"
- More potent

**Separating**: Transit moving away from exact aspect
- Waning influence
- Integration phase
- Less intense

## Using the Calculator

### Basic Syntax

```bash
source venv/bin/activate
python scripts/transits.py --profile PROFILE_NAME --date DATE [OPTIONS]
```

### Show Current Transits

```bash
python scripts/transits.py --profile darren --date today
```

Output shows:
1. **Transiting positions** (where planets are now)
2. **Transiting aspects to natal** (what's being triggered)

```
================================================================================
TRANSITING POSITIONS - 2025-10-06
================================================================================

Traditional Planets
--------------------------------------------------------------------------------
Sun          Libra         13°29'33"
Moon         Aries          4°23'59"
Saturn       Pisces        27°20'57" R
...

Transit-to-Natal Aspects
--------------------------------------------------------------------------------
Mars       sextile      Natal Neptune    (orb 0.13°) (applying) *** EXACT ***
Saturn     sextile      Natal Jupiter    (orb 0.30°) (applying) *** EXACT ***
Venus      trine        Natal Mercury    (orb 0.39°) (applying) *** EXACT ***
...
```

### Show Transits in Natal Houses

```bash
python scripts/transits.py --profile darren --date today --show-natal-houses
```

Adds natal house placement:
```
Sun          Libra         13°29'33"    (Natal House 3)
Moon         Aries          4°23'59"    (Natal House 9)
Saturn       Pisces        27°20'57" R  (Natal House 8)
```

**Shows which life areas are being activated**.

### Show Only Tight Orbs (<1°)

```bash
python scripts/transits.py --profile darren --date today --tight-orbs-only
```

Filters to exact/near-exact aspects only:
```
Mars       sextile      Natal Neptune    (orb 0.13°) (applying) *** EXACT ***
Saturn     sextile      Natal Jupiter    (orb 0.30°) (applying) *** EXACT ***
Venus      trine        Natal Mercury    (orb 0.39°) (applying) *** EXACT ***
Moon       square       Natal Saturn     (orb 0.66°) (applying)
```

### Traditional Planets Only

```bash
python scripts/transits.py --profile darren --date today --traditional-only
```

Excludes Uranus, Neptune, Pluto (faster calculation, traditional focus).

### Custom Date

```bash
python scripts/transits.py --profile darren --date 2025-12-25
```

Calculate transits for any date.

### Custom Orb

```bash
python scripts/transits.py --profile darren --date today --orb 1
```

Use 1° orb (very tight) instead of default 3°.

## Interpretation

### Transit Aspects by Type

**Conjunction** (0°): **Merging, Amplification**
- Transiting planet merges with natal planet
- Pure activation of natal theme
- Most powerful transit aspect

**Example**: Transit Jupiter conjunct natal Sun
- Expansion (Jupiter) merges with core identity (Sun)
- Opportunities, growth, confidence, visibility
- Best time for self-promotion, launches, risks

**Sextile** (60°): **Opportunity, Flow**
- Harmonious activation requiring some effort
- Open doors, available resources
- Must be grasped (not automatic like trine)

**Example**: Transit Venus sextile natal Moon
- Pleasure/beauty (Venus) harmonizes with emotions (Moon)
- Social opportunities, emotional ease available
- Good time for relationships, self-care

**Square** (90°): **Challenge, Friction, Growth**
- Conflicting energies create tension
- Crisis leading to development
- Uncomfortable but productive

**Example**: Transit Mars square natal Mercury
- Action/aggression (Mars) conflicts with thought/communication (Mercury)
- Arguments, rushed decisions, mental frustration
- Must manage energy constructively

**Trine** (120°): **Ease, Luck, Flow**
- Effortless harmony
- Natural talents activated
- Benefits come easily (sometimes TOO easily - less growth)

**Example**: Transit Jupiter trine natal Venus
- Expansion (Jupiter) flows with pleasure/love (Venus)
- Romance, artistic success, financial gain
- Enjoy without effort

**Opposition** (180°): **Awareness, Polarity, Balance**
- Face-to-face with transit
- Projection, partnerships, external events
- Must integrate opposites

**Example**: Transit Saturn opposite natal Moon
- Restriction (Saturn) opposes emotions (Moon)
- Emotional distance, relationship tests, maturity demanded
- Balance responsibility with feelings

### Transit Planets (What's Transiting)

**Transiting Sun** (~1 day per degree):
- Conscious focus, vitality activation
- Highlights natal planet's themes briefly
- Annual cycle through all natal planets

**Transiting Moon** (~2.5 days per sign, ~1 day per aspect):
- Emotional trigger, mood shifts
- Very brief but noticeable
- Monthly cycle, too fast for major prediction

**Transiting Mercury** (~1-2 weeks per aspect):
- Mental activation, communication themes
- Information, decisions, short trips
- Retrogrades (3x per year) review/revise themes

**Transiting Venus** (~3-4 weeks per aspect):
- Pleasure, relationships, values, money
- Romance, art, beauty, finances activated
- Retrogrades (every 18 months) review relationships/values

**Transiting Mars** (~2-3 months per sign):
- Action, energy, conflict, desire
- Initiates, provokes, energizes
- Retrogrades (every 2 years) frustrated action

**Transiting Jupiter** (~1 year per sign):
- Expansion, opportunity, growth, optimism
- Broadens, uplifts, brings luck
- Transits each natal planet ~once per 12 years

**Transiting Saturn** (~2.5 years per sign):
- Restriction, maturity, responsibility, structure
- Tests, limits, hardens, matures
- Transits each natal planet ~once per 29 years
- **Most important transit for long-term growth**

**Transiting Uranus** (~7 years per sign):
- Sudden change, revolution, freedom, innovation
- Breaks patterns, liberates, shocks
- Generational influence, individual when aspecting personal planets

**Transiting Neptune** (~14 years per sign):
- Dissolution, spirituality, confusion, idealism
- Blurs boundaries, inspires, deceives
- Very slow, long-term spiritual evolution

**Transiting Pluto** (~12-30 years per sign):
- Transformation, death/rebirth, power, intensity
- Destroys and regenerates
- Slowest, most profound when activated

### Transit Orbs and Duration

**Fast Transits** (Sun, Moon, Mercury, Venus, Mars):
- Use 1-3° orb
- Brief duration (days to weeks)
- Immediate, concrete events

**Slow Transits** (Jupiter, Saturn, Uranus, Neptune, Pluto):
- Use 1-5° orb (some use up to 10° for outer planets)
- Long duration (months to years)
- Background themes, major life developments

**Retrograde Stations**:
- Transit hits same natal planet 3 times (direct, retrograde, direct again)
- Extended activation period
- Lesson must be learned fully

### Transits by Natal House

Transiting planets also activate natal houses they're in:

**Transit Saturn in Natal 10th**: Career tests, public responsibility
**Transit Jupiter in Natal 7th**: Relationship expansion, partnership luck
**Transit Mars in Natal 2nd**: Financial action, resource assertiveness

Use --show-natal-houses to see this.

## Transit Interpretation Examples

### Example 1: Career Breakthrough

**Transit**: Jupiter conjunct natal Sun (orb 0.5°), transit in natal 10th house

**Interpretation**:
- Jupiter (expansion, opportunity) conjuncts Sun (core identity, vitality)
- Occurring in natal 10th house (career, public life)
- **Result**: Major career opportunity, recognition, promotion likely
- **Timing**: Peak within 1-2 weeks of exact aspect
- **Action**: Put yourself forward, take calculated risks, be visible

### Example 2: Relationship Challenge

**Transit**: Saturn square natal Venus (orb 1°), transit in natal 11th, Venus in natal 5th

**Interpretation**:
- Saturn (restriction, maturity) squares Venus (love, pleasure, values)
- Saturn transiting 11th (friends, groups, hopes)
- Natal Venus in 5th (romance, creativity, children)
- **Result**: Romantic tests, delayed gratification, relationship maturation
- **Timing**: Active for 2-3 months (Saturn moves slowly)
- **Growth**: Learn what you truly value, commit seriously or release

### Example 3: Mercury Retrograde Communication

**Transit**: Mercury retrograde square natal Mercury (orb 0.3°)

**Interpretation**:
- Mercury retrograde (review, revision, delays) squares natal Mercury (communication, thinking)
- **Result**: Miscommunications, tech issues, mental review period
- **Timing**: 3-week retrograde period, especially intense during exact square
- **Action**: Review projects, reconnect with past contacts, avoid new contracts

## Integration with Other Techniques

### Transits + Profections

**Profection**: Shows which natal house is active this year
**Transit**: Shows specific timing within that year

**Example at age 36** (Profection 1st house year):
- **Profection**: 1st house activated (self, body, identity)
- **Transit Jupiter** conjunct natal Ascendant (1st house ruler)
- **Synthesis**: Self-focused year (profection) receives major expansion trigger (Jupiter transit) = identity breakthrough, confidence boost

### Transits + Solar Returns

**SR**: Shows year's themes and potential
**Transit**: Activates those themes at specific times

**Example**:
- **SR Mars** in SR 10th house (career action theme for year)
- **Transit Pluto** conjuncts SR Mars in March
- **Synthesis**: Career action theme (SR Mars 10th) intensifies and transforms in March (transit Pluto)

### Transits + Zodiacal Releasing

**ZR**: Major life chapters (Fortune/Spirit L1/L2)
**Transit**: Immediate triggers within those chapters

**Example**:
- **ZR Spirit L1**: Leo (ages 25-44) - creative leadership chapter
- **ZR Spirit L2**: Virgo (ages 35-38) - service/refinement sub-period
- **Transit Saturn** conjunct natal Sun age 36
- **Synthesis**: Creative leadership phase (Leo L1) focused on detailed service (Virgo L2) receives maturation test (Saturn-Sun) = stepping into serious leadership role through mastery of details

### Transits + Secondary Progressions

**Progressions**: Inner psychological readiness
**Transits**: Outer manifestation triggers

**Example**:
- **Progressed Sun** conjunct natal Venus (inner opening to love/beauty)
- **Transit Jupiter** conjunct natal Venus (same time)
- **Synthesis**: Inner readiness (progression) meets outer opportunity (transit) = major relationship begins

**Triple activation = highest probability for manifestation**.

## Best Practices

### Focus on Major Transits

**Most Important**:
1. **Saturn transits** (responsibility, growth through restriction)
2. **Jupiter transits** (expansion, opportunity)
3. **Outer planet transits to personal planets** (Uranus/Neptune/Pluto to Sun/Moon/Asc)

**Less Critical** (unless very tight orb):
- Fast planet transits (Sun, Moon, Mercury, Venus, Mars)
- Outer planets to outer planets (generational, not personal)

### Use Tight Orbs

- **1° or less** = Exact, maximum effect
- **3° or less** = Noticeable, usable for timing
- **5°+** = Background only

### Track Retrograde Cycles

When a planet retrogrades over a natal planet:
1. **Direct pass**: Initial activation, introduction
2. **Retrograde pass**: Internal processing, review
3. **Direct pass again**: Final integration, completion

**Example**: Transit Saturn conjunct natal Sun
- Jan: Saturn conjunct Sun direct (initial test, external pressure)
- Mar-Jul: Saturn retrograde (internal reflection on responsibility)
- Sep: Saturn conjunct Sun direct again (final maturation, external resolution)

### Prioritize by Natal Importance

Transits to your **most important natal planets** matter most:

- Chart ruler (ruler of Ascendant)
- Sun (identity), Moon (emotions)
- Planets on angles (ASC, IC, DSC, MC)
- Heavily aspected natal planets

## Traditional Sources

Transits have been used since ancient astrology:

- **Ptolemy** (2nd century): "Tetrabiblos" - transit foundations
- **Vettius Valens** (2nd century): Transit timing techniques
- **Abu Ma'shar** (9th century): Detailed transit methods
- **William Lilly** (17th century): "Christian Astrology" - practical transit use

Modern Practice:
- **Robert Hand**: "Planets in Transit" (comprehensive transit guide)
- **Howard Sasportas**: "The Gods of Change" (outer planet transits)
- **Liz Greene**: Psychological approach to transits

## Python API

Use transits in your own scripts:

```python
from scripts.transits import (
    calculate_transiting_positions,
    find_transit_aspects_to_natal,
    find_transits_in_natal_houses
)

# Get current transits
transits = calculate_transiting_positions('2025-01-15', include_modern=True)

# See where planets are
for planet in transits['planets']:
    print(f"{planet['name']}: {planet['sign']} {planet['degree']:.2f}°")

# Find aspects to natal
aspects = find_transit_aspects_to_natal(transits, 'darren', orb=3.0)

for aspect in aspects:
    if aspect['exact']:
        print(f"EXACT: {aspect['transiting_planet']} {aspect['aspect_type']} "
              f"Natal {aspect['natal_planet']} (orb {aspect['orb']:.2f}°)")

# Add natal house placements
transits = find_transits_in_natal_houses(transits, 'darren')
for planet in transits['planets']:
    print(f"{planet['name']} in natal house {planet['natal_house']}")
```

## Troubleshooting

**Q: How long does a transit last?**
A: Depends on planet's speed. Jupiter = weeks to months, Saturn = months, Pluto = years. Use orb to determine when transit is "active."

**Q: Are retrograde transits more important?**
A: Retrograde creates **triple pass** (direct-retro-direct), making the transit longer and more internalized. Not stronger, but more thorough.

**Q: Which transits should I track?**
A: **Saturn and outer planets** for major life timing, **Jupiter** for opportunities, **Mars** for action windows. Ignore very fast (Sun/Moon) unless looking at specific day.

**Q: Can transits predict specific events?**
A: Transits show **themes and timing windows**, not specific events. Saturn square Moon = emotional challenge period, but whether that's a breakup, family issue, or career-life balance struggle depends on context.

**Q: What if multiple transits happen at once?**
A: **Stacked transits** (multiple aspects simultaneously) are most powerful. Example: Jupiter trine Sun + Venus trine Moon = double harmony = excellent relationship/creative timing.

## See Also

- `PROFECTIONS_GUIDE.md` - Annual house activation
- `SOLAR_RETURNS_GUIDE.md` - Annual chart forecast
- `ZODIACAL_RELEASING_GUIDE.md` - Major life periods
- `SECONDARY_PROGRESSIONS_GUIDE.md` - Inner development
- `PROFILES_GUIDE.md` - Managing profiles

## Next Steps

After understanding transits:

1. **Check current transits** - What's activating your chart now?
2. **Identify major transits** - Saturn/outer planets to personal planets
3. **Note exact dates** - When do aspects perfect?
4. **Integrate with other techniques** - Transits + profections + progressions
5. **Track retrograde cycles** - Triple passes for extended themes

---

*Transits is the most immediate timing technique showing real-time planetary activations.*
