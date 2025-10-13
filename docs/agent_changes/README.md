# Agent Changes Directory

**Purpose**: Track version history and comparison documents for astrology interpretation agents.

**Maintained by**: agent-prompt-refiner-astrology

---

## Contents

### Version Tracker
- **agent_version_tracker.md** - Central registry of all agent versions
- Shows active versions, version history, and archived versions
- Updated automatically when agent-prompt-refiner-astrology creates new versions

### Comparison Documents
Detailed before/after documentation for each version change:

- **[agent-name]_v1_to_v2_changes.md** - Version 1 → Version 2 comparison
- **[agent-name]_v2_to_v3_changes.md** - Version 2 → Version 3 comparison
- etc.

Each comparison document includes:
- Summary of changes (dimensions affected, sections modified)
- Detailed before/after text for each change
- Reasoning for changes
- Output comparison samples
- Testing notes
- Rollback instructions

---

## How This System Works

### When You Want to Refine an Agent

**Invoke**: `@agent-prompt-refiner-astrology`

**Process**:
1. Describe what needs improvement (style, tone, length, format, voice)
2. Agent shows current prompt sections
3. Agent proposes specific changes with reasoning
4. Agent generates test output (current vs. modified)
5. You review and provide feedback
6. Iterate until satisfied
7. Agent creates versioned file (e.g., `natal-interpreter-v2.md`)
8. Agent commits with git and creates comparison document
9. Agent updates version tracker

### Version Naming Convention

- **Original**: `agent-name.md`
- **Version 2**: `agent-name-v2.md`
- **Version 3**: `agent-name-v3.md`
- etc.

Original files are **kept for rollback**, not deleted.

### Comparison Documents

Each version change gets a comparison document showing:
- What changed (specific prompt sections)
- Why it changed (user feedback, quality issues)
- Impact on output (test results)
- Rollback instructions

---

## Example Workflow

### User Reports Issue
```
User: "The natal synthesis feels too clinical. I want it more poetic."
```

### Agent-Prompt-Refiner Process

1. **Discovery**: Ask which agent, which quality dimension, specific issue
2. **Display**: Show current Voice Standards section from natal-interpreter.md
3. **Propose**: Suggest specific edits to make voice more poetic
4. **Test**: Generate natal synthesis sample with current vs. modified prompt
5. **Review**: User sees difference, provides feedback
6. **Iterate**: Refine changes based on feedback
7. **Approve**: User approves final version
8. **Version**: Create `natal-interpreter-v2.md`
9. **Document**: Create `natal-interpreter_v1_to_v2_changes.md`
10. **Commit**: Git commit with descriptive message
11. **Update**: Update `agent_version_tracker.md`

### Result

- New version file: `.claude/agents/natal-interpreter-v2.md`
- Comparison doc: `docs/agent_changes/natal-interpreter_v1_to_v2_changes.md`
- Version tracker updated
- Original file kept for rollback
- Full git history of changes

---

## Quality Dimensions Tracked

### Style
- Clinical ↔ Poetic
- Analytical ↔ Narrative

### Tone
- Objective ↔ Empathetic
- Authoritative ↔ Therapeutic

### Length
- Verbose ↔ Concise
- Detailed ↔ Summary

### Format
- Section structure
- Paragraph length
- Subsection organization

### Voice
- Second person ↔ Third person
- Direct ↔ Descriptive

---

## Rollback Procedure

If a new version doesn't work as expected:

```bash
# Option 1: Use original file (kept in same directory)
cp .claude/agents/agent-name.md .claude/agents/agent-name-active.md

# Option 2: Use git to checkout previous version
git log --oneline .claude/agents/agent-name-v2.md
git checkout <commit-hash> .claude/agents/agent-name-v2.md
```

All version history preserved in git for full audit trail.

---

## Notes

**Testing Required**: All changes must be tested with actual profile data (Darren's profile) before versioning.

**User Approval Required**: agent-prompt-refiner-astrology will NOT version changes without explicit user approval.

**One Agent at a Time**: Focus refinement on single agent to maintain clarity and testing validity.

**Documentation is Mandatory**: Every version change must have comparison document.

---

## Current Agent Versions

See **agent_version_tracker.md** for up-to-date registry of all agent versions.

As of 2025-10-12:
- All agents at v1 (original implementations)
- No refinements yet
- System ready for iterative improvements
