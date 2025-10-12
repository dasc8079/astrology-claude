# Accuracy-Checker Agent Specification

**Created**: 2025-10-11
**Purpose**: Automated quality verification for all astrology interpretation outputs
**Status**: Design Phase
**Priority**: HIGH (runs after every interpretation)

---

## Executive Summary

The **accuracy-checker** agent is an automated verification system that runs after every interpretation agent (natal, life-arc, transit) completes its work. It validates output consistency, logic, completeness, and format compliance WITHOUT re-verifying deterministic calculations (which are assumed correct once working).

**Key Insight**: Calculations are deterministic and testable via unit tests. The accuracy-checker focuses on **interpretation quality** - data consistency, narrative logic, completeness, and format compliance.

---

## Purpose

**Problem Solved**: Interpretation agents may produce outputs with:
- Inconsistent data references (e.g., "Jupiter in Gemini 2026" when data says "Jupiter in Cancer")
- Missing required sections or content
- Format/structure issues
- Incomplete coverage of calculated data
- Logic errors in narrative (e.g., positive synthesis when data shows challenging transits)

**Solution**: Automated post-generation verification that catches quality issues before user sees output.

---

## Core Responsibilities

### 1. Data Consistency Validation

**Check**: Do interpretations match the underlying data?

**Examples**:
- If transit_data.json shows "Saturn in Pisces (2025-05-25 to 2026-02-15)", interpretation should NOT say "Saturn in Aquarius"
- If seed_data.json shows "Sun in Capricorn", interpretation should reflect Capricorn themes
- If daily_scores show mostly negative values, synthesis should not describe period as "highly favorable"

**Method**: Extract timeline/positions from data files, scan interpretation for conflicting statements

### 2. Completeness Verification

**Check**: Are all required sections present with appropriate content?

**Natal Reports**:
- ✅ Title page with birth data
- ✅ Introduction (2-4 paragraphs)
- ✅ All planetary sections (Sun through Saturn minimum)
- ✅ House rulers section
- ✅ Major aspects
- ✅ Poetic wrapup (4-8 sentences)

**Life Arc Reports**:
- ✅ Title page with age range
- ✅ Introduction (2-3 paragraphs)
- ✅ All major ZR L1 chapters within date range
- ✅ Current situation sub-chapter
- ✅ Convergence events documented
- ✅ Poetic wrapup

**Transit Reports** (Short):
- ✅ Summary synthesis (200-300 words)
- ✅ 2-4 movements with evocative titles
- ✅ Technical appendix with all transits
- ✅ Most auspicious/challenging days
- ✅ Terminal summary output

**Transit Reports** (Long):
- ✅ Quick Reference tables
- ✅ Overview section (300-500 words)
- ✅ ZR L2 chapters covering full date range
- ✅ Technical appendix
- ✅ Terminal summary output

### 3. Format Compliance

**Check**: Does output follow specified template?

**Standards**:
- Correct markdown structure (H1, H2, H3 hierarchy)
- Title page HTML div structure
- Bold dates woven into narrative (not listed)
- NO astrological jargon without immediate translation
- Second-person voice throughout synthesis
- Poetic wrapup has NO heading (flows as final paragraph)

### 4. Logic Verification

**Check**: Does narrative logic match the data?

**Examples**:
- If Saturn squares Moon, interpretation should reflect challenge/maturation (not expansion/ease)
- If multiple malefic transits converge, synthesis should acknowledge difficulty
- If ZR peak period (L2=L1), interpretation should mention heightened significance
- If Lord of Year is Saturn, Saturn transits should be emphasized

**Method**: Semantic analysis of synthesis against transit types, dignity states, timing technique activations

---

## What Accuracy-Checker Does NOT Do

