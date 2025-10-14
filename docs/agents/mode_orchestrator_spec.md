# mode-orchestrator Conversational Upgrade Specification

**Created**: 2025-10-13
**Status**: Planning Phase
**Current Implementation**: Phase 1 (Foundation)

---

## Vision

Transform mode-orchestrator into a rolling conversational astrology assistant that responds to ANY astrology question by understanding intent, loading relevant data, running calculations, querying knowledge sources, and synthesizing answers OR generating full reports as appropriate.

**Goal**: Turn this Claude instance into "Claude Astrology Mode" - an always-on astrology expert that can answer quick questions, generate detailed reports, and maintain conversational context.

---

## Core Concept

**Single Entry Point**: mode-orchestrator becomes THE interface for all astrology interactions

**Dual Functionality**:
1. **Quick Questions**: Brief synthesized answers (2-5 paragraphs) without full report generation
2. **Full Reports**: Complete PDF reports (natal, life arc, transits) with all formatting

**Intelligence**: Automatically detects question type and routes to appropriate workflow

---

## Implementation Phases

### Phase 1: Foundation (Current - In Progress)

**Status**: ✅ Mostly complete, final refinements in progress

**Capabilities**:
- mode-orchestrator routes report generation requests
- Detects mode (natal, life arc, transits, timing techniques)
- Loads profiles and seed data
- Invokes appropriate interpreter agents
- **Needs**: File handling fixes (synthesis vs process split, correct output location)

**Completed**:
- ✅ Mode detection (natal, life arc, transit, timing)
- ✅ Profile loading and validation
- ✅ Agent invocation workflow
- ✅ Basic output generation

**In Progress**:
- 🔄 File splitting (process vs synthesis)
- 🔄 Output location (profiles/{name}/output/)
- 🔄 Universal 3-page standard enforcement

---

### Phase 2: Quick Question Detection & Answer Synthesis

**Goal**: Answer focused astrology questions without generating full 20-page reports

**Timeline**: Next major feature (after Phase 1 complete)

**Complexity**: Moderate (2-3 days implementation)

#### Features

**Question Classification**:
```python
def classify_request(user_input):
    """
    Determine if user wants quick answer or full report

    Quick Question Indicators:
    - Question words: "what", "when", "where", "which", "how"
    - Specific focus: "my Saturn", "March 2026", "ages 35-40"
    - Comparative: "compare June vs July"
    - Single topic: "career timing", "Saturn return", "current transits"

    Full Report Indicators:
    - Generate/create: "generate natal horoscope", "create life arc"
    - Comprehensive: "complete analysis", "full report", "everything"
    - Profile name explicit: "natal for darren", "life arc for mom"

    Returns: "quick_question" | "full_report" | "ambiguous"
    """
```

**Question Types & Routing**:

| Question Type | Example | Workflow |
|---------------|---------|----------|
| **Current Transit** | "What's my Saturn doing now?" | Calculate current Saturn transit → Query RAG for Saturn interpretations → Synthesize 2-3 paragraphs |
| **Life Period** | "Tell me about ages 35-40" | Calculate ZR periods for age range → Query RAG for interpretations → Synthesize period summary |
| **Timing** | "When's my Saturn return?" | Calculate Saturn return date → Query RAG for return meanings → Synthesize timing + meaning |
| **Comparative** | "Compare career timing June vs July" | Calculate transits for both → Score periods → Synthesize comparison |
| **Placement** | "What does Mars in Aries mean for me?" | Load natal data → Query RAG for Mars/Aries → Synthesize personal interpretation |

**Synthesis Workflow**:
```
1. Parse question → Identify focus (planet, house, timing, life area)
2. Load profile seed data
3. Run any needed calculations (transits, progressions, ZR, profections)
4. Query RAG database:
   - Search for: planet/sign/house/aspect interpretations
   - Retrieve traditional sources (Brennan, Hand, George, etc.)
   - Get 3-5 most relevant chunks
5. Synthesize answer:
   - 2-5 paragraphs
   - Accessible language (no jargon)
   - Direct second person ("You are experiencing...")
   - Cite time frames if timing-related
6. Offer full report generation:
   - "Want a full transit report for this period?"
   - "Need a complete life arc analysis for ages 30-50?"
```

