# Solar Returns Guide

## Overview

A **Solar Return** is a chart cast for the exact moment the Sun returns to its natal position each year. This occurs around your birthday (within ±2 days) and describes the themes, events, and developments for the year ahead.

The solar return chart is active from one birthday to the next, providing a detailed "forecast" for that solar year.

## Key Principle

- **Every year**, the Sun completes its orbit and returns to the exact degree/minute/second it occupied at birth
- This moment (which varies slightly year-to-year) is the **solar return**
- A chart cast for this moment reveals the year's potential

### Example

- Natal Sun: 5°56' Capricorn
- Age 36 solar return: Sun returns to exactly 5°56' Capricorn on December 27, 2024 at 5:15 AM

## How It Works

### Calculating the Solar Return

1. **Find natal Sun position** (e.g., 5°56'20" Capricorn)
2. **Determine return year** (birth year + age)
3. **Calculate exact moment** Sun reaches that position in return year
4. **Cast chart** for that moment at:
   - **Natal location** (traditional method)
   - **Current location** (relocation/locality method - advanced)

### The Solar Return Chart

The SR chart includes:

- **SR Ascendant**: How the year presents itself, your approach
- **SR MC**: Public life, career direction for the year
- **SR Planets in SR Houses**: What areas are emphasized
- **SR Planets in Natal Houses**: How SR energy manifests in your life
- **SR Planets aspecting Natal Planets**: Specific activation points

## Using the Calculator

### Basic Syntax

```bash
source venv/bin/activate
python scripts/solar_returns.py --profile PROFILE_NAME --age AGE [OPTIONS]
```

### Calculate Solar Return for Age

```bash
python scripts/solar_returns.py --profile darren --age 36
```

Output:
```
================================================================================
SOLAR RETURN CHART - AGE 36 (2024)
================================================================================
Profile: darren
Solar Return: 2024-12-27 05:15:00
Location: Masan, South Korea

Chart Framework
--------------------------------------------------------------------------------
Ascendant:  Taurus       18°45'14"
Midheaven:  Aquarius     1°17'10"

Solar Return Planetary Positions
--------------------------------------------------------------------------------
Sun          Capricorn      5°56'20"    (SR House 9)
Moon         Scorpio       22°34'43"    (SR House 7)
Mercury      Sagittarius    14°4'49"    (SR House 8)
...
```

### Show SR Planets in Natal Houses

```bash
python scripts/solar_returns.py --profile darren --age 36 --show-natal-houses
```

This overlays SR planets onto your natal chart:
```
Sun          Capricorn      5°56'20"    (SR House 9, Natal House 6)
Moon         Scorpio       22°34'43"    (SR House 7, Natal House 4)
...
```

**SR House**: Where it is in the SR chart
**Natal House**: Where it falls in your natal chart

### Show SR-to-Natal Aspects

```bash
python scripts/solar_returns.py --profile darren --age 36 --show-aspects
```

Finds aspects between SR planets and natal planets:
```
Solar Return to Natal Aspects
--------------------------------------------------------------------------------
SR Sun conjunction Natal Sun (orb 0.00°)
SR Sun conjunction Natal Saturn (orb 0.88°)
SR Moon square Natal Moon (orb 2.88°)
SR Mercury conjunction Natal Venus (orb 1.94°)
...
```

**Most important aspects**: These show what gets activated during the year.

### Calculate by Calendar Year

```bash
python scripts/solar_returns.py --profile darren --year 2025
```

Alternative to using age - directly specify year.

## Interpretation

### SR Ascendant (Rising Sign)

The SR Ascendant shows **how you approach the year** and the **mask you wear**.

**Examples**:

- **SR ASC in Aries**: Assertive, pioneering year; take initiative
- **SR ASC in Taurus**: Stable, grounding year; build resources
- **SR ASC in Cancer**: Emotional, nurturing year; focus on home/family
- **SR ASC in Capricorn**: Structured, ambitious year; career focus

**Same as Natal ASC**: When SR ASC matches natal ASC (rare), the year strongly resonates with your core identity.

### SR Midheaven (MC)

The SR MC shows **career and public life direction** for the year.

**Examples**:

- **SR MC in Aries**: Career initiatives, leadership visibility
- **SR MC in Libra**: Partnership-based professional growth
- **SR MC in Capricorn**: Authority, recognition, achievement

### SR Planets in SR Houses

Shows **what areas are emphasized** during the year.

**Key Placements**:

**SR Sun in 1st**: Self-focused year, identity development, visibility
**SR Sun in 7th**: Partnership year, relationships central
**SR Sun in 10th**: Career peak year, public recognition

**SR Moon in 4th**: Emotional focus on home, family matters
**SR Moon in 10th**: Public emotional exposure, career-family balance

**SR Venus in 5th**: Pleasure, creativity, romance emphasized
**SR Venus in 2nd**: Financial improvement, values clarification

**SR Mars in 1st**: High energy, assertiveness, potential conflict
**SR Mars in 6th**: Work intensity, health focus

### SR Planets in Natal Houses

**Critical for practical interpretation** - shows where SR energy manifests in your actual life.

**Example**:
- **SR Mars in SR 4th house** = Domestic activity in the SR chart
- **SR Mars in Natal 10th house** = But actually manifests in career (if Mars falls in natal 10th)

**Always check both**: SR house gives the theme, natal house gives the arena.

### SR-to-Natal Aspects

**The most important SR technique** - aspects between SR planets and natal planets show what gets triggered.

**Conjunctions** (0°):
- **SR Sun conjunct Natal Venus**: Year of beauty, pleasure, relationships (Venus themes activated)
- **SR Mars conjunct Natal Mercury**: Year of mental intensity, assertive communication

**Squares** (90°):
- **SR Moon square Natal Sun**: Emotional challenges to identity, internal tension
- **SR Saturn square Natal Venus**: Relationship restrictions, delayed gratification

**Trines** (120°):
- **SR Jupiter trine Natal Sun**: Expansive, fortunate year for self-expression
- **SR Venus trine Natal Moon**: Emotional harmony, pleasurable experiences

**Oppositions** (180°):
- **SR Mars opposite Natal Mars**: Conflict year, competing drives
- **SR Venus opposite Natal Saturn**: Tension between desire and restriction

### SR Planets Repeating Natal Positions

**Powerful Years**:

**SR Sun conjunct Natal Sun** (every year by definition):
- Always present, but note the SR house it falls in

**SR Moon conjunct Natal Moon**:
- Emotional reset, return to natal emotional pattern
- Occurs roughly every 19 years (Metonic cycle)

**SR Venus conjunct Natal Venus**:
- ~8-year cycle
- Year of renewed values, relationship patterns

**SR Mars conjunct Natal Mars**:
- ~2-year cycle
- Peak energy, assertiveness matching natal drive

**SR Jupiter conjunct Natal Jupiter**:
- ~12-year cycle (Jupiter return)
- Expansion, philosophy, growth alignment

**SR Saturn conjunct Natal Saturn**:
- ~29.5-year cycle (Saturn return)
- Maturation, responsibility, life restructuring

### Angular Planets (SR 1st, 4th, 7th, 10th)

Planets on or near SR angles are **emphasized all year**.

**Examples**:
- **SR Saturn on ASC**: Serious, mature year; increased responsibility
- **SR Jupiter on MC**: Career expansion, public recognition
- **SR Moon on IC (4th)**: Deep emotional processing, family focus
- **SR Mars on DSC (7th)**: Partnership conflict or assertive relating

## Traditional Sources

Solar returns have ancient roots:

- **Masha'allah** (8th century): "On Solar Revolutions"
- **Abu Ma'shar** (9th century): Extensive solar return techniques
- **Bonatti** (13th century): "Liber Astronomiae" - detailed SR interpretation
- **Morin** (17th century): SR as primary predictive method

Modern Practice:
- **Robert Hand**: "Planets in Transit" (includes SR methods)
- **Mary Fortier Shea**: "Planets in Solar Returns"
- **Judith Hill**: Traditional techniques in modern practice

## Integration with Other Techniques

### SR + Profections

**Profection**: Annual house activation (rotating 12-year cycle)
**Solar Return**: Actual year's chart

Use together:
1. **Profection** shows which natal house is active
2. **SR** shows how that activation manifests in detail

**Example at age 36**:
- **Profection**: 1st house year (self, body, identity)
- **SR ASC**: Taurus (grounded, stable approach)
- **SR Mars in SR 4th**: Domestic action
- **Synthesis**: Self-focused year (profection 1st) with stable approach (SR Taurus ASC) emphasizing home projects (SR Mars 4th)

### SR + Zodiacal Releasing

**ZR**: Major life chapters (Fortune/Spirit L1/L2)
**SR**: Annual variation within those chapters

**Example**:
- **ZR Fortune L1**: Gemini (ages 23-43) - communication, learning chapter
- **ZR Spirit L1**: Capricorn (ages 12-39) - achievement, structure chapter
- **SR at age 36**: SR Sun in 10th, SR Saturn rising
- **Synthesis**: Career achievement themes (Capricorn Spirit + SR Sun 10th) within broader learning period (Gemini Fortune)

### SR + Secondary Progressions

**Progressions**: Inner psychological development
**SR**: Outer circumstances and events

**Example**:
- **Progressed Sun**: 12° Aquarius (innovative identity phase)
- **SR Sun**: Falls in natal 6th house
- **SR Mercury** conjunct Progressed Sun
- **Synthesis**: Inner innovation (prog Sun Aquarius) manifests through work/service (SR Sun natal 6th) with mental activation (SR Mercury)

### SR + Transits

**SR**: Year's potential and themes
**Transits**: Timing triggers within that year

**Example**:
- **SR Moon** in SR 5th house
- **Transit Jupiter** conjuncts SR Moon in March
- **Result**: Creative/romantic peak in March, activating year's 5th house emphasis

## Advanced Techniques

### Relocation Solar Returns

Cast SR for **current location** instead of natal location:

- Different ASC/MC than natal location SR
- Emphasizes different houses
- Used to "choose" year's themes by traveling for birthday

**Example**:
- Natal location SR: ASC Aries (assertive year)
- NYC relocation SR: ASC Libra (partnership year)
- **Travel to NYC for birthday = activate Libra themes instead**

*(Note: Full relocation not yet implemented in calculator)*

### Progressed Solar Returns

Progressions applied to SR chart:
- Progress SR chart through the year
- Shows sub-annual timing

### SR Moon Phases

SR Moon's phase (to SR Sun):
- New Moon SR: New beginnings, seed-planting
- Full Moon SR: Culmination, revelation
- Quarter Moons SR: Crisis, action required

### Prenatal Solar Returns

SR for the year **before birth**:
- Shows conditions leading to birth
- Pre-life karmic themes

## Python API

Use solar returns in your own scripts:

```python
from scripts.solar_returns import (
    calculate_solar_return_chart,
    find_sr_to_natal_aspects
)

# Calculate SR for age 36
sr_chart = calculate_solar_return_chart('darren', age=36)

# Access SR data
print(f"SR ASC: {sr_chart['ascendant']['sign']} {sr_chart['ascendant']['dms']}")
print(f"SR MC: {sr_chart['midheaven']['sign']}")

# SR planets
for planet in sr_chart['planets']:
    print(f"{planet['name']}: {planet['sign']} in SR House {planet['sr_house']}, "
          f"Natal House {planet['natal_house']}")

# Find aspects to natal
aspects = find_sr_to_natal_aspects(sr_chart, 'darren', orb=3.0)
for aspect in aspects:
    print(f"SR {aspect['sr_planet']} {aspect['aspect_type']} "
          f"Natal {aspect['natal_planet']}")
```

## Best Practices

### Focus on SR-to-Natal Aspects

These are **the most important** timing indicators:
- Which natal planets get activated this year?
- What themes (planets) are emphasized?

### Check Angular Planets

Planets on SR angles (ASC, IC, DSC, MC) dominate the year.

### Overlay on Natal Chart

Always check where SR planets fall in **natal houses** - this shows real-life manifestation.

### Integrate with Profections

SR fills in the details of the profection year.

### Use Tight Orbs

- 1-3° for aspects
- Tighter = stronger activation

## Troubleshooting

**Q: Why isn't my SR on my exact birthday?**
A: The Sun's return varies ±2 days around the birthday due to leap years and Earth's elliptical orbit.

**Q: Should I use natal or current location?**
A: Traditional: natal location. Modern: some use current location for "relocation" SRs. Start with natal.

**Q: How long is an SR active?**
A: From one solar return to the next (birthday to birthday, approximately 1 year).

**Q: Which is more important: SR houses or natal houses?**
A: Both! SR houses show the theme, natal houses show where it plays out.

**Q: Can SR predict specific events?**
A: SR shows potential and themes. Combine with transits for specific timing.

## See Also

- `PROFECTIONS_GUIDE.md` - Annual profections
- `ZODIACAL_RELEASING_GUIDE.md` - Major life periods
- `SECONDARY_PROGRESSIONS_GUIDE.md` - Inner development
- `PROFILES_GUIDE.md` - Managing profiles

## Next Steps

After calculating your solar return:

1. **Identify SR ASC/MC** - Overall approach and direction
2. **Note angular planets** - Dominant themes
3. **Check SR-to-natal aspects** - What gets activated
4. **Overlay on natal houses** - Where themes manifest
5. **Integrate with profections/ZR** - Complete picture
6. **Track transits to SR** - Month-by-month timing

---

*Solar Returns is a core component of the annual timing system.*
