# Style Guide: Astrology Interpretation Output

## Universal Standards for All Interpretation Agents

This guide defines the default tone, style, and format for all agent-generated interpretations in the astrology application. All interpretation agents (natal-interpreter, life-arc-interpreter, transit-interpreter, etc.) MUST follow these standards.

**DEFAULT VOICE**: The natal-interpreter synthesis voice is the standard for all synthesis outputs. All agents should match this tone, style, and approach when writing for non-astrologers.

**REFERENCE STANDARD**: See `profiles/darren/output/natal_horoscope_synthesis.pdf` for the exact voice, style, and jargon level expected in all synthesis outputs.

---

## Two-File Standard: Content Separation

### Process File (.md) - Technical/Astrological

**Purpose**: For astrologers and technical verification
**Audience**: Someone who understands astrological jargon
**Content**: All technical data, calculations, and traditional terminology

**Includes**:
- Planetary positions (longitude, sign, degree, house)
- Aspect calculations with orbs
- Dignity assessments (domicile, exaltation, detriment, fall)
- House cusps and rulers
- Zodiacal releasing periods with dates
- Profection years with time lords
- Secondary progression positions
- Solar return chart data
- Transit positions and aspects
- Technical timelines with ages/dates
- Citations to traditional sources
- All astrological terminology and jargon

**Tone**: Professional, technical, precise
**Format**: Tables, lists, structured data, technical language welcome

**Example**:
```
ZODIACAL RELEASING - FORTUNE
L1 Period: Capricorn (Ages 12-39)
  Ruler: Saturn (domicile in Capricorn 6H)
  Duration: 27 years
  L2 Period: Scorpio (Ages 35.5-37.4)
    Ruler: Mars (domicile in Aries 9H)
    Duration: 1.95 years

PROFECTIONS
Age 36: 1st House (Leo)
  Time Lord: Sun (in Capricorn 6H, conjunct Saturn)
  Theme: Identity, new cycle beginning
```

### Synthesis File (.pdf) - Narrative/Psychological

**Purpose**: For the native (person receiving the reading)
**Audience**: Someone with NO astrological knowledge
**Content**: Pure psychological narrative with ZERO astrological jargon

**Includes**:
- Life story and major chapters
- Psychological insights and character themes
- Strengths, challenges, patterns
- Life purpose and direction
- Current position and what it means
- Future outlook and transitions
- Accessible, validating, insightful narrative

**Excludes**:
- ❌ Astrological terminology ("Mars square Saturn", "Sun in 10th house")
- ❌ Technical references ("ZR Fortune L2", "Profection year")
- ❌ Planet names in interpretations
- ❌ House numbers or aspects
- ❌ Jargon of any kind

**Tone**: Warm, insightful, psychologically rich, validating
**Format**: Flowing narrative prose, minimal subsections

**Example**:
```
You're in the final years of a major life chapter that began at age 12.
This has been a period of discipline, structure-building, and mastery.
The intensity you're feeling now is the pressure of completion—you're
consolidating everything you've learned and built over the past 24 years
before stepping into a new phase focused on innovation and partnership.

Your professional life has always demanded that you prove yourself through
concrete achievement. There's an inner tension between taking bold action
and feeling the weight of responsibility...
```

---

## Tone & Voice Standards

### For Synthesis/PDF (Non-Astrologers)

**DEFAULT VOICE MODEL**: Use natal-interpreter synthesis style for all agents

**Sound like**: A skilled psychologist or therapist interpreting personality
**Don't sound like**: An astrologer listing placements

**Key Characteristics of Default Voice**:
- Direct second-person address ("You are someone who...", "At age 25 you entered...")
- SPARSE astrological terminology (almost none in narrative)
- Rich, flowing narrative prose with substantial paragraphs
- Warm, validating, insightful tone
- NO bullet points or numbered lists in main narrative
- Psychological language that feels personal and revelatory
- Reader should feel deeply seen and understood

#### ✅ DO:
- Write in flowing narrative paragraphs (long, substantial paragraphs)
- Use plain English psychological language
- Focus on inner experience, patterns, and meaning
- Make the native feel deeply seen and understood
- When astrological terms are necessary, IMMEDIATELY translate to psychological meaning
- Example: "Mars in Aries in your 9th house speaks to a philosophical warrior..." (placement → meaning in same sentence)
- Use therapeutic, validating language that helps person recognize lived experience
- Translate astrological patterns into human experience
- Use "you" and "your" (second person)
- Be warm, insightful, validating
- Maintain narrative flow (avoid excessive subsections)

