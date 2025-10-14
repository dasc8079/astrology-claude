# Secondary Progressions Guide

## Overview

**Secondary Progressions** is a traditional timing technique that advances the natal chart symbolically at a rate of **1 day = 1 year**. This method reveals inner psychological and spiritual development over the lifetime.

### Key Principle

- **Day 1 after birth** = Age 1
- **Day 30 after birth** = Age 30
- **Day 36 after birth** = Age 36

The progressed chart shows your evolving inner nature, psychological maturation, and spiritual unfoldment.

## How It Works

### The Day-for-a-Year Method

Starting from your birth moment, each day that passes represents one year of life:

1. **Calculate progressed date**: Birth date + age in days
2. **Cast chart for that date**: Using same birth time and location
3. **Compare to natal**: Progressed positions vs natal positions
4. **Interpret changes**: What's evolved, what aspects are forming

### Most Important Progressions

**1. Progressed Moon** (fastest mover):
- Moves ~12-13° per year (1° per month of life)
- Completes full zodiac cycle in ~27-28 years
- Changes sign every ~2.3 years
- Most personal and immediate timing indicator

**2. Progressed Sun**:
- Moves ~1° per year
- Changes sign every ~30 years
- Major life phase shifts

**3. Progressed Mercury/Venus** (if retrograde natally):
- Can turn direct by progression (or vice versa)
- Significant psychological shifts

**4. Progressed Angles** (ASC/MC):
- Evolve slowly but powerfully
- Represent changing life direction and identity

**5. Slower planets** (Mars, Jupiter, Saturn):
- Move very little by progression
- Aspects formed are long-lasting and significant

## Using the Calculator

### Basic Syntax

```bash
source venv/bin/activate
python scripts/secondary_progressions.py --profile PROFILE_NAME --age AGE [OPTIONS]
```

### Show Progressed Chart at Specific Age

```bash
python scripts/secondary_progressions.py --profile darren --age 36
```

Output shows all progressed planetary positions:
```
================================================================================
SECONDARY PROGRESSIONS - AGE 36.0
================================================================================
Profile: darren
Birth Date: 1988-12-27
Progressed Date: 1989-02-01 (36.0 days after birth)

                         Progressed Planetary Positions
--------------------------------------------------------------------------------
Sun          Aquarius       12°58'8"    (House 7)
Moon         Sagittarius   14°57'26"    (House 5)
Mercury      Capricorn      27°2'37" R  (House 6)
...
```

### Show Progressed-to-Natal Aspects

```bash
python scripts/secondary_progressions.py --profile darren --age 36 --show-aspects
```

Finds aspects between progressed planets and natal planets (3° orb):
```
Progressed-to-Natal Aspects
--------------------------------------------------------------------------------
Progressed Sun sextile Natal Venus (orb 0.83°)
Progressed Moon conjunction Natal Venus (orb 2.82°)
Progressed Mercury trine Natal Jupiter (orb 0.01°)
...
```

These are the most important timing indicators in progressions!

### Track Progressed Moon Through Signs

```bash
python scripts/secondary_progressions.py --profile darren --moon-cycle --age-range 0-50
```

Shows when progressed Moon changes signs:
```
Progressed Moon Cycle
--------------------------------------------------------------------------------
Ages 0-1: Leo (1 years)
Ages 1-3: Virgo (2 years)
Ages 3-6: Libra (3 years)
Ages 6-8: Scorpio (2 years)
...
```

The Moon cycle repeats approximately every 27-28 years.

## Interpretation

### Progressed Moon

**The Timer of Inner Development**

The progressed Moon is the single most important progression because it moves fastest and shows:

**Monthly Progression** (~1° per month):
- Current emotional focus
- What you're processing internally
- Short-term psychological themes

**Sign Changes** (every ~2.3 years):
- Major emotional reorientation
- New phase of inner development
- Shift in receptivity and response

**House Changes** (every ~2.3 years in whole-sign):
- New area of life becomes emotionally significant
- Where you're developing sensitivity
- Focus of inner growth

