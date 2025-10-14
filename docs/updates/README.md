# Updates Specifications Folder

**Purpose**: Temporary home for incremental update specifications. These are small, focused specs for adding features or modifying existing functionality WITHOUT immediately editing the main feature spec.

---

## What Goes Here

**Update Specs** - Incremental change specifications:
- Adding new calculations (antiscia, fixed stars, etc.)
- Enhancing existing features (convergence detection, adaptive weighting)
- Modifying interpretation guidelines
- Integrating new techniques

**IMPORTANT**: Update specs are **TEMPORARY**. After implementation and testing, they are:
1. Archived to `docs/archive/updates/[year]/[month]/`
2. Integrated into main feature spec
3. Removed from this folder

---

## File Naming Convention

```
[feature]_[update_name].md
```

**Examples**:
- `natal_antiscia_update.md`
- `natal_lilith_update.md`
- `lifeArc_convergence_update.md`
- `lifeArc_adaptive_scoring_update.md`
- `transit_retrograde_tracking_update.md`

**Pattern**: `[feature]` matches the feature spec name, `[update_name]` describes the specific change

---

## Update Spec Contents

Each update spec should include:

### 1. What's Being Added/Changed
- Clear description of the update
- What problem does this solve?
- What improves?

### 2. Why This Update is Needed
- User need or requirement
- Quality improvement
- Feature enhancement
- Bug fix

### 3. Technical Implementation Details
- Data structures to add/modify
- Calculation methods
- Script changes needed
- Agent prompt changes needed

### 4. Testing Requirements
- What profiles to test with?
- What outputs to verify?
- What edge cases to check?

### 5. Integration Notes
- Where do changes go in main feature spec?
- Which sections need updating?
- What version change (minor or major)?

---

## Workflow: Update Spec → Implementation → Integration

### Phase 1: Update Request

**Trigger**: User wants to add/change functionality

**Process**:
1. User describes update: "Add antiscia to natal horoscope"
2. `feature-designer-astrology` creates: `docs/updates/natal_antiscia_update.md`
3. Update spec written (NOT modifying main feature spec yet)

### Phase 2: Implementation

**Process**:
1. Implement changes using update spec as guide
2. Update scripts (e.g., `seed_data_generator.py`)
3. Update agent prompts if needed (e.g., `.claude/agents/natal-interpreter.md`)
4. Test with profile data
5. Validate output quality

### Phase 3: Integration & Archiving

**Trigger**: Implementation complete and tested

**Process** (`docs-updater-astrology` performs automatically):
1. **Archive update spec**:
   - Move from `docs/updates/` to `docs/archive/updates/[year]/[month]/`
   - Preserves detailed implementation notes

2. **Integrate into main feature spec**:
   - Read update spec
   - Read main feature spec
   - Identify where changes belong
   - Update feature spec OR create new version if major
   - Add entry to version history section

3. **Update agent spec** (if agent changed):
   - Update `docs/agents/[agent_name]_spec.md`
   - Note version alignment

4. **Update CURRENT_WORK.md**: Document completion

---

## Why This Workflow?

### Problem: Direct Spec Editing
- Main feature specs become cluttered with work-in-progress changes
- Hard to track what was added when
- Difficult to rollback if update fails

### Solution: Update Specs
- Small, focused documents (5-20KB)
- Clear scope and integration path
- Main spec stays clean during implementation
- Easy to archive after integration

### Benefits
- **Traceability**: Version history links to archived update specs
- **Clarity**: Main spec always shows current state
- **Manageable**: Update specs are small and focused
- **Searchable**: Archived updates preserve implementation details

---

## Example: Antiscia Update

### Before Implementation

**Update Spec Created**: `docs/updates/natal_antiscia_update.md`
```markdown
# Natal Horoscope Update: Antiscia Calculation

## What's Being Added
Add antiscia (mirror degrees) calculation to natal horoscope seed data
and interpretation guidelines.

## Technical Implementation
1. Add `calculate_antiscia()` to seed_data_generator.py
2. Update natal-interpreter.md with TERTIARY testimony guidelines
3. Add antiscia[] array to seed data JSON schema

## Integration Notes
- Update natal_horoscope_v2.md section: "Data Structures"
- Update natal_horoscope_v2.md section: "Interpretation Guidelines"
- Version: Minor update (v2.0 → v2.1)
```

### During Implementation

- Build `calculate_antiscia()` function
- Test with Darren_S profile
- Verify output quality

### After Implementation Complete

**docs-updater-astrology performs**:
1. Archive: `docs/archive/updates/2025/10-October/natal_antiscia_update.md`
2. Update: `docs/features/natal_horoscope_v2.md`
   - Add antiscia calculation details
   - Update interpretation guidelines
   - Add version history entry:
   ```markdown
   ### v2.1 (2025-10-14)
   **Update**: Added antiscia calculation
   **Changes**: Antiscia array in seed data, TERTIARY testimony guidelines
   **Archived**: [natal_antiscia_update.md](../archive/updates/2025/10-October/natal_antiscia_update.md)
   ```
3. Remove: `docs/updates/natal_antiscia_update.md` (now archived)

**Result**: Main spec is current, update is archived with full implementation notes, version history provides traceability.

---

## Current Updates

**Active** (in progress):
- *(Update specs appear here during implementation)*

**Recently Archived**:
- See `docs/archive/updates/2025/10-October/` for completed updates

---

## Related Folders

- `docs/features/` - Main feature specs that updates modify
- `docs/agents/` - Agent specs that may need updating
- `docs/archive/updates/` - Completed and integrated update specs

---

## Best Practices

✅ **DO**:
- Create update spec BEFORE modifying main feature spec
- Keep update specs focused and small (5-20KB)
- Test thoroughly before integration
- Archive immediately after integration
- Add version history entry to feature spec

❌ **DON'T**:
- Modify main feature spec directly for updates
- Let update specs languish without integration
- Skip archiving completed updates
- Forget to update version history
- Delete update specs (archive them)

---

## Update Creation Checklist

When creating a new update spec:

- [ ] Feature to update identified
- [ ] Clear description of what's changing
- [ ] Technical implementation details documented
- [ ] Integration notes specify where changes go
- [ ] Version change type determined (minor/major)
- [ ] Testing requirements defined
- [ ] File named: `[feature]_[update_name].md`

---

## Integration Checklist

When integrating a completed update:

- [ ] Implementation complete and tested
- [ ] Archive update spec to `docs/archive/updates/[year]/[month]/`
- [ ] Integrate changes into main feature spec
- [ ] Add version history entry with link to archived update
- [ ] Update agent spec if agent changed
- [ ] Remove update spec from `docs/updates/`
- [ ] Update CURRENT_WORK.md

---

**Questions?** See [DOCS_REFACTOR_PROPOSAL.md](../DOCS_REFACTOR_PROPOSAL.md) for complete workflow documentation.
