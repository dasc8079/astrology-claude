# Docs Folder Refactoring Proposal

**Created**: 2025-10-14
**Purpose**: Establish rigorous workflow for feature design → agent creation → incremental updates → archiving

---

## Problem Statement

Current `docs/` folder lacks clear organization for:
1. **Feature specifications** (comprehensive design documents)
2. **Agent specifications** (derived from features, used to build agents)
3. **Update specifications** (incremental changes to existing features)
4. **Version history** (tracking changes without bloating main specs)
5. **Archive strategy** (integrating updates into main specs, archiving update docs)

This leads to:
- Unclear which document is the "source of truth"
- No systematic workflow from design → implementation → updates
- Difficulty tracking changes and version history
- Potential for spec documents to become excessively long

---

## Proposed Docs Folder Structure

```
docs/
├── README.md                          # Overview of docs folder organization and workflow
│
├── features/                          # Feature design specifications (ACTIVE)
│   ├── README.md                      # Feature spec workflow and standards
│   ├── natal_horoscope_v1.md          # Main comprehensive feature spec
│   ├── life_arc_report_v1.md          # Main comprehensive feature spec
│   ├── transit_analysis_v1.md         # Main comprehensive feature spec
│   └── [feature_name]_v[N].md         # Versioned feature specs
│
├── agents/                            # Agent specifications (ACTIVE)
│   ├── README.md                      # Agent spec workflow and standards
│   ├── natal_interpreter_spec.md      # Agent spec (derived from feature spec)
│   ├── life_arc_interpreter_spec.md   # Agent spec (derived from feature spec)
│   ├── transit_analyzer_spec.md       # Agent spec (derived from feature spec)
│   └── [agent_name]_spec.md           # Agent specifications
│
├── updates/                           # Incremental update specifications (ACTIVE)
│   ├── README.md                      # Update spec workflow and standards
│   ├── [feature]_[update_name].md     # Incremental update specs
│   │
│   └── examples/
│       ├── natal_antiscia_update.md   # Example: Adding antiscia to natal horoscope
│       └── lifeArc_convergence_update.md  # Example: Adding convergence detection
│
├── archive/                           # Archived completed specs (HISTORICAL)
│   ├── README.md                      # Archive organization and search guide
│   ├── features/                      # Archived feature spec versions
│   ├── agents/                        # Archived agent spec versions
│   └── updates/                       # Archived and integrated update specs
│       ├── 2025/
│       │   ├── 10-October/
│       │   │   ├── natal_antiscia_update.md  # Integrated into natal_horoscope_v2.md
│       │   │   └── natal_lilith_update.md    # Integrated into natal_horoscope_v2.md
│       │   └── 09-September/
│       └── [year]/[month]/
│
├── reference/                         # Static reference documentation (STABLE)
│   ├── ASTROLOGY_REFERENCE.md         # Foundational astrology knowledge
│   ├── DATA_FORMATS.md                # JSON schemas and data structures
│   ├── OUTPUT_STYLE_GUIDE.md          # Universal output standards
│   └── PLANETARY_CONDITIONS_REFERENCE.md  # Dignities, aspects, etc.
│
├── guides/                            # Operational how-to guides (STABLE)
│   ├── PROFILES_GUIDE.md              # Profile creation and management
│   ├── TRANSITS_GUIDE.md              # Transit usage
│   ├── LIFE_ARC_GUIDE.md              # Life arc timeline usage
│   ├── PROFECTIONS_GUIDE.md           # Profections system
│   ├── ZODIACAL_RELEASING_GUIDE.md    # ZR system
│   ├── SECONDARY_PROGRESSIONS_GUIDE.md # Progressions
│   └── SOLAR_RETURNS_GUIDE.md         # Solar returns
│
├── technical/                         # Technical system documentation (STABLE)
│   ├── DEVELOPMENT_GUIDE.md           # Development workflow
│   ├── AGENTS_REFERENCE.md            # Agent catalog
│   ├── SCRIPTS_REFERENCE.md           # Script documentation
│   ├── TROUBLESHOOTING.md             # Debugging guides
│   ├── WORKFLOWS_VISUAL.md            # Visual workflow diagrams
│   └── AGENT_ORCHESTRATION_GUIDE.md   # mode-orchestrator usage
│
└── session_goals.md                   # North Star + future plans (ROOT LEVEL)
```

---

## Workflow: Feature Design → Implementation → Updates

### Phase 1: Feature Design (workflow-planner + feature-designer-astrology)

**Trigger**: User wants to build new feature or redesign existing one

**Workflow**:
1. User describes feature vision
2. `workflow-planner-2` provides technical recommendations (architecture, tools, frameworks)
3. `feature-designer-astrology` facilitates conversational requirement gathering
4. Output: `docs/features/[feature_name]_v1.md`

**Feature Spec Contents**:
- Problem statement and goals
- Functional requirements
- Technical approach
- Data structures
- Implementation phases
- Success criteria
- **Version History** (embedded in spec)

---

### Phase 2: Agent Creation (agent-creator)

**Trigger**: Feature spec complete and ready to implement