**Aspects to Natal Planets**:
- When progressed Moon aspects natal planet, that planetary theme activates
- Lasts ~1 month as it passes through orb
- Triggers events related to that natal planet

**Example Interpretation** (Progressed Moon in Sagittarius, Age 35-38):
"During ages 35-38, your emotional nature takes on Sagittarian qualities: seeking meaning, philosophical inquiry, desire for expansion and adventure. You're processing life through lens of optimism, faith, and broader perspectives."

### Progressed Sun

**The Arc of Life Purpose**

Progressed Sun moves slowly (~1° per year), showing:

**Sign Changes** (every ~30 years):
- Major life phase transitions
- Shift in core identity and purpose
- Often correlates with major life restructuring

**Aspects to Natal Planets**:
- Unfolds over several years (due to slow movement)
- Deep, sustained activation of natal themes
- Life direction shaped by that planetary principle

**Example**:
- Natal Sun in Capricorn
- Progressed Sun enters Aquarius at age 30
- **Interpretation**: "Around age 30, your core identity shifts from Capricornian achievement-focus to Aquarian innovation and community-orientation. Life purpose evolves from building structures to revolutionizing systems."

### Progressed-to-Natal Aspects

**When Progressed Planets Aspect Natal Positions**

These are the key timing indicators:

**Major Aspects** (conjunction, square, opposition, trine, sextile):
- **Conjunction**: Progressed planet merges with natal planet's theme
- **Square/Opposition**: Progressed planet challenges/activates natal planet
- **Trine/Sextile**: Progressed planet flows harmoniously with natal planet

**Orb**: Traditionally 1-3° (tight orbs more significant)

**Duration**:
- **Progressed Moon**: Active for ~1 month
- **Progressed Sun/Mercury/Venus**: Active for ~1-2 years
- **Slower planets**: Active for several years

**Example** (Progressed Sun trine Natal Jupiter):
"Progressed Sun at 15° Aquarius trines Natal Jupiter at 15° Gemini (orb 0°). This exact trine suggests a period of expansion, optimism, and philosophical development. Your core identity (progressed Sun) harmonizes with natural optimism and growth potential (natal Jupiter). Opportunities for teaching, travel, higher learning likely to manifest."

### Progressed Planets in Houses

Progressed planets changing houses (whole-sign) shows:

**New Life Areas Activated**:
- Progressed Sun entering 10th: Career/public life becomes central
- Progressed Moon entering 7th: Relationships become emotional focus
- Progressed Venus entering 5th: Creativity and pleasure emphasized

**Duration**: Depends on planet's speed and house size (whole-sign = one zodiac sign)

### Retrograde Stations

**Progressed Planet Turning Retrograde or Direct**

Very rare and significant:

- **Mercury/Venus** most likely to station (if natal retrograde)
- Represents major psychological reorientation
- Shift from internal to external expression (or vice versa)

**Example**: Natal Mercury retrograde turns direct by progression at age 40
- "Lifelong internal processing style becomes more externally communicative"
- Communication skills mature and externalize

## Integration with Other Techniques

### Progressions + Profections

Use together for annual timing:

**Profection**: Shows which house is activated this year (external focus)
**Progression**: Shows internal development during that activation

**Example at age 36**:
- **Profection**: 1st house year (self, body, new beginnings)
- **Progressed Moon**: Sagittarius in 5th house
- **Synthesis**: "External focus on self-renewal (1st house profection) while internal emotional development centers on creative expression and philosophical joy (progressed Moon Sagittarius 5th)"

### Progressions + Zodiacal Releasing

**ZR**: Life chapters and major periods (Fortune/Spirit)
**Progressions**: Inner development within those chapters

**Example**:
- **ZR Fortune**: Aquarius L1 (ages 27-54) - innovative material circumstances
- **Progressed Sun**: Enters Aquarius at age 30
- **Synthesis**: "External Aquarian chapter (ZR) reinforced by internal Aquarian development (progressed Sun). Maximum alignment of inner and outer life toward progressive ideals."

### Progressions + Transits

**Transits**: Immediate triggers and events
**Progressions**: Background psychological readiness

