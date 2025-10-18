# Remove Process Files from Interpretation Workflow - Specification

**Version**: 2.0 (AGGRESSIVE REMOVAL)
**Created**: 2025-10-18
**Updated**: 2025-10-18
**Status**: Draft - Pending Approval
**Estimated Impact**: Very High (1,500-2,500 token reduction PER AGENT INVOCATION, 40-60% reduction in output)

---

## Overview

### Problem Statement

The current two-file output system generates both process files (technical analysis with astrological jargon) and synthesis files (user-facing narrative) for every interpretation. Process files were originally included for verification purposes, but the accuracy-checker agent does NOT use them—it verifies synthesis files directly against seed_data. This creates TWO LAYERS of unnecessary cost:

1. **Output tokens**: 6,000-9,000 tokens per report (40-60% of total output)
2. **Prompt tokens**: 1,500-2,500 tokens per agent invocation (15-25% of each agent's prompt)

The process file generation instructions occupy significant space in every interpreter agent's prompt, consuming tokens EVERY TIME the agent is invoked, whether or not process files are generated.

### Goals (Version 2.0 - Aggressive Approach)

1. **Eliminate prompt token waste** - Remove 1,500-2,500 tokens PER AGENT INVOCATION by deleting process file instructions entirely
2. **Eliminate output token waste** - Remove 40-60% of interpretation output tokens by stopping process file generation
3. **Simplify agent prompts** - Cleaner, more focused instructions without conditional logic
4. **Archive, don't delete** - Preserve process file instructions in case reversal is needed
5. **Maintain quality** - accuracy-checker continues working (already uses seed_data, not process files)

### Non-Goals

- Changing accuracy-checker workflow (already doesn't use process files)
- Modifying PDF generation (already only uses synthesis files)
- Altering synthesis content or quality
- Removing seed_data files (these ARE used for verification)
- Deleting historical process files (leave in output folders as-is)

---

## Requirements

### Functional Requirements (Version 2.0 - Aggressive)

1. **Interpreter agents MUST NOT generate process files** (no conditional logic, no setting check)
2. **Process file generation instructions MUST be removed from ALL interpreter agent prompts**
3. **Removed instructions MUST be archived** to `/docs/archive/process_file_generation_prompts.md`
4. **Profile setting `include_process_file` becomes non-functional** (kept in profile.md as documentation only)
5. **accuracy-checker MUST continue working without process files** (no changes needed)
6. **PDF generation MUST continue working** (no changes needed)
7. **Documentation MUST reflect single-file workflow as ONLY workflow**

### Non-Functional Requirements

- **Prompt token savings**: 1,500-2,500 tokens PER AGENT INVOCATION (15-25% of prompt)
- **Output token savings**: 6,000-9,000 tokens per report (40-60% of output)
- **Reversibility**: Archived instructions can be restored if needed
- **Zero regression**: accuracy-checker and PDF generation unaffected
- **Cleaner codebase**: Simpler agent prompts, easier to maintain

### Edge Cases

1. **Profile has `include_process_file: true`**: Setting ignored, no process file generated (inform user via documentation)
2. **User requests process file**: Direct them to archived instructions, explain token cost
3. **Existing profiles with old reports**: No migration needed, old process files remain in output folders
4. **Future agent creation**: astrology-agent-creator template does NOT include process file instructions

---

## Design

### Architecture (Version 2.0 - Aggressive)

**Current State (Two-File System with Prompt Bloat)**:
```
User Request → mode-orchestrator → interpreter agent (10,000 token prompt):
  - 1,500-2,500 tokens: Process file generation instructions
  - 7,500-8,500 tokens: Synthesis instructions + workflow
  → Agent generates TWO files:
    1. {type}_process_{profile}_{date}.md (6,000-9,000 tokens, unused)
    2. {type}_synthesis_{profile}_{date}.md (6,000-9,000 tokens, used)
  → accuracy-checker (reads synthesis + seed_data, ignores process)
  → pdf_generator.py (reads synthesis, ignores process)
  → COST: 1,500-2,500 prompt tokens + 6,000-9,000 output tokens WASTED
```

**Proposed State (Single-File System, Clean Prompts)**:
```
User Request → mode-orchestrator → interpreter agent (7,500-8,500 token prompt):
  - 0 tokens: Process file instructions (REMOVED)
  - 7,500-8,500 tokens: Synthesis instructions + workflow (UNCHANGED)
  → Agent generates ONE file:
    1. {type}_synthesis_{profile}_{date}.md (6,000-9,000 tokens, used)
  → accuracy-checker (reads synthesis + seed_data) ✓ UNCHANGED
  → pdf_generator.py (reads synthesis) ✓ UNCHANGED
  → SAVINGS: 1,500-2,500 prompt tokens + 6,000-9,000 output tokens per report
```

### Data Flow (Version 2.0)

**Input**: Profile settings (`profiles/{name}/profile.md`)
```ini
[INTERPRETATION_SETTINGS]
include_process_file: false  # NON-FUNCTIONAL (kept for documentation only)
                             # Setting no longer checked by agents
```

**Processing**: Interpreter agent (NO setting check)
```python
# NEW behavior: No conditional logic, always synthesis only
generate_synthesis_file()  # ONLY action
# Process file generation code REMOVED from agent prompt
```

**Output**: One file to `profiles/{name}/output/`
- **Always**: `{type}_synthesis_{name}_{date}.md` + PDF
- **Never**: `{type}_process_{name}_{date}.md` (removed entirely)

### Extraction & Archive Plan

**Step 1: Extract Process File Instructions from Each Agent**

For each interpreter agent, identify and extract:
- Process file format specifications
- Process file content requirements
- Process file writing instructions
- Process file quality checks
- Any conditional logic related to process files

**Step 2: Archive Structure** (`/docs/archive/process_file_generation_prompts.md`)

```markdown
# Process File Generation Instructions - ARCHIVED

**Archived**: 2025-10-18
**Reason**: Token optimization (1,500-2,500 tokens per agent invocation)
**Restoration**: Copy sections back to agent prompts if reversal needed

---

## natal-interpreter.md - Process File Instructions

### Section: Output File Generation (Step 13)

[EXTRACTED INSTRUCTIONS HERE]

### Section: Process File Format

[EXTRACTED INSTRUCTIONS HERE]

### Section: Quality Checks

[EXTRACTED INSTRUCTIONS HERE]

---

## life-arc-interpreter-v3.md - Process File Instructions

[Similar structure for each agent]

---

## Transit Analyzers - Process File Instructions

[Combined or separate sections for transit-analyzer-short and transit-analyzer-long]

---

## Restoration Instructions

To restore process file generation:
1. Copy relevant section from this archive
2. Paste into agent prompt at original location
3. Update OUTPUT_STYLE_GUIDE.md to reflect two-file standard
4. Update profile.md template to make `include_process_file` functional
```

### Integration Points

**Unchanged Components** (no modifications needed):
- `accuracy-checker` - Already uses synthesis + seed_data
- `pdf_generator.py` - Already uses synthesis only
- `mode-orchestrator` - Expects synthesis file path (already correct)
- Seed data generation - No changes

**Modified Components (DELETION ONLY)**:
1. **Interpreter Agents** (7+ agents):
   - natal-interpreter.md - REMOVE all process file instructions
   - natal-interpreter-experiential.md - REMOVE all process file instructions
   - life-arc-interpreter-v3.md - REMOVE all process file instructions
   - transit-analyzer-short.md - REMOVE all process file instructions
   - transit-analyzer-long.md - REMOVE all process file instructions
   - [Future interpreters created without process file instructions]

2. **Documentation Files** (UPDATE to reflect single-file only):
   - OUTPUT_STYLE_GUIDE.md - Remove "Two-File Standard" section entirely
   - DEVELOPMENT_GUIDE.md - Update interpreter workflow to single-file
   - AGENTS_REFERENCE.md - Document single-file output for all interpreters
   - mode-orchestrator.md - Update workflow step 7 to expect one file only
   - astrology-agent-creator.md - Update template to exclude process file instructions

3. **Profile Templates** (MARK AS NON-FUNCTIONAL):
   - profile.md template - Add comment that `include_process_file` is deprecated
   - Existing profiles: No migration (setting ignored)

---

## Implementation Plan (Version 2.0 - Aggressive Removal)

### Phase 1: Extraction & Archive (High Priority, Low Risk)

**Step 1.1: Create Archive File**
- Create `/docs/archive/process_file_generation_prompts.md`
- Add header with archival metadata (date, reason, restoration instructions)

**Step 1.2: Extract from natal-interpreter.md**
1. Read `.claude/agents/natal-interpreter.md`
2. Identify all sections related to process file generation:
   - Search for "process_file", "process.md", "{type}_process_"
   - Output file format specifications (2-file system)
   - Process file content requirements (astrological jargon, technical breakdown)
   - Writing instructions (Step 13 or similar)
   - Quality checks (verify both files exist)
3. Copy ALL extracted sections to archive with clear section headers
4. Note original line numbers or section locations for easy restoration

**Step 1.3: Extract from life-arc-interpreter-v3.md**
- Repeat extraction process
- Document period-based process file requirements
- Archive convergence detection process file sections

**Step 1.4: Extract from Transit Analyzers**
- transit-analyzer-short.md - Extract transit-specific process instructions
- transit-analyzer-long.md - Extract multi-year transit process instructions
- May combine into single "Transit Analyzers" section if similar

**Step 1.5: Extract from Other Interpreters**
- natal-interpreter-experiential.md
- Any other current or planned interpreters

**Validation**:
- Archive file contains ALL process file instructions from ALL agents
- Each section clearly labeled with source agent
- Restoration instructions clear and actionable
- Original line numbers or locations documented

---

### Phase 2: Agent Prompt Cleanup (High Priority, Medium Risk)

**For EACH interpreter agent** (natal-interpreter, life-arc-interpreter-v3, transit-analyzer-short, transit-analyzer-long, natal-interpreter-experiential):

**Step 2.1: Remove Process File Instructions**
1. Delete ALL sections extracted in Phase 1
2. Remove conditional logic for process file generation
3. Remove process file format specifications
4. Remove process file writing steps
5. Remove quality checks for process file existence

**Step 2.2: Update Workflow Steps**
- **Old**: "Step 13: Save Files - 1. Process file ({type}_process_{name}_{date}.md), 2. Synthesis file ({type}_synthesis_{name}_{date}.md)"
- **New**: "Step 13: Save File - Generate synthesis file: {type}_synthesis_{name}_{date}.md"

**Step 2.3: Simplify Output Instructions**
- Remove all references to "two files"
- Change to "Generate ONE output file (synthesis)"
- Emphasize synthesis as sole deliverable
- Remove any mention of process files

**Step 2.4: Update Quality Checks**
- **Old**: "Verify both files exist: process.md and synthesis.md"
- **New**: "Verify synthesis file exists: {type}_synthesis_{name}_{date}.md"

**Step 2.5: Remove Profile Setting References**
- Delete any checks for `include_process_file` setting
- Remove conditional logic based on setting
- No setting checks needed (always synthesis only)

**Order of Updates**:
1. natal-interpreter.md (most frequently used, highest impact)
2. life-arc-interpreter-v3.md (second most used, complex structure)
3. transit-analyzer-long.md (moderate complexity)
4. transit-analyzer-short.md (moderate complexity)
5. natal-interpreter-experiential.md (least used, lowest priority)

**Validation per Agent**:
- Agent prompt size reduced by 1,500-2,500 tokens (15-25%)
- No references to process files remain
- Synthesis instructions clear and complete
- No broken workflow steps
- Test generation: Only synthesis file created

---

### Phase 3: Documentation Updates (Medium Priority, Low Risk)

**Step 3.1: Update OUTPUT_STYLE_GUIDE.md**
- **REMOVE**: Entire "Two-File Standard" section
- **ADD**: New "Single-File Standard" section
  - Synthesis file is ONLY output
  - Format specifications for synthesis
  - No mention of process files
- **UPDATE**: Chart Overview template sections (already synthesis-focused, verify)
- **ADD**: Historical note: "Process files were deprecated in Oct 2025 for token optimization"

**Step 3.2: Update mode-orchestrator.md**
- **Step 7 (OLD)**: "Agent produces TWO files: process and synthesis"
- **Step 7 (NEW)**: "Agent produces synthesis file: {type}_synthesis_{name}_{date}.md"
- **Step 9 (OLD)**: "Verify both files exist"
- **Step 9 (NEW)**: "Verify synthesis file exists"
- Remove any process file handling logic

**Step 3.3: Update DEVELOPMENT_GUIDE.md**
- **Section: Interpreter Creation Workflow**
  - Change from two-file to single-file output
  - Remove process file generation instructions
  - Update examples to show synthesis only
- **Section: Output Standards**
  - Reference OUTPUT_STYLE_GUIDE.md single-file section
  - Remove two-file workflow diagrams

**Step 3.4: Update AGENTS_REFERENCE.md**
- For each interpreter agent entry:
  - Change "Output: 2 files (process + synthesis)" → "Output: 1 file (synthesis)"
  - Remove process file descriptions
  - Update examples to show synthesis only

**Step 3.5: Update astrology-agent-creator.md**
- **Template Extraction**: Remove process file template sections
- **Agent Creation Instructions**: Default to single-file output
- **OUTPUT_STYLE_GUIDE.md Template**: Extract only synthesis sections (not process)
- **Quality Checks**: Remove "verify both files" instructions

**Step 3.6: Update PROFILE_STRUCTURE.md**
- Mark `include_process_file` as DEPRECATED
- Add note: "Setting no longer functional as of Oct 2025"
- Document historical purpose
- Remove from "active settings" list

**Validation**:
- Grep for "two-file", "two file", "2 files" → Should return zero results in active docs
- Grep for "process_file" → Should only appear in archive and deprecation notes
- All interpreter workflows describe single-file output
- All examples show synthesis only

---

### Phase 4: Profile Template Updates (Low Priority, Low Risk)

**Step 4.1: Update profile.md Template**
```ini
[INTERPRETATION_SETTINGS]

# OUTPUT SETTINGS
# include_process_file: false  # DEPRECATED (Oct 2025) - No longer functional
                               # All reports generate synthesis file only
                               # Process files removed for token optimization
```

**Step 4.2: Existing Profiles**
- **No migration required** - Setting simply ignored
- Users with `include_process_file: true` → Setting has no effect
- Document in PROFILE_STRUCTURE.md deprecation notice

**Validation**:
- New profiles created with deprecated setting commented out
- Existing profiles work without modification
- No errors if setting present (just ignored)

---

## Testing Strategy (Version 2.0)

### Unit Tests

**Test Case 1: Default Behavior (Setting Ignored)**
- **Given**: Profile has no `include_process_file` setting
- **When**: natal-interpreter runs after prompt cleanup
- **Then**: ONLY synthesis file generated
- **Validation**:
  - File count: 1 (synthesis.md only)
  - accuracy-checker passes (reads synthesis + seed_data)
  - PDF generates successfully
  - No errors or warnings about missing process file

**Test Case 2: Setting Present But Ignored**
- **Given**: Profile has `include_process_file: true` (legacy setting)
- **When**: life-arc-interpreter-v3 runs after prompt cleanup
- **Then**: ONLY synthesis file generated (setting ignored)
- **Validation**:
  - File count: 1 (synthesis.md only)
  - No process file created despite setting = true
  - accuracy-checker passes
  - PDF generates successfully

**Test Case 3: Prompt Token Reduction**
- **Given**: natal-interpreter.md before and after cleanup
- **When**: Measure prompt token count
- **Then**: Reduction of 1,500-2,500 tokens (15-25%)
- **Validation**:
  - Before: ~10,000 tokens
  - After: ~7,500-8,500 tokens
  - All synthesis instructions intact
  - No broken references

### Integration Tests

**Workflow Test 1: Full Natal Report Pipeline (Post-Cleanup)**
```
1. Profile: No include_process_file setting (or any value - ignored)
2. mode-orchestrator → natal-interpreter (cleaned prompt) → synthesis ONLY
3. accuracy-checker validates synthesis against seed_data → PASS
4. pdf_generator.py creates PDF from synthesis → SUCCESS
5. Files: synthesis.md, synthesis.pdf ONLY (no process.md ever created)
6. Token savings: 1,500-2,500 prompt + 6,000-9,000 output = 7,500-11,500 total
```

**Workflow Test 2: Full Life Arc Pipeline (Post-Cleanup)**
```
1. Profile: include_process_file: true (setting ignored)
2. mode-orchestrator → life-arc-interpreter-v3 (cleaned prompt) → synthesis ONLY
3. accuracy-checker validates → PASS
4. PDF generation → SUCCESS
5. Files: synthesis.md, synthesis.pdf ONLY (process.md NOT created despite setting)
6. Token savings: 1,500-2,500 prompt + 7,000-9,000 output = 8,500-11,500 total
```

**Workflow Test 3: Transit Long (Post-Cleanup)**
```
1. Profile: Any setting (ignored)
2. mode-orchestrator → transit-analyzer-long (cleaned prompt) → synthesis ONLY
3. accuracy-checker validates synthesis → PASS
4. PDF generation from synthesis → SUCCESS
5. Files: synthesis.md, synthesis.pdf ONLY
6. Token savings: 1,500-2,500 prompt + 8,000-10,000 output = 9,500-12,500 total
```

**Workflow Test 4: Archive Restoration (Reversal Test)**
```
1. Copy natal-interpreter section from archive
2. Paste into natal-interpreter.md at documented location
3. Run natal report
4. Files: process.md + synthesis.md generated (two-file mode restored)
5. Validates restoration path works if needed
```

### User Acceptance Criteria (Version 2.0)

1. ✅ **Default workflow generates ONE file** (synthesis) + PDF
2. ✅ **Prompt token usage reduces 15-25%** PER AGENT INVOCATION (1,500-2,500 tokens)
3. ✅ **Output token usage reduces 40-60%** per interpretation report (6,000-9,000 tokens)
4. ✅ **Total savings: 7,500-11,500 tokens per report** (combined prompt + output)
5. ✅ **accuracy-checker continues working** without process files (no changes needed)
6. ✅ **PDF generation continues working** without process files (no changes needed)
7. ✅ **Setting `include_process_file` ignored** (no errors, just no effect)
8. ✅ **Archive allows reversal** if process files needed in future
9. ✅ **No breaking changes** to existing workflows (except no process files)
10. ✅ **Cleaner agent prompts** (easier to maintain, more focused)

---

## Migration Strategy (Version 2.0)

### Backward Compatibility

**Existing Process Files**:
- **No deletion required** - All historical process files remain in `profiles/{name}/output/` folders
- Serve as historical reference for past interpretations
- No conflicts with new single-file approach
- Can be manually compared to future synthesis files if needed

**Existing Profiles**:
- **No mandatory updates** - All profiles continue working
- Setting `include_process_file` (if present) simply ignored
- No errors if setting present (just has no effect)
- Profile validation unchanged

**Agents**:
- All interpreter agents updated simultaneously (Phase 2)
- No gradual rollout - all-or-nothing deployment
- Cleaner prompts across all agents

### Rollback Plan

**If issues arise, restoration is straightforward**:

**Rollback Steps**:
1. **Open archive**: `/docs/archive/process_file_generation_prompts.md`
2. **Copy agent section**: Find affected agent (e.g., natal-interpreter)
3. **Paste to agent prompt**: Restore at documented location (line numbers provided)
4. **Update OUTPUT_STYLE_GUIDE.md**: Restore "Two-File Standard" section
5. **Update mode-orchestrator.md**: Change Step 7 back to "produces TWO files"
6. **Test**: Run interpretation to verify both files generated

**Rollback Triggers**:
- accuracy-checker unexpectedly fails without process files (unlikely - already verified it doesn't use them)
- PDF generation breaks (unlikely - already verified it doesn't use process files)
- User reports missing critical technical data not in synthesis
- Unknown workflow dependency on process files discovered
- Quality degradation in synthesis output (investigate before rollback)

**Partial Rollback**:
- Can restore ONE agent at a time if issue agent-specific
- Archive structure supports per-agent restoration
- Example: Restore natal-interpreter only, leave others clean

**Full Rollback**:
- Restore all interpreter agents from archive
- Update all documentation files
- Re-enable `include_process_file` as functional setting
- Communicate to users: "Two-file system restored temporarily"

---

## Open Questions (Version 2.0)

### Question 1: Should Archive Include Line Numbers?

**Option A: Include Line Numbers (Proposed)**
- Document exact line numbers where instructions were removed
- Makes restoration precise and fast
- Risk: Line numbers change if agents updated
- Mitigation: Include section headers as backup navigation

**Option B: Section Headers Only**
- No line numbers, just section names
- More resilient to agent updates
- Restoration requires manual searching
- Slower to restore

**Recommendation**: **Option A (Include Line Numbers + Section Headers)**
Rationale: Faster restoration, section headers provide fallback if line numbers drift

---

### Question 2: Should We Test Each Agent Individually?

**Option A: Sequential Testing (Safer)**
1. Extract + clean natal-interpreter
2. Test thoroughly
3. Extract + clean life-arc-interpreter-v3
4. Test thoroughly
5. Continue for each agent

**Option B: Batch Extraction + Testing (Faster)**
1. Extract ALL agents to archive
2. Clean ALL agent prompts
3. Test all agents together

**Recommendation**: **Option B (Batch Approach)**
Rationale: Process file removal is identical across agents, batch approach saves time. If issue found, rollback is easy via archive.

---

### Question 3: Archive Location - Single File or Per-Agent?

**Option A: Single Archive File (Proposed)**
- `/docs/archive/process_file_generation_prompts.md`
- All agents in one document
- Easy to search across agents
- Clear restoration instructions

**Option B: Per-Agent Archive Files**
- `/docs/archive/natal_interpreter_process_prompts.md`
- `/docs/archive/life_arc_interpreter_process_prompts.md`
- Separate file per agent
- More modular, easier to update individual agents

**Recommendation**: **Option A (Single Archive)**
Rationale: Simpler to maintain, all restoration logic in one place, easier to compare across agents

---

### Question 4: Should Documentation Updates Happen Before or After Agent Cleanup?

**Option A: Documentation First (Safer)**
1. Update OUTPUT_STYLE_GUIDE.md, DEVELOPMENT_GUIDE.md, etc.
2. Then clean agent prompts
3. Documentation ready before agents change

**Option B: Agent Cleanup First (Faster)**
1. Extract and clean agents
2. Then update documentation to match

**Recommendation**: **Option A (Documentation First)**
Rationale: Documentation serves as specification for agent changes. Update docs first ensures consistency and provides reference during cleanup.

---

### Question 5: Should Existing Process Files Be Moved/Archived?

**Option A: Leave In Place (Proposed)**
- No action on existing process files
- Remain in `profiles/{name}/output/` folders
- Historical reference

**Option B: Archive to Subfolder**
- Move to `profiles/{name}/output/archive_process/`
- Cleaner output folder
- Risk of breaking manual references

**Option C: Delete Entirely**
- Remove all historical process files
- Minimalist approach
- Irreversible

**Recommendation**: **Option A (Leave In Place)**
Rationale: No benefit to moving/deleting, historical record useful, zero risk

---

## Decision Log (Version 2.0)

| Decision | Rationale | Alternatives Considered | Date |
|----------|-----------|------------------------|------|
| **AGGRESSIVE REMOVAL**: Delete process file instructions entirely | Saves 1,500-2,500 prompt tokens PER INVOCATION + 6,000-9,000 output tokens | Conditional generation via setting (v1.0 approach) | 2025-10-18 |
| Archive instructions instead of deleting | Allows easy restoration if needed | Delete permanently, conditional setting | 2025-10-18 |
| Single archive file for all agents | Simpler maintenance, easier cross-agent comparison | Per-agent archive files | 2025-10-18 |
| Include line numbers + section headers | Fast restoration with fallback navigation | Section headers only | 2025-10-18 |
| Make `include_process_file` non-functional | No conditional logic = cleaner code | Keep setting functional (v1.0) | 2025-10-18 |
| Batch extraction and cleanup | Faster deployment, easy rollback | Sequential per-agent approach | 2025-10-18 |
| Update documentation before agent cleanup | Documentation serves as specification | Agent cleanup first | 2025-10-18 |
| Leave existing process files in place | No risk, historical value | Archive or delete old files | 2025-10-18 |
| Update all agents simultaneously | Consistent behavior across all modes | Gradual rollout | 2025-10-18 |

---

## Success Metrics (Version 2.0)

### Quantitative (Per Report)

- **Prompt token reduction**: 1,500-2,500 tokens per agent invocation (15-25%)
- **Output token reduction**: 6,000-9,000 tokens per report (40-60%)
- **Total token reduction**: 7,500-11,500 tokens per report (combined prompt + output)
- **File count reduction**: 1 MD + 1 PDF (down from 2 MD + 1 PDF)
- **Workflow time**: Slightly faster (fewer tokens = faster generation)
- **Quality**: Unchanged (accuracy-checker pass rate same or better)

### Quantitative (Aggregate)

Assuming 10 reports per month across all modes:
- **Monthly savings**: 75,000-115,000 tokens
- **Annual savings**: 900,000-1,380,000 tokens
- **Cost savings**: Depends on Claude API pricing tier

### Qualitative

- **User experience**: Simpler (fewer files, same quality)
- **Documentation clarity**: Improved (single-file workflow easier to understand)
- **Maintenance burden**: Significantly reduced (15-25% less prompt content per agent)
- **Agent prompt readability**: Improved (cleaner, more focused instructions)
- **Codebase simplicity**: No conditional logic for file generation

### Validation Criteria (Version 2.0)

1. ✅ **Default natal interpretation generates synthesis ONLY** (no process file)
2. ✅ **Setting `include_process_file: true` is IGNORED** (no process file despite setting)
3. ✅ **accuracy-checker passes without process file** (uses synthesis + seed_data)
4. ✅ **PDF generates correctly from synthesis** (no issues)
5. ✅ **Prompt token count reduced 15-25%** per agent (measured before/after)
6. ✅ **Output token count reduced 40-60%** per report (measured before/after)
7. ✅ **No workflow breakages** (all modes work correctly)
8. ✅ **Archive restoration works** (can restore process file generation if needed)
9. ✅ **Documentation accurate** (all docs reflect single-file workflow)
10. ✅ **No broken references** (no dangling process file mentions)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-18 | Initial specification - Conditional process file generation via setting |
| 2.0 | 2025-10-18 | **AGGRESSIVE REMOVAL** - Complete deletion of process file instructions, archive-based approach |

---

## Appendices

### Appendix A: Affected Files (Version 2.0)

**NEW: Archive File** (1 file):
- `/docs/archive/process_file_generation_prompts.md` (created to store extracted instructions)

**Interpreter Agents** (5 active files, PROMPT CLEANUP):
- `.claude/agents/natal-interpreter.md` - REMOVE all process file instructions
- `.claude/agents/natal-interpreter-experiential.md` - REMOVE all process file instructions
- `.claude/agents/life-arc-interpreter-v3.md` - REMOVE all process file instructions
- `.claude/agents/transit-analyzer-short.md` - REMOVE all process file instructions
- `.claude/agents/transit-analyzer-long.md` - REMOVE all process file instructions

**Documentation** (6 files, UPDATE to single-file workflow):
- `docs/OUTPUT_STYLE_GUIDE.md` - REMOVE "Two-File Standard" section, ADD "Single-File Standard"
- `docs/DEVELOPMENT_GUIDE.md` - UPDATE interpreter workflow to single-file
- `docs/AGENTS_REFERENCE.md` - UPDATE all interpreter entries to "Output: 1 file"
- `.claude/agents/mode-orchestrator.md` - UPDATE Step 7 to expect one file only
- `.claude/agents/astrology-agent-creator.md` - UPDATE template to exclude process file instructions
- `docs/PROFILE_STRUCTURE.md` - DEPRECATE `include_process_file` setting

**Profile Templates** (1 file, DEPRECATION COMMENT):
- `profiles/TEMPLATE/profile.md` (or similar) - COMMENT OUT `include_process_file` setting

**Deprecated Agents** (skip, no changes):
- `.claude/agents/life-arc-interpreter-v2.md` (deprecated)
- `.claude/agents/life-arc-interpreter-v2.md.bak` (backup)

### Appendix B: Token Savings Analysis (Version 2.0)

**Natal Report Example** (Darren S):
- **BEFORE**:
  - Prompt: ~10,000 tokens (includes 2,000 process file instructions)
  - Output: ~15,000 tokens total
    - Process: ~6,000 tokens (40%)
    - Synthesis: ~9,000 tokens (60%)
  - **Total**: 25,000 tokens
- **AFTER**:
  - Prompt: ~8,000 tokens (process instructions removed)
  - Output: ~9,000 tokens (synthesis only)
  - **Total**: 17,000 tokens
- **SAVINGS**: 8,000 tokens per report (32% reduction)
  - Prompt: 2,000 tokens (20%)
  - Output: 6,000 tokens (40%)

**Life Arc Report Example** (Ages 0-100):
- **BEFORE**:
  - Prompt: ~11,000 tokens (includes 2,500 process file instructions)
  - Output: ~18,000 tokens total
    - Process: ~7,000 tokens (39%)
    - Synthesis: ~11,000 tokens (61%)
  - **Total**: 29,000 tokens
- **AFTER**:
  - Prompt: ~8,500 tokens (process instructions removed)
  - Output: ~11,000 tokens (synthesis only)
  - **Total**: 19,500 tokens
- **SAVINGS**: 9,500 tokens per report (33% reduction)
  - Prompt: 2,500 tokens (23%)
  - Output: 7,000 tokens (39%)

**Transit Long Report Example** (5 years):
- **BEFORE**:
  - Prompt: ~10,500 tokens (includes 2,000 process file instructions)
  - Output: ~20,000 tokens total
    - Process: ~8,000 tokens (40%)
    - Synthesis: ~12,000 tokens (60%)
  - **Total**: 30,500 tokens
- **AFTER**:
  - Prompt: ~8,500 tokens (process instructions removed)
  - Output: ~12,000 tokens (synthesis only)
  - **Total**: 20,500 tokens
- **SAVINGS**: 10,000 tokens per report (33% reduction)
  - Prompt: 2,000 tokens (19%)
  - Output: 8,000 tokens (40%)

**Average Savings Per Report**:
- Prompt tokens: 1,500-2,500 (15-25% of prompt)
- Output tokens: 6,000-8,000 (40-60% of output)
- Total tokens: 7,500-11,500 per report (30-35% overall reduction)

### Appendix C: Grep Commands for Verification (Version 2.0)

**Find all process file references in active files**:
```bash
# Should return ZERO results after Phase 2 cleanup (except in archive)
grep -r "process.md\|process_file\|{type}_process_" .claude/agents/ docs/ --exclude-dir=archive
```

**Find "two-file" references**:
```bash
# Should return ZERO results after Phase 3 documentation updates (except in archive)
grep -r "two-file\|two file\|2 files" docs/ --exclude-dir=archive
```

**Find all interpreter agents**:
```bash
# Identifies agents needing prompt cleanup
find .claude/agents/ -name "*interpreter*.md" -o -name "*analyzer*.md" | grep -v ".bak" | grep -v "v2.md"
```

**Verify archive contains extracted instructions**:
```bash
# Should contain sections for natal-interpreter, life-arc-interpreter-v3, transit analyzers
grep -n "## natal-interpreter\|## life-arc-interpreter\|## transit-analyzer" docs/archive/process_file_generation_prompts.md
```

**Find profile setting references**:
```bash
# Verify setting marked as deprecated
grep -r "include_process_file" profiles/ docs/
```

### Appendix D: Profile Setting Changes (Version 2.0)

**Before** (Version 1.0 - conditional approach):
```ini
[INTERPRETATION_SETTINGS]
include_process_file: true  # Generate both files (default)
```

**After** (Version 2.0 - aggressive removal, setting DEPRECATED):
```ini
[INTERPRETATION_SETTINGS]
# include_process_file: false  # DEPRECATED (Oct 2025) - No longer functional
                               # All reports generate synthesis file only
                               # Process files removed for token optimization
                               # To restore: See /docs/archive/process_file_generation_prompts.md
```

**Existing Profiles** (no migration):
```ini
[INTERPRETATION_SETTINGS]
include_process_file: true   # Setting present but IGNORED
                             # No process file will be generated
                             # Setting has no effect
```

---

**END OF SPECIFICATION**

---

## Next Steps (Version 2.0)

### Immediate Actions

1. **User Review & Approval**
   - Review Version 2.0 specification (aggressive removal approach)
   - Confirm understanding of archive-based restoration
   - Approve implementation plan (4 phases)

2. **Pre-Implementation Validation**
   - Verify accuracy-checker doesn't use process files (already confirmed)
   - Verify PDF generation doesn't use process files (already confirmed)
   - Create test profile for post-cleanup validation

### Implementation Sequence (If Approved)

**Phase 1: Extraction & Archive** (1-2 hours)
1. Create `/docs/archive/process_file_generation_prompts.md`
2. Extract process file instructions from all 5 interpreter agents
3. Document line numbers and section locations
4. Add restoration instructions to archive

**Phase 2: Agent Prompt Cleanup** (2-3 hours)
1. Remove process file instructions from natal-interpreter.md
2. Remove from life-arc-interpreter-v3.md
3. Remove from transit-analyzer-long.md and transit-analyzer-short.md
4. Remove from natal-interpreter-experiential.md
5. Verify no broken references in each agent

**Phase 3: Documentation Updates** (2-3 hours)
1. Update OUTPUT_STYLE_GUIDE.md (remove two-file section)
2. Update mode-orchestrator.md (single-file workflow)
3. Update DEVELOPMENT_GUIDE.md (interpreter workflow)
4. Update AGENTS_REFERENCE.md (all interpreter entries)
5. Update astrology-agent-creator.md (template changes)
6. Update PROFILE_STRUCTURE.md (deprecate setting)

**Phase 4: Profile Template Updates** (30 minutes)
1. Update profile.md template with deprecated setting comment
2. Test new profile creation
3. Verify existing profiles still work

### Testing & Validation (If Approved)

**After Implementation**:
1. Generate natal report → Verify only synthesis created
2. Run accuracy-checker → Verify passes
3. Generate PDF → Verify successful
4. Measure token counts → Verify 30-35% reduction
5. Test all modes (natal, life arc, transits)
6. Verify archive restoration works

### Monitoring Post-Deployment

**Track for 1-2 weeks**:
- Token usage per report (should be 30-35% lower)
- Quality metrics (accuracy-checker pass rate)
- User feedback (any missing data?)
- Workflow issues (any broken integrations?)

---

## Questions for User

1. **Approach Approval**: Does the aggressive removal approach (delete from prompts, archive for restoration) make sense?

2. **Archive Structure**: Single archive file with all agents, or per-agent files?

3. **Implementation Timing**: Implement immediately, or test one agent first (natal-interpreter)?

4. **Documentation Order**: Update docs first (safer) or agent cleanup first (faster)?

5. **Historical Files**: Leave existing process files in output folders, or archive/delete?

6. **Ready to Proceed**: Approve specification and begin Phase 1 (extraction & archive)?

---

**Specification Status**: ✅ COMPLETE - Awaiting User Approval for Implementation

**Estimated Total Implementation Time**: 6-9 hours (all 4 phases)

**Estimated Token Savings**: 7,500-11,500 tokens per report (30-35% reduction)

**Risk Level**: Low (easy rollback via archive, no workflow dependencies on process files)