❌ **Re-calculate planetary positions** (calculations are deterministic, tested separately)
❌ **Re-query RAG database** (assumes RAG responses were appropriate)
❌ **Rewrite interpretations** (flags issues for correction, doesn't fix)
❌ **Judge astrological interpretation quality** (focuses on consistency, not interpretation philosophy)

---

## Workflow Integration

### Trigger Points

The accuracy-checker runs **automatically after**:
1. natal-interpreter completes
2. life-arc-interpreter completes
3. transit-analyzer-short completes
4. transit-analyzer-long completes

### Input Data Required

1. **Generated output file** (markdown)
2. **Source data files**:
   - seed_data.json (for natal/life-arc)
   - transit_data_*.json (for transit reports)
   - life_arc_data_*.json (for life arc reports)
3. **Report metadata**:
   - Report type (natal/life_arc/transit_short/transit_long)
   - Profile name
   - Date range (if applicable)

### Output Format

**Terminal Output**:
```
🔍 ACCURACY CHECK: [Report Type] for [Name]

DATA CONSISTENCY: ✅ PASS
  • All planetary positions match source data
  • Timeline references consistent with calculations

COMPLETENESS: ✅ PASS
  • All required sections present
  • Minimum word counts met
  • Technical appendix complete

FORMAT COMPLIANCE: ⚠️ WARNING
  • Missing bold dates in Movement II (line 245)
  • Astrological jargon without translation: "ZR L2" (line 89)

LOGIC VERIFICATION: ✅ PASS
  • Narrative tone matches transit types
  • Synthesis aligns with data indicators

OVERALL: ✅ PASS WITH WARNINGS
Report saved with 2 minor format issues flagged.
```

**Log File** (detailed):
```
/profiles/[name]/output/accuracy_check_[report_type]_[timestamp].log
```

---

## Verification Rules

### Data Consistency Rules

1. **Planetary Sign Timeline Extraction**:
   - Extract from data: "Jupiter: Cancer (2025-10 to 2026-08), Leo (2026-08 to 2027-06)"
   - Scan interpretation for mentions of Jupiter
   - Flag if interpretation says "Jupiter in Gemini 2026" (contradicts data)

2. **Daily Score Alignment**:
   - If average daily score for period is negative, synthesis should acknowledge challenges
   - If average daily score for period is positive, synthesis should reflect opportunities
   - Threshold: ±10 points = "significant" (must be mentioned)

3. **Timing Technique Consistency**:
   - If data shows Saturn profection year, interpretation should mention Saturn emphasis
   - If data shows ZR L2=L1 peak period, interpretation should mention heightened significance
   - If data shows Firdaria planet X, transits to planet X should be emphasized

### Completeness Rules

1. **Section Presence**: All sections from template must exist
2. **Word Count Minimums**:
   - Introduction: 100+ words
   - Synthesis sections: 200+ words
   - Movement narratives: 300+ words
   - Poetic wrapup: 60+ words (4-8 sentences)

3. **Data Coverage**:
   - Natal: All planets Sun-Saturn covered
   - Life Arc: All ZR L1 periods in date range covered
   - Transit Short: All movements have 2+ transits mentioned
   - Transit Long: All ZR L2 periods in date range covered

### Format Rules

1. **Markdown Structure**:
   - Title page: `<div class="title-page">` with required fields
   - Headings: Proper H1 > H2 > H3 hierarchy
   - No orphaned H3 without H2 parent

2. **Voice Consistency**:
   - Second person ("You") not third person ("The native")
   - No astrological jargon without immediate translation
   - Bold dates integrated into flowing narrative

3. **Poetic Wrapup**:
   - NO heading (e.g., "## Poetic Wrapup" is wrong)
   - 4-8 sentences
   - NO astrological terminology
   - Direct second-person address

### Logic Rules

1. **Transit Type Alignment**:
   - Hard aspects (square, opposition) = challenge/tension themes
   - Soft aspects (trine, sextile) = ease/opportunity themes
   - Saturn transits = maturation/limitation/structure
   - Jupiter transits = expansion/opportunity/growth

2. **Synthesis Tone Matching**:
   - Positive daily scores = opportunity/growth language
   - Negative daily scores = challenge/caution language
   - Mixed scores = nuanced both/and language

3. **Convergence Emphasis**:
   - MAJOR convergence (25+ points) = "highly significant", "rare alignment"
   - SIGNIFICANT convergence (15-24 points) = "important transition"
   - NOTABLE convergence (8-14 points) = "meaningful shift"

---

## Error Severity Levels

**CRITICAL** (blocks output, requires fix):
- Missing title page
- Missing required planetary section (natal)
- Missing required chapter (life arc/transit long)
- Major data contradiction (e.g., "Sun in Aries" when data shows Capricorn)

**WARNING** (flags issue, allows output):
- Missing bold dates in movement
- Astrological jargon without translation
- Word count slightly below minimum
- Minor formatting issue

**INFO** (logged, not flagged):
- Stylistic variation from examples
- Optional modern planet emphasis
- Additional content beyond minimum

---

## Agent Architecture

### Agent Type
- **Name**: accuracy-checker
- **Color**: Orange
- **Model**: Haiku (fast verification, deterministic checks)
- **Trigger**: Automatic after interpretation agents complete
- **Proactive**: YES (always runs, no user request needed)

### Input Parameters
```python
{
  "report_type": "natal|life_arc|transit_short|transit_long",
  "output_file": "/profiles/name/output/report.md",
  "data_files": {
    "seed_data": "/profiles/name/seed_data/seed_data.json",  # if applicable
    "transit_data": "/profiles/name/output/transit_data_*.json",  # if applicable
    "life_arc_data": "/profiles/name/output/life_arc_data_*.json"  # if applicable
  },
  "profile_name": "darren",
  "date_range": {  # if applicable
    "start": "2025-10-01",
    "end": "2026-01-31"
  }
}
```

### Output
- Terminal summary (pass/fail with key findings)
- Detailed log file
- Return code: 0 (pass), 1 (warnings), 2 (critical errors)

---

## Implementation Notes

### Phase 1: Core Validation (MVP)
- Data consistency extraction and comparison
- Completeness checking (section presence, word counts)
- Format validation (markdown structure, template compliance)
- Terminal output with pass/fail

### Phase 2: Logic Verification
- Semantic analysis of synthesis tone
- Transit type alignment checking
- Convergence emphasis validation

### Phase 3: Integration
- Automatic invocation from interpretation agents
- Logging to dedicated accuracy_check files
- Optional fix suggestions

---

## Related Documentation

- **astrology-output-debugger**: Deeper investigation when accuracy-checker finds issues
- **TROUBLESHOOTING.md**: Common accuracy issues and fixes
- **OUTPUT_STYLE_GUIDE.md**: Format standards for verification

---

## Benefits

✅ **Catches mistakes before user sees output**
✅ **Ensures consistent quality across all reports**
✅ **Validates data integrity automatically**
✅ **Reduces need for manual verification**
✅ **Documents quality checks for reference**
✅ **Fast execution (Haiku model for speed)**

---

## Next Steps

1. ✅ Create specification (this document)
2. ⏳ Create `.claude/agents/accuracy-checker.md` agent file
3. ⏳ Build verification scripts (data extraction, comparison logic)
4. ⏳ Integrate into interpretation agent workflows
5. ⏳ Test with real reports and iterate
6. ⏳ Document common issues in TROUBLESHOOTING.md