**Workflow**:
1. Read feature spec: `docs/features/[feature_name]_v1.md`
2. Extract agent requirements
3. `astrology-agent-creator` creates agent prompt with OUTPUT_STYLE_GUIDE.md standards
4. Output:
   - `.claude/agents/[agent_name].md` (agent prompt)
   - `docs/agents/[agent_name]_spec.md` (agent specification document)

**Agent Spec Contents**:
- Agent purpose and responsibilities
- Input data requirements
- Output format specifications
- Interpretation guidelines
- RAG query strategy
- Coordination with other agents
- **Derived From**: Link to source feature spec

---

### Phase 3: Implementation

**Workflow**:
1. Implement scripts, functions, data structures
2. Test with profile data
3. Refine agent prompts based on output quality
4. Mark feature COMPLETE ✅

---

### Phase 4: Incremental Updates (feature-designer-astrology + agent-creator)

**Trigger**: Need to add substantial feature or change existing functionality

**Workflow**:
1. User describes update: "Add antiscia to natal horoscope"
2. `feature-designer-astrology` creates: `docs/updates/natal_antiscia_update.md`
3. Update spec created (NOT modifying main feature spec yet)
4. Implement update using update spec
5. Test and validate
6. **Upon Completion**: `docs-updater-astrology` performs integration:
   - Archive update spec: `docs/archive/updates/2025/10-October/natal_antiscia_update.md`
   - Integrate changes into main feature spec: `docs/features/natal_horoscope_v2.md`
   - Update version history in feature spec
   - Update agent spec if agent changed

**Update Spec Contents**:
- What's being added/changed
- Why this update is needed
- Technical implementation details
- Testing requirements
- Integration notes (where changes go in main spec)

---

## Version History Strategy

### Embedded Version History (In Feature Specs)

Each feature spec includes version history section:

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
- Updated agent: natal-interpreter.md
**Archived**: [natal_hierarchical_update.md](../archive/updates/2025/10-October/natal_hierarchical_update.md)

