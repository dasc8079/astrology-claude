# Example Settings Block for Darren_Profile.txt

## Purpose

This settings block controls the depth and scope of natal chart interpretation, allowing progressive enhancement from traditional-only to comprehensive analysis including modern methods.

## Location

**Add to TOP of Darren_Profile.txt** (before Current Location)

---

## Conservative Settings (Traditional Only - Recommended Default)

```toml
[INTERPRETATION_SETTINGS]
# Depth control
depth = "standard"  # Options: minimal | standard | deep | comprehensive

# Traditional enhancements (all default true except antiscia)
house_rulers = true
lots = "basic"  # Options: basic | extended | full
angles_aspects = true
nodes = true
receptions = true
bonification = true
antiscia = false  # Default false, opt-in
triplicities_detailed = true
bounds_detailed = true

# Modern methods (Lilith/Chiron/Psychological default ON)
lilith = true  # Default ON, can toggle off
chiron = true  # Default ON, can toggle off
psychological = "basic"  # Default ON (basic), Options: false | basic | deep
harmonic_aspects = false
midpoints = false
vertex = false

# Output control
section_headers = true  # Show clear section headers
cite_sources = true  # Include source citations
```

**What this provides:**
- ✅ Traditional Hellenistic foundation (always present)
- ✅ Traditional enhancements (house rulers, lots, receptions, etc.)
- ✅ Lilith & Chiron (modern, commonly used)
- ✅ Basic psychological/Jungian themes (archetypal patterns)
- ❌ Harmonic aspects, midpoints, vertex (disabled)

**Result:** Deep traditional analysis with light modern psychological context

---

## Moderate Settings (Traditional + Light Modern Context)

```toml
[INTERPRETATION_SETTINGS]
# Depth control
depth = "deep"

# Traditional enhancements
house_rulers = true
lots = "extended"  # More lots beyond Fortune/Spirit
angles_aspects = true
nodes = true
receptions = true
bonification = true
antiscia = false  # Still opt-in
triplicities_detailed = true
bounds_detailed = true

# Modern methods
lilith = true
chiron = true
psychological = "deep"  # Upgrade to deep Jungian analysis
harmonic_aspects = false
midpoints = false
vertex = false

# Output control
section_headers = true
cite_sources = true
```

**What this adds:**
- ✅ Extended lots system (more Arabic parts)
- ✅ Deep Jungian psychological analysis (complexes, persona/shadow/anima-animus)
- ❌ Still no harmonic aspects, midpoints, or vertex

**Result:** Traditional foundation + enhanced traditional methods + deep psychological context

---

## Comprehensive Settings (All Features Enabled)

```toml
[INTERPRETATION_SETTINGS]
# Depth control
depth = "comprehensive"

# Traditional enhancements (all enabled)
house_rulers = true
lots = "full"  # All hermetic lots
angles_aspects = true
nodes = true
receptions = true
bonification = true
antiscia = true  # Enabled for comprehensive analysis
triplicities_detailed = true
bounds_detailed = true

# Modern methods (all enabled)
lilith = true
chiron = true
psychological = "deep"  # Deep Jungian analysis
harmonic_aspects = true  # Quintiles, septiles
midpoints = true  # Ebertin method
vertex = true  # Fated encounters point

# Output control
section_headers = true
cite_sources = true
```

**What this provides:**
- ✅ ALL traditional methods including antiscia
- ✅ Full lots system (all hermetic lots)
- ✅ ALL modern methods
- ✅ Deep psychological analysis

**Result:** Maximum depth analysis - very long, comprehensive interpretation

**⚠️ Warning:** This will produce a VERY long output. Only use if you want exhaustive detail.

---

## Minimal Settings (Lean Traditional Core Only)

```toml
[INTERPRETATION_SETTINGS]
# Depth control
depth = "minimal"

# Traditional enhancements (selective)
house_rulers = true
lots = "basic"
angles_aspects = false
nodes = false
receptions = false
bonification = false
antiscia = false
triplicities_detailed = false
bounds_detailed = false

# Modern methods (all disabled for minimal output)
lilith = false
chiron = false
psychological = false  # Disabled for truly minimal output
harmonic_aspects = false
midpoints = false
vertex = false

# Output control
section_headers = true
cite_sources = true
```

**What this provides:**
- ✅ Traditional core (sect, dignities, aspects, houses)
- ✅ House rulers only
- ✅ Basic lots (Fortune/Spirit)
- ❌ Everything else disabled

**Result:** Concise, focused traditional interpretation

---

## Custom Settings (Birth Time Unknown - No Angles)

