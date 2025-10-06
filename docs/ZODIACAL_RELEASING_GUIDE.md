# Zodiacal Releasing Guide

## Overview

**Zodiacal Releasing** (ZR) is a traditional Hellenistic timing technique that divides life into major periods based on the Lot of Fortune or Lot of Spirit. It reveals life chapters, peak periods, and critical transitions across the entire lifespan.

Unlike annual profections (which cycle yearly), ZR creates periods of varying lengths that can last from less than a year to over 27 years.

## How It Works

### Two Starting Points

ZR can be calculated from two different lots:

1. **Lot of Fortune** - Body, livelihood, fortune, material circumstances
2. **Lot of Spirit** - Mind, career, action, purposeful activity

Most astrologers calculate both to get a complete picture.

### Period Structure

**L1 Periods** (Level 1): Main life chapters
- Start from the Lot's sign
- Progress through all 12 signs in zodiacal order
- Each sign has a different period length (see table below)
- Total cycle: 228 years (covers entire life + theoretical extensions)

**L2 Periods** (Level 2): Sub-chapters within L1
- Each L1 period is subdivided into 12 L2 periods
- Also cycle through all signs in order
- Durations are proportional to parent L1 length
- Provide more detailed timing within major chapters

**L3 Periods** (Level 3): Fine detail within L2
- Further subdivisions (not currently implemented)
- Used for month-level precision

### Period Lengths (L1)

Based on traditional planetary years:

| Sign | Ruler | Years |
|------|-------|-------|
| Aries | Mars | 15 |
| Taurus | Venus | 8 |
| Gemini | Mercury | 20 |
| Cancer | Moon | 25 |
| Leo | Sun | 19 |
| Virgo | Mercury | 20 |
| Libra | Venus | 8 |
| Scorpio | Mars | 15 |
| Sagittarius | Jupiter | 12 |
| Capricorn | Saturn | 27 |
| Aquarius | Saturn | 27 |
| Pisces | Jupiter | 12 |

**Total**: 228 years for complete cycle

### Peak Periods

**Peak periods** occur when L1 and L2 are in the same sign. These are times of:
- Maximum expression of that sign's themes
- Heightened activity and significance
- Major events and turning points
- Often the most memorable years of that L1 period

**Example**:
- L1 in Aquarius (ages 27-54)
- L2 in Aquarius (ages 27-30.5)
- **Ages 27-30.5 = Peak period** for Aquarius themes

## Using the Calculator

### Basic Usage

Calculate ZR from Lot of Fortune:

```bash
source venv/bin/activate
python scripts/zodiacal_releasing.py --profile PROFILE_NAME --lot fortune --current-age AGE
```

Calculate ZR from Lot of Spirit:

```bash
python scripts/zodiacal_releasing.py --profile PROFILE_NAME --lot spirit --current-age AGE
```

### Show Specific Age Range

```bash
python scripts/zodiacal_releasing.py --profile test_profile --lot fortune --start-age 30 --end-age 50
```

### Examples

**Current period at age 35**:
```bash
python scripts/zodiacal_releasing.py --profile test_profile --lot fortune --current-age 35
```

**Output**:
```
================================================================================
ZODIACAL RELEASING FROM LOT OF FORTUNE
================================================================================

Profile: test_profile
Lot Position: Capricorn 19.09°
Birth Date: 1990-06-15
Current Age: 35.0

Current L1 Period: Aquarius (Ages 27.0-54.0)
Current L2 Period: Taurus (Ages 34.0-35.0)
```

**First 25 years from Spirit**:
```bash
python scripts/zodiacal_releasing.py --profile test_profile --lot spirit --start-age 0 --end-age 25
```

## Interpretation

### What ZR Tells You

1. **Life Chapters**: Each L1 period represents a major life phase with distinct themes
2. **Ruler Emphasis**: The planetary ruler of the period shows what's emphasized
3. **Peak Times**: When L1 and L2 match, themes intensify significantly
4. **Transitions**: Moving between L1 periods = major life shifts
5. **Duration Matters**: Longer periods (Saturn 27 years) vs shorter (Venus 8 years) have different pacing

### Fortune vs Spirit

**Lot of Fortune** (Body/Livelihood):
- Physical circumstances
- Material fortune and resources
- Body and health matters
- External conditions and environment
- "What happens to you"

**Lot of Spirit** (Mind/Career):
- Mental activity and purpose
- Career and ambition
- Intentional actions
- Achievements and goals
- "What you make happen"

Use both for complete picture:
- Fortune shows life circumstances
- Spirit shows your response and intentional activity

### Reading the Output

**L1 Period**: The main life chapter
- Sign shows the overall quality and themes
- Ruler indicates the managing planet
- Duration tells you how long this chapter lasts
- Dates give you exact timeframe

**L2 Sub-Periods**: Refinement within the chapter
- Shows how the L1 theme unfolds in stages
- Each L2 modifies the L1 expression
- Peak period (same sign) = purest expression
- Other signs = blending of themes

### Sign Themes (Brief)

