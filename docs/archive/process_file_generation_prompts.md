# Process File Generation Prompts - Archive

**Purpose**: This file archives all process file generation instructions that were removed from interpreter agent prompts to optimize token usage.

**Date Archived**: 2025-10-18
**Reason**: Process files consume 1,500-2,500 tokens per agent invocation but are unused by accuracy-checker (which verifies synthesis directly against seed_data). Removing these instructions saves 15-25% of prompt tokens per report.

**Token Savings**:
- Per agent invocation: 1,500-2,500 tokens (prompt optimization)
- Per report generation: 6,000-9,000 tokens (no process file output)
- Total per report: 7,500-11,500 tokens (30-35% reduction)

**Organization**: Organized by **process file type** (Natal, Life Arc, Transit) since each report type has distinct process file structures.

---

## Overview: Three Process File Types

### Type 1: Natal Process File
**Used by**: `natal-interpreter.md`, `natal-interpreter-experiential.md`

**Structure** (9 sections):
1. Chart Overview (sect, chart ruler, angular planets, stelliums, patterns)
2. Hierarchical Testimony Analysis (PRIMARY/SECONDARY/TERTIARY factors)
3. Core Identity (Sun/Moon/ASC with technical language)
4. Planetary Placements (signs, houses, dignities, aspects)
5. Benefic/Malefic Dynamics (sect considerations)
6. Major Life Themes (brief summary)
7. Planetary Strength Table
8. Custom Modifications (if applicable - date, user request, applied changes)
9. Sources (full bibliography)

### Type 2: Life Arc Process File
**Used by**: `life-arc-interpreter-v3.md`

**Structure** (timing-focused):
- Technical timing data for astrologers
- Profections table
- ZR L1/L2/L3 periods
- Firdaria, returns, progressions details
- Convergence scores and methodology
- V3 scoring breakdown (traditional overlays, Saturn aftermath, 15 lots)

### Type 3: Transit Process File
**Used by**: `transit-analyzer-long.md`

**Structure** (vaguely specified):
- Technical data
- Timing context
- Transit counts

---

# TYPE 1: NATAL PROCESS FILE

## Agent 1: natal-interpreter.md

**Lines Removed**: 364-377, 481-494, 511, 516-522

### Section 1: Technical Sections Header (Lines 364-377)

**Context**: This section defines what goes into the natal process file.

```markdown
## Technical Sections (Separate Process File)

Generate these sections for technical reference, but save them to `natal_process_{profile_name}_{date}.md`:

**I. Chart Overview** - Sect, chart ruler, angular planets, stelliums, patterns
**II. Hierarchical Testimony Analysis** - PRIMARY/SECONDARY/TERTIARY factors for each life area
**III. Core Identity** - Sun/Moon/ASC with technical language
**IV. Planetary Placements** - Signs, houses, dignities, aspects
**V. Benefic/Malefic Dynamics** - Sect considerations
**VI. Major Life Themes** - Brief summary
**VII. Planetary Strength Table**
**VIII. Custom Modifications** (if applicable) - Date, user request, applied changes
**IX. Sources** - Full bibliography

---
```

**Restoration Instructions**: Insert this section before `## Workflow` header (around line 364).

---

### Section 2: Custom Modifications Documentation (Lines 481-494)

**Context**: Instructions for documenting user-requested interpretation adjustments in the process file.

```markdown
### Step 11: Check for Custom Modifications
If user provided custom context or requested adjustments during generation (e.g., "emphasize technical skills", "soften language around finances"), document in process file:

**In process file, add section**:
```markdown
## Custom Modifications

- YYYY-MM-DD: [Description of modification and reasoning]
  - User request: "[User's specific guidance]"
  - Applied changes: [What was adjusted in interpretation]
```

**In seed data metadata**: Ensure `output_mode: Modified` is set in `seed_data['metadata']['output_mode']` (this will display in Chart Overview).

**If no custom modifications**: Leave this section out of process file, seed data will default to `output_mode: Standard`.
```

**Restoration Instructions**: Insert as Step 11 in the Workflow section (around line 481).

---

### Section 3: Quality Check Reference (Line 511)

**Context**: Quality checklist item referencing process file documentation.

```markdown
- ✅ **If custom modifications were made, document in process file and verify output_mode: Modified in seed data**
```

**Restoration Instructions**: Add to Step 12 quality check list (around line 511).

**Updated (Synthesis-Only)**: Remove this line entirely or change to:
```markdown
- ✅ **If custom modifications were made, verify output_mode: Modified in seed data**
```

---

### Section 4: Save Files Instructions (Lines 516-522)

**Context**: Final step instructing agent to save both process and synthesis files.

