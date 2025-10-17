# PDF Formatter Agent Design Document

**Created**: 2025-10-16
**Status**: ⚠️ DEPRECATED - Agent approach abandoned in favor of script-based solution
**Purpose**: Separate interpretation logic from presentation logic for astrology reports

---

## ⚠️ DEPRECATION NOTICE

**This design document describes an agent-based approach that was NOT implemented.**

**What Actually Happened** (2025-10-16):
- **Agent Approach**: Proposed pdf-formatter agent to handle PDF generation
- **Script Approach**: Enhanced `scripts/pdf_generator.py` to build all front matter automatically
- **Result**: Script-based approach chosen (zero token cost, simpler, more maintainable)

**Current Implementation**:
- Interpreters output plain markdown starting with `# Introduction`
- `scripts/pdf_generator.py` reads markdown + seed_data.json
- Script builds all front matter (title, TOC, Chart Overview) automatically
- mode-orchestrator passes `--seed-data` flag to pdf_generator.py
- All PDF logic consolidated in one script (not distributed across agents)

**Why Script-Based Won**:
- Zero token cost (script vs agent invocation)
- Simpler workflow (one script vs agent coordination)
- Easier maintenance (update one script vs update agent + mode-orchestrator)
- Cleaner separation (scripts handle presentation, agents handle content)

**This Document Preserved For**:
- Historical design rationale
- Chart Overview template specifications (still used by script)
- Original problem analysis and benefits (still valid)

---

## Problem Statement

**Current Issues**:
1. Interpretation agents contain 100+ lines of HTML/CSS formatting instructions
2. Formatting changes require updating 3+ agent files
3. Mixing interpretation logic with presentation logic
4. Agent prompts are bloated (natal-interpreter: 455 lines, life-arc-interpreter: 920 lines)
5. If we change PDF styling, must update all interpreters

**Goal**: Separate concerns - interpreters focus on CONTENT, pdf-formatter handles PRESENTATION.

---

## Architecture Overview

### New Workflow

```
┌─────────────────────┐
│  Interpretation     │
│  Agent              │
│  (natal/life-arc/   │
│   transit)          │
└──────────┬──────────┘
           │
           │ Outputs simple markdown
           │ (headings, paragraphs only)
           ▼
┌─────────────────────┐
│  Seed Data          │
│  (master_seed_data  │
│   .yaml/json)       │
└──────────┬──────────┘
           │
           │ Both files passed to formatter
           ▼
┌─────────────────────┐
│  pdf-formatter      │
│  Agent              │
│                     │
│  Reads markdown +   │
│  seed data          │
│                     │
│  Builds:            │
│  - HTML title page  │
│  - Table of Contents│
│  - Chart Overview   │
│    (REPORT-SPECIFIC)│
│  - Formatted content│
└──────────┬──────────┘
           │
           │ Outputs styled PDF
           ▼
┌─────────────────────┐
│  Final PDF          │
│  (natal_synthesis   │
│   _NAME_DATE.pdf)   │
└─────────────────────┘
```

### Separation of Concerns

| Component | Responsibility |
|-----------|---------------|
| **Interpretation Agents** | Content quality, astrological synthesis, hierarchical analysis |
| **pdf-formatter Agent** | Page layout, HTML structure, CSS styling, Chart Overview (report-specific) |
| **CSS Files** | Typography, colors, spacing, print optimization |

---

## Input Specification

### pdf-formatter Inputs

```python
{
    'markdown_file': 'profiles/Sam_P/output/natal_synthesis_Sam_P_2025-10-15.md',
    'seed_data_file': 'profiles/Sam_P/seed_data/master_seed_data.yaml',
    'output_pdf': 'profiles/Sam_P/output/natal_synthesis_Sam_P_2025-10-15.pdf',
    'report_type': 'natal',  # or 'life_arc', 'transit_short', 'transit_long'
    'profile_name': 'Sam P',
    'birth_data': {
        'date': 'July 11, 1990',
        'time': '1:20 PM',
        'location': 'Merriam, Kansas',
        'coordinates': '39.0236°N, 94.6947°W'
    }
}
```