### v1.0 (2025-09-20)
**Initial Release**: Natal horoscope generation system
```

### Consolidation Strategy (Prevent Bloat)

**When Feature Spec Exceeds 100KB**:
1. Create new major version: `[feature_name]_v[N+1].md`
2. Consolidate all updates into new comprehensive spec
3. Archive old version: `docs/archive/features/[feature_name]_v[N].md`
4. Keep version history section showing all changes
5. Link between versions for traceability

**Example**:
- `natal_horoscope_v1.md` (2025-09-20) - Initial 50KB
- Receive 10 updates, grows to 120KB
- Create `natal_horoscope_v2.md` (2025-12-01) - Consolidated 65KB
- Archive `natal_horoscope_v1.md` to `docs/archive/features/`

---

## Agent Coordination

### docs-updater-astrology (Enhanced Responsibilities)

**New Archiving Workflow**:

After update implementation complete:
1. **Archive update spec**: Move `docs/updates/[update_spec].md` → `docs/archive/updates/[year]/[month]/`
2. **Integrate into main spec**:
   - Read update spec
   - Read main feature spec
   - Identify where changes should be integrated
   - Create new feature spec version OR update current version
   - Add entry to Version History section
3. **Update agent spec** (if agent changed):
   - Update `docs/agents/[agent_name]_spec.md`
   - Note derivation from feature spec version
4. **Update CURRENT_WORK.md**: Document completion

### feature-designer-astrology

**Two Modes**:
1. **Feature Mode**: Create comprehensive feature spec (`docs/features/`)
2. **Update Mode**: Create incremental update spec (`docs/updates/`)

**Detects mode based on user request**:
- "Create a natal horoscope generator" → Feature Mode
- "Add antiscia to natal horoscope" → Update Mode

---

## Benefits of This Structure

### 1. Clear Source of Truth
- Main feature spec is always comprehensive and current
- Update specs are temporary (archived after integration)
- Version history embedded in feature spec

### 2. Manageable File Sizes
- Update specs are small and focused (5-20KB)
- Main specs consolidated periodically (65-100KB)
- Archive preserves full history without bloating active docs

### 3. Systematic Workflow
```
Design → Spec → Agent → Implementation → Updates → Integration → Archive
```

### 4. Traceability
- Version history shows all changes
- Archived updates preserve detailed implementation notes
- Links between feature specs, agent specs, and archived updates

### 5. Searchability
- Archive organized by date (year/month)
- Version history provides change summary
- README files guide navigation

---

## Migration Plan

### Step 1: Create New Structure
```bash
mkdir -p docs/features docs/agents docs/updates docs/archive/{features,agents,updates}
mkdir -p docs/reference docs/guides docs/technical
```

### Step 2: Move Existing Files

**Feature Specs** (to `docs/features/`):
- `life_arc_v3_specification.md` → `life_arc_report_v3.md`
- `NATAL_DATA_MODEL_OPTIMIZATION.md` → Could inform `natal_horoscope_v2.md` update
- `single_event_design.md` → `single_event_analysis_v1.md`

**Agent Specs** (to `docs/agents/`):
- `natal_interpreter_agent_spec.md` → Keep as is
- `accuracy_checker_agent_spec.md` → Keep as is
- `orchestrator_conversational_upgrade_spec.md` → `mode_orchestrator_spec.md`

**Update Specs** (to `docs/updates/` or archive if complete):
- `TRANSIT_SHORT_DUAL_MODE_UPDATE.md` → Archive (complete)
- `PLANETARY_CONDITIONS_IMPLEMENTATION_PRIORITY.md` → Keep in reference?

**Reference Docs** (to `docs/reference/`):
- `ASTROLOGY_REFERENCE.md` → Keep as is
- `DATA_FORMATS.md` → Keep as is
- `OUTPUT_STYLE_GUIDE.md` → Keep as is
- `PLANETARY_CONDITIONS_REFERENCE.md` → Keep as is
- `firdaria_reference.md` → Keep as is
- `seed_data_schema.yaml` → Keep as is
- `SEED_DATA_SPECIFICATION.md` → Keep as is

**Guides** (to `docs/guides/`):
- `PROFILES_GUIDE.md` → Keep as is
- `TRANSITS_GUIDE.md` → Keep as is
- `LIFE_ARC_GUIDE.md` → Keep as is
- `PROFECTIONS_GUIDE.md` → Keep as is
- `ZODIACAL_RELEASING_GUIDE.md` → Keep as is
- `SECONDARY_PROGRESSIONS_GUIDE.md` → Keep as is
- `SOLAR_RETURNS_GUIDE.md` → Keep as is

**Technical Docs** (to `docs/technical/`):
- `DEVELOPMENT_GUIDE.md` → Keep as is
- `AGENTS_REFERENCE.md` → Keep as is
- `SCRIPTS_REFERENCE.md` → Keep as is
- `TROUBLESHOOTING.md` → Keep as is
- `WORKFLOWS_VISUAL.md` → Keep as is
- `AGENT_ORCHESTRATION_GUIDE.md` → Keep as is

**Uncertain** (analyze and categorize):
- `alternative_synthesis_structure_experiential.md` → Archive or update spec?
- `FUTURE_ENHANCEMENTS.md` → Integrate into session_goals.md?
- `OUTPUT_STRUCTURE.md` → Keep in reference?
- `PROFILE_STRUCTURE.md` → Keep in reference or guides?

### Step 3: Create README Files

Create README.md for each subfolder explaining:
- Purpose of this folder
- Workflow for creating/updating files
- Naming conventions
- When to archive

### Step 4: Update docs-updater-astrology

Add archiving and integration workflow logic:
- Detect update completion
- Archive update spec with date organization
- Integrate into main feature spec
- Update version history

### Step 5: Update DEVELOPMENT_GUIDE.md

Document new workflow:
- Feature design process
- Agent creation from specs
- Incremental update process
- Archiving and integration

---

## Example Workflows

### Example 1: New Feature (Transit Analyzer)

1. **Design Phase**:
   - User: "I want to build a transit analyzer for 1-5 year timelines"
   - `workflow-planner-2`: Technical recommendations
   - `feature-designer-astrology`: Creates `docs/features/transit_analysis_v1.md`

2. **Agent Creation**:
   - `astrology-agent-creator`: Creates `.claude/agents/transit-analyzer-long.md`
   - Creates `docs/agents/transit_analyzer_long_spec.md`

3. **Implementation**:
   - Build scripts, test, refine

4. **Completion**:
   - Mark COMPLETE ✅
   - `docs-updater-astrology`: Updates CURRENT_WORK.md

### Example 2: Incremental Update (Add Antiscia)

1. **Update Request**:
   - User: "Add antiscia calculation to natal horoscope"
   - `feature-designer-astrology`: Creates `docs/updates/natal_antiscia_update.md`

2. **Implementation**:
   - Update seed_data_generator.py
   - Update natal-interpreter.md agent
   - Test with profiles

3. **Completion & Integration**:
   - `docs-updater-astrology`:
     - Archives: `docs/archive/updates/2025/10-October/natal_antiscia_update.md`
     - Updates: `docs/features/natal_horoscope_v2.md` (integrates antiscia changes)
     - Updates version history in feature spec
     - Updates: `docs/agents/natal_interpreter_spec.md`

---

## Success Metrics

A well-organized docs folder has:
- ✅ Clear separation: features / agents / updates / archive
- ✅ Active specs focused on current state
- ✅ Version history embedded in feature specs
- ✅ Update specs archived after integration
- ✅ Feature specs under 100KB (consolidated when needed)
- ✅ README files guiding navigation
- ✅ Systematic workflow documented

---

## Next Steps

1. ✅ Review this proposal with user
2. Finalize folder structure and naming conventions
3. Create new directory structure
4. Migrate existing files
5. Create README files for each subfolder
6. Update docs-updater-astrology with new workflow
7. Update DEVELOPMENT_GUIDE.md
8. Test workflow with sample feature spec and update spec

---

**Questions for User**:
1. Does this structure support your workflow needs?
2. Should version history be embedded in feature specs OR in separate changelog file?
3. When should we consolidate feature specs (100KB threshold reasonable)?
4. Any other organizational needs I'm missing?
