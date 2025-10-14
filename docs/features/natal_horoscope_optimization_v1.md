# Natal Data Model Optimization Specification

**Version**: 1.1
**Created**: October 12, 2025
**Updated**: October 12, 2025 (After Planning Session)
**Purpose**: Define optimal natal interpretation data model with prioritized techniques and settings integration
**Status**: Design Complete - Ready for Implementation
**Note**: Reflects user decisions from planning session, implementation difficulty analysis, and default mode specification

---

## Executive Summary

This document specifies the optimal natal data model for the astrology application, prioritizing traditional Hellenistic techniques. **Current focus: DEFAULT MODE ONLY** with on/off switches for techniques. Settings control WHICH techniques to include, not output style modulation (depth levels are future enhancement).

**Key Findings**:
1. **House Rulers** are the #1 PRIMARY technique (need deeper agent integration)
2. **Sect** is foundational but underutilized (must filter ALL planet interpretations through sect lens)
3. **Lot Selection** - DEFAULT MODE: 4 lots (Fortune, Spirit, Eros, Necessity); 8 additional lots for Life Arc Report
4. **New techniques approved**: Antiscia (EASY, HIGH value), Fixed Stars (EASY, HIGH value), Triplicity (ZERO effort - already calculated)
5. **Accessible synthesis language IS the default style** (not an optional "psychological overlay")
6. **Settings = on/off switches** for techniques; depth levels = future architectural vision

---

## I. Data Point Priority Classification

### PRIMARY Techniques (Always Calculate, Always Interpret)

These are the core of traditional Hellenistic interpretation. NEVER skip these.

**1. House Rulers** (Highest Priority)
- **Why PRIMARY**: Shows HOW each life area manifests (the path, not just the terrain)
- **Current Status**: Calculated correctly, needs deeper agent integration
- **Optimization**: Must mention THREE things for every life area: what's IN house, WHO RULES, how ruler CONNECTS
- **Interpretive Weight**: 30% of synthesis content
- **Example**: "Your career path (10th ruler Venus in 5th) finds expression through creative joy and children"
- **User Decision**: MUST be deeply integrated - always mention IN/RULE/CONNECT

**2. Sect Determination** (Foundational - CRITICAL)
- **Why PRIMARY**: Changes benefic/malefic status, affects ALL planet interpretations
- **Current Status**: Calculated correctly, severely underutilized in interpretation
- **Optimization**: Filter EVERY planet interpretation through sect lens - this is non-negotiable
- **Interpretive Weight**: Affects 100% of planetary interpretations (modifier, not standalone content)
- **Example**: Day chart with Mars in Aries - "Mars, contrary to sect in your day chart, brings more reactive energy than constructive initiative"
- **User Decision**: Emphasize MORE - sect is the interpretive lens for EVERYTHING

**3. Essential Dignities** (Traditional Foundation)
- **Why PRIMARY**: Core traditional technique showing planetary strength
- **Current Status**: Calculated correctly (domicile, exaltation, detriment, fall, triplicity)
- **Optimization**: USE triplicity (already calculated), SKIP bounds/decans for now (low value for natal)
- **Interpretive Weight**: 15% of synthesis content (strength assessments)
- **Include**: Domicile, exaltation, detriment, fall, triplicity (by sect)
- **Skip for now**: Bounds/terms (medium effort, low value), Decans/faces (easy effort, low value)
- **User Decision**: Use triplicity (zero effort), defer bounds/decans (low natal value)

**4. Classical Aspects** (Traditional Foundation)
- **Why PRIMARY**: Core interaction patterns between planets
- **Current Status**: Calculated correctly (conjunction, sextile, square, trine, opposition, ±8° orbs)
- **Optimization**: Perfect as-is, maintain traditional aspects only
- **Interpretive Weight**: 20% of synthesis content (relationship dynamics)
- **Never Include**: Harmonic aspects, midpoints (not traditional)

**5. Angles & Angularity** (Accidental Dignity)
- **Why PRIMARY**: Angular planets (houses 1, 4, 7, 10) carry extra weight
- **Current Status**: Calculated correctly (ASC/MC/DSC/IC + planetary aspects to angles)
- **Optimization**: Continue emphasizing angular placements
- **Interpretive Weight**: 10% of synthesis content (strength modifier)
- **Include**: Aspects to angles (±8° orbs)

**6. Lunar Nodes** (Evolutionary Path)
- **Why PRIMARY**: Shows growth direction (North Node) and release patterns (South Node)
- **Current Status**: Calculated correctly
- **Optimization**: Integrate naturally into Life Path & Purpose section
- **Interpretive Weight**: 5% of synthesis content (one dedicated paragraph)

**7. Antiscia** (Mirror Degrees - NEW)
- **Why PRIMARY**: Traditional technique showing hidden connections between planets
- **Implementation Difficulty**: EASY (~30 lines of code)
- **Formula**: Mirror across 0° Cancer/Capricorn axis (e.g., 15° Aries antiscion = 15° Virgo)
- **Interpretive Value**: HIGH when present (powerful traditional technique)
- **Interpretive Weight**: 2-3% of synthesis content (when present)
- **User Decision**: INCLUDE - easy implementation, high traditional value

**8. Fixed Stars** (Major Conjunctions - NEW)
- **Why PRIMARY**: Dramatic effects when conjunct planets/angles
- **Implementation Difficulty**: EASY (~50 lines, Swiss Ephemeris has built-in `swe.fixstar_ut()`)
- **Major 5**: Regulus, Spica, Algol, Antares, Aldebaran
- **Orb**: ±1° conjunction only (tight orbs)
- **Interpretive Value**: HIGH when present (rare but powerful)
- **Interpretive Weight**: 3% of synthesis content (when present)
- **User Decision**: INCLUDE - easy implementation, high value when present

**9. Triplicity** (Elemental Dignity - NEW)
- **Why PRIMARY**: Shows elemental comfort/ease
- **Implementation Difficulty**: ZERO (already calculated in seed_data_generator.py lines 81-93)
- **Current Status**: Calculated but underutilized
- **Interpretive Value**: MODERATE (elemental layer to dignity assessment)
- **Interpretive Weight**: Woven into dignity assessments (not standalone)
- **User Decision**: USE IT - already calculated, zero effort, moderate value

### SECONDARY Techniques (Calculate, Interpret Based on Settings)

These add depth but aren't essential for basic interpretation. Users should be able to toggle these.

**7. Lots** (Hellenistic Core - DEFAULT MODE: 4 LOTS)
- **Why SECONDARY**: Traditional technique, essential but not as foundational as house rulers/sect
- **Current Status**: 12 lots calculated (excessive for natal)
- **DEFAULT MODE** (User Decision): 4 lots - Fortune, Spirit, Eros, Necessity
- **Interpretive Weight**: 5-8% of synthesis content (Fortune = resources/body, Spirit = action/career, Eros = desire/attraction, Necessity = constraints/fate)
- **User Decision**: "Let's use those 4 lots" for DEFAULT MODE
- **Remaining 8 lots** (Marriage, Children, Siblings, Nemesis, Courage, Victory, Basis, Exaltation): More relevant for Life Arc Report (Mode 2)
- **Note**: These 8 additional lots have higher value for life timeline interpretation than natal snapshot

**8. Receptions** (Traditional Technique - INCLUDE)
- **Why SECONDARY**: Powerful when present, but only ~20% of charts have significant receptions
- **Current Status**: Calculated correctly (mutual reception by domicile/exaltation)
- **Optimization**: Calculate always, emphasize when significant (especially mutual reception)
- **Interpretive Weight**: 2-3% of synthesis content (when present)
- **User Decision**: INCLUDE - ensure mutual reception is emphasized in default mode
- **Settings**: `include_receptions: true` (default on)

**9. Bonification** (Benefic Support)
- **Why SECONDARY**: Mitigates malefic difficulties, important for malefic-heavy charts
- **Current Status**: Calculated correctly (Venus/Jupiter supporting Mars/Saturn)
- **Optimization**: Calculate always, mention only when present
- **Interpretive Weight**: 2% of synthesis content (when present)
- **Settings**: `include_bonification: true` (default on)

