# Troubleshooting Guide

**Purpose**: Common issues, debug workflows, and fix patterns for the Astrogy_Claude astrology interpretation system.

**Last Updated**: 2025-10-11

---

## Quick Index

- [Profile Issues](#profile-issues)
- [Seed Data Problems](#seed-data-problems)
- [Calculation Errors](#calculation-errors)
- [Interpretation Quality Issues](#interpretation-quality-issues)
- [RAG Database Problems](#rag-database-problems)
- [Output Generation Failures](#output-generation-failures)
- [Agent Coordination Issues](#agent-coordination-issues)
- [PDF Generation Problems](#pdf-generation-problems)

---

## Profile Issues

### Profile Not Found

**Symptom**: `Profile 'name' not found` error when running horoscope generator or mode-orchestrator.

**Causes**:
- Profile directory doesn't exist in `/profiles/`
- Typo in profile name
- Case sensitivity issue (Mac filesystem is case-insensitive by default, but code may be case-sensitive)

**Fix**:
```bash
# Create profile with correct birth data
python scripts/create_profile.py --name <name> --date 'YYYY-MM-DD' --time 'HH:MM' --location 'City, State/Country'

# Example
python scripts/create_profile.py --name darren --date '1978-11-28' --time '17:15' --location 'Chicago, IL'
```

**Verify**:
```bash
ls profiles/<name>/
# Should show: profile.txt or profile.md
```

### Missing Birth Data Fields

**Symptom**: Profile exists but missing required fields (date, time, location, coordinates).

**Causes**:
- Manually created profile without using create_profile.py
- Incomplete profile.txt
- Corrupted profile file

**Fix**:
1. Check profile.txt format:
   ```
   Name: John Doe
   Date: 1985-03-15
   Time: 14:30
   Location: New York, NY
   Latitude: 40.7128
   Longitude: -74.0060
   Timezone: America/New_York
   ```

2. Regenerate profile if corrupted:
   ```bash
   # Backup existing profile first
   cp -r profiles/<name> profiles/<name>_backup

   # Regenerate
   python scripts/create_profile.py --name <name> --date 'YYYY-MM-DD' --time 'HH:MM' --location 'City, State'
   ```

**Verify**:
```bash
cat profiles/<name>/profile.txt
# Check all required fields present
```

---

## Seed Data Problems

### Seed Data Missing

**Symptom**: `Seed data not found for profile 'name'` error from mode-orchestrator or horoscope generator.

**Causes**:
- Never generated seed data for this profile
- Seed data deleted or moved
- Wrong seed data path

**Fix**:
```bash
# Generate seed data using profile's birth data
python scripts/seed_data_generator.py --profile <name>

# This creates:
# profiles/<name>/seed_data/seed_data.json
# profiles/<name>/seed_data/natal_interpretation_enhanced.md
```

**Verify**:
```bash
ls profiles/<name>/seed_data/
# Should show: seed_data.json and natal_interpretation_enhanced.md
```

### Incomplete Seed Data

**Symptom**: Interpretation fails with missing planetary positions, houses, or aspects.

**Causes**:
- Seed data generation interrupted mid-process
- Swiss Ephemeris calculation error
- JSON structure corruption

**Fix**:
1. Check seed_data.json structure:
   ```bash
   python -m json.tool profiles/<name>/seed_data/seed_data.json > /dev/null
   # If error: JSON is corrupted, regenerate
   ```

2. Regenerate seed data:
   ```bash
   # Backup existing
   cp profiles/<name>/seed_data/seed_data.json profiles/<name>/seed_data/seed_data_backup.json

   # Regenerate
   python scripts/seed_data_generator.py --profile <name>
   ```

**Verify**:
```bash
# Check for required sections
grep -E '(planetary_positions|houses|aspects|dignities)' profiles/<name>/seed_data/seed_data.json
```

### Seed Data Schema Mismatch

**Symptom**: Interpretation agent fails with KeyError or missing attribute errors.

**Causes**:
- Old seed data format (from earlier version)
- Manual edits to seed_data.json
- Schema changed but profile not regenerated

**Fix**:
```bash
# Regenerate seed data with current schema
python scripts/seed_data_generator.py --profile <name>
```

**Check Schema Version**:
```bash
# Current schema should include:
# - planetary_positions (Sun through Saturn + modern planets)
# - houses (1-12 with whole-sign boundaries)
# - aspects (all major aspects with orbs)
# - dignities (domicile, exaltation, detriment, fall, etc.)
# - lots (Fortune, Spirit)
# - sect (day/night)
# - profection_year
```

---

## Calculation Errors

### Swiss Ephemeris Errors

**Symptom**: `Swiss Ephemeris calculation failed` or astronomical calculation errors.

**Causes**:
- pyswisseph not installed
- Swiss Ephemeris data files missing
- Invalid date/time/location

**Fix**:
1. Verify pyswisseph installed:
   ```bash
   pip list | grep pyswisseph
   # Should show: pyswisseph 2.10.3.2
   ```

2. Reinstall if missing:
   ```bash
   pip install pyswisseph==2.10.3.2
   ```

3. Check date/time validity:
   ```bash
   # Valid ranges:
   # Date: 1800-01-01 to 2100-12-31 (ephemeris range)
   # Time: 00:00 to 23:59
   # Latitude: -90 to 90
   # Longitude: -180 to 180
   ```

**Verify**:
```bash
python scripts/ephemeris_helper.py
# Run basic test calculations
```

### Transit Calculation Failures

**Symptom**: Transit calculator fails or returns empty results.

**Causes**:
- Invalid date range (start > end)
- Date outside ephemeris range
- Missing natal data for comparison

**Fix**:
```bash
# Check date range
python scripts/transit_calculator.py \
  --profile <name> \
  --start-date 2025-01-01 \
  --end-date 2025-12-31 \
  --report-type short

# Common issues:
# - Start date after end date (swap them)
# - Dates before 1800 or after 2100 (use valid range)
# - Missing natal positions (regenerate seed data)
```

**Verify**:
```bash
# Output should create:
# profiles/<name>/output/transit_data_<dates>.json
ls profiles/<name>/output/transit_data_*.json
```

---

## Interpretation Quality Issues

### Data Inconsistency in Output

**Symptom**: Report says "Jupiter in Gemini" but data shows "Jupiter in Cancer".

**Causes**:
- RAG retrieval returned incorrect sign reference
- LLM hallucination during synthesis
- Stale data passed to interpreter

**Fix**:
1. Run accuracy-checker (when implemented):
   ```bash
   # Will automatically flag data mismatches
   ```

2. Manual verification:
   ```bash
   # Compare report against source data
   cat profiles/<name>/seed_data/seed_data.json | grep Jupiter
   grep -i jupiter profiles/<name>/output/natal_horoscope_*.md
   ```

3. Regenerate report:
   ```bash
   # Use mode-orchestrator to regenerate
   # Ensure fresh seed data loaded
   ```

**Prevention**:
- Always use mode-orchestrator (validates data before passing to agents)
- Run accuracy-checker after generation
- Never manually edit seed data

### Missing Required Sections

**Symptom**: Report missing planetary sections, house rulers, or synthesis.

**Causes**:
- Agent prompt incomplete
- LLM output truncated
- Template not followed

**Fix**:
1. Check report structure:
   ```bash
   # Natal reports should have:
   grep -E '^## (Sun|Moon|Mercury|Venus|Mars|Jupiter|Saturn)' profiles/<name>/output/natal_horoscope_*.md

   # Should show 7 planetary sections minimum
   ```

2. Regenerate if incomplete:
   ```bash
   # Delete incomplete report
   rm profiles/<name>/output/natal_horoscope_<date>.md

   # Regenerate via mode-orchestrator
   ```

**Verify with accuracy-checker** (when implemented):
- Completeness check ensures all sections present
- Word count minimums enforced
- Template compliance verified

### Astrological Jargon Without Translation

**Symptom**: Report uses terms like "ZR L2", "profection year", "sect light" without explanation.

**Causes**:
- Agent not following accessibility guidelines
- RAG retrieval included technical terminology
- Template not enforced

**Fix**:
1. Check output style compliance:
   ```bash
   # Search for untranslated jargon
   grep -i -E '(ZR L[0-9]|profection|sect light|ASC|MC)' profiles/<name>/output/natal_horoscope_*.md

   # Each should have immediate translation
   ```

2. Manual fix (temporary):
   - Replace "ZR L2" with "Zodiacal Releasing sub-period"
   - Replace "profection year" with "annual timing cycle"
   - Replace "sect light" with "chart luminary (Sun for day charts, Moon for night charts)"

3. Long-term fix:
   - accuracy-checker will flag jargon violations
   - Agent prompts emphasize accessibility

**Prevention**:
- Agents instructed: NO astrological jargon without immediate translation
- accuracy-checker enforces (when implemented)

### Narrative Logic Errors

**Symptom**: Report describes Saturn square as "expansive opportunity" or Jupiter trine as "challenging constraint".

**Causes**:
- LLM confusion between planet archetypes
- RAG retrieval included contradictory interpretations
- Hard vs soft aspect logic reversed

**Fix**:
1. Manual verification:
   ```bash
   # Check Saturn aspects
   grep -A 5 'Saturn.*square' profiles/<name>/output/natal_horoscope_*.md
   # Should describe: challenge, limitation, maturation, structure

   # Check Jupiter aspects
   grep -A 5 'Jupiter.*trine' profiles/<name>/output/natal_horoscope_*.md
   # Should describe: expansion, opportunity, growth, ease
   ```

2. Regenerate if logic errors found

**Prevention**:
- accuracy-checker logic verification (when implemented)
- Validates transit types align with interpretations

---

## RAG Database Problems

### RAG Query Returns Empty Results

**Symptom**: Interpretation agent says "No RAG context found for [topic]".

**Causes**:
- Query too specific (no semantic matches)
- RAG database not built
- Embedding generation failed

**Fix**:
1. Check RAG database exists:
   ```bash
   ls output/database/astrology_rag_database.jsonl
   # Should be ~30MB file with 2,472 chunks
   ```

2. Rebuild RAG database if missing:
   ```bash
   python scripts/build_rag_database.py
   ```

3. Test query:
   ```bash
   python scripts/query_rag_database.py "Jupiter in Gemini"
   # Should return 5+ chunks from reference books
   ```

**Verify**:
```bash
# Check chunk count
wc -l output/database/astrology_rag_database.jsonl
# Should show 2472 lines
```

### RAG Database Corruption

**Symptom**: JSON decode errors when querying RAG database.

**Causes**:
- Incomplete build process
- File truncation
- Manual editing

**Fix**:
```bash
# Backup corrupted database
cp output/database/astrology_rag_database.jsonl output/database/astrology_rag_database_corrupted.jsonl

# Rebuild from source PDFs
python scripts/build_rag_database.py
```

**Verify**:
```bash
# Each line should be valid JSON
head -n 1 output/database/astrology_rag_database.jsonl | python -m json.tool
# Should parse without error
```

---

## Output Generation Failures

### Report Not Saved

**Symptom**: Agent completes but no markdown file in `/output/` or `/profiles/<name>/output/`.

**Causes**:
- Permissions error
- Directory doesn't exist
- Disk full

**Fix**:
1. Check output directory exists:
   ```bash
   ls -la profiles/<name>/output/
   # If missing:
   mkdir -p profiles/<name>/output/
   ```

2. Check permissions:
   ```bash
   ls -la profiles/<name>/
   # output/ should be writable
   ```

3. Check disk space:
   ```bash
   df -h .
   # Ensure sufficient space (reports are ~100KB-1MB)
   ```

**Verify**:
```bash
# Try creating test file
touch profiles/<name>/output/test.txt
# If error: permissions or disk issue
```

### Terminal Summary Not Displayed

**Symptom**: Report generates successfully but no synthesis section displayed in terminal.

**Causes**:
- Agent not following terminal output instructions
- Output truncated by system
- Wrong section extracted

**Fix**:
1. Check agent terminal output instructions:
   - natal-interpreter: Should output Introduction
   - life-arc-interpreter: Should output Introduction
   - transit-analyzer-short: Should output Summary Synthesis
   - transit-analyzer-long: Should output "Your [X]-Year Transit Arc"

2. Manual extraction:
   ```bash
   # Extract introduction from natal report
   awk '/^## Introduction/,/^## [A-Z]/' profiles/<name>/output/natal_horoscope_*.md
   ```

**Verify**:
- Check that agent follows "Terminal Summary Output" section in instructions
- Ensure complete section (200-300 words) is output, not shortened summary

---

## Agent Coordination Issues

### mode-orchestrator Not Routing Correctly

**Symptom**: Request for natal chart generates transit report (or wrong mode).

**Causes**:
- Ambiguous user request
- mode-orchestrator mode detection logic issue
- Missing agent availability check

**Fix**:
1. Use explicit mode keywords:
   ```
   # Natal horoscope:
   "Generate natal horoscope for darren"

   # Life arc:
   "Generate life arc for darren"

   # Transits:
   "Generate transit report for darren, next 3 months"
   ```

2. Check agent availability in mode-orchestrator instructions:
   ```bash
   grep -A 10 "Existing Agents" .claude/agents/mode-orchestrator.md
   # Verify agent is listed as COMPLETE
   ```

**Prevention**:
- Always use mode-orchestrator (never invoke interpreters directly)
- Use clear mode keywords in requests

### Agent Not Triggered

**Symptom**: Request recognized but appropriate agent not invoked.

**Causes**:
- Agent file missing from `.claude/agents/`
- Agent not in mode-orchestrator's invocation list
- Permission issues

**Fix**:
1. Check agent exists:
   ```bash
   ls .claude/agents/natal-interpreter.md
   ls .claude/agents/life-arc-interpreter.md
   ls .claude/agents/transit-analyzer-short.md
   ls .claude/agents/transit-analyzer-long.md
   ```

2. Verify permissions in `.claude/settings.local.json`:
   ```json
   {
     "permissions": {
       "allow": [
         "Read(//Users/[user]/.claude/agents/**)"
       ]
     }
   }
   ```

**Verify**:
```bash
# Test agent invocation manually
# (mode-orchestrator should handle this automatically)
```

---

## PDF Generation Problems

### PDF Missing Title Page

**Symptom**: PDF starts with content directly, no cover page.

**Causes**:
- CSS not applied
- Title page div missing from markdown
- create_synthesis_pdf.py not using base.css

**Fix**:
1. Check markdown has title page:
   ```bash
   grep -A 10 'class="title-page"' profiles/<name>/output/natal_horoscope_*.md
   # Should show title page HTML div
   ```

2. Verify CSS configuration:
   ```bash
   grep 'page-break-after' scripts/css/base.css
   # Should show: .title-page { page-break-after: always; }
   ```

3. Regenerate PDF:
   ```bash
   python scripts/create_synthesis_pdf.py \
     --input profiles/<name>/output/natal_horoscope_<date>.md \
     --output profiles/<name>/output/natal_horoscope_<date>.pdf
   ```

**Verify**:
```bash
# Open PDF and check:
# - Page 1: Title page only
# - Page 2: Content starts
```

### PDF Formatting Issues

**Symptom**: PDF has broken layout, missing fonts, or incorrect spacing.

**Causes**:
- ReportLab not installed
- CSS not loading
- Font files missing

**Fix**:
1. Reinstall ReportLab:
   ```bash
   pip install reportlab markdown
   ```

2. Check CSS path in create_synthesis_pdf.py:
   ```python
   # Should reference: scripts/css/base.css
   ```

3. Regenerate PDF with verbose output:
   ```bash
   python scripts/create_synthesis_pdf.py \
     --input <markdown_file> \
     --output <pdf_file> \
     --verbose
   ```

---

## Debug Workflows

### General Debug Workflow

When encountering ANY issue:

1. **Check Input Data**:
   - Profile exists and complete?
   - Seed data generated and valid?
   - Date ranges valid?

2. **Check Calculation Layer**:
   - Swiss Ephemeris working?
   - Transit calculations successful?
   - JSON output valid?

3. **Check Interpretation Layer**:
   - Agent invoked correctly?
   - RAG database accessible?
   - Output generated?

4. **Check Output Layer**:
   - Markdown saved successfully?
   - PDF generated (if requested)?
   - Terminal summary displayed?

### Using astrology-output-debugger

**Symptom**: Any interpretation quality issue.

**How to invoke**:
```
"I'm seeing incorrect planetary positions in the natal report. Can you debug?"

Agent will:
1. Load source data (seed_data.json)
2. Load generated report
3. Compare planetary positions
4. Flag inconsistencies
5. Check RAG queries that generated interpretation
6. Suggest fix
```

**Common Scenarios**:
- Data inconsistencies → astrology-output-debugger investigates
- Missing sections → astrology-output-debugger checks template compliance
- Logic errors → astrology-output-debugger validates synthesis against data

### Using accuracy-checker (When Implemented)

**Automatic Invocation**: Runs after every interpretation agent completes.

**Manual Invocation**:
```bash
# After report generation, accuracy-checker automatically runs
# Check log file:
cat profiles/<name>/output/accuracy_check_<report_type>_<timestamp>.log
```

**Output**:
```
🔍 ACCURACY CHECK: Natal Horoscope for Darren

DATA CONSISTENCY: ✅ PASS
COMPLETENESS: ✅ PASS
FORMAT COMPLIANCE: ⚠️ WARNING (2 minor issues)
LOGIC VERIFICATION: ✅ PASS

OVERALL: ✅ PASS WITH WARNINGS
```

---

## Common Error Messages

### "Profile not found"
**Fix**: Create profile with `python scripts/create_profile.py --name <name> --date ... --time ... --location ...`

### "Seed data not found"
**Fix**: Generate seed data with `python scripts/seed_data_generator.py --profile <name>`

### "Swiss Ephemeris calculation failed"
**Fix**: Check date/time validity, reinstall pyswisseph if needed

### "RAG database not found"
**Fix**: Build database with `python scripts/build_rag_database.py`

### "Agent not available"
**Fix**: Verify agent file exists in `.claude/agents/` and permissions allow reading

### "Transit calculation failed"
**Fix**: Check date range validity (start < end, within 1800-2100)

---

## Best Practices for Debugging

1. **Always Start with mode-orchestrator**: Never invoke interpretation agents directly
2. **Check Logs**: Most scripts create logs in `/output/` or profile output directories
3. **Verify Data First**: Before debugging interpretation, verify seed data is correct
4. **Use astrology-output-debugger**: For interpretation quality issues
5. **Regenerate When in Doubt**: Fresh calculation often fixes stale data issues
6. **Document New Issues**: Add to this file or ERROR_DATABASE.md for future reference

---

## Related Documentation

- **accuracy_checker_agent_spec.md**: Automated quality verification system (design)
- **ERROR_DATABASE.md**: Centralized error solutions (to be created)
- **WORKFLOWS_VISUAL.md**: Visual workflow diagrams
- **DATA_FORMATS.md**: JSON schemas and data structures (to be created)

---

*This troubleshooting guide will be updated as new issues are discovered and resolved.*