**RAG Integration**:
```python
def answer_quick_question(question, profile_data):
    # Parse question to identify astrological focus
    focus = parse_question(question)

    # Load relevant seed data
    seed_data = load_seed_data(profile_data['name'])

    # Run calculations if needed
    if focus['type'] == 'transit':
        calculations = calculate_current_transits(seed_data)
    elif focus['type'] == 'period':
        calculations = calculate_zr_period(seed_data, focus['age_range'])

    # Query RAG database
    rag_query = f"{focus['planet']} in {focus['sign']}"
    interpretations = query_rag_database(rag_query, max_results=5)

    # Synthesize answer
    answer = synthesize_interpretation(
        calculations,
        interpretations,
        seed_data,
        style='brief',  # 2-5 paragraphs
        audience='non_astrologer'
    )

    return {
        'answer': answer,
        'offer_full_report': suggest_report_type(focus),
        'calculations': calculations  # For transparency
    }
```

**Example Interactions**:

**Example 1: Current Transit Question**
```
User: "What's my Saturn doing right now?"

mode-orchestrator:
1. Classifies as "quick_question" type "transit"
2. Loads darren profile
3. Calculates current Saturn position (transit Saturn at 15° Pisces)
4. Calculates aspect to natal Saturn (Saturn at 5° Capricorn)
5. Queries RAG: "Saturn transit square natal Saturn"
6. Synthesizes:

"You're currently experiencing Saturn in Pisces forming a square to your natal
Saturn in Capricorn—a challenging aspect that occurs roughly every 7 years in
the Saturn cycle. This is a time when external responsibilities feel heavier,
when the structures you've built are tested, and when you're asked to integrate
discipline with compassion and surrender.

Your natal Saturn sits in the 6th house of daily work and health, already creating
a strong pull toward mastery through routine and service. Transit Saturn's square
from the 8th house adds themes of shared resources, emotional depth, and
transformation. You may feel tension between maintaining your disciplined approach
and needing to release control or trust in processes you can't fully manage.

This transit lasts several months and marks a maturation point in how you handle
responsibility. The key is not to push harder, but to refine your approach—to
work smarter, to honor limitations, and to build structures that can flex rather
than break."

Want a full transit report for the next 6-12 months showing all major transits
and timing windows?
```

**Example 2: Life Period Question**
```
User: "Tell me about my life from ages 35-40"

mode-orchestrator:
1. Classifies as "quick_question" type "period"
2. Loads darren profile
3. Calculates ZR periods for ages 35-40:
   - Ages 35.5-37.4: Scorpio L2 (Mars sub-period)
   - Ages 37.4-39: Sagittarius L2 (Jupiter sub-period)
   - Age 39+: Major transition (Capricorn L1 → Aquarius L1)
4. Queries RAG: "Scorpio period Mars", "Sagittarius period Jupiter", "life chapter transition"
5. Synthesizes:

"Ages 35-40 mark a pivotal transition period in your life story. You're in the
final years of a major 27-year chapter (Capricorn Fortune, ages 12-39) that has
defined your adult life through themes of discipline, achievement, and proving
yourself through sustained effort.

The intensity you're feeling now (ages 35-37) comes from a Mars sub-period—a time
of directed action, cutting away what no longer serves, and confronting what needs
to change. This isn't comfortable, but it's necessary preparation for what's ahead.

At age 39, you'll cross a major threshold into an entirely new 27-year chapter
(Aquarius Fortune). The relentless weight of proving yourself through traditional
achievement will lift, replaced by themes of innovation, collaboration, and
intellectual exploration. Ages 35-40 are the bridge—intense, transitional, but
ultimately preparing you for a much lighter and more expansive phase of life."

Want a complete Life Arc Report showing your full timeline from birth to age 100?
```

