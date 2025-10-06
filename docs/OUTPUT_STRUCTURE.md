# Output Structure Guidelines

## Universal Rule for All Agent Outputs

**All agent-generated outputs MUST follow this structure:**

```
profiles/
└── {profile_name}/
    ├── seed_data/
    │   └── master_seed_data.yaml              # Input data
    └── output/
        ├── {tool_name}_process_{details}.md    # Technical/process data
        └── {tool_name}_synthesis_{details}.pdf  # Narrative interpretation
```

## Core Principles

### 1. Profile-Based Organization
- Everything for a profile stays together under `profiles/{profile_name}/`
- Seed data in `profiles/{profile_name}/seed_data/`
- Outputs in `profiles/{profile_name}/output/`
- Example: `profiles/darren/`, `profiles/alice/`, etc.

### 2. Input-Output Pairing
- **Input (Seed Data)**: `profiles/{profile_name}/seed_data/master_seed_data.yaml`
- **Output (Reports)**: `profiles/{profile_name}/output/{tool_name}_*.{md|pdf}`
- Seed data and outputs are paired within the same profile directory

### 3. Two-File Output Standard

Every agent tool that generates reports MUST produce two files with **distinct content and audiences**:

#### Process File (`.md`) - FOR ASTROLOGERS

- **Naming**: `{tool_name}_process_{details}.md`
- **Audience**: Astrologers, technical verification
- **Purpose**: Complete technical data for validation
- **Format**: Markdown with tables, lists, structured data
- **Tone**: Technical, precise, astrological terminology

**Content**:
- ✅ All planetary positions (longitude, sign, degree, house)
- ✅ Aspect calculations with orbs
- ✅ Dignity assessments (domicile, exaltation, detriment, fall)
- ✅ House cusps and rulers
- ✅ ZR periods (L1/L2) with exact ages and dates
- ✅ Profection years with time lords
- ✅ Secondary progression data
- ✅ Solar return chart details
- ✅ Transit positions and aspects
- ✅ Technical timelines with ages/dates
- ✅ Source citations and footnotes
- ✅ All astrological jargon and terminology

**Example**: `life_arc_process_ages_0-46.md`
```markdown
================================================================================
ZODIACAL RELEASING - FORTUNE
================================================================================
Lot Position: Sagittarius 25.86°

L1 PERIOD: Capricorn (Ages 12.0-39.0)
  Ruler: Saturn (domicile in Capricorn 6H)
  Duration: 27 years

  L2: Scorpio (Ages 35.5-37.4) ⭐ CURRENT
    Ruler: Mars (domicile in Aries 9H)
    Duration: 1.95 years
    Dates: 2024-06-25 to 2026-06-06

PROFECTIONS
Age 36: 1st House (Leo)
  Time Lord: Sun (Capricorn 6H, conjunct Saturn 0.88° orb)
  Theme: Identity, body, self-assertion, new cycle

TRANSITS (2025-10-06)
- Uranus conjunct Natal Jupiter 10H (orb 0.13°) *** EXACT ***
- Saturn sextile Natal Jupiter (orb 0.30°)
```

#### Synthesis File (`.pdf`) - FOR THE NATIVE

- **Naming**: `{tool_name}_synthesis_{details}.pdf`
- **Audience**: The person receiving the reading (NO astrology knowledge assumed)
- **Purpose**: Psychological narrative interpretation
- **Format**: Professional PDF with Helvetica font, left-aligned
- **Tone**: Warm, insightful, psychologically rich, validating

**Content**:
- ✅ Pure psychological narrative
- ✅ Life story and major chapters
- ✅ Current position and meaning
- ✅ Strengths, challenges, patterns
- ✅ Future outlook and transitions
- ✅ Accessible, flowing prose
- ✅ Human-centered language

