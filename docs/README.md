# Astrology Project Documentation

**Last Refactored**: 2025-10-14
**Structure**: Systematic workflow from feature design → agent creation → incremental updates → archiving

---

## Quick Navigation

### Planning & Vision
- **[session_goals.md](session_goals.md)** - North Star vision and future implementation plans
- **[FUTURE_ENHANCEMENTS.md](FUTURE_ENHANCEMENTS.md)** - Deferred features and enhancements

### Feature Design & Implementation
- **[features/](features/)** - Comprehensive feature specifications (source of truth)
- **[agents/](agents/)** - Agent technical specifications
- **[updates/](updates/)** - Incremental update specifications (temporary)
- **[archive/](archive/)** - Completed updates and old spec versions

### Reference Documentation
- **[reference/](reference/)** - Static knowledge (astrology systems, data formats, standards)
- **[guides/](guides/)** - Operational how-to guides (profiles, transits, timing techniques)
- **[technical/](technical/)** - System documentation (development, agents, scripts, troubleshooting)

---

## Documentation Structure

```
docs/
├── README.md                          # This file - navigation hub
├── session_goals.md                   # North Star + future plans
├── FUTURE_ENHANCEMENTS.md             # Deferred features
├── DOCS_REFACTOR_PROPOSAL.md          # Refactoring design document
│
├── features/                          # Feature specifications (ACTIVE)
│   ├── README.md                      # Feature workflow guide
│   ├── natal_horoscope_*.md           # Natal feature specs
│   ├── life_arc_report_*.md           # Life arc feature specs
│   ├── transit_analysis_*.md          # Transit feature specs
│   └── [feature_name]_v[N].md         # Versioned feature specs
│
├── agents/                            # Agent specifications (ACTIVE)
│   ├── README.md                      # Agent workflow guide
│   ├── natal_interpreter_spec.md      # Agent specs
│   ├── mode_orchestrator_spec.md
│   └── [agent_name]_spec.md
│
├── updates/                           # Update specifications (TEMPORARY)
│   ├── README.md                      # Update workflow guide
│   ├── examples/                      # Example update specs
│   └── [feature]_[update].md          # Active updates (archived after integration)
│
├── archive/                           # Historical documentation
│   ├── README.md                      # Archive organization guide
│   ├── features/                      # Old feature spec versions
│   ├── agents/                        # Old agent spec versions
│   ├── updates/                       # Integrated update specs (by year/month)
│   └── design/                        # Legacy design docs
│
├── reference/                         # Static reference (STABLE)
│   ├── ASTROLOGY_REFERENCE.md         # Foundational astrology knowledge
│   ├── DATA_FORMATS.md                # JSON schemas
│   ├── OUTPUT_STYLE_GUIDE.md          # Universal output standards
│   ├── OUTPUT_STRUCTURE.md            # Folder organization
│   ├── PROFILE_STRUCTURE.md           # Profile standards
│   ├── SEED_DATA_SPECIFICATION.md     # Seed data spec
│   └── [other reference docs]
│
├── guides/                            # Operational how-to (STABLE)
│   ├── PROFILES_GUIDE.md              # Profile management
│   ├── TRANSITS_GUIDE.md              # Transit usage
│   ├── LIFE_ARC_GUIDE.md              # Life arc usage
│   ├── PROFECTIONS_GUIDE.md           # Profections system
│   ├── ZODIACAL_RELEASING_GUIDE.md    # ZR system
│   └── [other timing guides]
│
└── technical/                         # System documentation (STABLE)
    ├── DEVELOPMENT_GUIDE.md           # Development workflow
    ├── AGENTS_REFERENCE.md            # Agent catalog
    ├── SCRIPTS_REFERENCE.md           # Script documentation
    ├── TROUBLESHOOTING.md             # Debugging guides
    └── WORKFLOWS_VISUAL.md            # Visual workflow diagrams
```

---

## Systematic Workflow

### Design → Spec → Agent → Implementation → Updates → Archive

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: Feature Design                                      │
│                                                               │
│ User describes feature vision                                │
│   ↓                                                          │
│ workflow-planner-2: Technical recommendations                │
│   ↓                                                          │
│ feature-designer-astrology: Conversational design            │
│   ↓                                                          │
│ Output: docs/features/[feature_name]_v1.md                   │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 2: Agent Creation                                      │
│                                                               │
│ astrology-agent-creator reads feature spec                   │
│   ↓                                                          │
│ Creates agent prompt: .claude/agents/[agent_name].md         │
│   ↓                                                          │
│ Creates agent spec: docs/agents/[agent_name]_spec.md         │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 3: Implementation                                      │
│                                                               │
│ Build scripts, test, refine, mark COMPLETE ✅                │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 4: Incremental Updates                                 │
│                                                               │
│ User describes update                                        │
│   ↓                                                          │
│ feature-designer-astrology: Creates update spec              │
│   Output: docs/updates/[feature]_[update].md                 │
│   ↓                                                          │
│ Implement → Test → Validate                                  │
│   ↓                                                          │
│ docs-updater-astrology (upon completion):                    │
│   1. Archive: docs/archive/updates/[year]/[month]/           │
│   2. Integrate into feature spec                             │
│   3. Add version history entry                               │
│   4. Update agent spec if needed                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Version Management