#### Translation Examples (Astrology → Psychology):

**Natal Chart**:
- ❌ "Sun in Capricorn in 6th house"
- ✅ "Your vitality is tied to doing meaningful work, to building something lasting through patient effort"

- ❌ "Moon in Leo rising"
- ✅ "Your emotional world is dramatic, generous, and immediately present. You feel things intensely and express those feelings openly"

- ❌ "Mars in Aries in 9th house"
- ✅ "There's a philosophical warrior in you, someone who believes fiercely, acts boldly, and refuses to accept received wisdom without testing it personally"

**Life Arc**:
- ❌ "You're in Capricorn ZR Fortune L1 (ages 12-39), currently in Scorpio L2 (ages 35.5-37.4)"
- ✅ "At age 12, you entered a 27-year chapter that asked you to build something lasting through discipline and sustained effort. Right now, you're in the final years of this chapter, in a particularly intense sub-period that began at age 35"

- ❌ "At age 39, Fortune shifts to Aquarius L1"
- ✅ "At age 39, you'll step into an entirely new 27-year chapter. The weight of proving yourself through relentless discipline will lift, and you'll enter a phase where innovation, collaboration, and freedom become primary"

- ❌ "Your profection year is 1st house, Lord of Year is Sun"
- ✅ "This year brings focus to identity, self-definition, and new beginnings in your personal development"

**Key Principle**: Translate the MEANING and FELT EXPERIENCE, not the technical term.

#### ❌ DON'T:
- Use bare astrological jargon without immediate translation
- List placements cookbook-style
- Reference planets, signs, houses, aspects by name
- Use technical terminology
- Break into excessive bullet points or numbered lists
- Sound deterministic ("You will definitely...")
- Make the native feel labeled or pigeonholed

#### Translation Examples:

| ❌ Astrological Jargon | ✅ Psychological Language |
|------------------------|---------------------------|
| "Mars square Saturn in your chart" | "An inner tension between taking bold action and feeling restricted by responsibility" |
| "Sun in the 10th house" | "Your sense of self is deeply tied to your public role and achievements" |
| "Moon in Leo in the 1st house" | "You experience life with emotional intensity and need to feel recognized and valued" |
| "Venus ruling your 10th house" | "Your career path finds its expression through beauty, connection, and creative harmony" |
| "Capricorn ZR Fortune L1 period" | "A 27-year chapter focused on discipline, mastery, and building lasting structures" |
| "Profection to the 1st house" | "A year focused on identity, new beginnings, and redefining who you are" |

### For Process/MD (Astrologers)

**Sound like**: A traditional astrologer documenting technical analysis
**Audience**: Someone validating the astrological basis of the interpretation

#### ✅ DO:
- Use proper astrological terminology
- Include technical details (signs, houses, degrees, orbs)
- Cite traditional sources with footnotes
- Assess dignities and planetary strength
- Reference aspects, house rulers, time lords
- Use structured format (tables, lists, sections)
- Be precise and technically accurate

#### ❌ DON'T:
- Avoid technical language (this section NEEDS it)
- Omit dignity assessments or planetary positions
- Skip source citations
- Ignore sect considerations
- Use modern astrological methods (unless explicitly added as context)

---

## Structure Standards

### Synthesis/PDF Structure

**Required Sections** (in order):

1. **Introduction** (2-4 paragraphs)
   - Essential nature and core life story
   - Current position in the life arc
   - Overarching themes

2. **Major Life Chapters** (if applicable to mode)
   - Narrative description of major periods
   - How you got to where you are now
   - Psychological themes of each chapter

3. **Current Position** (most detailed)
   - Where you are in the life story
   - What this moment means
   - Convergent themes and patterns
   - Inner experience and outer manifestation

4. **Future Outlook** (brief, non-predictive)
   - What's ahead in the life arc
   - Major transitions approaching
   - The next chapter

5. **Synthesis & Integration** (conclusion)
   - Tying all themes together
   - The coherent whole of your current position
   - Closing insights