**Excludes** (CRITICAL):
- ❌ NO astrological jargon ("Mars square Saturn", "10th house")
- ❌ NO planet names in interpretations
- ❌ NO house numbers or aspect types
- ❌ NO technical references ("ZR L2", "Profection")
- ❌ NO tables or technical data
- ❌ NO source citations (that's for the MD file)

**Example**: `life_arc_synthesis_ages_0-46.pdf`
```
You're in the final years of a profound 27-year chapter that has shaped
your adult life. This period has been about discipline, proving yourself,
and building something lasting through sustained effort. The intensity
you're experiencing now—the sense that something is ending, that the
ground is shifting beneath you—is real. You're not stuck; you're in the
final preparation for the most significant transition you've experienced
as an adult.

At age 39, everything changes. The weight lifts. The structures you've
built remain, but the relentless pressure to prove, achieve, and master
gives way to a lighter phase focused on innovation, collaboration, and
freedom. You've earned this. The next 27 years will feel entirely
different...

[Continues as flowing narrative with NO astrological terminology]
```

**Style Requirements for Synthesis**:
- Sound like a **skilled therapist**, not an astrologer
- Write in **flowing narrative prose**, not bullet points
- The native should feel **deeply seen and understood**
- Translate all astrological patterns into **human psychological experience**
- See `docs/STYLE_GUIDE.md` for complete guidelines

## Implementation Examples

### Life Arc Interpreter
```bash
# Input
profiles/darren/seed_data/master_seed_data.yaml

# Outputs
profiles/darren/output/life_arc_process_ages_0-46.md      # Technical timeline
profiles/darren/output/life_arc_synthesis_ages_0-46.pdf   # Narrative interpretation

# Synthesis Structure (Simplified)
## Your Life Arc Story
   [Narrative synthesis integrating all timing techniques - major chapters, current position, what's ahead]
   [Ends with 3-5 sentence poetic wrapup paragraph - NO heading for this paragraph]

## Theme Convergences
   [Where 2+ timing techniques align]

## Major Transitions
   [Key age markers and chapter changes]
```

### Natal Chart Interpreter (Mode 1)
```bash
# Input
profiles/darren/seed_data/master_seed_data.yaml

# Outputs
profiles/darren/output/natal_chart_process.md             # Planet positions, aspects, houses
profiles/darren/output/natal_chart_synthesis.pdf          # Birth chart interpretation

# Note: Synthesis ends with 3-5 sentence poetic wrapup paragraph (NO heading for this paragraph)
```

### Transit Report (Mode 3 - Future)
```bash
# Input
profiles/darren/seed_data/master_seed_data.yaml

# Outputs
profiles/darren/output/transit_process_2025-01_to_2026-12.md   # Transit timeline with dates
profiles/darren/output/transit_synthesis_2025-01_to_2026-12.pdf # Transit interpretation
```

## Directory Structure

```
Astrogy_Claude/
├── profiles/
│   ├── darren/
│   │   ├── profile.md                          # Profile metadata
│   │   ├── seed_data/
│   │   │   └── master_seed_data.yaml          # Input: natal chart data
│   │   └── output/
│   │       ├── natal_chart_process.md
│   │       ├── natal_chart_synthesis.pdf
│   │       ├── life_arc_process_ages_0-46.md
│   │       ├── life_arc_synthesis_ages_0-46.pdf
│   │       ├── transit_process_2025-01_to_2026-12.md
│   │       └── transit_synthesis_2025-01_to_2026-12.pdf
│   │
│   └── alice/
│       ├── profile.md
│       ├── seed_data/
│       │   └── master_seed_data.yaml
│       └── output/
│           ├── natal_chart_process.md
│           └── natal_chart_synthesis.pdf
│
└── scripts/
    ├── seed_data_generator.py                  # Generates input
    ├── life_arc_generator.py                   # Generates process data
    └── [other calculators]
```

## Testing and Versioning

**During development/testing**: Do NOT overwrite existing outputs. Use versioning to preserve comparisons:

```bash
# Version outputs during testing
profiles/darren/output/life_arc_synthesis_ages_0-46_v1.md
profiles/darren/output/life_arc_synthesis_ages_0-46_v2.md
profiles/darren/output/life_arc_synthesis_ages_0-46.md  # Final version

# Or timestamp versions
profiles/darren/output/life_arc_synthesis_ages_0-46_20251006.md
```

**Production**: Use standard filenames (no versioning) for final outputs delivered to clients.

## Agent Implementation Requirements

### All Agents Must:

1. **Accept `profile_name` parameter**
   - Use to load seed data from `profiles/{profile_name}/seed_data/`
   - Use to determine output location `profiles/{profile_name}/output/`

2. **Create profile output directory if needed**
   ```python
   output_dir = Path(f"profiles/{profile_name}/output")
   output_dir.mkdir(parents=True, exist_ok=True)
   ```

3. **Generate both process and synthesis files with distinct content**
   - **Process file (.md)**: ALL technical data, astrological jargon, calculations, tables
   - **Synthesis file (.md → .pdf)**: PURE narrative, ZERO jargon, psychological interpretation

4. **Follow standard output workflow**
   ```python
   # Step 1: Generate process data (ALL technical content)
   process_data = generate_technical_data(...)  # Includes all astrological jargon
   process_path = output_dir / f"{tool_name}_process_{details}.md"
   with open(process_path, 'w') as f:
       f.write(process_data)

   # Step 2: Generate synthesis markdown (PURE narrative, NO jargon)
   synthesis_content = generate_narrative_synthesis(...)  # Psychological language only
   synthesis_md_path = output_dir / f"{tool_name}_synthesis_{details}.md"
   with open(synthesis_md_path, 'w') as f:
       f.write(synthesis_content)

   # Step 3: Convert synthesis to PDF (Helvetica, left-aligned)
   import subprocess
   subprocess.run([
       'python', 'scripts/pdf_generator.py',
       str(synthesis_md_path),
       '--title', f"{Tool Name}: {profile_name.title()}"
   ], check=True)
   ```

5. **Use consistent naming**
   - `{tool_name}_process_{details}.md` - Technical data
   - `{tool_name}_synthesis_{details}.md` - Narrative (markdown)
   - `{tool_name}_synthesis_{details}.pdf` - Narrative (PDF, auto-generated)
   - Details can include: ages, date ranges, specific focus

6. **Handle multiple profiles gracefully**
   - Never hardcode profile names
   - Support running same tool for different profiles
   - Keep outputs separate by profile

## Standard PDF Generation Workflow

### Step 1: Generate Synthesis Markdown

All agents should first generate the synthesis as markdown:

```python
synthesis_md_path = Path(f"profiles/{profile_name}/output/{tool_name}_synthesis_{details}.md")

with open(synthesis_md_path, 'w') as f:
    f.write(synthesis_content)
```

### Step 2: Convert to PDF Using pdf_generator.py

Use the standardized `scripts/pdf_generator.py` utility:

```bash
# Command line usage
python scripts/pdf_generator.py profiles/darren/output/life_arc_synthesis_ages_0-46.md

# With custom title
python scripts/pdf_generator.py profiles/darren/output/life_arc_synthesis_ages_0-46.md \
    --title "Life Arc Interpretation: Darren (Ages 0-46)"

# With custom output path
python scripts/pdf_generator.py input.md output.pdf --title "My Report"
```

### Step 3: Programmatic Usage in Agents

```python
from pathlib import Path
import subprocess

def generate_synthesis_pdf(
    markdown_path: str,
    title: str = "Astrology Report"
) -> str:
    """
    Convert synthesis markdown to PDF using standard utility.

    Args:
        markdown_path: Path to synthesis markdown file
        title: Document title for PDF metadata

    Returns:
        Path to generated PDF (same name, .pdf extension)
    """
    result = subprocess.run([
        'python',
        'scripts/pdf_generator.py',
        markdown_path,
        '--title',
        title
    ], check=True, capture_output=True, text=True)

    # PDF path is same as markdown, with .pdf extension
    pdf_path = Path(markdown_path).with_suffix('.pdf')

    return str(pdf_path)

# Example usage in agent
synthesis_md = f"profiles/{profile_name}/output/life_arc_synthesis_ages_0-46.md"
synthesis_pdf = generate_synthesis_pdf(
    synthesis_md,
    title=f"Life Arc Interpretation: {profile_name.title()} (Ages {start_age}-{end_age})"
)
```

### PDF Features

The standard PDF generator (`scripts/pdf_generator.py`) provides:

- **Professional typography**: Helvetica sans-serif font, proper line height, left-aligned text
- **Structured styling**: Hierarchical headings with color coding
- **Page layout**: Letter size, 2.5cm margins, page numbers
- **Readable design**: Clean, accessible layout for non-technical audience
- **Markdown extensions**: Tables, fenced code, smart quotes, sane lists
- **Responsive sizing**: Auto-adjusts for content length
- **File size**: Optimized (~250KB for typical 6,900 word report)

**Style Standards**:
- Font: Helvetica (not Georgia)
- Alignment: Left (not justified)
- Audience: Non-astrologers
- Content: Pure narrative, zero jargon
- See `docs/STYLE_GUIDE.md` for complete requirements

### Dependencies

Required Python packages (already in requirements.txt):

```bash
pip install markdown weasyprint
```

These are installed in the virtual environment and available to all agents.

## Why This Structure?

### Benefits:

1. **Clarity**: Process vs synthesis separation
2. **Organization**: All profile data in one place (seed_data + output together)
3. **Scalability**: Easy to add new profiles
4. **Professionalism**: PDF synthesis for end users
5. **Debugging**: Technical .md files for troubleshooting
6. **Version Control**: Markdown files are git-friendly
7. **User Experience**: PDFs are readable, shareable, printable
8. **Self-Contained**: Each profile directory contains everything for that person

### Prevents:

- ❌ Outputs scattered across project
- ❌ Mixing different users' data
- ❌ Confusion about which file is which
- ❌ Difficulty finding reports
- ❌ Seed data / output mismatch
- ❌ Separation of input and output data

## Migration Path

When implementing this for existing tools:

1. Update agent to accept `profile_name` parameter
2. Create `profiles/{profile_name}/output/` directory
3. Generate process .md file first (technical output)
4. Generate synthesis .md file second (narrative interpretation)
5. Convert synthesis to PDF using `scripts/pdf_generator.py`
6. Update documentation with new file paths
7. Test with multiple profiles to verify separation

### Complete Agent Workflow Example

```python
#!/usr/bin/env python3
"""
Example Agent Tool - Life Arc Interpreter
Demonstrates standard output workflow.
"""
from pathlib import Path
import subprocess

def generate_life_arc_report(profile_name: str, start_age: int, end_age: int):
    """Generate life arc report following standard workflow."""

    # 1. Load seed data
    seed_data_path = Path(f"profiles/{profile_name}/seed_data/master_seed_data.yaml")
    # ... load data ...

    # 2. Create output directory
    output_dir = Path(f"profiles/{profile_name}/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 3. Generate process data (technical timeline)
    process_data = generate_technical_timeline(...)  # Your logic here
    process_path = output_dir / f"life_arc_process_ages_{start_age}-{end_age}.md"
    with open(process_path, 'w') as f:
        f.write(process_data)
    print(f"✅ Process data: {process_path}")

    # 4. Generate synthesis (narrative interpretation)
    synthesis_content = generate_narrative_synthesis(...)  # Your logic here
    synthesis_md_path = output_dir / f"life_arc_synthesis_ages_{start_age}-{end_age}.md"
    with open(synthesis_md_path, 'w') as f:
        f.write(synthesis_content)
    print(f"✅ Synthesis markdown: {synthesis_md_path}")

    # 5. Convert synthesis to PDF
    subprocess.run([
        'python',
        'scripts/pdf_generator.py',
        str(synthesis_md_path),
        '--title',
        f"Life Arc Interpretation: {profile_name.title()} (Ages {start_age}-{end_age})"
    ], check=True)

    synthesis_pdf_path = synthesis_md_path.with_suffix('.pdf')
    print(f"✅ Synthesis PDF: {synthesis_pdf_path}")

    return {
        'process': str(process_path),
        'synthesis_md': str(synthesis_md_path),
        'synthesis_pdf': str(synthesis_pdf_path)
    }
```

## Critical: Content Separation

**The most important rule**: Process and Synthesis files contain **DIFFERENT CONTENT** for **DIFFERENT AUDIENCES**.

### Process File (.md):
- **For**: Astrologers validating the work
- **Contains**: ALL technical data, calculations, jargon
- **Language**: Astrological terminology expected and required

### Synthesis File (.pdf):
- **For**: The native (person receiving reading)
- **Contains**: ONLY psychological narrative interpretation
- **Language**: ZERO astrological jargon, plain English only

**Common Mistake**: Putting the same content in both files.
**Correct Approach**: Separate technical data (MD) from narrative interpretation (PDF).

## See Also

- `STYLE_GUIDE.md` - ⭐ **READ THIS** for tone, voice, and content standards
- `PROFILES_GUIDE.md` - Profile management
- `DEVELOPMENT.md` - Development guidelines
- `README.md` - Project overview