**10. Chart Patterns** (Modern Technique)
- **Why SECONDARY**: Useful pattern recognition, but not traditional
- **Current Status**: Calculated correctly (stelliums, elemental/modality balance)
- **Optimization**: Continue current approach
- **Interpretive Weight**: 3% of synthesis content (overview section)
- **Include**: Stelliums (3+ planets in sign/house), element/modality balance
- **Settings**: Always calculate (foundational overview)

**11. Bounds & Decans** (Minor Dignities - DEFERRED)
- **Why SECONDARY**: Add texture, but low interpretive value for natal work
- **Current Status**: Can be calculated
- **Optimization**: SKIP for now (see user decisions below)
- **Interpretive Weight**: <1% of synthesis content
- **User Decision - Bounds/Terms**: Medium effort, low value → SKIP for default mode (defer to future)
- **User Decision - Decans/Faces**: Easy effort, low value → SKIP for default mode (defer to future)
- **Note**: Triplicity is already calculated and WILL be used (see PRIMARY techniques above)
- **Settings**: `include_bounds_detailed: false` (default off), `include_decans_detailed: false` (default off)

### OPTIONAL Techniques (Calculate Only When Enabled)

These are modern methods or advanced traditional techniques. Performance-conscious users may disable.

**12. Modern Planets** (Uranus, Neptune, Pluto)
- **Why OPTIONAL**: Not traditional, but add psychological depth
- **Current Status**: Calculated correctly, used as secondary context
- **Optimization**: Perfect approach - keep as secondary psychological overlay
- **Interpretive Weight**: 8% of synthesis content (psychological context only)
- **Settings**: `include_modern_planets: true` (default on, but clearly labeled as modern)
- **Usage**: Never use for house rulership, always secondary to traditional planets

**13. Chiron** (Modern Psychological)
- **Why OPTIONAL**: Wounded healer archetype, powerful but not traditional
- **Current Status**: Calculated when enabled
- **Optimization**: Good as optional addition
- **Interpretive Weight**: 2% of synthesis content (one paragraph when enabled)
- **Settings**: `include_chiron: true` (default off)

**14. Black Moon Lilith** (Modern Psychological)
- **Why OPTIONAL**: Shadow feminine, primal instincts
- **Current Status**: Calculated when enabled
- **Optimization**: Good as optional addition
- **Settings**: `include_lilith: true` (default off)
- **Interpretive Weight**: 2% of synthesis content (one paragraph when enabled)

**15. Vertex** (Mathematical Point)
- **Why OPTIONAL**: Fated encounters, less reliable than traditional techniques
- **Current Status**: Calculated when enabled
- **Optimization**: Keep as niche option
- **Settings**: `include_vertex: false` (default off)
- **Interpretive Weight**: <1% of synthesis content

**16. Output Style Modulation** (REMOVED FROM SETTINGS)
- **User Decision**: "Remove the psychological overlay, that is the default way language we are using"
- **Clarification**: The accessible, therapeutic synthesis language IS the default style (not an optional overlay)
- **Current Status**: Agents write in accessible, archetypal language by default
- **No Setting Needed**: This is not a toggled feature - it's how the synthesis is written
- **Future Enhancement**: Output style modulation (formal vs. accessible, brief vs. detailed) is part of depth levels (see Section VII - FUTURE FEATURE)
- **Settings**: NO SETTING (this is the writing style, not a technique toggle)

---

## II. Approved New Techniques (From Planning Session)

**IMPLEMENTATION STATUS**: These techniques have been approved for PRIMARY inclusion based on implementation difficulty analysis.

### Antiscia (Mirror Degrees) - APPROVED ✅

- **Definition**: Mirror points across 0° Cancer/Capricorn axis (e.g., 15° Aries antiscion = 15° Virgo)
- **Traditional Technique**: Used in Hellenistic and Medieval astrology
- **Interpretive Value**: HIGH - shows hidden connections between planets
- **Implementation Difficulty**: EASY (~30 lines of code)
- **Implementation Details**:
  - Formula: 180° - longitude (for signs Aries-Gemini, Cancer-Virgo)
  - Or: longitude (for signs Libra-Sagittarius, Capricorn-Pisces, flipped)
  - Calculate antiscion for each planet, check for antiscia conjunctions (±1° orb)
- **User Decision**: INCLUDE as PRIMARY technique
- **Settings**: `include_antiscia: true` (default on in default mode)
- **Interpretive Weight**: 2-3% when present
- **Status**: MOVED from "missing techniques" to PRIMARY (Section I)

### Fixed Stars (Major 5) - APPROVED ✅

- **Definition**: Conjunction of planets/angles to major fixed stars
- **Major 5**: Regulus (29° Leo), Spica (23° Libra), Algol (26° Taurus), Antares (9° Sagittarius), Aldebaran (9° Gemini)
- **Traditional Technique**: Medieval/Renaissance staple
- **Interpretive Value**: HIGH when present (rare but powerful - dramatic effects)
- **Implementation Difficulty**: EASY (~50 lines, Swiss Ephemeris has built-in `swe.fixstar_ut()`)
- **Implementation Details**:
  - Call `swe.fixstar_ut(star_name, jd)` for each of Major 5
  - Check conjunctions with natal planets/angles (±1° orb only)
  - Only report when conjunction present (most charts have none)
- **User Decision**: "If they are really easy include it" → INCLUDE as PRIMARY technique
- **Settings**: `include_fixed_stars: true` (default on in default mode)
- **Interpretive Weight**: 3% when present
- **Status**: MOVED from "missing techniques" to PRIMARY (Section I)

### Triplicity (Elemental Dignity) - APPROVED ✅

- **Definition**: Elemental rulership showing comfort/ease in element
- **Traditional Technique**: Core dignity system (after domicile/exaltation)
- **Interpretive Value**: MODERATE - adds elemental layer to dignity assessment
- **Implementation Difficulty**: ZERO (already calculated in seed_data_generator.py lines 81-93)
- **Current Status**: Calculated but underutilized in interpretation
- **User Decision**: USE IT - zero effort, moderate value
- **Settings**: Always included (PRIMARY technique)
- **Interpretive Weight**: Woven into dignity assessments (not standalone content)
- **Status**: MOVED from "underutilized" to PRIMARY (Section I)

### Deferred Techniques (Low Value for Natal)

**Planetary Hours** - LOW PRIORITY
- **Definition**: Planetary hour of birth (Chaldean order)
- **Interpretive Value**: Minor for natal work (more relevant for horary/electional/timing)
- **Implementation Effort**: Low (simple calculation)
- **Decision**: DEFER - low natal value, better for Mode 2/3 (timing techniques)
- **Settings**: `include_planetary_hours: false` (default off)

**Bounds/Terms** - DEFERRED
- **Implementation Effort**: Medium (requires bounds tables by system)
- **Interpretive Value**: Low for natal work (more relevant for profections/directions)
- **User Decision**: SKIP for default mode (medium effort, low value)
- **Future**: May add for advanced users or Mode 2 (Life Arc Report)

**Decans/Faces** - DEFERRED
- **Implementation Effort**: Easy (simple 10° divisions)
- **Interpretive Value**: Low for natal work (adds texture but minimal meaning)
- **User Decision**: SKIP for default mode (low value)
- **Future**: May add for comprehensive mode

### Future Enhancements (Not Current Priority)

**Almuten Figuration** - CONSIDER FOR FUTURE
- **Definition**: Most powerful planet in chart (weighted dignity + accidental strength)
- **Traditional Technique**: Medieval technique
- **Interpretive Value**: Medium (identifies "most powerful" planet)
- **Implementation Effort**: High (complex weighted calculation)
- **Decision**: Not current priority - house rulers provide more useful information
- **Settings**: `include_almuten: false` (default off, advanced users only)
- **Future**: May add for advanced comprehensive mode

### NOT Recommended (Correctly Excluded)

**Harmonic Aspects** (Quintile, Septile, etc.) - NO
- **Why Not**: Not traditional, low reliability, adds noise to interpretation
- **Current Status**: Correctly excluded
- **Decision**: Continue excluding (not traditional)

**Midpoints** - NO
- **Why Not**: Not traditional, modern technique with mixed results
- **Current Status**: Correctly excluded
- **Decision**: Continue excluding (not traditional)