### Simplified Markdown Structure (from interpreters)

**Natal Reports**:
```markdown
# Introduction

Your life centers on teaching and service. [300 words...]

# Inner Life

## Emotional Landscape

[500 words about Moon, 4th house, emotional patterns...]

## Inner Dialogue & Self-Perception

[450 words about Sun-Moon, sect light, identity...]

[... continue with all sections ...]

## Reflection

Your path is clear. You are the teacher who serves through knowledge. There is within you a gift that only you can give—share it freely, and the world responds.
```

**Life Arc Reports**:
```markdown
# Introduction

You stand at age 46 in a decades-long chapter that began at age 12. [300 words...]

# Ages 0-12: Early Formation (Sagittarius Chapter)

[Narrative about first life chapter...]

# Ages 12-39: Building Through Discipline (Capricorn Chapter)

[Narrative about second life chapter...]

## Saturn Return at Age 29

[Milestone narrative...]

## Current Situation: Age 46

[Current position narrative with detail...]

[... continue through all chapters to age 100 ...]

## Reflection

You have walked through fire and emerged stronger. The chapter ahead asks you to trust what you have built. There is within you a foundation that cannot be shaken.
```

**Key Points**:
- Simple markdown headings (`#`, `##`, `###`)
- Plain paragraphs (no HTML divs)
- NO page break specifications
- NO CSS class names
- NO HTML title page structure
- Ends with `## Reflection` heading + poetic wrapup (3-5 sentences)

---

## pdf-formatter Responsibilities

### 1. Extract Metadata

From `seed_data`:
- Profile name
- Birth date, time, location, coordinates
- Chart data (sect, chart ruler, angular planets, etc.)
- ZR L1/L2 periods (for context)
- Report generation date

### 2. Build HTML Title Page

```html
<div class="title-page">
  <h1>Natal Horoscope</h1>
  <div class="profile-name">Sam P</div>
  <div class="birth-data">Born: July 11, 1990 at 1:20 PM<br>Merriam, Kansas<br>39.0236°N, 94.6947°W</div>
  <div class="report-date">Report Generated: October 16, 2025</div>
</div>
```

**Report type determines H1**:
- `natal` → "Natal Horoscope"
- `life_arc` → "Life Arc Report"
- `transit_short` → "Transit Report"
- `transit_long` → "Long-Term Transit Analysis"

### 3. Generate Table of Contents

Parse markdown headings to build hierarchical TOC:

```markdown
## Table of Contents

**Introduction** (p. 4)

**I. Inner Life**
- Emotional Landscape
- Inner Dialogue & Self-Perception
- Dreams, Fears & Shadows
- Psychological Wounds & Healing

**II. Outer Expression**
- Identity & Presence
- Voice & Communication Style
- Public Role & Reputation
- Style & Creative Self-Expression

[... etc ...]

**Reflection**
```

**Logic**:
- `# Heading` → Main section (bold)
- `## Subheading` → Subsection (indented, bullet)
- `### Sub-subheading` → Sub-subsection (double-indented)
- Page numbers are estimates (or omitted)

### 4. Build Chart Overview Page (REPORT-SPECIFIC)

**CRITICAL**: Chart Overview content depends on report type.

---

#### A. Natal Reports (Template A: Chart-Based)

**Purpose**: Quick reference to chart highlights for astrologers

**Format**: Bullet list with astrological data

**Required Data** (from seed_data):
- Sect (day/night)
- Chart Ruler (planet, sign, house, dignity)
- Sect Light (Sun/Moon, sign, condition)
- Angular Planets (planets in 1st, 4th, 7th, 10th)
- Stelliums (if present)
- Key Dignities (2-3 strongest: domicile/exaltation)
- Key Challenges (1-2 weakest: detriment/fall)
- Major Aspects (2-3 most significant patterns)

