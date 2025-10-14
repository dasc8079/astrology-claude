# Annual Profections Guide

## Overview

**Annual profections** is a traditional Hellenistic timing technique that cycles through the 12 houses, activating one house per year of life. It's one of the most fundamental predictive methods in traditional astrology.

## How It Works

### The Cycle

Starting from your natal Ascendant:
- **Age 0-1**: 1st house activated (Ascendant sign)
- **Age 1-2**: 2nd house activated
- **Age 2-3**: 3rd house activated
- ...continues through all 12 houses...
- **Age 11-12**: 12th house activated
- **Age 12-13**: Returns to 1st house (cycle repeats)

Every 12 years, you return to the same house profection.

### Formula

```
Profected House = (Current Age mod 12) + 1
```

**Examples**:
- Age 24 → (24 mod 12) = 0 → House 1 (same as birth)
- Age 35 → (35 mod 12) = 11 → House 12
- Age 36 → (36 mod 12) = 0 → House 1 (new 12-year cycle)

### Lord of the Year

The **ruler** of the profected sign becomes the "Lord of the Year" or "time-lord". This planet shows the primary themes and areas of focus for that year.

**Example**:
- Age 35 profects to 12th house
- If 12th house = Virgo
- Virgo is ruled by Mercury
- **Mercury** becomes Lord of the Year
- Check Mercury's natal position to see where the year's energy flows

## Using the Calculator

### Basic Usage

Calculate profection for a single age:

```bash
source venv/bin/activate
python scripts/profections_calculator.py --profile PROFILE_NAME --age AGE
```

**Example**:
```bash
python scripts/profections_calculator.py --profile test_profile --age 35
```

**Output**:
```
============================================================
PROFECTION FOR AGE 35
============================================================

Profected House:  12 (Virgo)
Lord of Year:     Mercury

Lord of Year Natal Position:
  Location:       Gemini (House 9)
  Degree:         6.16°
  Retrograde:     False
  Dignities:      domicile, triplicity (night)

Profected House (Natal):
  Planets:        None

Interpretation:
  This year activates the 12 house (Virgo).
  Mercury becomes the time-lord, showing primary themes.
  Mercury in natal Gemini (house 9) indicates
  where this year's energy flows and what topics are emphasized.
```

### Age Range

Calculate profections for multiple years:

```bash
python scripts/profections_calculator.py --profile PROFILE_NAME --age-range START-END
```

**Example**:
```bash
python scripts/profections_calculator.py --profile test_profile --age-range 30-40
```

This shows profections for ages 30 through 40, useful for seeing patterns across a decade.

### List Profiles

See available profiles:

```bash
python scripts/profections_calculator.py --list-profiles
```

## Interpretation

### What Profections Tell You

1. **Primary Life Area**: The profected house shows which area of life is emphasized this year
2. **Time-Lord**: The Lord of the Year is the "manager" of the year's events
3. **Energy Flow**: Where the Lord of Year sits natally shows where themes manifest
4. **Natal Planets**: Planets in the profected house get activated this year

### House Meanings (Brief)

- **1st**: Self, vitality, physical body, new beginnings
- **2nd**: Money, possessions, resources, values
- **3rd**: Communication, siblings, short trips, learning
- **4th**: Home, family, roots, endings
- **5th**: Creativity, children, romance, pleasure
- **6th**: Work, health, service, daily routines
- **7th**: Partnerships, marriage, open enemies
- **8th**: Transformation, shared resources, death/rebirth
- **9th**: Philosophy, travel, higher education, meaning
- **10th**: Career, public status, achievements
- **11th**: Friends, groups, hopes, social causes
- **12th**: Solitude, spirituality, hidden matters, losses

### Reading the Output

**Profected House & Sign**: Shows which area of life is activated and its qualities

**Lord of Year**: The ruling planet becomes the "manager" for the year
- Strong dignity (domicile/exaltation) = easier year, more control
- Weak dignity (detriment/fall) = challenging year, less control
- Retrograde = internal focus, revisiting past themes

**Lord's Natal House**: Where the profected house's energy flows
- Example: 5th house profects, Lord in 10th house natally
- Interpretation: Creative projects (5th) impact career/public life (10th)

**Planets in Profected House**: Natal planets get "activated" during profection
- Personal planets (Sun, Moon, Mercury, Venus, Mars) = direct personal impact
- Social planets (Jupiter, Saturn) = broader life themes

## Example Interpretation

```
Age 35, 12th house profection (Virgo)
Lord: Mercury in Gemini, 9th house, domicile + night triplicity
```

**Interpretation**:
- **12th house year**: Focus on spirituality, solitude, behind-the-scenes work, or letting go
- **Virgo qualities**: Analytical, service-oriented, health-focused, detail work
- **Mercury as time-lord**: Communication, learning, mental activity are key
- **Mercury in Gemini (domicile)**: Very strong placement, operates smoothly
- **Mercury in 9th house**: Hidden/spiritual work (12th) connects to philosophy, teaching, or travel (9th)
- **Dignities strong**: Easier to navigate the year's challenges with skill and wisdom

**Possible manifestations**:
- Writing or researching in solitude
- Spiritual study or teaching
- Health analysis and self-care routines
- Service work that's mentally engaging
- Travel for retreat or spiritual purposes

## Integration with Transits

Profections work powerfully with transits:

1. **Priority filter**: Transits to the Lord of Year matter most
2. **House activation**: Transits to planets in the profected house are significant
3. **Transit timing**: When transiting planets enter the profected sign, themes intensify

**Example**:
- Age 35: Mercury is Lord of Year
- Saturn transits to natal Mercury → **major timing** for the year
- Without profections, this transit might seem ordinary
- With profections, it's the primary event of the year

## Python API

Use profections in your own scripts:

```python
from scripts.profections_calculator import calculate_profection_with_natal

# Calculate for specific age
profection = calculate_profection_with_natal('test_profile', 35)

print(f"Age {profection['profection']['age']}")
print(f"Profected House: {profection['profection']['profected_house']}")
print(f"Profected Sign: {profection['profection']['profected_sign']}")
print(f"Lord of Year: {profection['profection']['lord_of_year']}")
print(f"Lord's Natal House: {profection['lord_natal_position']['house']}")
```

## Traditional Sources

Annual profections comes from **Hellenistic astrology** (c. 2nd century BCE - 7th century CE):

- Described in Vettius Valens, Dorotheus, and other ancient sources
- One of the most commonly used timing techniques in traditional practice
- Chris Brennan's "Hellenistic Astrology" (2017) provides comprehensive modern treatment
- Also called "circumambulation" (walking around the chart)

## Next Steps

After understanding your current profection:

1. **Note the Lord of Year**: Track this planet's transits carefully
2. **Watch the profected house**: Transits through this sign activate the year
3. **Combine with transits**: Use profections to prioritize which transits matter most
4. **Look for returns**: Planetary returns to the Lord of Year are especially significant
5. **Check progressions**: Secondary progressions + profections = powerful combo

## See Also

- `PROFILES_GUIDE.md` - How to create and manage profiles
- `seed_data_generator.py` - Generate natal chart data
- `profile_loader.py` - Load profile data for calculations

## Future Enhancements

Planned additions:
- Zodiacal releasing (another time-lord system)
- Profected lunar returns (monthly refinement)
- Integration with transit calculator
- Visual timeline of profections across lifetime