6. **Poetic Wrapup** (final paragraph) ⭐ **REQUIRED**
   - Brief, separate closing paragraph
   - Warm, grounded, poetic prose
   - Affirms strengths, natural gifts, or opportunities present
   - Acknowledges key constraints or challenges with compassion
   - Frames the moment, choice, or path now before them
   - Offers direction without pressure or determinism
   - Closure in tone but not in possibility
   - Leaves them feeling understood, empowered, and ready

**Format**:
- Flowing narrative prose
- Minimal subsections (avoid over-structuring)
- No numbered lists or bullet points in narrative
- Smooth transitions between sections
- Readable as a unified essay

### Process/MD Structure

**Flexible** based on tool, but typically:

1. **Chart/Data Overview**
   - Birth data or calculation parameters
   - Sect, chart ruler, angular planets
   - Key technical facts

2. **Technique-by-Technique Breakdown**
   - Profections timeline
   - Zodiacal Releasing periods (L1 and L2)
   - Secondary Progressions data
   - Solar Return chart
   - Transits

3. **Tables & Structured Data**
   - Planetary positions
   - Aspect tables
   - Dignity assessments
   - Timeline data

4. **Technical Notes**
   - Calculation methods
   - Source citations
   - Traditional references

---

## Length Guidelines

### Synthesis/PDF

**Natal Chart Interpretation**:
- 3,000-5,000 words
- ~10-15 pages

**Life Arc Interpretation**:
- 5,000-8,000 words
- ~15-20 pages

**Transit Report (future Mode 3)**:
- 2,000-4,000 words
- ~8-12 pages

**General Rule**: Match length to complexity, but favor thoroughness over brevity. The native should feel comprehensively understood.

### Process/MD

**No length limit**: Include all technical data needed for verification.

---

## PDF Generation System

**How It Works**:
- Markdown synthesis files are converted to PDF using `scripts/pdf_generator.py`
- Process: Markdown → HTML (via Python `markdown` library) → PDF (via WeasyPrint)
- Styling is defined in CSS within `pdf_generator.py` (no separate template files)
- All styling changes must be made in the CSS string within `pdf_generator.py`

**Usage**:
```bash
# Convert markdown to PDF
python scripts/pdf_generator.py input.md output.pdf --title "Report Title"

# Default output (same name, .pdf extension)
python scripts/pdf_generator.py input.md
```

**Standard Workflow**:
1. Agent generates synthesis markdown file
2. Agent calls `pdf_generator.py` to convert to PDF
3. Both .md and .pdf files saved to profiles/{name}/output/

**No Templates**: There are no separate PDF template files. All formatting is CSS-based within the generator script.

## Visual/PDF Formatting

### Typography

- **Font**: Helvetica (sans-serif)
- **Body text**: 11pt
- **Line height**: 1.6
- **Alignment**: Left-aligned (NOT justified)
- **Margins**: 2.5cm (1 inch) all sides
- **Page numbers**: Bottom center

### Headings

- **H1**: 24pt, bold, black bottom border (3px)
- **H2**: 18pt, bold, black bottom border (2px)
- **H3**: 14pt, bold
- **H4**: 12pt, bold

### Color Palette