**Auto-Fill Remaining Space** (up to ~12 total bullets):

Priority order for additional items:
1. **Fixed Stars** (if within 1° of planet/angle)
   - "Spica conjunct Mercury (exaltation, success)"
2. **Lot Placements** (Fortune, Spirit, Eros, Necessity)
   - "Lot of Fortune: Sagittarius in 6th house"
3. **Mutual Receptions** (if present)
   - "Venus in Aries receives Mars in Taurus (mutual reception)"
4. **Cazimi/Combust** (if present)
   - "Mercury cazimi (empowered by Sun's heart)"
5. **Antiscia** (if within 3° of planet/angle)
   - "Mars antiscion conjunct Venus (hidden harmony)"
6. **Planetary Conditions** (stationary, swift, slow)
   - "Jupiter stationary (intensified expansion)"
7. **Elemental/Modal Emphasis** (if notable)
   - "Fire emphasis (4 planets in fire signs)"

**Example Output**:
```markdown
## Chart Overview

**Sect**: Day chart (Sun above horizon)
**Chart Ruler**: Venus in Gemini in 9th house (peregrine)
**Sect Light**: Sun in Cancer in 10th house (strong, angular)
**Angular Planets**: Sun (10th), Moon (1st), Jupiter (10th), Mercury (10th)
**Stellium**: 4 planets in Cancer (Sun, Mercury, Jupiter, Venus)
**Key Dignities**: Jupiter exalted in Cancer (maximum strength), Moon in Leo (strong)
**Key Challenges**: Saturn in Capricorn in 6th house (domicile but health challenges)
**Major Aspects**: Sun-Moon trine (harmony), Saturn-Mercury square (mental discipline)
**Lot of Fortune**: Sagittarius in 6th house (service-oriented fortune)
**Lot of Spirit**: Pisces in 9th house (spiritual teaching purpose)
**Fixed Stars**: Spica conjunct Mercury (success through communication)
**Mutual Reception**: Venus in Gemini receives Mercury in Taurus

<div class="page-break"></div>
```

---

#### B. Life Arc Reports (Template B: Timeline-Based)

**Purpose**: Major Life Events Timeline - what happens when

**Format**: Accessible table with NO astrological jargon

**Content**: Age ranges + life event descriptions

**Translation Rules**:
- NO bare astrological terms ("Fortune shifts to Aquarius", "Saturn return")
- YES accessible life descriptions ("profound relief arrives", "career recognition", "health crisis")
- Focus on EXPERIENCE: what it feels like, what changes, what becomes possible
- Mark current age clearly
- Include both challenges and relief points

**Example Output**:
```markdown
## Major Life Events Timeline

| Age | Life Event |
|-----|------------|
| 0-12 | Early childhood - themes of expansion and learning, but with early lessons about limits |
| 12 | A profound 27-year chapter begins - discipline, proving yourself, carrying weight becomes central |
| 29 | Major crisis and reckoning - health challenges, everything you've built is tested |
| 36 | Pressure intensifies - mental challenges peak before major relief |
| 39 | **← Current age** - Standing at threshold of profound relief |
| 39 | Entire life chapter shifts - weight lifts, innovation becomes possible, freedom arrives |
| 43 | New emotional depth emerges - focus turns to feeling, nurturing, legacy |
| 54 | Career recognition peak - leadership and teaching come to forefront |
| 66 | Life softens - spiritual themes, meaning-making, release of rigidity |
| 78 | Completion energy - wisdom-sharing phase, preparing legacy |

<div class="page-break"></div>
```

**Data Sources**:
- ZR L1 period changes (major chapter shifts)
- Planetary returns (Jupiter ~12yrs, Saturn ~29yrs)
- ZR L2 peak periods (bonification, matching L1)
- Major convergences (2+ techniques align)
- Current age position

