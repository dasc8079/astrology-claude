# Zodiac Symbol Standardization Audit

**Date**: 2025-10-17
**Purpose**: Ensure zodiac symbol text abbreviation solution is properly documented across all system components

---

## Current Implementation

### Solution
- **Format**: Text abbreviations (CAP, LEO, ARI, etc.) instead of Unicode zodiac symbols
- **Reason**: WeasyPrint cannot render Unicode zodiac symbols as monochrome (always colored emojis)
- **Big Three Display**: `☉ CAP • ☽ LEO • ↑ LEO`
- **Location**: Title page (Page 1) of all PDF reports

### Technical Components

#### ✅ COMPLETE: pdf_generator.py
- **File**: `/scripts/pdf_generator.py`
- **Function**: `zodiac_sign_to_symbol()` (lines 266-292)
- **Status**: Implemented with text abbreviations
- **Documentation**: Function docstring explains WeasyPrint limitation
- **Debug output**: Includes verification logging

#### ✅ COMPLETE: base.css
- **File**: `/scripts/css/base.css`
- **Section**: Lines 3-20 (custom font @font-face template)
- **Section**: Lines 101-124 (zodiac symbol styling)
- **Status**: Documented with clear comments about text abbreviation mode vs custom font mode
- **Features**:
  - Default: Text abbreviation mode (Helvetica, 600 weight, letter-spacing)
  - Optional: Custom font mode (commented out with clear instructions)

#### ✅ COMPLETE: Title Page HTML Template
- **File**: `/scripts/pdf_generator.py`
- **Function**: `build_title_page()` (lines 295-378)
- **Status**: Includes astronomical symbols (☉ ☽ ↑) before zodiac abbreviations
- **Format**: `<span class="astro-symbol">☉</span>{sun_symbol} • <span class="astro-symbol">☽</span>{moon_symbol} • <span class="astro-symbol">↑</span>{rising_symbol}`

---

## Documentation to Update

### 1. OUTPUT_STYLE_GUIDE.md ❌ NEEDS UPDATE
**File**: `/docs/reference/OUTPUT_STYLE_GUIDE.md`
**Section**: Title Page Standards (line 509+)
**Missing**:
- No mention of zodiac symbol format or abbreviations
- No documentation of "big three" display
- No explanation of WeasyPrint limitations

**Required Addition**:
```markdown
**Big Three Format** (Sun, Moon, Rising):
- Display format: `☉ CAP • ☽ LEO • ↑ LEO`
- Astronomical symbols: ☉ (Sun), ☽ (Moon), ↑ (Rising/Ascendant)
- Zodiac signs: 3-letter abbreviations (CAP, LEO, ARI, TAU, GEM, CAN, VIR, LIB, SCO, SAG, AQU, PIS)
- Separator: Bullet character (•) between elements
- Technical note: Text abbreviations used instead of Unicode zodiac symbols due to WeasyPrint rendering limitations (cannot convert colored emojis to monochrome)
```

### 2. DEVELOPMENT_GUIDE.md ❓ CHECK
**File**: `/docs/DEVELOPMENT_GUIDE.md`
**Check**: Does it document PDF generation system and css/base.css?
**Action**: Verify and update if needed

### 3. Agent Documentation ❓ CHECK
**Files to audit**:
- natal-interpreter.md
- natal-interpreter-experiential.md
- life-arc-interpreter.md (v2, v3)
- transit-analyzer.md
- transit-analyzer-short.md
- transit-analyzer-long.md

**Check**:
- Do agents have instructions about title page formatting?
- Do agents try to generate zodiac symbols in markdown?
- Do agents correctly reference pdf_generator.py for title page creation?

**Note**: Agents should NOT be generating zodiac symbols themselves - pdf_generator.py extracts big three from seed data and builds title page automatically.

---

## Files That DON'T Need Updates

### ✅ Scripts
- **pdf_generator.py**: Already implements text abbreviations
- **ephemeris_helper.py**: Not involved in symbol display

### ✅ CSS Files
- **base.css**: Already documented with clear comments
- **chart_based.css**: No zodiac symbol styling needed
- **timeline_based.css**: No zodiac symbol styling needed
- **movement_based.css**: No zodiac symbol styling needed

### ✅ Profile Structure
- Profile files don't generate zodiac symbols - this is handled by pdf_generator.py

---

## Recommended Updates

### Priority 1: OUTPUT_STYLE_GUIDE.md
**Add to "Title Page Standards" section** (after line 520):

```markdown
#### Big Three Display Format

Every report title page includes the "Big Three" (Sun, Moon, Rising signs) with astronomical symbols and zodiac abbreviations.

**Display Format**:
```
☉ CAP • ☽ LEO • ↑ LEO
```

**Components**:
1. **Astronomical Symbols**:
   - ☉ (Sun) - U+2609
   - ☽ (Moon) - U+263D
   - ↑ (Ascendant/Rising) - U+2191

2. **Zodiac Sign Abbreviations** (3 letters, uppercase):
   - ARI (Aries), TAU (Taurus), GEM (Gemini)
   - CAN (Cancer), LEO (Leo), VIR (Virgo)
   - LIB (Libra), SCO (Scorpio), SAG (Sagittarius)
   - CAP (Capricorn), AQU (Aquarius), PIS (Pisces)

3. **Separator**: Bullet character (•) between elements

**Technical Implementation**:
- Generated automatically by `pdf_generator.py` function `build_title_page()`
- Extracts Sun, Moon, Rising from seed data
- Converts sign names to abbreviations via `zodiac_sign_to_symbol()`
- CSS styling: `.astro-symbol` (astronomical symbols), `.zodiac-symbol` (sign abbreviations)

**Why Text Abbreviations?**
WeasyPrint (PDF rendering library) cannot style Unicode zodiac symbols (♈ ♉ ♊ etc.) as monochrome - they always render as colored emojis. Text abbreviations provide clean, professional black-and-white appearance.

**Future Enhancement**: Custom font with monochrome zodiac glyphs can be used by:
1. Placing font file in `scripts/fonts/`
2. Uncommenting `@font-face` declaration in `base.css`
3. Setting `USE_CUSTOM_ZODIAC_FONT = True` in `pdf_generator.py`
4. Updating `.zodiac-symbol` font-family in `base.css`
```

### Priority 2: Agent Instructions
**Check if agents try to generate title pages or zodiac symbols**
- Agents should reference seed data only
- pdf_generator.py handles all title page creation
- No agent should hardcode zodiac symbols in markdown

### Priority 3: DEVELOPMENT_GUIDE.md
**Add section on PDF generation if missing**:
- Document pdf_generator.py workflow
- Document CSS file structure
- Document zodiac symbol implementation

---

## Testing Checklist

After documentation updates, verify:

- [ ] OUTPUT_STYLE_GUIDE.md documents zodiac symbol format
- [ ] DEVELOPMENT_GUIDE.md documents PDF generation system
- [ ] No agent hardcodes zodiac symbols in markdown
- [ ] All agents correctly reference pdf_generator.py
- [ ] base.css comments are clear and accurate
- [ ] pdf_generator.py includes zodiac symbol mapping documentation

---

## Conclusion

**Current Status**: Implementation is COMPLETE and WORKING
**Documentation Status**: INCOMPLETE - needs standardization documentation

**Next Steps**:
1. Update OUTPUT_STYLE_GUIDE.md with zodiac symbol section
2. Audit agent files to ensure no hardcoded symbols
3. Update DEVELOPMENT_GUIDE.md if needed
4. Mark standardization complete

**Fallback Option**: Custom font implementation is documented and ready if user wants to use actual zodiac glyphs in future