**Additional Lots Beyond Core Set** - NO (for Mode 1)
- **Why Not**: The 8 remaining lots (beyond Fortune/Spirit/Eros/Necessity) have limited natal value
- **Current Status**: 12 lots calculated (excessive for natal)
- **User Decision**: Use 4 lots for Mode 1 (DEFAULT MODE), reserve 8 additional lots for Mode 2 (Life Arc Report)
- **Reasoning**: "These other lots will be better for the life arc report right?" (User confirmation)

---

## III. DEFAULT MODE SPECIFICATION (Current Implementation)

**CRITICAL CLARIFICATION**: This section defines what is included in the CURRENT default mode implementation. The agents work on DEFAULT MODE ONLY right now.

### What is "Default Mode"?

**Current Focus**: DEFAULT MODE = single interpretation approach with technique on/off switches
- Settings control WHICH TECHNIQUES to include (on/off switches)
- NOT output style modulation (formal vs. accessible, brief vs. detailed)
- NOT depth level variations (minimal/standard/deep/comprehensive) ← FUTURE FEATURE

**User Decision**: "We don't have depth programmed into our agents. We could add this in the future, but we are just working on the default mode now."

### Default Mode Technique Inclusion

**PRIMARY Techniques** (Always Included):
1. House Rulers (deeply integrated - IN/RULE/CONNECT)
2. Sect (filter ALL planet interpretations through sect lens)
3. Essential Dignities (domicile, exaltation, detriment, fall, triplicity)
4. Classical Aspects (conjunction, sextile, square, trine, opposition)
5. Angles & Angularity (angular house emphasis, aspects to angles)
6. Lunar Nodes (evolutionary path)
7. Antiscia (mirror degrees - NEW)
8. Fixed Stars (Major 5 when conjunct - NEW)
9. Triplicity (elemental dignity - already calculated, now emphasized)

**SECONDARY Techniques** (On/Off Switches):
- Lots: 4 lots (Fortune, Spirit, Eros, Necessity) ← Default ON
- Receptions: Mutual reception emphasized ← Default ON
- Bonification: Benefic support for malefics ← Default ON
- Chart Patterns: Stelliums, element/modality balance ← Always ON

**OPTIONAL Techniques** (User Can Toggle):
- Modern Planets: Uranus, Neptune, Pluto (secondary context) ← Default ON
- Chiron: Wounded healer archetype ← Default OFF
- Black Moon Lilith: Shadow feminine ← Default OFF
- Vertex: Fated encounters ← Default OFF

**DEFERRED Techniques** (Not in Default Mode):
- Bounds/Terms: Low natal value, deferred
- Decans/Faces: Low natal value, deferred
- Planetary Hours: Low natal value, deferred
- Additional 8 lots: Reserved for Mode 2 (Life Arc Report)

### Output Style (NOT a Setting)

**Synthesis Language**: Accessible, therapeutic, archetypal language is THE DEFAULT
- This is not an optional "psychological overlay" - it's how synthesis is written
- User Decision: "Remove the psychological overlay, that is the default way language we are using"
- No setting needed - this is the agent's writing style

### Settings Implementation (Current)

Settings control **WHICH TECHNIQUES** to include, not output style or depth:

```ini
[INTERPRETATION_SETTINGS]

# PRIMARY TECHNIQUES (always on)
# House rulers, sect, dignities, aspects, angles, nodes, antiscia, fixed stars, triplicity
# → No settings needed (always included)

# SECONDARY TECHNIQUES (default on, can toggle off)
include_lots: true  # Enables Fortune, Spirit, Eros, Necessity
include_receptions: true
include_bonification: true
include_chart_patterns: true

# OPTIONAL TECHNIQUES (default varies)
include_modern_planets: true  # Uranus, Neptune, Pluto (secondary context)
include_chiron: false
include_lilith: false
include_vertex: false

# DEFERRED TECHNIQUES (not yet implemented)
include_bounds_detailed: false
include_decans_detailed: false
include_planetary_hours: false
```

**Key Insight**: Simple on/off switches. No depth modulation. No style modulation. Just technique inclusion.

---

## IV. DEPTH LEVELS (FUTURE FEATURE - NOT YET IMPLEMENTED)

⚠️ **WARNING: SPECULATIVE FUTURE FEATURE** ⚠️

**This section describes a FUTURE architectural vision for depth level variations.** It is NOT currently implemented. The agents work on DEFAULT MODE ONLY (see Section III above).

**User Decision**: "We don't have depth programmed into our agents. We could add this in the future, but we are just working on the default mode now. Make a note of this. Update the documentation, that this is a speculative future feature. Same with all other output modulation other than turning variables on and off."

**Current Reality**:
- Agents produce ONE synthesis style (default mode)
- Settings = on/off switches for techniques (not depth modulation)
- Output length/style is NOT user-configurable yet

**Future Vision** (When Implemented):
- Depth levels would modulate output length, detail level, technique emphasis
- "minimal" = 3-5 pages, core themes only
- "standard" = 8-12 pages, full traditional reading (current default)
- "deep" = 12-18 pages, psychological depth added
- "comprehensive" = 20-30 pages, everything included

**Why Document This Now?**
- Architectural planning for future enhancement
- Shows where the system could grow
- Helps understand design decisions in current default mode

**Do NOT Implement Depth Levels Yet** - Focus on perfecting default mode first.

---

### Depth: "minimal" (Quick Overview) - FUTURE

**Purpose**: 3-5 page synthesis, essential themes only
**Target Audience**: Casual users wanting basic understanding
**Calculation Set**: PRIMARY techniques only

**Include**:
- Core Identity (Sun/Moon/ASC)
- House rulers (brief mentions)
- Essential dignities (domicile/exaltation only)
- Major aspects (±3° orbs only)
- Sect determination (basic)
- Chart patterns (stelliums only)

**Exclude**:
- All lots
- Receptions
- Bonification
- Modern planets (Uranus/Neptune/Pluto)
- Chiron, Lilith, Vertex
- Psychological overlays
- Decans, bounds, antiscia, fixed stars

**Interpretive Focus**: Core personality, strengths, challenges (straightforward)
**Expected Length**: 3-5 pages (2,000-3,000 words)
**Performance**: Fastest generation

---

### Depth: "standard" (Comprehensive Traditional)

**Purpose**: 8-12 page synthesis, full traditional interpretation
**Target Audience**: Most users seeking complete natal understanding
**Calculation Set**: PRIMARY + SECONDARY techniques (traditional only)

**Include**:
- All PRIMARY techniques (house rulers, sect, dignities, aspects, angles, nodes)
- Lots: Fortune + Spirit only
- Receptions (when significant)
- Bonification (when present)
- Chart patterns (full)
- Elemental/modality balance
- Modern planets (secondary context only)

**Exclude**:
- Chiron, Lilith, Vertex
- Deep psychological overlays
- Antiscia, fixed stars (unless specifically requested)
- Decans/bounds details
- Additional lots beyond Fortune/Spirit

**Interpretive Focus**: Complete traditional portrait with psychological integration
**Expected Length**: 8-12 pages (6,000-8,000 words)
**Performance**: Standard generation time
**Settings**: This is the DEFAULT depth

---

### Depth: "deep" (Enhanced Traditional + Psychological)

**Purpose**: 12-18 page synthesis, traditional + psychological depth
**Target Audience**: Serious students, therapy-oriented users
**Calculation Set**: PRIMARY + SECONDARY + some OPTIONAL

**Include**:
- All PRIMARY and SECONDARY techniques
- Lots: Fortune, Spirit, Eros, Necessity (4 total)
- Chiron (wounded healer)
- Psychological overlays: "basic" mode (archetypal language)
- Modern planets (full psychological context)
- Receptions and bonification (detailed)

**Exclude**:
- Lilith, Vertex (too niche)
- Antiscia, fixed stars (unless requested)
- Additional lots beyond core 4
- Harmonic aspects, midpoints

**Interpretive Focus**: Deep psychological portrait with traditional foundation
**Expected Length**: 12-18 pages (8,000-12,000 words)
**Performance**: Slower (more RAG queries)
**Settings**: Opt-in for depth-focused users

---

### Depth: "comprehensive" (Everything)

**Purpose**: 20-30 page synthesis, kitchen sink approach
**Target Audience**: Advanced students, astrology professionals
**Calculation Set**: PRIMARY + SECONDARY + ALL OPTIONAL

