# Agent Version Tracker

**Purpose**: Track all versions of astrology interpretation agents, documenting refinements, improvements, and changes over time.

**Maintained by**: agent-prompt-refiner-astrology

---

## Active Versions (Current Production)

| Agent | Active Version | File | Last Updated | Changes Summary |
|-------|---------------|------|--------------|-----------------|
| natal-interpreter | v1 | natal-interpreter.md | 2025-10-05 | Original implementation |
| life-arc-interpreter | v1 | life-arc-interpreter.md | 2025-10-07 | Original implementation |
| transit-analyzer | v1 | transit-analyzer.md | 2025-10-10 | Original implementation |
| transit-analyzer-long | v1 | transit-analyzer-long.md | 2025-10-10 | Original implementation |
| astrology-output-debugger | v1 | astrology-output-debugger.md | 2025-10-07 | Original implementation |

---

## Version History

### natal-interpreter

**v1** (2025-10-05):
- Original implementation
- Template A (Chart-Based)
- Model: Opus, Color: Green
- File: `natal-interpreter.md`

---

### life-arc-interpreter

**v1** (2025-10-07):
- Original implementation
- Template B (Timeline-Based)
- Model: Sonnet, Color: Purple
- File: `life-arc-interpreter.md`

---

### transit-analyzer

**v1** (2025-10-10):
- Original implementation
- Template C2 (Pure Movement-Based)
- Model: Sonnet, Color: Yellow
- File: `transit-analyzer.md`

---

### transit-analyzer-long

**v1** (2025-10-10):
- Original implementation
- Template C1 (Movement + Chapters)
- Model: Sonnet, Color: Yellow
- File: `transit-analyzer-long.md`

---

### astrology-output-debugger

**v1** (2025-10-07):
- Original implementation
- Debugging/quality assurance agent
- Model: Sonnet, Color: Yellow
- File: `astrology-output-debugger.md`

---

## Archived Versions

*No archived versions yet*

When an agent is versioned, the previous version file will be listed here for rollback purposes.

---

## How to Use This Tracker

**When refining an agent**:
1. agent-prompt-refiner-astrology creates new version file (e.g., `agent-name-v2.md`)
2. agent-prompt-refiner-astrology updates this tracker with new version entry
3. agent-prompt-refiner-astrology creates comparison document (`agent_name_v1_to_v2_changes.md`)
4. Original version moves to "Archived Versions" section (kept for rollback)

**To rollback to previous version**:
- Copy original file from `.claude/agents/[agent-name].md`
- Or use git to checkout previous commit

**To compare versions**:
- See comparison documents in `docs/agent_changes/`
- Each document shows detailed before/after changes with reasoning

---

## Notes

- Only interpretation agents are tracked here (natal, life arc, transit)
- Meta-agents (agent-creator, prompt-refiner, etc.) are not versioned through this system
- Version numbers increment sequentially (v1 → v2 → v3)
- All versions kept in git history for full audit trail
