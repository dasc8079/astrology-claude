# Life Arc Timeline Guide

## Overview

The **Life Arc Generator** creates a unified timeline combining three traditional Hellenistic timing techniques:

1. **Annual Profections** - Yearly house activation + Lord of Year
2. **Zodiacal Releasing from Fortune** - Body/livelihood/material life chapters
3. **Zodiacal Releasing from Spirit** - Mind/career/purposeful activity chapters

This integrated view shows how all techniques align across your lifespan, revealing major life chapters, turning points, and the interplay between material circumstances (Fortune) and intentional activity (Spirit).

## Why Combine Techniques?

Each technique reveals different aspects of life timing:

- **Profections**: Annual focus, what house is activated each year
- **Fortune ZR**: Material circumstances, what happens TO you
- **Spirit ZR**: Mental/career activity, what you MAKE happen

When combined:
- See which house (profections) is active during specific ZR periods
- Understand how annual themes (profections) relate to longer chapters (ZR)
- Identify convergence points where all techniques align powerfully
- Track major transitions across multiple time scales

## Using the Generator

### Basic Syntax

```bash
source venv/bin/activate
python scripts/life_arc_generator.py --profile PROFILE_NAME [OPTIONS]
```

### Output Formats

Three output formats available via `--format` flag:

1. **detailed** (default) - Year-by-year or age snapshot
2. **summary** - Major periods overview
3. **transitions** - List of major life transitions

###  Format 1: Detailed Timeline

**Single Age Snapshot**:
```bash
python scripts/life_arc_generator.py --profile test_profile --current-age 35
```

Output shows all active techniques at age 35:
```
================================================================================
AGE 35
================================================================================

📅 ANNUAL PROFECTION:
   House 12 (Virgo)
   Lord of Year: Mercury
   Lord in: Gemini (House 9)

💰 FORTUNE (Body/Livelihood):
   L1: Aquarius (Ages 27-54)
   L2: Taurus (Ages 34.0-35.0)

🎯 SPIRIT (Mind/Career):
   L1: Leo (Ages 25-44)
   L2: Aquarius (Ages 34.2-36.7)
```

**Age Range** (year-by-year):
```bash
python scripts/life_arc_generator.py --profile test_profile --start-age 25 --end-age 30
```

Shows every year from 25 to 30 with all techniques aligned.

**Custom Interval** (every N years):
```bash
python scripts/life_arc_generator.py --profile test_profile --start-age 0 --end-age 100 --interval 5
```

Shows ages 0, 5, 10, 15, ... 100 (useful for overview of entire life).

### Format 2: Summary

Shows major period overview without year-by-year detail:

```bash
python scripts/life_arc_generator.py --profile test_profile --start-age 0 --end-age 50 --format summary
```

Output:
```
================================================================================
LIFE ARC SUMMARY: AGES 0-50
Profile: test_profile
================================================================================

💰 FORTUNE PERIODS:
   Capricorn: Ages 0-27 (27 years, Saturn time-lord)
   Aquarius: Ages 27-54 (27 years, Saturn time-lord)

🎯 SPIRIT PERIODS:
   Cancer: Ages 0-25 (25 years, Moon time-lord)
   Leo: Ages 25-44 (19 years, Sun time-lord)
   Virgo: Ages 44-64 (20 years, Mercury time-lord)

📅 PROFECTION CYCLE:
   12-year cycles within this range:
   Age 0: New 12-year cycle begins
   Age 12: New 12-year cycle begins
   Age 24: New 12-year cycle begins
   Age 36: New 12-year cycle begins
   Age 48: New 12-year cycle begins
```

Perfect for understanding major life chapters at a glance.

### Format 3: Transitions

Identifies and lists major transitions:

```bash
python scripts/life_arc_generator.py --profile test_profile --start-age 20 --end-age 35 --format transitions
```

Output:
```
================================================================================
MAJOR TRANSITIONS: AGES 20-35
================================================================================

Age 24.0: Profection Cycle Reset
  → New 12-year profection cycle begins

Age 25.0: Spirit L1 Transition
  → Spirit shifts from Cancer to Leo

Age 27.0: Fortune L1 Transition
  → Fortune shifts from Capricorn to Aquarius
```

Use this to identify critical turning points in life.

### Additional Options