```markdown
### Step 13: Save Files
After completing interpretation and quality check:

1. **Save Process File**: `profiles/{profile_name}/output/natal_process_{profile_name}_{date}.md`
   - Include Custom Modifications section if user provided custom guidance
2. **Save Synthesis File**: `profiles/{profile_name}/output/natal_synthesis_{profile_name}_{date}.md`
3. **Confirm Success**: Report both file paths to user

**NOTE**: PDF generation is handled automatically by mode-orchestrator after this agent completes. You only need to generate the two markdown files.
```

**Restoration Instructions**: Replace Step 13 entirely (around line 516).

**Updated (Synthesis-Only)**:
```markdown
### Step 13: Save File
After completing interpretation and quality check:

1. **Save Synthesis File**: `profiles/{profile_name}/output/natal_synthesis_{profile_name}_{date}.md`
2. **Confirm Success**: Report file path to user

**NOTE**: PDF generation is handled automatically by mode-orchestrator after this agent completes.
```

---

## Agent 2: natal-interpreter-experiential.md

**Lines Removed**: 410-424, 511-524, 541-542

### Section 1: Technical Sections Header (Lines 410-424)

**Context**: Same as natal-interpreter.md but for experiential domain structure.

```markdown
## Technical Sections (Separate Process File)

Generate these sections for technical reference, but save them to `natal_process_{profile_name}_{date}.md`:

**I. Chart Overview** - Sect, chart ruler, angular planets, stelliums, patterns
**II. Hierarchical Testimony Analysis** - PRIMARY/SECONDARY/TERTIARY factors for each domain
**III. Core Identity** - Sun/Moon/ASC with technical language
**IV. Planetary Placements** - Signs, houses, dignities, aspects
**V. Benefic/Malefic Dynamics** - Sect considerations
**VI. Major Life Themes** - Brief summary
**VII. Planetary Strength Table**
**VIII. Custom Modifications** (if applicable) - Date, user request, applied changes
**IX. Sources** - Full bibliography

---
```

**Note**: Nearly identical to natal-interpreter.md, only difference is "each domain" vs "each life area" in section II.

**Restoration Instructions**: Insert before `## Workflow` header (around line 410).

---

### Section 2: Custom Modifications Documentation (Lines 511-524)

**Context**: Identical to natal-interpreter.md custom modifications section.

```markdown
### Step 11: Check for Custom Modifications
If user provided custom context or requested adjustments during generation (e.g., "emphasize technical skills", "soften language around finances"), document in process file:

**In process file, add section**:
```markdown
## Custom Modifications

- YYYY-MM-DD: [Description of modification and reasoning]
  - User request: "[User's specific guidance]"
  - Applied changes: [What was adjusted in interpretation]
```

**In seed data metadata**: Ensure `output_mode: Modified` is set in `seed_data['metadata']['output_mode']` (this will display in Chart Overview).

**If no custom modifications**: Leave this section out of process file, seed data will default to `output_mode: Standard`.
```

**Restoration Instructions**: Insert as Step 11 in Workflow section (around line 511).

---

### Section 3: Quality Check & Save Files (Lines 541-542)

**Context**: Quality check item and save files instructions.

```markdown
- ✅ **If custom modifications were made, document in process file and verify output_mode: Modified in seed data**

1. **Save Process File**: `profiles/{profile_name}/output/natal_process_{profile_name}_{date}.md`
   - Include Custom Modifications section if user provided custom guidance
```

**Restoration Instructions**: Add to Step 12 quality check and Step 13 save files (around lines 541-542).

**Updated (Synthesis-Only)**:
```markdown
- ✅ **If custom modifications were made, verify output_mode: Modified in seed data**

1. **Save Synthesis File**: `profiles/{profile_name}/output/natal_synthesis_{profile_name}_{date}.md`
```

---

# TYPE 2: LIFE ARC PROCESS FILE

## Agent 3: life-arc-interpreter-v3.md

**Lines Removed**: 727-733, 757, 765, 879-886

### Section 1: Output File Path Reference (Lines 727-733)

**Context**: Specifies what the life arc process file contains (timing-focused).

```markdown
   **Process File**: `profiles/{profile}/output/life_arc_process_{profile}_ages_{start}-{end}_v3_{YYYY-MM-DD}.md`
   - Technical timing data for astrologers
   - Profections table, ZR L1/L2/L3 periods
   - Firdaria, returns, progressions details
   - Convergence scores and methodology
   - V3 scoring breakdown (traditional overlays, Saturn aftermath, 15 lots)

   **Synthesis File**: `profiles/{profile}/output/life_arc_synthesis_{profile}_ages_{start}-{end}_v3_{YYYY-MM-DD}.md`
```

**Restoration Instructions**: Insert in output files section (around line 727).

**Updated (Synthesis-Only)**: Remove process file lines, keep only synthesis file specification.

---

### Section 2: Custom Modifications Documentation (Line 757)