---

#### C. Transit Reports (Template C: Movement-Based)

**Purpose**: Quick reference to current timing context and active transits

**Format**: Bullet list with current timing state

**Content**: L1 context + L2 periods + profections + active transits

**ALWAYS Include L1 Context** - provides the "frame" for understanding transits

**Example Output**:
```markdown
## Chart Overview

**Current Age**: 46
**Current Chapter**: Ages 12-39 (Capricorn Period) - Final year before major shift
**Next Chapter**: Ages 39-66 (Aquarius Period) - Begins December 2025
**Current Sub-Period (Fortune)**: Ages 35-39 (Scorpio L2) - Intense transformation phase
**Current Sub-Period (Spirit)**: Ages 43-46 (Pisces L2) - Spiritual deepening
**Profection Year**: 10th house (career focus), Lord: Sun in Cancer
**Report Window**: March-June 2025 (4 months)

**Key Transits in Effect**:
- Saturn in Pisces transiting 9th house (restructuring beliefs)
- Jupiter in Gemini transiting 12th house (hidden opportunities)
- Uranus in Taurus transiting 11th house (friendship upheaval)

**Major Transit Events This Period**:
- March 15: Saturn square natal Saturn (crisis point)
- April 8: Jupiter trine natal Sun (relief and expansion)
- May 22: Mars conjunct natal Mercury (mental energy surge)

<div class="page-break"></div>
```

**Why L1 Matters in Transit Reports**:

Same transit = different meaning depending on L1 chapter:

- "Saturn square Saturn" during Capricorn L1 = culmination of 27-year discipline chapter
- "Saturn square Saturn" during Aquarius L1 = integration test in innovation chapter

**L1 provides context** - without it, transits feel random. With it, they're part of coherent story.

---

### 5. Format Introduction Section

Take first H1 section from markdown (should be "Introduction"), ensure it:
- Has proper H2 heading (`## Introduction`)
- Is ~300 words
- Ends with page break: `<div class="page-break"></div>`

### 6. Format Main Content

Process remaining markdown:
- Convert H1 → H2 (main sections: "I. Inner Life")
- Convert H2 → H3 (subsections: "Emotional Landscape")
- Add page breaks strategically (prevent orphans/widows)
- Preserve all paragraph structure

### 7. Format Reflection Section (Poetic Wrapup)

**Detection Logic**:
- Look for `## Reflection` heading (explicitly provided by interpreter)
- Should contain 3-5 sentences
- Visionary/commanding voice

**Styling**:
- Keep `## Reflection` heading
- Ensure proper spacing before section
- Distinguish from body text with formatting

**Example**:
```markdown
## Reflection

Your path is clear. You are the teacher who serves through knowledge. There is within you a gift that only you can give—share it freely, and the world responds.
```

### 8. Add CSS and Generate PDF

```bash
python scripts/pdf_generator.py \
  formatted_output.md \
  output.pdf \
  --report-type natal
```

**CSS Loading by Report Type**:
- `natal` → `base.css` + `chart_based.css`
- `life_arc` → `base.css` + `timeline_based.css`
- `transit_short` → `base.css` + `movement_based.css`
- `transit_long` → `base.css` + `movement_based.css`

---

## Agent Specification

### Agent Metadata

```yaml
name: pdf-formatter
description: Formats plain markdown astrology reports into professionally styled PDFs with cover pages, table of contents, report-specific chart overview, and proper page layout.
model: sonnet
extended_thinking: false
color: cyan
```

### Agent Prompt (Condensed)

See full agent file for complete prompt. Key responsibilities:

1. **Read Input Files**: markdown + seed data
2. **Build Report Structure**:
   - Page 1: HTML title page
   - Page 2: Table of Contents
   - Page 3: Chart Overview (REPORT-SPECIFIC - see design doc)
   - Page 4: Introduction (~300 words)
   - Pages 5+: Main content
   - Final: Reflection section (poetic wrapup with heading)
