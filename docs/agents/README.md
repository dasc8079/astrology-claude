# Agent Specifications Folder

**Purpose**: Agent specification documents that serve as technical references for agent prompts stored in `.claude/agents/`.

---

## What Goes Here

**Agent Specs** - Technical documentation for interpretation agents:
- natal-interpreter
- life-arc-interpreter
- transit-analyzer-short
- transit-analyzer-long
- mode-orchestrator
- accuracy-checker
- Any new interpretation agent

**Note**: This folder contains SPECIFICATIONS about agents, not the agent prompts themselves. Agent prompts live in `.claude/agents/`.

---

## File Naming Convention

```
[agent_name]_spec.md
```

**Examples**:
- `natal_interpreter_spec.md`
- `life_arc_interpreter_spec.md`
- `transit_analyzer_short_spec.md`
- `mode_orchestrator_spec.md`
- `accuracy_checker_spec.md`

---

## Agent Spec Contents

Each agent spec should include:

### 1. Agent Purpose & Responsibilities
- What does this agent do?
- What is its role in the system?
- When should it be invoked?

### 2. Derived From
- Link to source feature spec
- Which feature does this agent implement?
- Version relationship

**Example**:
```markdown
## Derived From

**Feature Spec**: [natal_horoscope_v2.md](../features/natal_horoscope_v2.md)
**Agent Prompt**: [.claude/agents/natal-interpreter.md](../../.claude/agents/natal-interpreter.md)
**Version**: Aligned with Natal Horoscope v2.1 (antiscia update)
```

### 3. Input Data Requirements
- What seed data does this agent need?
- What format must inputs be in?
- What's optional vs required?

### 4. Output Format Specifications
- What files does this agent generate?
- What format standards apply? (OUTPUT_STYLE_GUIDE.md)
- Two-file system (process + synthesis)

### 5. Interpretation Guidelines
- What astrological methods does it use?
- What hierarchical frameworks apply?
- What testimony levels (PRIMARY/SECONDARY/TERTIARY)?

### 6. RAG Query Strategy
- When should this agent query the RAG database?
- What types of queries are appropriate?
- How many queries per interpretation?

### 7. Coordination with Other Agents
- Which agents does this one depend on?
- Which agents invoke this one?
- What's the typical workflow?

### 8. Testing & Validation
- What profiles test this agent?
- What outputs verify correctness?
- What edge cases need checking?

---

## Workflow: Feature Spec → Agent Creation

### Step 1: Feature Spec Complete

Feature spec exists in `docs/features/[feature_name]_v[N].md`

### Step 2: Agent Creation

**Process**:
1. `astrology-agent-creator` reads feature spec
2. Extracts agent requirements
3. Creates agent prompt: `.claude/agents/[agent_name].md`
4. Creates agent spec: `docs/agents/[agent_name]_spec.md`

### Step 3: Implementation & Testing

- Build supporting scripts
- Test with profile data
- Refine agent prompt based on output quality
- Update agent spec with learnings

### Step 4: When Feature Updates

**Process**:
1. Feature spec updated (new version or version history entry)
2. If agent behavior changes:
   - Update agent prompt: `.claude/agents/[agent_name].md`
   - Update agent spec: `docs/agents/[agent_name]_spec.md`
   - Note version alignment in spec

---

## Relationship: Agent Spec ↔ Agent Prompt

### Agent Spec (THIS FOLDER)
- **Purpose**: Technical reference and design documentation
- **Audience**: Developers, future maintainers
- **Content**: Requirements, design decisions, integration details
- **Updates**: When feature changes or design evolves

### Agent Prompt (`.claude/agents/`)
- **Purpose**: Instructions for Claude Code agent execution
- **Audience**: Claude Code AI
- **Content**: Behavior instructions, output standards, examples
- **Updates**: When interpretation approach changes or quality needs improvement

### Example Relationship

**Feature Spec**: `docs/features/natal_horoscope_v2.md`
↓ derives agent requirements
**Agent Spec**: `docs/agents/natal_interpreter_spec.md`
↓ informs creation of
**Agent Prompt**: `.claude/agents/natal-interpreter.md`

---

## Current Agent Specs

**Active**:
- `natal_interpreter_spec.md` - Natal horoscope synthesis agent
- `mode_orchestrator_spec.md` - Central routing and orchestration
- `accuracy_checker_spec.md` - Output quality verification

**Future**:
- `life_arc_interpreter_spec.md` - Life arc timeline synthesis
- `transit_analyzer_short_spec.md` - Short-term transit analysis
- `transit_analyzer_long_spec.md` - Long-term transit analysis

---

## Related Folders

- `docs/features/` - Feature specs that agents implement
- `.claude/agents/` - Actual agent prompts (execution instructions)
- `docs/updates/` - Update specs that may affect agents
- `docs/archive/agents/` - Archived old agent spec versions

---

## Best Practices

✅ **DO**:
- Keep agent specs aligned with feature specs
- Link agent spec to source feature spec
- Document design decisions and tradeoffs
- Update spec when agent behavior changes
- Include testing guidance

❌ **DON'T**:
- Duplicate agent prompt content in spec (reference it)
- Skip noting feature spec version alignment
- Let agent specs become outdated
- Mix agent spec with agent prompt
- Forget to update spec when feature updates

---

## Agent Creation Checklist

When creating a new agent:

- [ ] Feature spec exists and is complete
- [ ] Agent requirements extracted from feature spec
- [ ] Agent prompt created: `.claude/agents/[name].md`
- [ ] Agent spec created: `docs/agents/[name]_spec.md`
- [ ] Agent spec links to feature spec
- [ ] Testing profiles identified
- [ ] Coordination with other agents documented
- [ ] RAG query strategy defined
- [ ] Output format standards specified

---

**Questions?** See [DOCS_REFACTOR_PROPOSAL.md](../DOCS_REFACTOR_PROPOSAL.md) for complete workflow documentation.