```toml
[INTERPRETATION_SETTINGS]
# Depth control
depth = "standard"

# Traditional enhancements
house_rulers = true
lots = "basic"
angles_aspects = false  # DISABLED - no exact birth time
nodes = true
receptions = true
bonification = true
antiscia = false
triplicities_detailed = true
bounds_detailed = true

# Modern methods
lilith = true
chiron = true
psychological = false
harmonic_aspects = false
midpoints = false
vertex = false  # DISABLED - requires exact birth time

# Output control
section_headers = true
cite_sources = true
```

**When to use:**
- Birth time unknown or uncertain
- Houses approximated or unavailable
- Angles (ASC/MC/DC/IC) unreliable

**What changes:**
- ❌ No angles_aspects analysis
- ❌ No vertex (requires exact time)
- ✅ All other features work with approximate time

---

## Settings Reference Guide

### Depth Options

| Setting | Description | Output Length |
|---------|-------------|---------------|
| `minimal` | Core traditional only | Short (~2-3 pages) |
| `standard` | Traditional + key enhancements | Medium (~5-7 pages) |
| `deep` | Enhanced traditional + light modern | Long (~10-15 pages) |
| `comprehensive` | All features enabled | Very long (~20-30 pages) |

### Lots Options

| Setting | Description | Lots Included |
|---------|-------------|---------------|
| `basic` | Essential lots | Fortune, Spirit |
| `extended` | Common lots | + Eros, Necessity, Courage |
| `full` | All hermetic lots | + Victory, Siblings, Marriage, Children, etc. |
| `false` | Disabled | None |

### Psychological Options

| Setting | Description | Themes Included |
|---------|-------------|-----------------|
| `false` | Disabled | None |
| `basic` | Light archetypal themes | Basic archetypes, shadow basics |
| `deep` | Full Jungian analysis | Complexes, persona/shadow/anima-animus |

---

## How to Add Settings to Your Profile

1. **Open** `/Darren_Profile.txt`

2. **Add settings block at the TOP** (before everything else):

```
[INTERPRETATION_SETTINGS]
depth = "standard"
house_rulers = true
lots = "basic"
... [rest of settings]

[Current Location for Transits]
Latitude: 45.511429
Longitude: -122.639119

[Birth Data]
...
```

3. **Choose a template** from above (Conservative, Moderate, Comprehensive, etc.)

4. **Customize** specific settings as desired

5. **Save** the file

6. **Run** natal interpretation - settings will be automatically parsed

---

## Default Behavior (No Settings Block)

If NO settings block is present in Darren_Profile.txt, the system uses these defaults:

- **Depth:** `standard`
- **Traditional enhancements:** All enabled except `antiscia`
- **Modern methods:** Only `lilith` and `chiron` enabled
- **Output:** Headers and citations enabled

**This maintains the traditional foundation while providing common enhancements.**

---

## Important Notes

### ⚠️ Traditional Foundation Protection

**The following are ALWAYS true, regardless of settings:**

1. Traditional methods ALWAYS appear first
2. Sect-based analysis ALWAYS primary
3. Essential dignities ALWAYS foundational
4. Classical aspects only in core analysis
5. `traditional_first` setting is non-configurable (always `true`)

### ✅ Progressive Enhancement

- Start with conservative settings
- Test output length and depth
- Progressively enable features as desired
- Each setting is independent and toggleable

### 📚 Source Quality

Settings marked as "LIMITED" coverage in the database scan may have:
- Fewer interpretive examples
- Need for manual fallback to astrology_reference.py
- Less detailed delineations

Current coverage (from Phase 3 scan):
- 🟢 GOOD: Nodes, Angles, Harmonic Aspects, Chiron
- 🟡 MODERATE: Most traditional methods
- 🟠 LIMITED: Vertex, Antiscia

---

## Troubleshooting

**Q: Settings not being applied?**
- Verify `[INTERPRETATION_SETTINGS]` header is exact (case-sensitive)
- Check settings block is at TOP of file
- Ensure no syntax errors (key = value format)

**Q: Output too long?**
- Reduce `depth` to `standard` or `minimal`
- Set `lots = "basic"` instead of `extended` or `full`
- Disable optional modern methods

**Q: Want more detail?**
- Increase `depth` to `deep` or `comprehensive`
- Enable more traditional enhancements
- Consider `psychological = "basic"` for archetypal themes

**Q: Birth time uncertain?**
- Set `angles_aspects = false`
- Set `vertex = false`
- Other features still work with approximate time

---

**Recommended Starting Point:** Use "Conservative Settings" template above for balanced traditional + enhancement analysis.
