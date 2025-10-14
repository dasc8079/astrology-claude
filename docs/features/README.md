# Features Specifications Folder

**Purpose**: Comprehensive feature design specifications that serve as the source of truth for major system features.

---

## What Goes Here

**Feature Specs** - Comprehensive design documents for major features:
- Natal Horoscope system
- Life Arc Report system
- Transit Analysis system
- Single Event Analysis system
- Any new major feature requiring full design

---

## File Naming Convention

```
[feature_name]_v[N].md
```

**Examples**:
- `natal_horoscope_v2.md`
- `life_arc_report_v3.md`
- `transit_analysis_v1.md`
- `single_event_analysis_v1.md`

---

## Feature Spec Contents

Each feature spec should include:

### 1. Problem Statement & Goals
- What problem does this feature solve?
- What are the goals and non-goals?
- Who is this for?

### 2. Functional Requirements
- What must the feature do?
- User stories or use cases
- Input/output specifications

### 3. Technical Approach
- Data structures
- Calculation methods
- Integration points
- Dependencies

### 4. Implementation Phases
- How will this be built incrementally?
- What are the milestones?
- What can be deferred?

### 5. Success Criteria
- How do we know it's working?
- What metrics matter?
- What constitutes "complete"?

### 6. Version History (CRITICAL)
Embedded version history showing all changes:

```markdown
## Version History

### v2.1 (2025-10-14)
**Update**: Added antiscia and fixed stars calculation
**Changes**:
- New data structure: `antiscia[]` array in seed data
- New interpretation guidelines for antiscia (TERTIARY testimony)
- Updated agent: natal-interpreter.md
**Archived**: [natal_antiscia_update.md](../archive/updates/2025/10-October/natal_antiscia_update.md)

### v2.0 (2025-10-12)
**Update**: Added hierarchical testimony framework
**Changes**:
- PRIMARY (60-80%), SECONDARY (15-30%), TERTIARY (5-15%) framework
- Updated interpretation weighting system
**Archived**: [natal_hierarchical_update.md](../archive/updates/2025/10-October/natal_hierarchical_update.md)

### v1.0 (2025-09-20)
**Initial Release**: Natal horoscope generation system
```

---

## Workflow: Feature Design → Implementation

### Phase 1: Feature Design (NEW Feature)

**Trigger**: User wants to build new feature

**Process**:
1. User describes feature vision
2. `workflow-planner-2` provides technical recommendations
3. `feature-designer-astrology` facilitates conversational design
4. Output: `docs/features/[feature_name]_v1.md`

### Phase 2: Agent Creation

**Trigger**: Feature spec complete

**Process**:
1. Read feature spec
2. `astrology-agent-creator` creates agent prompt
3. Output:
   - `.claude/agents/[agent_name].md`
   - `docs/agents/[agent_name]_spec.md`

### Phase 3: Implementation

Build → Test → Refine → Mark COMPLETE ✅

### Phase 4: Incremental Updates

**Trigger**: Need to add/change functionality

**Process**:
1. User describes update
2. `feature-designer-astrology` creates: `docs/updates/[feature]_[update_name].md`
3. Implement using update spec
4. Test and validate
5. **Upon Completion**: `docs-updater-astrology` performs integration:
   - Archive update spec: `docs/archive/updates/[year]/[month]/`
   - Integrate changes into feature spec (create new version if needed)
   - Update version history

---

## Version Management Strategy

### When to Create New Version

**Minor Updates** (v2.0 → v2.1):
- Add new calculation or data point
- Enhance existing functionality
- Add optional features
- Update interpretation guidelines
- **Action**: Update current spec file, add version history entry

**Major Updates** (v2.x → v3.0):
- Complete redesign or refactor
- Breaking changes to data structures
- Fundamental approach changes
- **Action**: Create new spec file (`[feature]_v3.md`), archive old version

### Consolidation Strategy

**When Feature Spec Exceeds 100KB**:
1. Create new major version: `[feature_name]_v[N+1].md`
2. Consolidate all updates into new comprehensive spec
3. Archive old version: `docs/archive/features/[feature_name]_v[N].md`
4. Keep version history section showing all changes
5. Link between versions for traceability

---

## Current Feature Specs

**Active**:
- `natal_horoscope_optimization_v1.md` - Natal optimization planning
- `life_arc_report_v3.md` - Life Arc Report v3 with convergence scoring
- `single_event_analysis_v1.md` - Single event analysis design

**Archived**:
- See `docs/archive/features/` for previous versions

---

## Related Folders

- `docs/agents/` - Agent specs derived from feature specs
- `docs/updates/` - Incremental update specs (temporary)
- `docs/archive/` - Completed updates and old spec versions

---

## Best Practices

✅ **DO**:
- Keep feature specs comprehensive and current
- Embed version history in spec
- Link to archived update specs
- Create major version when spec exceeds 100KB
- Reference related agent specs

❌ **DON'T**:
- Modify main spec directly for updates (create update spec first)
- Let specs grow indefinitely without consolidation
- Skip version history entries
- Delete old versions (archive them)
- Forget to update agent specs when feature changes

---

**Questions?** See [DOCS_REFACTOR_PROPOSAL.md](../DOCS_REFACTOR_PROPOSAL.md) for complete workflow documentation.