**Include**:
- All PRIMARY, SECONDARY, and OPTIONAL techniques
- Lots: All 12 lots
- Chiron, Lilith, Vertex (all modern points)
- Psychological overlays: "deep" mode (dedicated sections)
- Antiscia (if implemented)
- Fixed stars (if implemented)
- Decans and bounds (detailed)
- Triplicities (detailed)

**Interpretive Focus**: Exhaustive analysis covering every technique
**Expected Length**: 20-30 pages (15,000-20,000 words)
**Performance**: Slowest (maximum RAG queries)
**Settings**: Opt-in for completeness-focused users

---

## V. Settings Implementation Strategy (Current Default Mode)

### Current Problem

**Profile settings exist but agents don't read them**. This is the #1 gap.

Example from `profiles/Darren_S/profile.md`:
```ini
include_house_rulers: true
include_lots: true
include_lot_fortune: true
include_lot_spirit: true
# ... 30+ more settings
```

**But**: natal-interpreter agent doesn't check these settings - it interprets everything regardless.

### Updated Understanding (From Planning Session)

**Settings control WHICH TECHNIQUES to include** (on/off switches), NOT:
- Output style (accessible language is THE DEFAULT)
- Depth levels (future feature, not current implementation)
- Synthesis length (agents produce default length synthesis)

**Focus**: Make agents respect technique on/off switches in default mode.

---

### Solution Architecture (Simplified for Default Mode)

**Three-Phase Implementation**:

#### Phase 1: Settings Loader (Immediate Priority)

Create `scripts/profile_settings_loader.py`:

```python
def load_interpretation_settings(profile_name):
    """
    Load interpretation settings from profile.md
    Returns dict of enabled/disabled features (DEFAULT MODE)

    NOTE: Settings control WHICH TECHNIQUES to include (on/off switches).
    NOT depth levels (future feature) or output style (always accessible).
    """
    profile_path = f"profiles/{profile_name}/profile.md"
    settings = parse_settings_from_profile(profile_path)

    # Return simplified settings dict for DEFAULT MODE
    return {
        # PRIMARY TECHNIQUES (always on, no settings needed)
        # house_rulers, sect, dignities, aspects, angles, nodes always included

        # NEW PRIMARY TECHNIQUES (always on in default mode)
        'antiscia': True,  # Always on (approved for PRIMARY)
        'fixed_stars': True,  # Always on (approved for PRIMARY)
        'triplicity': True,  # Always on (already calculated)

        # SECONDARY TECHNIQUES (on/off switches)
        'lots': {
            'fortune': settings.get('include_lot_fortune', True),  # Default on
            'spirit': settings.get('include_lot_spirit', True),  # Default on
            'eros': settings.get('include_lot_eros', True),  # Default on (Mode 1 uses 4 lots)
            'necessity': settings.get('include_lot_necessity', True),  # Default on (Mode 1 uses 4 lots)
            # Remaining 8 lots default OFF (reserved for Mode 2 - Life Arc Report)
            'courage': settings.get('include_lot_courage', False),
            'victory': settings.get('include_lot_victory', False),
            'basis': settings.get('include_lot_basis', False),
            'exaltation': settings.get('include_lot_exaltation', False),
            'nemesis': settings.get('include_lot_nemesis', False),
            'marriage': settings.get('include_lot_marriage', False),
            'children': settings.get('include_lot_children', False),
            'siblings': settings.get('include_lot_siblings', False),
        },
        'receptions': settings.get('include_receptions', True),  # Default on
        'bonification': settings.get('include_bonification', True),  # Default on
        'chart_patterns': settings.get('include_chart_patterns', True),  # Always on

        # OPTIONAL TECHNIQUES (user can toggle)
        'modern_planets': settings.get('include_modern_planets', True),  # Default on (secondary context)
        'chiron': settings.get('include_chiron', False),  # Default off
        'lilith': settings.get('include_lilith', False),  # Default off
        'vertex': settings.get('include_vertex', False),  # Default off

        # DEFERRED TECHNIQUES (not yet implemented)
        'bounds_detailed': False,  # Deferred (low natal value)
        'decans_detailed': False,  # Deferred (low natal value)
        'planetary_hours': False,  # Deferred (low natal value)
    }
```

**Integration Point**: Call this at the START of natal interpretation workflow, pass settings dict to agent.

**NOTE**: No 'depth' key (depth levels are future feature). No 'psychological' key (accessible language is default style).

---

#### Phase 2: Agent Awareness (High Priority)

Update `natal-interpreter.md` to:

1. **Receive settings dict** at workflow start
2. **Check settings before interpreting** each technique
3. **Skip disabled techniques** (don't query RAG, don't write synthesis)
4. **Integrate sect-awareness** (filter ALL planet interpretations through sect lens)
5. **Integrate house rulers deeply** (always mention IN/RULE/CONNECT for life areas)

Example agent logic:
```markdown
## Workflow Enhancement: Settings-Aware Interpretation (DEFAULT MODE)

### Step 1: Load User Settings

Before beginning interpretation, load the user's interpretation settings:

```python
from scripts.profile_settings_loader import load_interpretation_settings
settings = load_interpretation_settings(profile_name)
```

### Step 2: PRIMARY Techniques (Always Interpret)

These techniques are ALWAYS interpreted (no settings check needed):

1. **House Rulers** - For EVERY life area section, mention:
   - What's IN the house (planets, if any)
   - WHO RULES the house (ruler's placement)
   - How the ruler CONNECTS (aspects, condition)

2. **Sect** - For EVERY planet interpretation, filter through sect lens:
   - Benefic in sect: "your benefic of sect" + "most easily brings..."
   - Benefic contrary to sect: "helpful but less accessible..."
   - Malefic in sect: "constructive challenges" + "tests that build..."
   - Malefic contrary to sect: "more reactive" + "particularly difficult..."

3. **Essential Dignities** - Use triplicity (already calculated), domicile, exaltation, detriment, fall

4. **Classical Aspects, Angles, Nodes** - Always include

5. **Antiscia** - Check for antiscia conjunctions (±1° orb), mention when present

6. **Fixed Stars** - Check Major 5 conjunctions (±1° orb), mention when present

7. **Triplicity** - Weave into dignity assessments (elemental comfort)

### Step 3: SECONDARY Techniques (Check Settings)

For each synthesis section, check settings before including:

**Example - Lots Section**:
```python
if settings['lots']['fortune']:
    # Query RAG for Lot of Fortune interpretation
    # Write Fortune synthesis
if settings['lots']['spirit']:
    # Query RAG for Lot of Spirit interpretation
    # Write Spirit synthesis
if settings['lots']['eros']:
    # Query RAG for Lot of Eros interpretation (DEFAULT MODE includes this)
    # Write Eros synthesis
if settings['lots']['necessity']:
    # Query RAG for Lot of Necessity interpretation (DEFAULT MODE includes this)
    # Write Necessity synthesis
# Skip remaining 8 lots (reserved for Mode 2)
```

**Example - Receptions**:
```python
if settings['receptions']:
    # Check for mutual receptions
    # Emphasize when significant
```

### Step 4: OPTIONAL Techniques (Check Settings)

```python
if settings['modern_planets']:
    # Include Uranus, Neptune, Pluto (secondary context only)

if settings['chiron']:
    # Include Chiron wounded healer analysis

if settings['lilith']:
    # Include Lilith shadow feminine analysis

if settings['vertex']:
    # Include Vertex fated encounters analysis
```
```

