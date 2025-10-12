# Deprecated Scripts

This directory contains scripts that are **no longer used in production** but preserved for historical reference and understanding the project's evolution.

## ⚠️ DO NOT USE THESE SCRIPTS FOR PRODUCTION WORK ⚠️

---

## Contents

### life_arc_synthesis_simplified.py

**Status**: Deprecated (replaced by life-arc-interpreter agent)
**Created**: October 2025 (development phase)
**Purpose**: Testing/development script for Mode 2 (Life Arc Reports)

**What it does**:
- Generates basic 3-section life arc interpretation
  1. Your Life Arc Story (narrative)
  2. Theme Convergences (alignment points)
  3. Major Transitions (age markers)
- Direct script execution bypassing agent system
- Simplified output without convergence scoring

**Why it's deprecated**:
- Missing 25-point convergence scoring system (Tier 1-3 analysis)
- No proper chapter narrative structure
- Limited psychological depth
- Doesn't follow OUTPUT_STYLE_GUIDE formatting standards
- No access to agent-specific prompt engineering
- Generated reports lack professional polish

**What to use instead**:
Use the **life-arc-interpreter agent** for all Mode 2 (Life Arc) reports:
```python
# Correct approach:
Task(
    subagent_type="life-arc-interpreter",
    prompt="Generate life arc report for profile 'name' ages 0-100, current age X"
)
```

The agent provides:
- ✅ Proper convergence analysis with scoring
- ✅ Chapter-based narrative structure (Template B from OUTPUT_STYLE_GUIDE)
- ✅ Psychological depth with therapeutic tone
- ✅ Zero astrological jargon for accessibility
- ✅ Professional PDF output with proper CSS styling

---

## When Scripts Get Deprecated

Scripts move to this folder when:
1. **Replaced by agent** - Agent-based approach provides superior output
2. **Testing complete** - Script served its purpose during development
3. **Better approach found** - Architecture evolved to better solution
4. **Standards changed** - No longer matches OUTPUT_STYLE_GUIDE requirements

## Preservation Rationale

We keep deprecated scripts because:
- **Historical context** - Shows project evolution
- **Learning resource** - Demonstrates what didn't work and why
- **Code reference** - May contain useful logic for future features
- **Avoid regression** - Prevents accidentally recreating deprecated approaches

---

**Last Updated**: 2025-10-10