- **Aries**: Initiative, independence, courage, conflict
- **Taurus**: Stability, resources, sensuality, building
- **Gemini**: Communication, learning, diversity, connections
- **Cancer**: Nurture, family, emotions, security
- **Leo**: Leadership, creativity, recognition, performance
- **Virgo**: Service, analysis, health, refinement
- **Libra**: Partnership, balance, aesthetics, diplomacy
- **Scorpio**: Transformation, depth, crisis, power
- **Sagittarius**: Expansion, philosophy, travel, meaning
- **Capricorn**: Structure, achievement, authority, mastery
- **Aquarius**: Innovation, community, ideals, detachment
- **Pisces**: Spirituality, dissolution, imagination, compassion

## Example Interpretation

```
Lot of Fortune in Capricorn
Ages 0-27: Capricorn L1 (Peak ages 0-3.25)
Ages 27-54: Aquarius L1 (Peak ages 27-30.5)
```

**Ages 0-27 (Capricorn L1)**:
- Saturn-ruled period (structure, achievement, responsibility)
- Fortune themes: Material circumstances focused on building foundations
- Peak ages 0-3.25: Earliest years establish Capricorn patterns
- Interpretation: Life circumstances emphasize responsibility, structure, hard work from birth

**Ages 27-54 (Aquarius L1)**:
- Saturn-ruled but different expression (innovation, community, ideals)
- Fortune themes: Material circumstances shift to progressive, unconventional
- Peak ages 27-30.5: Major life shift toward Aquarian themes
- Interpretation: Around 27, life circumstances become more innovative, community-focused

**Transition at age 27**:
- Major life shift from Capricorn to Aquarius
- Often correlates with significant external changes
- Saturn return (age 29) falls within peak Aquarius period
- Powerful combination of multiple timing techniques

## Integration with Other Techniques

### ZR + Profections

Use together for maximum precision:

1. **ZR** = Overall life chapter (Fortune/Spirit)
2. **Profections** = Annual focus within that chapter
3. **Transits** = Specific timing triggers

**Example at age 35**:
- ZR Fortune: Aquarius L1, Taurus L2 (material stability within innovation)
- Profection: 12th house, Mercury time-lord (hidden work, communication)
- Transits to Mercury or Aquarius/Taurus = major timing

### Traditional Practice

In Hellenistic astrology, ZR was considered one of the most important predictive techniques:

- **Chris Brennan**: Extensive treatment in "Hellenistic Astrology" (2017)
- **Ancient sources**: Vettius Valens, Dorotheus
- **Modern revival**: Robert Schmidt, Project Hindsight translations

## Python API

Use ZR in your own scripts:

```python
from scripts.zodiacal_releasing import calculate_zr_from_lot, find_current_period

# Calculate complete ZR
zr_data = calculate_zr_from_lot('test_profile', 'fortune', max_age=100)

# Access Lot info
print(f"Lot Position: {zr_data['lot_info']['sign']} {zr_data['lot_info']['degree']}°")

# Find current periods
current_l1 = find_current_period(zr_data['l1_periods'], 35.0)
current_l2 = find_current_period(zr_data['l2_periods'], 35.0)

print(f"L1: {current_l1['sign']} (ages {current_l1['start_age']}-{current_l1['end_age']})")
print(f"L2: {current_l2['sign']} (ages {current_l2['start_age']:.1f}-{current_l2['end_age']:.1f})")

if current_l2['is_peak']:
    print("*** PEAK PERIOD ***")
```

## Advanced Features

### Loosing of the Bond

When reaching the end of major periods (especially Saturn periods or the end of the Fortune/Spirit cycle), there can be significant life transitions called "loosing of the bond":

- End of long L1 periods (e.g., Saturn 27 years)
- Completion of full 228-year cycle (theoretical)
- Major releases and new chapters beginning

### Multiple Lots

While Fortune and Spirit are primary, ZR can theoretically be calculated from other lots:
- Lot of Eros (desires)
- Lot of Necessity (fate)
- Other Hermetic lots

Currently the calculator supports Fortune and Spirit as these are most traditional.

## Troubleshooting

**Q: Which Lot should I use?**
A: Calculate both! Fortune shows life circumstances, Spirit shows your intentional activity. They often tell complementary stories.

**Q: What if I'm in a very long period?**
A: Saturn periods (27 years) are the longest. The L2 sub-periods provide more granular timing within the long chapter.

**Q: Do peak periods always mean good things?**
A: Peak periods mean *intensity* of that sign's themes. Whether "good" or "challenging" depends on the sign and natal chart context.

**Q: How accurate are the dates?**
A: Dates use 365.25 days per year. For exact precision to the day, consult a professional astrologer with precise calculation methods.

## See Also

- `PROFECTIONS_GUIDE.md` - Annual profections timing
- `PROFILES_GUIDE.md` - Creating and managing profiles
- `seed_data_generator.py` - Generate natal chart with Lots

## Future Enhancements

Planned additions:
- L3 periods (month-level precision)
- Loosing of the bond detection
- Integration with transits for complete timing
- Visual timeline combining ZR + profections
- Analysis of historical events against ZR periods