**Critical**: Agent must SKIP techniques that are disabled (not just hide them in output - don't calculate/query them at all).

**User Decisions Implemented**:
- Sect emphasis MORE (filter ALL planet interpretations)
- House rulers deeply integrated (IN/RULE/CONNECT always mentioned)
- 4 lots in default mode (Fortune, Spirit, Eros, Necessity)
- Antiscia and Fixed Stars included as PRIMARY
- Triplicity used (already calculated)
- Reception emphasized (especially mutual reception)
- Accessible synthesis language is THE DEFAULT (no setting needed)

---

#### Phase 3: Seed Data Generator Optimization (Future Enhancement)

**Currently**: seed_data_generator.py calculates EVERYTHING (all 12 lots, all modern points, all dignities).

**Future**: Make seed_data_generator.py settings-aware:

```python
def generate_seed_data(args, settings=None):
    """
    Generate seed data based on user settings.
    If settings provided, only calculate enabled techniques.
    """
    if settings is None:
        settings = load_interpretation_settings(args.name)

    # Always calculate PRIMARY techniques
    planet_data = calculate_planets(jd)
    house_info = calculate_houses(jd, args.lat, args.lon)
    sect = determine_sect(...)
    aspects = calculate_aspects(planet_data)

    # Conditionally calculate SECONDARY techniques
    if settings['lots']['fortune'] or settings['lots']['spirit']:
        lots = calculate_lots(jd, asc_longitude, planet_data, sect['type'],
                             enabled_lots=settings['lots'])

    if settings['modern_points']['chiron']:
        chiron = calculate_chiron(jd)

    # ... etc
```

**Benefit**: Faster seed data generation, cleaner output files, less noise.

**Priority**: FUTURE (Phase 3) - not critical since seed data generation is already fast.

---

### Settings Granularity Recommendations

**Too Granular** (Current State):
- 12 individual lot toggles (include_lot_fortune, include_lot_spirit, etc.)
- Individual bound/decan toggles
- Result: 30+ settings switches, overwhelming

**Optimal Granularity** (Recommended):

```ini
[INTERPRETATION_SETTINGS]

# DEPTH & CORE SETTINGS
depth: standard  // "minimal" | "standard" | "deep" | "comprehensive"

# TRADITIONAL TECHNIQUES (grouped)
include_lots: true  // Enables Fortune + Spirit (standard), or all lots (comprehensive)
include_house_rulers: true  // PRIMARY - rarely disable
include_angles_aspects: true  // PRIMARY - rarely disable
include_nodes: true  // PRIMARY - rarely disable
include_receptions: true  // SECONDARY - mention when present
include_bonification: true  // SECONDARY - mention when present

# MODERN METHODS (individual toggles appropriate here)
include_chiron: false
include_lilith: false
include_vertex: false
include_psychological: "basic"  // false | "basic" | "deep"

# ADVANCED TRADITIONAL (rarely used)
include_antiscia: false
include_fixed_stars: false
include_bounds_detailed: false
```

**Key Changes**:
1. **Depth level drives most behavior** - use "comprehensive" to get all lots, not individual toggles
2. **Group related settings** - "lots" setting enables sensible defaults based on depth
3. **Individual toggles for modern methods** - these are truly opt-in/out
4. **Simplify from 30+ switches to ~10 meaningful controls**

---

## VI. Sect-Based Interpretation Guidelines (CRITICAL EMPHASIS)

### The Sect Problem

**Current State**: Sect is calculated correctly, but severely underutilized in interpretation.

**User Decision**: "Yes to both" (sect guidelines + update agent) + "Emphasize sect MORE in interpretations"

**What MUST Happen**: Filter ALL planet interpretations through the sect lens. This is non-negotiable and critical for traditional astrology.

---

### Sect Interpretation Formula

For EVERY planet, consider:

1. **Is this a benefic or malefic?**
   - Benefics: Jupiter, Venus
   - Malefics: Mars, Saturn
   - Luminaries: Sun, Moon (not benefic/malefic, but have sect preferences)

2. **Is it in sect or contrary to sect?**
   - **Day charts** (Sun above horizon):
     - In sect: Sun, Jupiter, Saturn
     - Contrary to sect: Moon, Venus, Mars
   - **Night charts** (Sun below horizon):
     - In sect: Moon, Venus, Mars
     - Contrary to sect: Sun, Jupiter, Saturn

3. **Apply the sect modifier**:
   - **Benefic in sect**: Most helpful, easiest expression
   - **Benefic contrary to sect**: Still helpful, but less accessible
   - **Malefic in sect**: Less harsh, more constructive challenges
   - **Malefic contrary to sect**: More difficult, reactive challenges

---

### Sect Integration Examples

**Example 1: Jupiter in Day Chart** (in sect)
- ❌ **Without sect awareness**: "Jupiter in Taurus brings abundance through practical means"
- ✅ **With sect awareness**: "Jupiter, your benefic of sect in this day chart, offers its gifts most readily through practical Taurus stability. This is where fortune flows most naturally."

**Example 2: Mars in Day Chart** (contrary to sect)
- ❌ **Without sect awareness**: "Mars in Aries brings bold initiative"
- ✅ **With sect awareness**: "Mars, contrary to sect in your day chart, expresses more reactively than constructively. Your Aries boldness may feel more defensive than pioneering at times."

**Example 3: Venus in Night Chart** (in sect)
- ❌ **Without sect awareness**: "Venus in Libra brings harmony in relationships"
- ✅ **With sect awareness**: "Venus, your benefic of sect in this night chart, is the planet that most easily brings grace and ease. In Libra, this relational gift is at its most refined."

**Example 4: Saturn in Night Chart** (contrary to sect)
- ❌ **Without sect awareness**: "Saturn in Capricorn builds lasting structures"
- ✅ **With sect awareness**: "Saturn, contrary to sect in your night chart, can feel particularly restrictive and punishing. The Capricorn drive to build may come with harsher self-criticism than necessary."

---

### Agent Implementation

**Update natal-interpreter.md**:

```markdown
## Sect-Aware Interpretation (CRITICAL)

For EVERY planetary placement you interpret:

1. State the chart sect (day or night) ONCE in Chart Overview section
2. For EACH planet, internally note:
   - Is it a benefic, malefic, or luminary?
   - Is it in sect or contrary to sect?
3. Weave sect status into your interpretation:
   - Benefic in sect: "your benefic of sect" + "most easily brings..."
   - Benefic contrary to sect: "helpful but less accessible..."
   - Malefic in sect: "constructive challenges" + "tests that build..."
   - Malefic contrary to sect: "more reactive" + "particularly difficult..."

**DO NOT** list sect status mechanically. INTEGRATE it into the narrative naturally.

Example synthesis:
"Venus, your benefic of sect, brings grace most readily through the creative fifth house. This is where relationships flow with least effort—through play, art, joy."
```

---

## VII. House Ruler Integration Guidelines (PRIMARY TECHNIQUE)

### The House Ruler Problem

**Current State**: House rulers are calculated perfectly, but need deeper integration in synthesis.

**User Decision**: "Yes" to deeper integration + always mention what's IN house, WHO RULES, how ruler CONNECTS

**What MUST Happen**: House rulers should be woven throughout the narrative as the PRIMARY lens for understanding life areas. For EVERY life area, mention IN/RULE/CONNECT.

---

### House Ruler Interpretive Priority

**House Rulers > Planets in Houses**

Traditional astrology teaches:
1. **Ruler OF the house** shows HOW that life area manifests (the path, the story arc)
2. **Planets IN the house** show WHAT happens there (events, themes)

**Both are important, but RULERS are the primary technique.**

---

### House Ruler Integration Strategy

**For Major Life Areas** (Career, Relationships, Home, etc.), ALWAYS mention:

1. **What's IN the house** (if planets are present)
2. **WHO RULES the house** (the ruler's placement)
3. **How the ruler connects** (aspects, condition)

**Example Structure**:

**Career Section**:
```
Your tenth house of career is in [Sign], ruled by [Planet]. This [Planet]
is placed in your [House], [condition assessment]. This tells us that your
professional calling finds its path through [house themes].

[If planets in 10th]: With [planets] also in your tenth house, [describe
what happens in career], but the deeper story is told by [ruler]'s placement
in [house], which says [how it manifests].
```

**Relationship Section**:
```
Your seventh house of partnership is in [Sign], ruled by [Planet]. Look to
this [Planet] in your [House] to understand HOW partnership enters your life.
[Describe ruler's condition and house placement]. This is the path through
which committed relationship unfolds for you.
```

---

### Examples of House Ruler Integration

**Example 1: Career (10th House)**
- ❌ **Without house ruler**: "You have Venus in the 10th house, so career involves beauty, art, or relationships."
- ✅ **With house ruler**: "Your tenth house in Taurus is ruled by Venus, placed in your fifth house. Your career path unfolds through creative self-expression, children, or artistic pursuits. The professional calling isn't separate from joy—it's found within it."

**Example 2: Home/Family (4th House)**
- ❌ **Without house ruler**: "Your 4th house is empty, so home life is less emphasized."
- ✅ **With house ruler**: "Your fourth house in Scorpio is ruled by Mars in your ninth house. Home and family are tied to your philosophical explorations, travel, or teaching. You may live abroad, or your family roots are connected to foreign lands. Mars here suggests an active, somewhat turbulent domestic foundation."

**Example 3: Relationships (7th House)**
- ❌ **Without house ruler**: "No planets in 7th house, so relationships are less important."
- ✅ **With house ruler**: "Your seventh house in Aquarius is ruled by Saturn in your sixth house. Partnership manifests through work, service, health contexts. You may meet partners through your job, or relationships have a practical, duty-bound quality. Saturn's condition [strong/weak] tells us whether this feels supportive or burdensome."

---

### Agent Implementation

**Update natal-interpreter.md**:

```markdown
## House Ruler Integration (PRIMARY Technique)

House rulers are THE PRIMARY technique for understanding life areas. For any life
area you discuss (career, relationships, home, health, etc.), you MUST include:

1. **The house ruler**: Which planet rules this house cusp?
2. **Where it's placed**: What house does the ruler occupy?
3. **Its condition**: Is the ruler strong (angular, dignified) or weak (cadent, debilitated)?
4. **The interpretation**: What does this ruler placement say about HOW this life area manifests?

**Structure for Major Life Area Sections**:

### [Life Area Name]

**Opening paragraph**: Describe the house and its ruler.
"Your [Nth house] in [Sign] is ruled by [Planet], placed in your [House]. This
placement tells us that [life area] unfolds through [house themes of ruler's location]."

**Middle paragraphs**: Describe ruler's condition and aspects.
"[Ruler] is [strong/moderate/weak] here because [angular/succedent/cadent] and
[dignity status]. [Describe aspects to ruler that affect this life area]."

**Integration paragraph**: Connect to planets IN the house (if any).
"[If planets in house]: With [planets] also here, [describe what happens], but
the deeper pattern is shown by [ruler]'s placement in [house]."

**NEVER write**: "You have an empty [house]." Instead write: "Your [house] is ruled by..."
```

---

## VII. Performance Optimization

### Current Performance

**Seed Data Generation**: Fast (~2-3 seconds for complete chart)
**Natal Interpretation**: Moderate (~30-60 seconds depending on RAG queries)
**PDF Generation**: Fast (~1-2 seconds)

**Total Time**: ~45-75 seconds for complete natal horoscope

---

### Optimization Opportunities

**1. Reduce RAG Queries for Optional Techniques**

**Current State**: Agent queries RAG for every technique (even disabled ones)

**Optimization**: Skip RAG queries for disabled techniques
- If `include_chiron: false`, don't query "Chiron in [sign]"
- If `include_lot_eros: false`, don't query "Lot of Eros interpretation"

**Expected Speedup**: 20-30% for "minimal" depth, 10-15% for "standard" depth

---

**2. Batch RAG Queries**

**Current State**: Sequential RAG queries (one at a time)

**Optimization**: Batch related queries
- Query all planetary positions together: "Sun in Capricorn, Moon in Leo, Mercury in Capricorn"
- Query all lots together: "Lot of Fortune in Virgo, Lot of Spirit in Capricorn"

**Expected Speedup**: 10-20% (network latency reduction)

---

**3. Pre-Calculated Dignity Tables**

**Current State**: Dignities calculated on-the-fly during seed data generation

**Optimization**: Already optimal (dignity calculations are fast lookups)

**No change needed**

---

**4. Caching Seed Data**

**Current State**: Seed data regenerated on every interpretation request

**Optimization**: Cache seed data, only regenerate if birth data changes
- Store `seed_data.json` with timestamp
- Check if birth data unchanged since last generation
- Reuse cached seed data if valid

**Expected Speedup**: ~2-3 seconds per interpretation (seed data generation time)

---

### Performance Recommendations

**Implement in Priority Order**:

1. **Settings-aware RAG skipping** (Phase 2 above) - Biggest impact
2. **Seed data caching** - Simple to implement, meaningful speedup
3. **Batch RAG queries** - Moderate complexity, moderate benefit

**Don't Optimize**:
- Dignity calculations (already fast)
- Aspect calculations (already fast)
- PDF generation (already fast)

---

## VIII. Implementation Roadmap (Updated with User Decisions)

### Phase 1: Antiscia + Fixed Stars + Triplicity Usage (Week 1)

**PRIORITY**: Implement the 3 approved new techniques (EASY implementation, HIGH value)

**Tasks**:
1. **Antiscia Implementation** (~30 lines):
   - Add `calculate_antiscia(longitude)` function to ephemeris_helper.py
   - Calculate antiscion for each natal planet
   - Check for antiscia conjunctions (±1° orb)
   - Add to seed_data.json output

2. **Fixed Stars Implementation** (~50 lines):
   - Add `calculate_fixed_star_conjunctions(planet_positions)` to ephemeris_helper.py
   - Use Swiss Ephemeris `swe.fixstar_ut()` for Major 5 (Regulus, Spica, Algol, Antares, Aldebaran)
   - Check conjunctions with planets/angles (±1° orb)
   - Add to seed_data.json output (only when present)

3. **Triplicity Emphasis**:
   - Update natal-interpreter.md to use triplicity in dignity assessments
   - Weave elemental comfort into interpretations
   - (Already calculated in seed_data_generator.py lines 81-93 - just needs agent awareness)

**Deliverables**:
- Enhanced seed_data_generator.py with antiscia and fixed stars
- Updated natal-interpreter.md to use triplicity
- Test outputs with antiscia/fixed stars present

**Success Criteria**:
- Antiscia correctly calculated (mirror across 0° Cancer/Capricorn)
- Fixed stars identified when conjunct (Major 5 only, ±1° orb)
- Triplicity woven into dignity assessments

---

### Phase 2: Settings Foundation (Week 2)

**Tasks**:
1. Create `scripts/profile_settings_loader.py` (DEFAULT MODE focus)
2. Update profile.md settings format (simplified for on/off switches)
3. Update `profiles/Darren_S/profile.md` with new format
4. Test settings loader with existing profiles

**Deliverables**:
- Working settings loader (returns technique on/off switches)
- Simplified profile.md format (no depth levels, no psychological overlay setting)
- Documentation in DEVELOPMENT_GUIDE.md

**Success Criteria**: Settings loader returns correct dict for all profiles (DEFAULT MODE)

---

### Phase 3: Agent Settings Integration + Sect/House Ruler Emphasis (Week 3-4)

**Tasks**:
1. Update `natal-interpreter.md` with settings-aware workflow (DEFAULT MODE)
2. Add conditional technique integration (lots, modern points, etc.)
3. **CRITICAL**: Add sect-aware interpretation guidelines (filter ALL planet interpretations)
4. **CRITICAL**: Enhance house ruler integration guidelines (always IN/RULE/CONNECT)
5. Update natal-interpreter.md to use antiscia, fixed stars, triplicity
6. Test with technique on/off switches

**Deliverables**:
- Settings-aware natal-interpreter agent (DEFAULT MODE)
- Test outputs with various technique combinations
- Verification that disabled techniques are SKIPPED (not just hidden)

**Success Criteria**:
- Disabled techniques don't appear in synthesis (not calculated/queried)
- **Sect status woven throughout ALL planetary interpretations** (benefics/malefics filtered by sect)
- **House rulers prominently featured** in life area sections (IN/RULE/CONNECT always mentioned)
- Antiscia mentioned when present (±1° orb conjunctions)
- Fixed stars mentioned when present (Major 5, ±1° orb)
- Triplicity woven into dignity assessments (elemental comfort)
- Reception emphasized (especially mutual reception)
- 4 lots used (Fortune, Spirit, Eros, Necessity) - remaining 8 lots OFF for Mode 1

---

### Phase 4: Seed Data Optimization (Future - Optional)

**NOTE**: This phase is OPTIONAL and deferred. Current seed data generation is already fast (~2-3 seconds).

**Tasks** (if pursued later):
1. Make seed_data_generator.py settings-aware (optional calculations)
2. Implement seed data caching (skip regeneration if unchanged)
3. Add batch RAG query support (if feasible)

**Deliverables**:
- Optimized seed_data_generator.py
- Seed data caching logic
- Performance benchmark report

**Success Criteria**:
- Seed data generation only calculates enabled techniques
- Cached seed data reused when valid
- ~20% performance improvement

**Decision**: DEFER this phase - focus on perfecting default mode interpretation first

---

### Phase 5: Depth Levels (FUTURE - Not Current Priority)

**NOTE**: Depth levels are a FUTURE architectural vision, NOT current implementation focus.

**User Decision**: "We don't have depth programmed into our agents. We could add this in the future, but we are just working on the default mode now."

**Tasks** (when ready to implement):
1. Design depth level variations (minimal/standard/deep/comprehensive)
2. Create output length modulation logic
3. Add style variations (formal vs. accessible, brief vs. detailed)
4. Test each depth level for appropriate length and content

**Deliverables**:
- Depth level logic in natal-interpreter.md
- Test outputs for each depth level (3-5 pages, 8-12 pages, 12-18 pages, 20-30 pages)
- User documentation for depth level selection

**Success Criteria**:
- "minimal" depth produces 3-5 pages (core themes only)
- "standard" depth produces 8-12 pages (full traditional reading)
- "deep" depth produces 12-18 pages (psychological depth)
- "comprehensive" depth produces 20-30 pages (everything)

**Decision**: DEFER to future - perfect default mode first, then add depth variations later

---

## IX. Quality Assurance

### Testing Strategy

**Test Profiles** (use existing profiles):
1. **Darren** - Complex chart, many techniques active
2. **Mom** - Simpler chart for baseline testing
3. **Sister** - Different birth location for timezone testing

**Test Matrix**:

| Depth | Expected Length | Techniques Included | Test Case |
|-------|----------------|---------------------|-----------|
| minimal | 3-5 pages | PRIMARY only | "Quick overview for Mom" |
| standard | 8-12 pages | PRIMARY + SECONDARY traditional | "Standard natal for Darren" |
| deep | 12-18 pages | + Chiron + 4 lots + psychological | "Deep reading for Sister" |
| comprehensive | 20-30 pages | Everything | "Complete analysis for Darren" |

---

### Validation Checks

**For Each Test Output**:

1. **Length Validation**: Does output match expected page count?
2. **Technique Inclusion**: Are only enabled techniques present?
3. **Technique Exclusion**: Are disabled techniques completely absent (not just hidden)?
4. **Sect Integration**: Is sect status mentioned for benefics/malefics?
5. **House Ruler Integration**: Are house rulers featured prominently in life area sections?
6. **Settings Respected**: Does output reflect profile settings?
7. **Performance**: Is generation time within expected range?

---

### Quality Metrics

**Measure These**:
- Interpretation length (words/pages) by depth level
- Generation time (seconds) by depth level
- RAG queries per interpretation (should decrease with minimal depth)
- User satisfaction (qualitative feedback)

**Targets**:
- Minimal: <30 seconds generation
- Standard: 30-60 seconds generation
- Deep: 60-90 seconds generation
- Comprehensive: 90-120 seconds generation

---

## X. User Experience Recommendations

### Profile Setup Wizard (Future Enhancement)

Instead of editing profile.md manually, create an interactive setup:

```bash
python scripts/profile_wizard.py

Welcome to Natal Chart Profile Setup!

Enter your name: John Doe
Enter birth date (YYYY-MM-DD): 1990-01-15
Enter birth time (HH:MM): 14:30
Enter birth location: New York, NY

Choose interpretation depth:
  1. Minimal (3-5 pages, core themes only)
  2. Standard (8-12 pages, full traditional reading) [DEFAULT]
  3. Deep (12-18 pages, psychological depth)
  4. Comprehensive (20-30 pages, everything)

Enter choice [2]: 2

Enable modern techniques?
  - Chiron (wounded healer) [y/N]: n
  - Black Moon Lilith (shadow) [y/N]: n
  - Psychological overlays [none/basic/deep, default=basic]: basic

Profile created: profiles/John_Doe/profile.md
Generate seed data? [Y/n]: y

✅ Seed data generated
✅ Profile ready for interpretation
```

**Benefits**:
- User-friendly
- Prevents settings errors
- Provides guidance on depth levels
- Generates seed data immediately

---

### Depth Level Descriptions (Add to Profile.md)

Make depth levels self-documenting:

```ini
# Choose your interpretation depth:
#
# minimal: 3-5 pages, essential themes only (Sun/Moon/ASC, house rulers, major aspects)
#          Best for: Quick overview, gift readings, beginners
#
# standard: 8-12 pages, complete traditional reading (all PRIMARY + SECONDARY techniques)
#          Best for: Most users, comprehensive self-understanding, balanced approach
#          Includes: House rulers, sect analysis, dignities, aspects, Fortune, Spirit, receptions
#
# deep: 12-18 pages, traditional + psychological depth (adds Chiron, 4 lots, archetypal language)
#          Best for: Therapy-oriented readings, serious students, depth psychology focus
#
# comprehensive: 20-30 pages, everything (all 12 lots, modern points, advanced techniques)
#          Best for: Astrology professionals, students, completists
#          Warning: Can be overwhelming for general readers

depth: standard
```

---

## XI. Documentation Updates Needed

### Files to Create

1. **`scripts/profile_settings_loader.py`** - Settings loader (NEW)
2. **`scripts/profile_wizard.py`** - Interactive setup (FUTURE)

### Files to Update

1. **`natal-interpreter.md`** - Add settings-aware workflow, sect guidelines, house ruler guidelines
2. **`DEVELOPMENT_GUIDE.md`** - Document settings system, depth levels
3. **`PROFILES_GUIDE.md`** - Update with new settings format
4. **`profiles/Darren_S/profile.md`** - Simplify to new settings format (example)
5. **`SEED_DATA_SPECIFICATION.md`** - Document optional calculation behavior
6. **`REFERENCE.md`** - Add antiscia, fixed stars (when implemented)

### Documentation Sections to Add

**DEVELOPMENT_GUIDE.md additions**:
- Settings system architecture
- How to add new optional techniques
- Depth level guidelines for agent creators

**PROFILES_GUIDE.md additions**:
- Depth level descriptions
- Settings examples for common use cases
- How settings affect output

---

## XII. Migration Plan for Existing Profiles

### Existing Profiles

**Current State**:
- `profiles/Darren_S/profile.md` - Has 30+ granular settings
- `profiles/mom/profile.txt` - Has basic birth data only
- `profiles/sister/profile.txt` - Has basic birth data only

### Migration Strategy

**Option 1: Automatic Migration Script**
```bash
python scripts/migrate_profiles.py

✅ Converted Darren_S/profile.md to new format
✅ Created mom/profile.md with default settings
✅ Created sister/profile.md with default settings

3 profiles migrated successfully
```

**Option 2: Manual Update**

Update Darren's profile:
```ini
# Before (30+ lines)
include_house_rulers: true
include_lot_fortune: true
include_lot_spirit: true
include_lot_eros: true
include_lot_necessity: true
include_lot_courage: true
include_lot_victory: true
include_lot_basis: true
include_lot_exaltation: true
# ... 20+ more lines

# After (10 lines)
depth: standard
include_lots: true
include_house_rulers: true
include_chiron: false
include_lilith: false
include_psychological: basic
```

---

### Backward Compatibility

**Requirement**: Old settings format must still work during transition.

**Implementation**: Settings loader checks for both formats:
```python
def load_interpretation_settings(profile_name):
    settings = parse_settings_from_profile(profile_path)

    # Check if new format (has 'depth' key)
    if 'depth' in settings:
        return parse_new_format(settings)

    # Fall back to old format (individual lot toggles)
    else:
        return parse_old_format(settings)
```

---

## XIII. Success Criteria Summary

### Technical Success

- ✅ Settings loader correctly parses profile.md
- ✅ Agents respect depth level (minimal/standard/deep/comprehensive)
- ✅ Disabled techniques are SKIPPED (not calculated or interpreted)
- ✅ Performance improves for minimal depth (20-30% faster)
- ✅ Seed data caching works correctly
- ✅ All 4 depth levels generate expected output lengths

### Interpretive Success

- ✅ Sect status integrated naturally into ALL planetary interpretations
- ✅ House rulers featured prominently in life area sections
- ✅ Traditional techniques prioritized over modern
- ✅ Synthesis feels cohesive (not a list of techniques)
- ✅ User can understand output without being an astrologer

### User Experience Success

- ✅ Settings are intuitive (not overwhelming)
- ✅ Depth levels clearly described
- ✅ Default settings produce great results (standard depth)
- ✅ Advanced users can enable comprehensive mode
- ✅ Generation time is reasonable (<2 minutes for comprehensive)

---

## XIV. Resolved Questions (From Planning Session)

All major design questions have been resolved with user decisions:

1. **Lot Reduction**: ✅ RESOLVED
   - **Decision**: Use 4 lots for Mode 1 (Fortune, Spirit, Eros, Necessity)
   - **Rationale**: Remaining 8 lots more relevant for Mode 2 (Life Arc Report)
   - **User Quote**: "Let's use those 4 lots" + "These other lots will be better for the life arc report right?"

2. **Antiscia Implementation Priority**: ✅ RESOLVED
   - **Decision**: INCLUDE as PRIMARY technique (HIGH priority)
   - **Rationale**: EASY implementation (~30 lines), HIGH traditional value
   - **User Decision**: "Include antiscia" + "Add antiscia"

3. **Fixed Stars Implementation**: ✅ RESOLVED
   - **Decision**: INCLUDE as PRIMARY technique (Major 5 only: Regulus, Spica, Algol, Antares, Aldebaran)
   - **Rationale**: EASY implementation (Swiss Ephemeris built-in), HIGH value when present
   - **Orb**: ±1° (tight conjunctions only)
   - **User Quote**: "How hard are the fixed stars? If they are really easy include it" → Analysis showed EASY → INCLUDE

4. **Minor Dignities (Bounds/Decans)**: ✅ RESOLVED
   - **Triplicity**: USE IT (already calculated, zero effort, moderate value)
   - **Bounds/Terms**: SKIP for now (medium effort, low natal value)
   - **Decans/Faces**: SKIP for now (easy effort, low natal value)
   - **User Quote**: "How hard and how much value do these add?" → Analysis showed low natal value → DEFER

5. **Psychological Overlay**: ✅ RESOLVED
   - **Decision**: REMOVE from settings - accessible synthesis language IS the default style
   - **User Quote**: "Remove the psychological overlay, that is the default way language we are using"
   - **Clarification**: This is NOT an optional feature - it's how synthesis is written

6. **Depth Levels**: ✅ RESOLVED
   - **Decision**: DEFER to future - not current implementation focus
   - **Current Focus**: DEFAULT MODE ONLY with technique on/off switches
   - **User Quote**: "We don't have depth programmed into our agents. We could add this in the future, but we are just working on the default mode now."
   - **Status**: Documented as FUTURE architectural vision (Section IV)

7. **Sect Integration**: ✅ RESOLVED
   - **Decision**: Emphasize MORE - filter ALL planet interpretations through sect lens
   - **User Quote**: "Yes to both" (sect guidelines + update agent)

8. **House Ruler Integration**: ✅ RESOLVED
   - **Decision**: Deepen integration - always mention IN/RULE/CONNECT for life areas
   - **User Quote**: "Yes" to deeper integration

9. **Reception**: ✅ RESOLVED
   - **Decision**: INCLUDE - ensure mutual reception is emphasized
   - **User Quote**: "Update so reception is included"

---

## XV. Conclusion

### Summary of User-Approved Priorities

**PHASE 1 - IMMEDIATE (Week 1)**: New Techniques Implementation
1. ✅ **Antiscia calculation** (EASY - ~30 lines, HIGH traditional value)
2. ✅ **Fixed Stars calculation** (EASY - ~50 lines with Swiss Ephemeris, HIGH value when present)
3. ✅ **Triplicity emphasis** (ZERO effort - already calculated, moderate value)

**PHASE 2 (Week 2)**: Settings Foundation
4. ✅ **Settings loader** (DEFAULT MODE focus - technique on/off switches only)
5. ✅ **Simplified profile format** (no depth levels, no psychological overlay setting)
6. ✅ **4 lots for Mode 1** (Fortune, Spirit, Eros, Necessity) - reserve 8 lots for Mode 2

**PHASE 3 (Week 3-4)**: Agent Integration & Critical Emphasis
7. ✅ **Sect integration** (CRITICAL - filter ALL planet interpretations through sect lens)
8. ✅ **House ruler integration** (CRITICAL - always mention IN/RULE/CONNECT for life areas)
9. ✅ **Reception emphasis** (ensure mutual reception highlighted)
10. ✅ **Settings-aware interpretation** (respect technique on/off switches)

**DEFERRED** (Future Enhancements):
- Depth levels (minimal/standard/deep/comprehensive) - FUTURE architectural vision
- Output style modulation - FUTURE feature
- Seed data optimization - OPTIONAL (current speed already good)
- Bounds/Terms - Low natal value
- Decans/Faces - Low natal value
- Planetary Hours - Low natal value for Mode 1
- Almuten Figuration - Medium value, high complexity

### Key Design Decisions

**DEFAULT MODE FOCUS**:
- Current implementation = DEFAULT MODE ONLY with technique on/off switches
- Settings control WHICH TECHNIQUES to include (not depth, not style)
- Accessible synthesis language IS the default (not an optional overlay)
- Depth levels are FUTURE architectural vision (documented but not implemented yet)

**NEW PRIMARY TECHNIQUES** (Approved & Added):
- Antiscia (mirror degrees) - easy to implement, high traditional value
- Fixed Stars (Major 5) - easy to implement, high value when present
- Triplicity (elemental dignity) - already calculated, now emphasized

**CRITICAL EMPHASIS** (Must Implement):
- **Sect**: Filter EVERY planet interpretation through sect lens (non-negotiable)
- **House Rulers**: Always mention IN/RULE/CONNECT for life areas (PRIMARY technique)

**LOTS DECISION**:
- Mode 1 (Natal): 4 lots (Fortune, Spirit, Eros, Necessity)
- Mode 2 (Life Arc): All 12 lots (remaining 8 more relevant for timeline)

### Next Steps

1. **Implement Phase 1** (Week 1) - Antiscia, Fixed Stars, Triplicity emphasis
2. **Implement Phase 2** (Week 2) - Settings loader, simplified profile format
3. **Implement Phase 3** (Week 3-4) - Agent integration with CRITICAL sect/house ruler emphasis
4. **Test thoroughly** - Verify sect filtering, house ruler integration, technique on/off switches
5. **Document** - Update DEVELOPMENT.md, agent instructions, user guides

### Success Criteria

**Technical Success**:
- ✅ Antiscia calculated correctly (mirror across 0° Cancer/Capricorn axis)
- ✅ Fixed stars identified when conjunct (Major 5 only, ±1° orb)
- ✅ Triplicity woven into dignity assessments
- ✅ Settings loader returns correct technique on/off switches
- ✅ Agents respect settings (skip disabled techniques entirely)

**Interpretive Success**:
- ✅ **Sect status integrated into ALL planetary interpretations** (most critical)
- ✅ **House rulers featured prominently** (IN/RULE/CONNECT always mentioned)
- ✅ Reception emphasized (especially mutual reception)
- ✅ 4 lots used for Mode 1 (remaining 8 reserved for Mode 2)
- ✅ Synthesis remains cohesive (not a technique checklist)

**User Experience Success**:
- ✅ Settings are simple on/off switches (not overwhelming)
- ✅ Default mode produces excellent results out-of-box
- ✅ Traditional techniques prioritized over modern
- ✅ Accessible language is the default (not optional)

---

**Version**: 1.1 (Updated with Planning Session Decisions)
**Maintained by**: docs-updater-astrology (based on workflow-planner-2 recommendations and user decisions)
**Implementation by**: Development team + natal-interpreter agent updates
**Status**: Ready for implementation - all design questions resolved

---

*This specification represents the optimal natal data model for DEFAULT MODE based on traditional Hellenistic astrology principles, user decisions from planning session, and implementation difficulty analysis. All approved techniques have been evaluated for effort (EASY/MEDIUM/HIGH) and value (LOW/MODERATE/HIGH). Focus: Perfect default mode first, then add depth variations later.*