**Example 3: Timing Electional Question**
```
User: "When should I apply for this new job opportunity?"

mode-orchestrator:
1. Classifies as "quick_question" type "timing"
2. Identifies need for current transits + profections + progressions
3. Calculates:
   - Current profection year (1st house, Sun as time lord)
   - Upcoming favorable transits (next 30-60 days)
   - Current progressions
4. Queries RAG: "career timing", "10th house activation", "application timing"
5. Synthesizes:

"You're currently in a 1st house profection year (age 36), which emphasizes
identity and new beginnings rather than career advancement per se—but your Sun
as time lord sits in the 6th house of daily work, creating a strong link between
identity development and professional refinement.

Looking at the next 60 days, the most auspicious timing window is mid-November
when Jupiter (your 10th house ruler) receives a trine from transit Venus. This
creates support for professional opportunities and public-facing initiatives.
Apply during this window if possible.

However, given your age and overall life chapter (final years before major
transition at 39), this job may serve more as a stepping stone than a final
destination. The key question isn't just "when to apply" but "does this align
with where I'm headed at age 39+?" Consider whether this opportunity builds
toward the innovation and collaboration themes that will dominate your next
life chapter."

Want a full career timing report analyzing the next 1-3 years for professional
opportunities?
```

#### Implementation Checklist

**Detection**:
- [ ] Question classifier function (quick vs full vs ambiguous)
- [ ] Focus parser (planet, sign, house, timing, life area extraction)
- [ ] Ambiguity handler (ask clarifying questions)

**Calculation Integration**:
- [ ] On-demand transit calculator (current date or user-specified date)
- [ ] ZR period calculator (by age range)
- [ ] Profection calculator (current year)
- [ ] Progression calculator (current positions)

**RAG Query System**:
- [ ] Query builder from parsed question
- [ ] Result ranker (most relevant interpretations)
- [ ] Source citation formatter
- [ ] Multi-source synthesis (combine Brennan + Hand + George)

**Synthesis Engine**:
- [ ] Brief answer template (2-5 paragraphs)
- [ ] Jargon translator (astrology → psychology)
- [ ] Timing formatter (date ranges, age ranges)
- [ ] Full report offer generator (contextual suggestions)

**Testing**:
- [ ] Test 10 question types with known answers
- [ ] Verify RAG retrievals are relevant
- [ ] Check synthesis quality (no jargon, accurate, insightful)
- [ ] Confirm full report offers are contextual

---

### Phase 3: Todo List Planning for Complex Requests

**Goal**: For multi-step questions, orchestrator creates execution plan using TodoWrite tool

**Timeline**: After Phase 2 stable (1-2 months later)

**Complexity**: Moderate-High (needs planning logic + step tracking)

#### Features

**Complex Question Detection**:
```
Triggers for todo planning:
- Multiple sub-questions: "Compare career timing 2026 vs 2027 AND tell me about Saturn return"
- Multi-step analysis: "Analyze my relationships from ages 30-50"
- Comparative analysis: "Which is better for travel: June, July, or August 2026?"
- Comprehensive requests: "Tell me everything happening in 2026"
```

**Planning Logic**:
```python
def create_execution_plan(complex_question):
    """
    Break complex question into discrete todos
    Use TodoWrite to track progress
    Execute steps sequentially
    """

    # Example: "Compare career timing 2026 vs 2027"
    todos = [
        {
            'content': 'Calculate 2026 career-related transits and time lord periods',
            'status': 'pending',
            'activeForm': 'Calculating 2026 career timing'
        },
        {
            'content': 'Calculate 2027 career-related transits and time lord periods',
            'status': 'pending',
            'activeForm': 'Calculating 2027 career timing'
        },
        {
            'content': 'Score both years using timing quality metrics',
            'status': 'pending',
            'activeForm': 'Scoring timing quality'
        },
        {
            'content': 'Synthesize comparative analysis with recommendations',
            'status': 'pending',
            'activeForm': 'Synthesizing comparison'
        }
    ]

    TodoWrite(todos)

    for todo in todos:
        # Update status to in_progress
        # Execute step
        # Mark completed
        # Move to next

    return final_synthesis
```