3. **Generate Formatted Markdown**: Add HTML structure, page breaks
4. **Generate PDF**: Call pdf_generator.py with appropriate --report-type
5. **Confirm Success**: Report file paths to user

**Chart Overview Logic**:
- `natal` → Astrological data bullets (sect, ruler, dignities, auto-fill)
- `life_arc` → Major Life Events Timeline table (ages + accessible descriptions)
- `transit_short/long` → Current timing context (L1, L2, profections, active transits)

---

## Interpreter Simplification

### What to Remove from Interpreters

**Remove**:
- All HTML structure instructions (`<div class="title-page">`)
- CSS class specifications
- Page break instructions (`<div class="page-break"></div>`)
- Table of Contents generation instructions
- Chart Overview formatting instructions
- Title page formatting
- "Start with this exact HTML structure" directives

**Keep**:
- Content structure (H1, H2, H3 headings)
- Word count targets (300-word introduction, section lengths)
- Interpretation methodology
- Hierarchical framework
- RAG query instructions
- Reflection section requirements (`## Reflection` heading + 3-5 sentences)

### Example Simplified Instructions

**Before** (natal-interpreter-experiential, lines 178-189):
```markdown
### Page 1: Cover Page

**CRITICAL - START YOUR SYNTHESIS FILE WITH THIS EXACT HTML STRUCTURE**:

<div class="title-page">
  <h1>Natal Horoscope</h1>
  <div class="profile-name">[Profile Name]</div>
  <div class="birth-data">Born: [Date] at [Time]<br>[Location]<br>[Coordinates]</div>
  <div class="report-date">Report Generated: [Date]</div>
</div>

## Table of Contents
```

**After**:
```markdown
### Output Structure

Start your synthesis file with:

# Introduction

[300 words identifying PRIMARY life theme...]

# Inner Life

## Emotional Landscape

[500 words...]

[Continue with all sections...]

## Reflection

[3-5 sentence poetic wrapup with visionary voice]
```

---

## Implementation Plan

### Phase 1: Build pdf-formatter Agent

1. ✅ Create design document (this file)
2. Create agent file: `.claude/agents/pdf-formatter.md`
3. Implement Chart Overview logic for all 3 report types
4. Test with existing formatted markdown (manually created)
5. Verify PDF generation works correctly

### Phase 2: Simplify One Interpreter (Proof of Concept)

1. Simplify natal-interpreter-experiential.md
   - Remove HTML/CSS instructions (~80 lines)
   - Keep content structure and methodology
   - Update output instructions to plain markdown
   - Add `## Reflection` heading requirement
2. Test with Sam_P profile
3. Verify pdf-formatter produces correct output
4. Compare quality with manually created PDFs

### Phase 3: Update mode-orchestrator

1. Add pdf-formatter invocation after interpretation completes
2. Pass markdown file + seed data + profile info + report type
3. Handle errors gracefully
4. Confirm PDF generation success

### Phase 4: Migrate Remaining Interpreters

If POC successful:
1. Simplify natal-interpreter.md
2. Simplify life-arc-interpreter.md
3. Simplify transit-analyzer-short.md (when created)
4. Simplify transit-analyzer-long.md (when created)

### Phase 5: Documentation

1. Update DEVELOPMENT_GUIDE.md with new workflow
2. Update AGENTS_REFERENCE.md with pdf-formatter info
3. Update OUTPUT_STYLE_GUIDE.md with Reflection section standard
4. Archive this design document to /docs/

---

## Expected Benefits

### Token Reduction

| Agent | Current Lines | After Simplification | Reduction |
|-------|--------------|---------------------|-----------|
| natal-interpreter | 455 lines | ~375 lines | ~80 lines (17%) |
| natal-interpreter-experiential | 435 lines | ~355 lines | ~80 lines (18%) |
| life-arc-interpreter | 920 lines | ~840 lines | ~80 lines (9%) |