**Context**: Brief reference to documenting custom modifications.

```markdown
   - Document in process file with date, request, and applied changes
```

**Restoration Instructions**: Add to custom modifications workflow step (around line 757).

**Updated (Synthesis-Only)**: Remove this line or change to reference seed data only.

---

### Section 3: File Paths Confirmation (Line 765)

**Context**: Return confirmation message mentioning both files.

```markdown
   - File paths confirmation (process.md, synthesis.md)
```

**Restoration Instructions**: Add to workflow completion step (around line 765).

**Updated (Synthesis-Only)**:
```markdown
   - File path confirmation (synthesis.md)
```

---

### Section 4: Output Template Reference (Lines 879-886)

**Context**: Example showing what life arc process file contains.

```markdown
**Process File** (life_arc_process.md):
- Technical timing data
- Profections table, ZR L1/L2/L3 periods
- Firdaria, returns, progressions
- Convergence scores and methodology
- V3 scoring breakdown (traditional overlays, Saturn aftermath, 15 lots)
- For astrologers and verification

**Synthesis File** (life_arc_synthesis.pdf):
```

**Restoration Instructions**: Insert in examples/templates section (around line 879).

**Updated (Synthesis-Only)**: Remove process file description entirely.

---

# TYPE 3: TRANSIT PROCESS FILE

## Agent 4: transit-analyzer-long.md

**Lines Removed**: 279, 510

### Section 1: Output File Path (Line 279)

**Context**: Specifies transit process file path in file paths section.

```markdown
- `profiles/{profile}/output/transit_report_{profile}_{duration}_{start-date}_to_{end-date}_process.md` (technical data)
```

**Restoration Instructions**: Add to file paths list (around line 279).

**Updated (Synthesis-Only)**: Remove this line entirely.

---

### Section 2: Save Files Instructions (Line 510)

**Context**: Workflow step specifying process file path with versioning.

```markdown
   - **Process file**: `profiles/{profile}/output/transit_report_{profile}_{duration}_{start-date}_to_{end-date}[_vN]_process.md` (technical data, timing context, transit counts)
```

**Restoration Instructions**: Add to save files workflow step (around line 510).

**Updated (Synthesis-Only)**: Remove this line entirely.

---

# AGENTS WITHOUT PROCESS FILES

## Agent 5: transit-analyzer-short.md

**No process file instructions found** - This agent generates synthesis-only output already.

**Lines containing "process"**: Only found in context of "mental processes" (planet interpretation) and "RAG Response Processing" (workflow step). No file generation instructions.

---

# SUMMARY

## Affected Agents by Type

**Type 1 - Natal Process File** (2 agents):
- `natal-interpreter.md` (4 sections removed)
- `natal-interpreter-experiential.md` (3 sections removed)

**Type 2 - Life Arc Process File** (1 agent):
- `life-arc-interpreter-v3.md` (4 sections removed)

**Type 3 - Transit Process File** (1 agent):
- `transit-analyzer-long.md` (2 sections removed)

**Total**: 4 agents updated, 13 sections removed

## Token Savings Breakdown

**Per Agent Invocation** (prompt optimization):
- Natal agents: ~2,000 tokens saved each
- Life arc agent: ~1,800 tokens saved
- Transit long agent: ~400 tokens saved
- **Average**: ~1,550 tokens per agent invocation

**Per Report Generation** (no process file output):
- Natal: ~8,000 tokens saved
- Life arc: ~7,000 tokens saved
- Transit long: ~5,000 tokens saved
- **Average**: ~6,700 tokens per report

**Total Per Report**: ~8,250 tokens saved (32% reduction)

## Related Documentation Updates Needed

1. **docs/OUTPUT_STYLE_GUIDE.md** - Remove "Two-File Standard" section
2. **docs/DEVELOPMENT_GUIDE.md** - Update workflow to single-file
3. **docs/PROFILE_STRUCTURE.md** - Deprecate `include_process_file` setting
4. **.claude/agents/mode-orchestrator.md** - Update file expectations
5. **.claude/agents/accuracy-checker.md** - Already correct (uses seed_data)

## Restoration Procedure

If process files need to be restored for any reason:

1. **Open this archive file** and locate the relevant agent and section
2. **Open the agent file** in `.claude/agents/`
3. **Copy the archived instructions** from the appropriate section
4. **Insert at line numbers specified** in restoration instructions
5. **Update OUTPUT_STYLE_GUIDE.md** to document two-file workflow
6. **Test with one report** to verify process file generation works
7. **Update specification** to note restoration completed

---

**Archived by**: Process file removal implementation (Specification v2.0)
**Archive Date**: 2025-10-18
**Specification**: `/docs/remove_process_files_specification.md`
**Git Commit**: TBD (will be added when changes committed)
