# Custom Modifications System

**Status**: Implemented (2025-10-16)

---

## Overview

The custom modifications tracking system allows you to request specific adjustments to interpretation output while maintaining institutional memory of what was changed and why.

## Use Cases

### 1. Emphasizing Specific Themes
- User: "Emphasize Sam's technical and artistic skills"
- Agent applies emphasis in relevant sections
- Documents modification in process file

### 2. Softening Challenging Language
- User: "Sam has faced financial struggles - please be sensitive with language around money/resources"
- Agent adjusts tone in 2nd house / resources sections
- Documents modification in process file

### 3. Context-Specific Adjustments
- User: "This person is going through a career transition - emphasize adaptability"
- Agent weaves career transition context throughout
- Documents modification in process file

---

## How It Works

### 1. User Provides Custom Context

When generating a report, provide custom instructions to mode-orchestrator or the interpretation agent:

```
Generate natal horoscope for Sam_P. Note: Sam is a skilled technical artist who has
faced financial struggles. Emphasize his creative/technical abilities and be sensitive
with language around resources/money.
```

### 2. Agent Applies Custom Guidance

The interpretation agent naturally incorporates the custom guidance throughout the interpretation:
- **Natal interpreters**: Adjustments applied in Step 6 (Craft Synthesis Section)
- **Life arc interpreters**: Adjustments applied in Step 6 (Write Narrative Life Story)
- **Example**: If user says "emphasize technical skills", agent will:
  - Highlight Mercury-Venus placements in Career section
  - Emphasize problem-solving abilities in Strengths section
  - Connect technical themes throughout synthesis

### 3. Agent Documents in Process File

The interpretation agent adds a "Custom Modifications" section to the process file:

```markdown
## Custom Modifications

- 2025-10-16: Emphasized technical/artistic skills, softened language around finances
  - User request: "Sam is a skilled technical artist who has faced financial struggles.
    Emphasize his creative/technical abilities and be sensitive with language around
    resources/money."
  - Applied changes:
    - Highlighted Mercury-Venus technical creativity in Career section
    - Emphasized artistic problem-solving in Strengths section
    - Used gentle, therapeutic language in 2nd house (resources) section
    - Focused on creative potential rather than material challenges
```

### 4. Chart Overview Shows "Modified" Status

The Chart Overview in the PDF includes an "Output Mode" field:

**Standard Report**:
```
Output Mode: Standard
Sect: Day
Chart Ruler: Moon
...
```

**Modified Report**:
```
Output Mode: Modified
Sect: Day
Chart Ruler: Moon
...
```

This appears on the Chart Overview page (between title page and synthesis content). It's **cryptic enough** that the recipient won't know specifics, but **professional enough** to look intentional.

### 5. Metadata Stored in Seed Data

The `output_mode` is stored in seed_data.json metadata:

```json
{
  "metadata": {
    "output_mode": "Modified",
    "generation_date": "2025-10-16",
    ...
  }
}
```

This allows the PDF generator to extract and display the status automatically.

---

## Workflow Integration

### Standard Generation (No Modifications)
1. User: "Generate natal horoscope for Darren_S"
2. Agent generates interpretation with standard approach
3. Process file: No "Custom Modifications" section
4. Seed data: `output_mode: Standard` (default)
5. Chart Overview displays: "Output Mode: Standard"

### Custom Generation (With Modifications)
1. User: "Generate natal for Sam_P. Emphasize technical skills, soften money language."
2. Agent generates interpretation with requested adjustments
3. Agent documents modifications in process file with date/request/changes
4. Agent ensures seed data includes `output_mode: Modified`
5. Chart Overview displays: "Output Mode: Modified"

---

## What Gets Tracked

### In Process File (Internal Documentation)
- **Date**: When modification was made
- **User Request**: Exact guidance provided
- **Applied Changes**: What sections were adjusted and how

### In Chart Overview (External Signal)
- **Output Mode field**: "Standard" or "Modified"
- No details about what was modified (cryptic by design)

### In Seed Data Metadata
- **output_mode**: "Standard" or "Modified"
- Enables automatic Chart Overview generation

---

## Benefits

### 1. Institutional Memory
- Track what was customized across multiple reports
- Remember context for future regenerations
- Understand evolution of interpretation approach

### 2. Professional Presentation
- Recipient sees "Modified" indicator without knowing specifics
- Looks intentional and professional
- No awkward explanations needed

### 3. Quality Control
- Verify modifications were applied correctly
- Audit interpretation decisions
- Maintain consistency across custom reports

---

## Future Enhancement: Difficulty Flag System

**Status**: Planned (see session_goals.md)

Automatically detect challenging chart configurations and adjust tone:

**Detection Criteria**:
- Angular malefics contrary to sect
- Hard aspects to chart ruler or sect light
- Multiple detriment/fall planets in angular houses
- Chiron or Saturn in prominent positions (1st, 10th)
- Major T-squares or grand crosses affecting angles

**Difficulty Categories**:
- `standard` - Normal tone
- `sensitive` - Softer language recommended
- `gentle` - Therapeutic approach needed

**Implementation**: Add `difficulty_assessment` field to seed_data.json, interpreter agents check flag and adjust voice automatically.

**Benefit**: Reduces need for manual custom modifications in challenging charts.

---

## Agent Instructions

### natal-interpreter.md
- **Step 6**: Apply custom modifications during synthesis (if user provided guidance)
- **Step 11**: Document custom modifications in process file
- **Step 12**: Quality Check includes verifying custom mod documentation
- **Step 13**: Save Files includes Custom Modifications section in process file
- Technical Sections template includes "Custom Modifications" section

### natal-interpreter-experiential.md
- **Step 6**: Apply custom modifications during synthesis (if user provided guidance)
- **Step 11**: Check for Custom Modifications (same as standard natal-interpreter)
- Technical Sections template includes "Custom Modifications" section

### life-arc-interpreter.md
- **Step 6**: Apply custom modifications during narrative writing (if user provided guidance)
- **Step 9**: Document custom modifications in process file
- Same documentation approach as natal interpreters

### life-arc-interpreter-v3.md
- **Step 6**: Apply custom modifications during narrative writing (if user provided guidance)
- **Step 9**: Document custom modifications in process file
- Same documentation approach as natal interpreters

### pdf_generator.py
- Lines 342-354: Extract `output_mode` from seed_data metadata
- Display as first field in Chart Overview
- Default to "Standard" if not specified

---

## Testing

**Test Case**: Generate a report with custom instructions and verify:
1. ✅ Process file includes "Custom Modifications" section
2. ✅ Seed data metadata includes `output_mode: Modified`
3. ✅ Chart Overview displays "Output Mode: Modified"
4. ✅ Interpretation reflects requested adjustments

**Next Steps**: Test with Sam_P profile using financial sensitivity guidance.

---

*Created: 2025-10-16*
*System Version: 1.0*