**Total reduction**: ~240 lines across 3 agents

### Maintainability

- **Single source of truth** for PDF formatting
- **Easy style changes** without touching interpreters
- **Consistent output** across all report types
- **Testable** formatting logic separately from interpretation
- **Report-specific Chart Overview** logic centralized

### Flexibility

- Could add new output formats (web, ebook, plain text)
- Could create multiple PDF styles (formal, modern, minimalist)
- Could generate different Chart Overview layouts per user preference
- Easy to A/B test different formatting approaches

---

## Testing Strategy

### Unit Tests

1. **pdf-formatter with valid inputs** → correct formatted markdown + PDF
2. **Chart Overview - natal** → fills to ~12 bullets intelligently
3. **Chart Overview - life_arc** → accessible timeline table with current age marked
4. **Chart Overview - transit** → L1 context + L2 + profections + active transits
5. **Table of Contents generation** → matches content structure
6. **Reflection section detection** → correctly identifies and styles with heading

### Integration Tests

1. **natal-interpreter-experiential → pdf-formatter** → valid PDF (Sam_P)
2. **life-arc-interpreter → pdf-formatter** → valid PDF (Darren_S)
3. **Verify content preservation** → no interpretation text lost
4. **Compare with manual PDFs** → quality matches or exceeds

### Quality Checks

- PDF opens correctly in Preview/Acrobat
- Page breaks appropriate (no orphaned headings)
- Chart Overview informative and report-appropriate
- Typography consistent with existing PDFs
- File sizes reasonable (~50-100KB for natal report)
- Reflection section properly formatted with heading

---

## Risks and Mitigations

### Risk 1: Chart Overview Logic Complexity

**Risk**: Three different Chart Overview formats could be complex to maintain
**Mitigation**: Clear separation in agent code, well-documented logic per report type

### Risk 2: Content Loss During Formatting

**Risk**: Markdown parsing could lose content or structure
**Mitigation**: Extensive testing, compare input/output word counts, manual review

### Risk 3: Interpreters Still Generate HTML

**Risk**: Agents might still output HTML despite simplified instructions
**Mitigation**: Clear examples in simplified prompts, test thoroughly, iterate instructions

### Risk 4: PDF Generation Failures

**Risk**: pdf_generator.py might fail with new formatted markdown
**Mitigation**: Test with multiple profiles, handle errors gracefully, log failures

### Risk 5: L1 Context Extraction for Transits

**Risk**: Extracting correct L1 periods from seed data for transit reports
**Mitigation**: Ensure seed data structure is consistent, add validation checks

---

## Success Criteria

1. ✅ pdf-formatter agent successfully formats Sam_P natal report
2. ✅ Generated PDF matches quality of manually created PDFs
3. ✅ Chart Overview contains appropriate content for report type:
   - Natal: ~10-12 astrological bullets
   - Life Arc: Timeline table with major events
   - Transit: L1 context + current timing state
4. ✅ All interpretation content preserved
5. ✅ Reflection section formatted with heading
6. ✅ natal-interpreter-experiential simplified by ~80 lines
7. ✅ Token usage reduced in agent prompts
8. ✅ Formatting changes now isolated to one agent

---

## Future Enhancements

### Short-Term
- Add Chart Overview customization per profile (verbose vs minimal)
- Generate Chart Overview diagram (visual wheel/aspects) for natal reports
- Add "Glossary" page for astrological terms
- Variable timeline detail for life arc reports (5-year increments vs every year)

### Long-Term
- Multiple PDF style templates (formal, modern, minimalist)
- Web output format (HTML with interactive timeline for life arc)
- ePub/Kindle format for e-readers
- Customizable page layouts per user preference
- Interactive Chart Overview (clickable elements in digital versions)

---

**Status**: Design Complete - Ready for Implementation
**Next Step**: Create pdf-formatter agent
**Owner**: Claude Code
**Date**: 2025-10-16