**Exclude Fortune or Spirit**:
```bash
# Only Spirit + Profections
python scripts/life_arc_generator.py --profile test_profile --current-age 35 --no-fortune

# Only Fortune + Profections
python scripts/life_arc_generator.py --profile test_profile --current-age 35 --no-spirit
```

**Short age range syntax**:
```bash
python scripts/life_arc_generator.py --profile test_profile --age-range 30-50
```

Equivalent to `--start-age 30 --end-age 50`.

## Interpretation

### Reading a Year Snapshot

Example at age 27:

```
📅 ANNUAL PROFECTION:
   House 4 (Capricorn)
   Lord of Year: Saturn
   Lord in: Capricorn (House 4)

💰 FORTUNE (Body/Livelihood):
   L1: Aquarius (Ages 27-54)
   L2: Aquarius (Ages 27.0-30.5) *** PEAK ***

🎯 SPIRIT (Mind/Career):
   L1: Leo (Ages 25-44)
   L2: Virgo (Ages 26.7-29.0)
```

**Interpretation**:

**Profection** (Annual Focus):
- 4th house year (home, family, roots, endings)
- Saturn is Lord of Year (structure, responsibility, maturity)
- Saturn in own house (4th) = strong emphasis on foundations

**Fortune** (Material Circumstances):
- Starting new 27-year Aquarius period (innovation, community, progressive)
- L2 also Aquarius = PEAK PERIOD (ages 27-30.5)
- Major shift in material circumstances toward Aquarian themes
- Peak years = most intense expression of new chapter

**Spirit** (Intentional Activity):
- Still in Leo period started age 25 (creativity, leadership, performance)
- L2 in Virgo (service, analysis, refinement)
- Purposeful activity focuses on analytical/service work within creative chapter

**Synthesis**:
Age 27 marks a major transition year with:
- Saturn profection emphasizing foundations and structure
- Fortune entering 27-year Aquarius chapter AT PEAK STRENGTH (ages 27-30.5)
- Spirit L2 shifting to Virgo (practical application)
- Themes: Rebuilding foundations (4th house) with innovative approach (Aquarius Fortune) through detailed service work (Virgo Spirit)

### Peak Periods

**What They Are**:
Peak periods occur when L1 and L2 ZR are in the same sign (marked `*** PEAK ***`).

**Why They Matter**:
- Purest expression of that sign's themes
- Most intense and memorable years of the L1 period
- Often correlate with major life events
- High activity and significance

**Example**:
- Fortune L1 in Aquarius (ages 27-54)
- Fortune L2 in Aquarius (ages 27-30.5) *** PEAK ***
- **Ages 27-30.5 = Peak Aquarian fortune years**
- Material circumstances most strongly innovative/progressive

### Major Transitions

Transitions mark the boundaries between life chapters:

**ZR L1 Transitions** (Fortune or Spirit):
- Major life chapter changes
- Can last decades
- Often remembered as "before/after" this age
- Example: Fortune shifts Capricorn → Aquarius at age 27

**Profection Cycle Resets** (every 12 years):
- Ages 12, 24, 36, 48, 60, 72, 84, 96
- Return to 1st house (fresh cycle)
- Often coincide with life reassessments

**Saturn Returns** (every 29.5 years):
- Ages ~29, 58, 87
- Not directly shown but often fall during ZR transitions
- Major maturation points

### Convergence Points

Most powerful timing occurs when multiple techniques align:

**Example: Age 36**:
- Profection cycle reset (new 12-year cycle)
- Possibly within ZR peak period
- Near Saturn return (age 35.5-37)
- **Triple convergence = major life turning point**

## Python API

Use the life arc generator in your own scripts:

```python
from scripts.life_arc_generator import (
    generate_life_arc_timeline,
    get_year_snapshot,
    identify_major_transitions
)

# Generate complete timeline
timeline = generate_life_arc_timeline(
    'test_profile',
    start_age=0,
    end_age=100,
    include_fortune=True,
    include_spirit=True
)

# Get snapshot for specific age
snapshot = get_year_snapshot(timeline, 35)

print(f"Age: {snapshot['age']}")
print(f"Profection House: {snapshot['profection']['profection']['profected_house']}")
print(f"Fortune L1: {snapshot['fortune_l1']['sign']}")
print(f"Spirit L1: {snapshot['spirit_l1']['sign']}")

# Find all major transitions
transitions = identify_major_transitions(timeline)
for trans in transitions:
    print(f"Age {trans['age']}: {trans['type']}")
    print(f"  {trans['description']}")
```