**Example**:
- **Progressed Moon** conjunct natal Venus (ages 35-36)
- **Transit Jupiter** conjunct natal Venus (single pass during that year)
- **Synthesis**: "Inner emotional opening to love/pleasure (progressed Moon-Venus) meets outer opportunity for relationship/beauty (transit Jupiter-Venus). Triple activation = high probability of significant relationship development."

## Traditional Sources

Secondary progressions were used extensively in medieval and Renaissance astrology:

- **Ptolemy** (2nd century): Referenced symbolic time progressions
- **Al-Biruni** (11th century): Day-for-a-year methods
- **William Lilly** (17th century): Used progressions alongside primary directions
- **Sepharial** (19th-20th century): Popularized secondary progressions in modern astrology

Modern Revival:
- **Noel Tyl**: Extensive work on progressed Moon cycles
- **Robert Hand**: "Planets in Transit" includes progression techniques
- **Steven Forrest**: "The Inner Sky" - evolutionary astrology via progressions

## Python API

Use secondary progressions in your own scripts:

```python
from scripts.secondary_progressions import (
    calculate_progressed_positions,
    find_progressed_aspects_to_natal,
    track_progressed_moon_cycle
)

# Get progressed positions at age 36
progressed = calculate_progressed_positions('darren', 36)

# Access progressed planets
for planet in progressed['progressed_planets']:
    print(f"{planet['name']}: {planet['sign']} {planet['degree']:.2f}°")

# Find aspects to natal chart
aspects = find_progressed_aspects_to_natal('darren', 36, orb=3.0)
for aspect in aspects:
    print(f"Progressed {aspect['progressed_planet']} {aspect['aspect_type']} "
          f"Natal {aspect['natal_planet']}")

# Track Moon cycle through life
moon_cycles = track_progressed_moon_cycle('darren', start_age=0, end_age=100)
for cycle in moon_cycles:
    print(f"Ages {cycle['start_age']}-{cycle['end_age']}: {cycle['sign']}")
```

## Best Practices

### Focus on the Big Three

1. **Progressed Moon** - Most important, fastest, most personal
2. **Progressed Sun** - Life phase and core identity evolution
3. **Progressed-to-Natal Aspects** - Specific timing triggers

Don't get lost in minor details - slower planets barely move.

### Use Tight Orbs

- **1° orb** for exactitude (most powerful)
- **3° orb** for broader context
- Avoid wide orbs (5°+) - dilutes meaning

### Progressed Moon is the Annual Timer

The progressed Moon:
- Changes sign every ~2.3 years
- Moves 1° per month
- Use as your "progressed profection" - shows the year's inner theme

### Combine with Transits

Progressions show **readiness**, transits show **activation**.

When progressed aspect forms AND transit hits the same point = maximum effect.

## Troubleshooting

**Q: Why do slower planets barely move?**
A: At 1 day = 1 year, even 40 years of life = only 40 days of planetary motion. Mars moves ~0.5° per day, so 40 years = only 20° of motion. This is normal.

**Q: Which is more important: progressions or transits?**
A: Both matter. Progressions = inner development, transits = outer events. Use together.

**Q: How accurate are the dates?**
A: Progressions are symbolic (1 day = 1 year), not literal. The positions are astronomically accurate for the progressed date.

**Q: Can I use progressions for prediction?**
A: Yes, but they show **psychological readiness** for events, not the events themselves. Combine with transits for event timing.

## See Also

- `PROFECTIONS_GUIDE.md` - Annual profections timing
- `ZODIACAL_RELEASING_GUIDE.md` - ZR major life periods
- `LIFE_ARC_GUIDE.md` - Unified timeline integration
- `PROFILES_GUIDE.md` - Creating and managing profiles

## Next Steps

After understanding secondary progressions:

1. **Calculate your current progressions** - Know where you are now
2. **Track your progressed Moon** - Understand your ~27-year cycle
3. **Find progressed-to-natal aspects** - See what's activating
4. **Integrate with profections and ZR** - Complete timing picture
5. **Add transits** - Real-time triggers (coming in Mode 3)

---

*Secondary Progressions is a core component of the Life Arc timing system.*