**User Visibility**:
- User sees todo list as orchestrator works
- Transparent reasoning about approach
- Can interrupt/redirect if plan is wrong

**Example**:
```
User: "Compare my career prospects for 2026, 2027, and 2028"

mode-orchestrator:
"I'll analyze career timing for all three years. Here's my plan:
[Shows todo list with 7 steps]

Starting now..."

[Updates todos as it works through each step]

[Final output: Comparative analysis of all 3 years with recommendations]
```

#### Implementation Checklist

**Planning Engine**:
- [ ] Question decomposer (complex → steps)
- [ ] Todo generator (create structured plan)
- [ ] Dependency tracker (which steps require previous completions)
- [ ] Plan optimizer (minimize redundant calculations)

**Execution Framework**:
- [ ] Sequential step executor
- [ ] Todo status updater (pending → in_progress → completed)
- [ ] Progress display to user
- [ ] Error handling (if step fails, what to do)

**User Controls**:
- [ ] Plan approval before execution ("Does this approach work for you?")
- [ ] Mid-execution interruption ("Actually, skip 2028")
- [ ] Plan modification requests

---

### Phase 4: Conversational Memory Within Sessions

**Goal**: Remember context within current conversation for natural follow-ups

**Timeline**: After Phase 3 (3-4 months later)

**Complexity**: High (needs memory system + context tracking)

#### Features

**Session Memory**:
```python
class ConversationMemory:
    def __init__(self):
        self.questions = []  # List of user questions in order
        self.answers = []    # List of orchestrator answers
        self.profiles_used = []  # Which profiles accessed
        self.calculations = {}   # Cache of calculations done
        self.topics = []     # Topics discussed

    def add_interaction(self, question, answer, calculations):
        self.questions.append(question)
        self.answers.append(answer)
        self.calculations.update(calculations)
        self.topics.append(extract_topic(question))

    def get_context(self):
        """
        Return relevant context for current question
        """
        return {
            'recent_topics': self.topics[-3:],  # Last 3 topics
            'cached_calculations': self.calculations,
            'active_profiles': self.profiles_used
        }
```

**Context-Aware Follow-ups**:
```
User: "What's my Saturn doing now?"
Orchestrator: [Answers about Saturn transit square...]

User: "How long will that last?"
Orchestrator: [Knows "that" = Saturn transit, uses cached calculations]
"The Saturn square to your natal Saturn lasts from October 2025 through
February 2026, with exact hits in November 2025 and January 2026..."

User: "What about Jupiter?"
Orchestrator: [Knows user is asking about current transits, calculates Jupiter]
"Your Jupiter is currently in Gemini in the 11th house, trining your natal
Mercury. This brings..."

User: "Tell me more about that Mercury trine"
Orchestrator: [Retrieves Jupiter-Mercury trine from memory, expands]
```

**Proactive Suggestions**:
```
Orchestrator: "You've been asking about timing for career changes and Saturn
transits. Would you like me to generate a complete career timing report for
the next 2 years showing how these themes converge?"
```

#### Implementation Checklist

