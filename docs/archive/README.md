# Archive Folder

**Purpose**: Permanent storage for completed update specs, old feature spec versions, and historical design documents.

---

## What Goes Here

### 1. Integrated Update Specs (`updates/`)
**Organized by**: Year / Month
**Contents**: Update specs that have been integrated into main feature specs

After an update is implemented, tested, and integrated:
- Update spec moves from `docs/updates/` to `docs/archive/updates/[year]/[month]/`
- Main feature spec updated with changes
- Version history entry links to archived update

**Example Structure**:
```
archive/
└── updates/
    └── 2025/
        ├── 10-October/
        │   ├── natal_antiscia_update.md
        │   ├── natal_lilith_update.md
        │   └── lifeArc_convergence_update.md
        └── 09-September/
            └── natal_hierarchical_update.md
```

### 2. Old Feature Spec Versions (`features/`)
**Contents**: Previous major versions of feature specs

When feature spec is consolidated (exceeds 100KB):
- New major version created (e.g., v3.0)
- Old version archived here
- Version history preserved

**Example**:
```
archive/
└── features/
    ├── natal_horoscope_v1.md
    └── life_arc_report_v2.md
```

### 3. Old Agent Spec Versions (`agents/`)
**Contents**: Previous versions of agent specs (if major redesign)

**Example**:
```
archive/
└── agents/
    └── natal_interpreter_spec_v1.md
```

### 4. Legacy Design Documents (`design/`)
**Contents**: Pre-refactoring design documents

These were created before the systematic workflow was established. Kept for historical reference.

**Current Contents**:
- `transit_interpretation_design.md`
- `life_arc_report_design.md`
- `timing_techniques_plan.md`
- And others

---

## Archive Organization Principles

### Date-Based Organization (for updates/)
- Year folders: `2025/`, `2026/`, etc.
- Month folders: `01-January/`, `02-February/`, etc.
- Enables chronological browsing
- Preserves implementation timeline

### Version-Based Organization (for features/ and agents/)
- Named by version: `[feature_name]_v[N].md`
- Enables comparison between versions
- Shows evolution of design

---

## How Files Get Here

### Automated (docs-updater-astrology)

When update implementation complete:
```
docs/updates/natal_antiscia_update.md
  ↓ (docs-updater-astrology archives)
docs/archive/updates/2025/10-October/natal_antiscia_update.md
```

### Manual (when consolidating)

When feature spec exceeds 100KB:
```
docs/features/natal_horoscope_v2.md → docs/archive/features/
docs/features/natal_horoscope_v3.md (new consolidated version)
```

---

## Searching the Archive

### By Date (Update Specs)
"What updates did we do in October 2025?"
→ Check `archive/updates/2025/10-October/`

### By Feature (Update Specs)
"What updates have we made to life arc?"
→ Search for files starting with `lifeArc_` across all date folders

### By Version (Feature Specs)
"What was in natal horoscope v1?"
→ Check `archive/features/natal_horoscope_v1.md`

### Via Version History
Each feature spec has version history linking to archived updates:
```markdown
### v2.1 (2025-10-14)
**Archived**: [natal_antiscia_update.md](../archive/updates/2025/10-October/natal_antiscia_update.md)
```

---

## Archive vs History

### docs/archive/
- **Purpose**: Completed specs and design documents
- **Contents**: Update specs, old feature versions, legacy designs
- **Organization**: By date (updates) or version (features)
- **Use**: "What was the antiscia update?" "What changed in v2?"

### history/ (project root)
- **Purpose**: Completed work stages and milestones
- **Contents**: Stage archives, major milestones
- **Organization**: By stage number and completion date
- **Use**: "What happened in Stage 3?" "When did we complete authentication?"

**Both preserve institutional knowledge, different purposes.**

---

## What NOT to Archive

❌ **Don't Archive**:
- Active feature specs (keep in `docs/features/`)
- Active agent specs (keep in `docs/agents/`)
- Work-in-progress update specs (keep in `docs/updates/`)
- Reference docs (keep in `docs/reference/`)
- Guides (keep in `docs/guides/`)
- Technical docs (keep in `docs/technical/`)

✅ **DO Archive**:
- Completed and integrated update specs
- Old feature spec versions (when consolidated)
- Old agent spec versions (if major redesign)
- Legacy design docs from before refactoring

---

## Archive Maintenance

### Automatic (docs-updater-astrology)
- Archives update specs after integration
- Creates year/month folders as needed
- Updates feature spec version history with archive links

### Manual (periodic review)
- Archive old feature spec versions when consolidating
- Archive old agent spec versions if major redesign
- Ensure archive folder structure is clean

---

## Current Archive Contents

### Updates (by date)
- `2025/10-October/` - Antiscia, Lilith, convergence detection updates

### Features (old versions)
- *(Will contain old versions when specs are consolidated)*

### Agents (old versions)
- *(Will contain old versions if agents are redesigned)*

### Legacy Design
- `design/` - Pre-refactoring design documents

---

## Best Practices

✅ **DO**:
- Archive update specs immediately after integration
- Keep archive organized (year/month for updates)
- Link from feature spec version history to archived updates
- Preserve all archived files (don't delete)
- Use descriptive file names

❌ **DON'T**:
- Archive active specs
- Delete archived specs
- Move files out of archive back to active folders
- Skip creating archive links in version history
- Forget to update archive structure as needed

---

## Example: Antiscia Update Lifecycle

**Phase 1**: Update spec created
```
docs/updates/natal_antiscia_update.md
```

**Phase 2**: Implementation complete

**Phase 3**: docs-updater-astrology performs integration
```
1. Archive: docs/archive/updates/2025/10-October/natal_antiscia_update.md
2. Integrate into: docs/features/natal_horoscope_v2.md
3. Add version history entry with link to archive
4. Remove: docs/updates/natal_antiscia_update.md
```

**Result**: Update preserved in archive, main spec updated, version history provides traceability.

---

**Questions?** See [DOCS_REFACTOR_PROPOSAL.md](../DOCS_REFACTOR_PROPOSAL.md) for complete workflow documentation.