### Embedded Version History (In Feature Specs)

Each feature spec includes version history:

```markdown
## Version History

### v2.1 (2025-10-14)
**Update**: Added antiscia calculation
**Changes**: Antiscia array in seed data, TERTIARY testimony guidelines
**Archived**: [natal_antiscia_update.md](../archive/updates/2025/10-October/natal_antiscia_update.md)

### v2.0 (2025-10-12)
**Update**: Hierarchical testimony framework
**Changes**: PRIMARY/SECONDARY/TERTIARY weighting system
**Archived**: [natal_hierarchical_update.md](../archive/updates/2025/10-October/natal_hierarchical_update.md)

### v1.0 (2025-09-20)
**Initial Release**: Natal horoscope generation system
```

### Consolidation Strategy

**When Feature Spec Exceeds 100KB**:
1. Create new major version: `[feature_name]_v[N+1].md`
2. Consolidate all updates into new comprehensive spec
3. Archive old version: `docs/archive/features/`
4. Keep version history showing all changes

---

## Key Agents & Responsibilities

### Planning & Design
- **workflow-planner-2**: Technical architecture recommendations
- **feature-designer-astrology**: Feature specification creation

### Agent Management
- **astrology-agent-creator**: Creates agents from feature specs
- **agent-prompt-refiner-astrology**: Refines existing agent prompts

### Documentation Maintenance
- **docs-updater-astrology**: Updates docs, archives completed work, integrates updates

### Quality Assurance
- **accuracy-checker**: Validates interpretation output quality
- **astrology-output-debugger**: Debugs interpretation issues

### Orchestration
- **mode-orchestrator**: Routes all interpretation requests (Modes 1-4+)

---

## Documentation Update Triggers

### session_goals.md
**Updated By**: workflow-planner (creates), docs-updater (tracks progress)
**When**: Approach changes, stages complete, vision evolves

### Feature Specs (features/)
**Updated By**: feature-designer-astrology (creates), docs-updater (integrates updates)
**When**: New features designed, updates integrated

### Agent Specs (agents/)
**Updated By**: astrology-agent-creator (creates), docs-updater (updates)
**When**: New agents created, feature changes affect agents

### Update Specs (updates/)
**Updated By**: feature-designer-astrology (creates), docs-updater (archives)
**When**: Incremental changes needed (created), implementation complete (archived)

### Reference Docs (reference/)
**Updated By**: reference-guide-updater (rarely)
**When**: Foundational systems change, new standards adopted

### Technical Docs (technical/)
**Updated By**: docs-updater-astrology
**When**: Development workflow changes, new agents/scripts added

---

## Best Practices

### ✅ DO
- Create update spec BEFORE modifying main feature spec
- Keep update specs focused (5-20KB)
- Archive completed updates immediately
- Maintain version history in feature specs
- Link between related documents
- Use README files in each folder

### ❌ DON'T
- Modify main feature spec directly for updates
- Let update specs languish without integration
- Delete archived specs (keep history)
- Skip version history entries
- Let feature specs exceed 100KB without consolidation

---

## Getting Started

### For New Features
1. Describe feature vision to `workflow-planner-2`
2. Work with `feature-designer-astrology` to create spec
3. Use `astrology-agent-creator` to build agents
4. Implement, test, refine

### For Feature Updates
1. Describe update to `feature-designer-astrology`
2. Receive update spec in `docs/updates/`
3. Implement using update spec
4. Upon completion, `docs-updater-astrology` handles integration

### For Finding Past Work
1. Check `docs/archive/` for completed updates
2. Check feature spec version history for change links
3. Check `history/` folder (project root) for stage archives

---

## Questions?

- **Workflow Details**: See [DOCS_REFACTOR_PROPOSAL.md](DOCS_REFACTOR_PROPOSAL.md)
- **Feature Specs**: See [features/README.md](features/README.md)
- **Agent Specs**: See [agents/README.md](agents/README.md)
- **Updates**: See [updates/README.md](updates/README.md)
- **Archive**: See [archive/README.md](archive/README.md)

---

**Last Updated**: 2025-10-14 by docs refactoring initiative