**All colors should be black (#000000)**:
- **Body text**: Black (#000000)
- **Headings**: Black (#000000)
- **Borders**: Black (#000000)
- **Tables**: Black headers, alternating row backgrounds (light grey)

### Page Layout

- **Size**: Letter (8.5" x 11")
- **Orientation**: Portrait
- **Page breaks**: Avoid orphaned headings
- **Page numbers**: Include on all pages

---

## Writing Guidelines

### Narrative Flow

**✅ Good Example** (Synthesis):
```
You're in the final stretch of a profound 27-year chapter that has shaped
your adult life. This period has been about discipline, proving yourself,
and building something lasting through sustained effort. The intensity
you're experiencing now—the sense that something is ending, that the ground
is shifting beneath you—is real. You're not stuck; you're in the final
preparation for the most significant transition you've experienced as an adult.

At age 39, everything changes. The weight lifts. The structures you've built
remain, but the relentless pressure to prove, achieve, and master gives way
to a lighter phase focused on innovation, collaboration, and freedom. You've
earned this. The next 27 years will feel entirely different.
```

**❌ Bad Example** (Too much jargon):
```
Your ZR Fortune L1 Capricorn period (ages 12-39) is ending soon. Saturn rules
this period and is in domicile in Capricorn in your 6th house, conjunct your
Sun. At age 39, you'll transition to ZR Fortune L1 Aquarius, which will bring
a different energy. Saturn also rules Aquarius, so there will be continuity,
but the Aquarian expression is about innovation and groups rather than
traditional Capricorn structure.
```

### Psychological Depth

**✅ Good** (Insightful):
```
There's a part of you that needs to be recognized for what you build and
achieve. Your sense of self is tied to your public role—not from vanity,
but from a deep need to know that your work matters, that you're contributing
something of lasting value. This can create an inner tension: the drive to
excel can sometimes feel like a burden, as if you're carrying the weight of
expectations that never quite let you rest.
```

**❌ Bad** (Superficial):
```
You care about your career and want to be successful. You work hard and
sometimes feel stressed. You value achievement.
```

### Validation & Insight Balance

**✅ Good** (Validating but honest):
```
The challenges you've faced aren't random obstacles—they're part of a larger
pattern designed to refine and strengthen you. The restrictions you've felt,
the delays, the moments where you had to prove yourself again and again—these
have been shaping you into someone with depth, resilience, and hard-won wisdom.
The frustration is real, but so is the growth.
```

**❌ Bad** (Overly positive / toxic positivity):
```
Everything happens for a reason! Your challenges are actually blessings in
disguise. You should be grateful for all your obstacles because they make
you stronger!
```

### Poetic Wrapup (Required Final Paragraph - No Heading)

Every synthesis PDF MUST end with a 3-5 sentence poetic closing paragraph. **IMPORTANT**: Do NOT add a heading for this paragraph - it should flow naturally as the final paragraph of the last section.

**Requirements**:
- **Length**: 3-5 sentences
- **Tone**: Visionary, commanding voice
- **Voice**: Direct second person ("You are here to...", "You must...", "There is within you...")
- **Purpose**: Reiterate key themes to deepen the emotional impact of the reading
- **Language**: Accessible psychological language - NO astrological jargon

**✅ Excellent Examples**:

**For Natal Chart**:
```
You are here to build something lasting while keeping your eyes on distant horizons. The tension between proving yourself and breaking free is the creative friction that will shape your most meaningful work. Trust both the structures you've built and the innovations you're being called to bring forth.
```

**For Life Arc**:
```
You stand at the threshold between worlds—the old chapter dissolving, the new one waiting. There is within you a strength forged through years of discipline, and it is time now to trust what you have built. The intensity you feel is not breakdown but breakthrough, the final transformation before you step into what comes next.
```

**❌ Bad Examples**:

**Too deterministic**:
```
You will definitely achieve great success in your career. Everything is going
to work out perfectly. Your challenges are behind you now.
```

**Too vague**:
```
Trust the universe. Everything happens for a reason. You're on the right path.
Keep believing in yourself.
```

**Too technical / jargon**:
```
With Saturn conjunct your Sun and your ZR Fortune L1 in Capricorn, you're
in a period of discipline. When you transition to Aquarius Fortune at age 39,
things will shift. Mars in domicile supports your drive.
```

### Strengths & Challenges Balance

- **Present both honestly**
- Don't sugarcoat challenges
- Don't oversell strengths
- Show how they work together
- Validate the native's experience

---

## Technical Standards (Process/MD)

### Traditional Astrology Foundation

**Required**:
- Hellenistic methods as base
- Whole-sign houses (WSH)
- Traditional rulerships only
- Classical aspects (0°, 60°, 90°, 120°, 180°)
- Sect awareness (day/night charts)
- Essential dignities (domicile, exaltation, detriment, fall)

**Optional Context**:
- Modern planets (Uranus, Neptune, Pluto) for psychological depth
- Modern psychological frameworks (with traditional base)

**Forbidden**:
- Modern house systems (Placidus, Koch, etc.) as primary
- Modern aspects (quincunx, semi-sextile, etc.)
- Modern rulerships (Pluto ruling Scorpio, etc.)
- Cookbook interpretations without synthesis

### Source Citations

**In Process/MD file**:
- Cite all traditional sources
- Use footnote format: [1], [2], [3]
- Include bibliography at end
- Specify page numbers when available

**Example**:
```
Mars in Aries brings assertive, pioneering energy, expressing the planet's
natural significations without impediment.[1] When placed in the 9th house,
this manifests as a quest for meaning through direct experience and action.[2]

---
[1] Brennan, Chris. Hellenistic Astrology: The Study of Fate and Fortune, p. 342
[2] George, Demetra. Astrology and the Authentic Self, p. 178
```

---

## Quality Checklist

Before delivering any interpretation, verify:

### Synthesis/PDF:
- ✅ Zero astrological jargon (no planet names, houses, aspects)
- ✅ Flowing narrative prose (not excessive bullet points)
- ✅ Psychologically rich and insightful
- ✅ Validates the native's experience
- ✅ Sounds like a therapist, not an astrologer
- ✅ Native would feel deeply understood
- ✅ Readable by someone with no astrology knowledge
- ✅ Helvetica font, left-aligned, professional formatting

### Process/MD:
- ✅ All technical data included
- ✅ Astrological terminology used correctly
- ✅ Traditional methods documented
- ✅ Sources cited with footnotes
- ✅ Calculations verifiable
- ✅ Structured for astrologer review

### Both:
- ✅ Sect-aware interpretation
- ✅ Dignity-based strength assessment
- ✅ House ruler insights integrated
- ✅ Thematic coherence throughout
- ✅ No contradictions between files
- ✅ Professional tone maintained

---

## Examples by Mode

### Mode 1: Natal Chart Interpretation

**Synthesis/PDF**: "Who you are at your essence—your character, strengths, challenges, and life path based on your birth chart."

**Process/MD**: Complete technical breakdown of planetary positions, aspects, houses, dignities, with traditional source citations.

### Mode 2: Life Arc Timeline

**Synthesis/PDF**: "Your life story in major chapters—where you've been, where you are now, and what's ahead, showing the arc of your development over decades."

**Process/MD**: Technical timeline showing profections, ZR Fortune/Spirit L1/L2 periods, progressions, solar returns, transits with exact dates and ages.

### Mode 3: Transit Report (Future)

**Synthesis/PDF**: "What's coming in the next 6 months to 3 years—major themes, timing windows, and how current sky movements activate your natal chart."

**Process/MD**: Chronological transit timeline with exact dates, orb windows, aspect types, retrograde cycles, and technical data.

---

## Common Mistakes to Avoid

### ❌ In Synthesis/PDF:

1. **Using astrological jargon**
   - Bad: "Your Mars square Saturn creates tension"
   - Good: "There's an inner conflict between taking bold action and feeling restricted"

2. **Listing placements**
   - Bad: "You have Sun in Capricorn, Moon in Leo, Venus in Sagittarius..."
   - Good: "You experience life through a lens of achievement and responsibility..."

3. **Breaking into excessive subsections**
   - Bad: 20 tiny subsections with 1-2 sentences each
   - Good: Flowing narrative with natural section breaks

4. **Being overly deterministic**
   - Bad: "You will definitely become a CEO"
   - Good: "There's a strong pull toward leadership and public achievement"

5. **Toxic positivity**
   - Bad: "All your challenges are blessings!"
   - Good: "Your challenges have refined you, though they've been genuinely difficult"

### ❌ In Process/MD:

1. **Avoiding technical language**
   - This file NEEDS astrological terminology

2. **Omitting source citations**
   - Always cite traditional sources

3. **Skipping dignity assessments**
   - Document planetary strength

4. **Ignoring sect**
   - Day/night charts interpret differently

5. **Using modern methods as primary**
   - Hellenistic base, modern context only

---

## Tool-Specific Notes

### pdf_generator.py

The standard PDF generator (`scripts/pdf_generator.py`) automatically applies these style standards:

- Helvetica font
- Professional layout
- Proper heading hierarchy
- Page numbers
- Clean, readable design

**Agents should**:
1. Generate synthesis in markdown (pure narrative, no jargon)
2. Call `pdf_generator.py` to convert to PDF
3. Generated PDF follows this style guide automatically

### All Interpretation Agents

Every agent that generates interpretations MUST:
1. Follow this style guide for tone, format, and content
2. Generate both process (.md) and synthesis (.pdf) files
3. Separate technical data from narrative
4. Use proper voice for each audience

---

## Summary: The Core Principle

**Two audiences, two files, two voices:**

1. **For the native (PDF)**: Psychological narrative with zero jargon
2. **For the astrologer (MD)**: Technical data with full terminology

The native should feel **deeply understood**.
The astrologer should be able to **verify every claim**.

Both should feel they received a **professional, thorough, insightful** interpretation grounded in traditional astrology but expressed in the appropriate voice for each audience.