**Memory System**:
- [ ] Session memory data structure
- [ ] Context extractor (what's relevant from history)
- [ ] Calculation cache (avoid recalculating)
- [ ] Topic tracker (conversation themes)

**Reference Resolution**:
- [ ] Pronoun resolver ("that", "it", "those")
- [ ] Implicit topic handler ("How long?" → knows what user means)
- [ ] Context inheritance (follow-up questions use prior context)

**Proactive Intelligence**:
- [ ] Pattern detector (identify what user is exploring)
- [ ] Suggestion generator (offer relevant next steps)
- [ ] Report recommendations (when to offer full PDF)

---

### Phase 5: Advanced Assistant Features

**Goal**: Full astrology assistant with cross-session memory, scheduling, preferences

**Timeline**: Long-term (6+ months out)

**Complexity**: Very High (needs persistence, user profiles, scheduling)

#### Features

**Cross-Session Memory**:
- Remember user across sessions
- Track question history over time
- User preference storage (detail level, focus areas, report formats)
- Report generation history

**Scheduled Check-ins**:
```
"March is approaching (Saturn return month you asked about in January).
Want to review transit timing for that period?"

"You're entering a new profection year next week (2nd house, Venus time lord).
Should I generate a year-ahead forecast?"
```

**Natural Language Report Customization**:
```
User: "Generate natal horoscope but focus more on career and less on relationships"

Orchestrator: [Generates custom-weighted natal report with expanded career
section, brief relationship section]
```

**Calendar Integration** (aspirational):
- Export timing windows to user's calendar
- Set reminders for important transits
- Flag auspicious timing for scheduled events

**Preference Learning**:
```
After 5 interactions:
"I notice you prefer brief answers with option to go deeper. Should I continue
this format?"

"You often ask about career timing. Would you like quarterly career timing
check-ins?"
```

#### Implementation Checklist

**Persistence**:
- [ ] User profile storage system
- [ ] Conversation history database
- [ ] Preference storage and retrieval
- [ ] Report generation history

**Scheduling**:
- [ ] Timing reminder system
- [ ] Proactive check-in generator
- [ ] Calendar integration (if possible)

**Customization**:
- [ ] Report weight customizer (expand/collapse sections)
- [ ] Detail level adjuster (brief vs comprehensive)
- [ ] Focus area selector (career, relationships, health, etc.)

**Intelligence**:
- [ ] Preference learner (detect patterns in user questions)
- [ ] Suggestion optimizer (what user finds most valuable)
- [ ] Conversation style adapter (formal vs casual, brief vs detailed)

---

## Technical Architecture

### Data Flow

```
User Question
    ↓
mode-orchestrator (Question Classifier)
    ↓
    ├─→ Quick Question Route
    │   ├─→ Parse Question (extract focus)
    │   ├─→ Load Profile Data
    │   ├─→ Run Calculations (transits, ZR, profections)
    │   ├─→ Query RAG Database
    │   ├─→ Synthesize Answer (2-5 paragraphs)
    │   └─→ Return Answer + Offer Full Report
    │
    └─→ Full Report Route
        ├─→ Detect Mode (natal, life arc, transit)
        ├─→ Load Profile & Seed Data
        ├─→ Invoke Interpreter Agent
        ├─→ Split Files (process vs synthesis)
        ├─→ Generate PDF
        └─→ Return Complete Report
```

### Component Integration

**mode-orchestrator.md**:
- Central intelligence (question classification, routing)
- Memory management (session context)
- Workflow coordination

**Calculation Tools**:
- `scripts/ephemeris_helper.py` (current positions)
- `scripts/zodiacal_releasing.py` (ZR periods)
- `scripts/profections.py` (annual profections)
- `scripts/progressions.py` (secondary progressions)

**RAG System**:
- `scripts/query_rag_database.py` (semantic search)
- `output/database/astrology_rag_database.jsonl` (knowledge base)

**Interpreter Agents**:
- `natal-interpreter.md` (full natal reports)
- `life-arc-interpreter.md` (life timeline reports)
- `transit-analyzer-*.md` (transit reports)

**Synthesis Templates**:
- Brief answer format (2-5 paragraphs, no jargon)
- Full report format (20-page PDFs)
- Comparative analysis format (side-by-side)

---

## Testing Strategy

### Phase 2 Testing (Quick Questions)

**Question Types to Test**:
1. Current transit: "What's Saturn doing now?"
2. Life period: "Tell me about ages 35-40"
3. Timing: "When's my Saturn return?"
4. Comparison: "Compare June vs July for career"
5. Placement: "What does Mars in Aries mean for me?"
6. General: "What's happening astrologically right now?"
7. Specific event: "Is March 2026 good for travel?"
8. Aspect: "Tell me about my Sun-Saturn conjunction"
9. House: "What does my 10th house say about career?"
10. Life area: "What's my chart say about relationships?"

**Success Criteria**:
- ✅ Correct classification (quick vs full)
- ✅ Relevant RAG retrieval (interpretations match question)
- ✅ Accurate calculations
- ✅ Synthesized answer is accessible (no jargon)
- ✅ Answer is insightful (not generic)
- ✅ Contextual report offer (makes sense to ask)

### Phase 3 Testing (Todo Planning)

**Complex Questions to Test**:
1. "Compare career timing 2026, 2027, 2028"
2. "Analyze my relationships from ages 30-50"
3. "Tell me everything happening March-May 2026"
4. "Compare travel timing: June, July, or August?"
5. "Show me all major life transitions 2025-2030"

**Success Criteria**:
- ✅ Reasonable plan created (todos make sense)
- ✅ Steps execute in correct order
- ✅ Progress visible to user
- ✅ Final synthesis integrates all steps
- ✅ User can understand orchestrator's approach

### Phase 4 Testing (Conversational Memory)

**Follow-up Scenarios to Test**:
1. Initial: "What's Saturn doing?" → Follow-up: "How long will that last?"
2. Initial: "Tell me about ages 35-40" → Follow-up: "What happens after 40?"
3. Initial: "Is June good for travel?" → Follow-up: "What about July?"
4. Multi-topic: Saturn → Jupiter → "Compare those two"
5. Pronoun resolution: "Tell me about Mars" → "When does it go retrograde?"

**Success Criteria**:
- ✅ Correctly resolves references ("that", "it")
- ✅ Uses cached calculations (no redundant work)
- ✅ Maintains topic continuity
- ✅ Proactive suggestions make sense
- ✅ Context feels natural (not robotic)

---

## Success Metrics

### Phase 2 (Quick Questions)
- **Accuracy**: 95%+ of answers are factually correct
- **Relevance**: 90%+ of RAG retrievals are relevant to question
- **Accessibility**: 100% of answers use zero jargon in synthesis
- **User Satisfaction**: Users prefer quick answers over generating full reports for simple questions

### Phase 3 (Todo Planning)
- **Plan Quality**: 90%+ of generated plans are logical and complete
- **Transparency**: Users understand what orchestrator is doing
- **Efficiency**: Multi-step requests complete 2x faster than manual approach

### Phase 4 (Conversational Memory)
- **Context Accuracy**: 95%+ of follow-ups correctly interpret user intent
- **Convenience**: Users save 50%+ time by not re-explaining context
- **Naturalness**: Conversation feels fluid, not transactional

### Phase 5 (Advanced Assistant)
- **Retention**: Users return for multiple sessions
- **Engagement**: Proactive suggestions are accepted 30%+ of the time
- **Customization**: Custom reports better match user needs than standard

---

## Future Enhancements (Beyond Phase 5)

**Multi-User Profiles**:
- Compare two people's charts (synastry)
- Family analysis (parent-child, siblings)
- Relationship compatibility

**Predictive Intelligence**:
- "Based on your questions, you might want to know about..."
- Seasonal forecasts ("Here's what spring 2026 looks like for you")
- Life milestone predictions ("Your Saturn return is 5 years away - here's how to prepare")

**Educational Mode**:
- Teach astrology concepts as questions arise
- "Why does Saturn square feel challenging? Let me explain sect and malefics..."
- Build user's astrological literacy over time

**Integration Features**:
- Export reports to PDF/email
- Share specific answers (formatted for social media)
- Print-friendly formatting
- Calendar integration (export timing windows)

---

## Conclusion

This 5-phase plan transforms mode-orchestrator from a simple report router into an intelligent conversational astrology assistant. Each phase builds on the previous, with clear implementation paths and testing criteria.

**Current Priority**: Complete Phase 1 (file handling, output formatting) before moving to Phase 2.

**Timeline**:
- Phase 1: Current (completion within 1 week)
- Phase 2: Next major feature (2-4 weeks)
- Phase 3: 2-3 months out
- Phase 4: 4-6 months out
- Phase 5: 6+ months out

**Status**: Document created. Implementation begins after Phase 1 refinements complete.