## Use Cases

### Career Planning

Use Spirit ZR + profections to identify optimal career timing:

```bash
python scripts/life_arc_generator.py --profile yourname --age-range 25-65 --no-fortune --format summary
```

Shows career-related periods (Spirit) with annual focus (profections).

### Life Review

Understand past major transitions:

```bash
python scripts/life_arc_generator.py --profile yourname --start-age 0 --end-age [current-age] --format transitions
```

Lists all major shifts you've experienced.

### Future Planning

See upcoming major periods:

```bash
python scripts/life_arc_generator.py --profile yourname --start-age [current-age] --end-age 100 --interval 5
```

Overview of remaining life chapters.

### Relationship Timing

Identify periods activating 7th house (partnerships):

1. Generate timeline for your current age range
2. Look for years when profection is in 7th house
3. Note if during ZR peak periods
4. Cross-reference with partner's chart

## Advanced Interpretation

### Fortune vs Spirit Divergence

When Fortune and Spirit are in very different signs:

**Example**:
- Fortune L1: Capricorn (structure, achievement, material building)
- Spirit L1: Pisces (spirituality, dissolution, imagination)

**Interpretation**: Material circumstances (Fortune) are conservative and structured, but intentional activity (Spirit) is dissolving boundaries and seeking transcendence. Possible tension between external demands and internal calling.

### Profection Lord in ZR Sign

When annual profection's Lord of Year is located in a sign emphasized by ZR:

**Example at age 30**:
- Profection: 7th house (Aries), Lord = Mars
- Mars natal in Leo
- Spirit L1: Leo (ages 25-44)

**Interpretation**: Annual partnership focus (7th house) connects directly to Spirit chapter (Leo). Relationships this year serve the broader purpose of creative self-expression.

### Double Peak Years

When both Fortune and Spirit are in peak periods simultaneously:

**Very rare** - occurs only when:
- Fortune L1 = Fortune L2 (peak)
- Spirit L1 = Spirit L2 (peak)
- At the same time

**Interpretation**: Maximum intensity year. Both material circumstances and intentional activity at peak expression. Major life events highly likely.

## Integration with Other Tools

The life arc timeline integrates with other Mode 2 components:

**Current Stack**:
- `seed_data_generator.py` → Natal chart + Lots
- `profections_calculator.py` → Annual timing
- `zodiacal_releasing.py` → ZR from Fortune/Spirit
- `life_arc_generator.py` → **Unified timeline** (this tool)

**Future Integration** (coming in later stages):
- Transit calculator → Real-time triggers within timeline
- Life arc report → AI-generated narrative synthesis
- Visual timeline → Graphical representation

## Troubleshooting

**Q: Why are there no transitions in my age range?**
A: ZR L1 periods can last 8-27 years. Your range may fall entirely within one L1 period. Expand the range or use detailed format to see L2 transitions.

**Q: What if Fortune and Spirit tell different stories?**
A: This is normal! Fortune shows external circumstances, Spirit shows intentional activity. They often diverge and that divergence is meaningful.

**Q: How do I know which technique to prioritize?**
A: All three matter. For annual planning, prioritize profections. For life chapters, prioritize ZR. For complete picture, use all three together.

**Q: Can I generate timeline for someone else?**
A: Yes, if you have their birth data in a profile. Use `--profile [name]`.

## See Also

- `PROFECTIONS_GUIDE.md` - Annual profections details
- `ZODIACAL_RELEASING_GUIDE.md` - ZR detailed explanation
- `PROFILES_GUIDE.md` - Creating and managing profiles
- `seed_data_generator.py` - Generate natal chart with Lots

## Next Steps

After understanding your life arc timeline:

1. **Identify current periods** - Know where you are now
2. **Note upcoming transitions** - Prepare for major shifts
3. **Check peak periods** - Maximize high-intensity years
4. **Integrate with transits** - Add real-time triggers (coming soon)
5. **Generate narrative report** - AI-synthesized life story (coming soon)

---

*The life arc timeline is Stage 4 of Mode 2: Life Arc Report Generator*
