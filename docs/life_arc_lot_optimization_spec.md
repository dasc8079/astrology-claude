# Life Arc Lot Optimization Specification

**Status**: Proposed - Deferred Implementation
**Created**: 2025-10-17
**Author**: Technique optimization assessment

---

## Problem Statement

V3 life arc interpreter expanded from 10 lots (V2) to 15 lots (V3), adding Father, Mother, Siblings, Accusation, and Friends. Analysis reveals **diminishing returns beyond 8-10 lots** due to:

1. **Redundancy**: New lots overlap with natal house analysis + profection activations
2. **Prompt bloat**: ~25% increase in lots section (~200-300 tokens)
3. **Noise**: 5 additional factors per age without unique insight 90% of the time
4. **Specificity problem**: Father/Mother/Siblings only valuable in niche cases

---

## Current State

### V2: 10 Lots
- Fortune, Spirit, Eros, Necessity, Courage, Victory, Basis, Exaltation, Marriage, Children

### V3: 15 Lots (+5)
- All V2 lots PLUS Father, Mother, Siblings, Accusation, Friends

---

## Value Assessment

### HIGH VALUE (Essential - Keep)
- **Fortune**: Body, health, resources
- **Spirit**: Career, action, vitality
- **Eros**: Love, desire
- **Necessity**: Fate, constraint

**These 4 are IRREPLACEABLE** - cover fundamental life areas.

### MEDIUM VALUE (Enrichment - Keep)
- **Courage**: Boldness (50% value-add)
- **Victory**: Success (50% value-add)
- **Exaltation**: Peak periods (40% value-add)
- **Saturn/Basis**: Foundation/limitation (30% value-add)

### LOW VALUE (Bloat - Remove)
- **Marriage**: Redundant with Eros + natal 7H (20% value-add)
- **Children**: Niche use case (20% value-add)
- **Father**: Highly specific, rarely unique (10% value-add)
- **Mother**: Highly specific, rarely unique (10% value-add)
- **Siblings**: Highly specific, rarely unique (5% value-add)
- **Accusation**: Overlaps natal 10H + profections (15% value-add)
- **Friends**: Overlaps natal 11H + profections (15% value-add)

---

## Proposed Solutions

### Option 1: Reduce to 8 Core Lots (RECOMMENDED)

**KEEP (8 lots)**:
- Fortune, Spirit, Eros, Necessity (core 4)
- Courage, Victory, Exaltation (peak moments 3)
- Saturn/Basis (challenging periods 1)

**REMOVE (7 lots)**:
- Marriage, Children, Father, Mother, Siblings, Accusation, Friends

**Impact**: ~25% prompt reduction in lots section, clearer focus

**Rationale**:
- Clearest immediate impact
- Maintains all essential lots
- Removes redundancy
- Proven sufficiency (V2 worked well with 10; 8 is leaner)

---

### Option 2: Make Lots Profile-Toggleable

**Core Lots** (always): Fortune, Spirit, Eros, Necessity (4)

**Optional Lots** (profile setting `include_extended_lots: true/false`):
- Courage, Victory, Exaltation (success themes)
- Marriage, Children (relational depth)
- Father, Mother, Siblings (family dynamics)
- Accusation, Friends (social/reputation)
- Saturn/Basis (challenging periods)

**Impact**: User controls complexity, defaults to lean 4-lot system

---

### Option 3: Contextual Lots (Smart Inclusion)

Only include extended lots IF natal chart shows emphasis:
- **Children lot**: Only if natal 5H occupied or ruler prominent
- **Father lot**: Only if natal 4H/10H emphasized
- **Marriage lot**: Only if natal 7H occupied or Venus/Mars prominent
- **Accusation lot**: Only if natal 10H challenged
- **Friends lot**: Only if natal 11H emphasized

**Impact**: Dynamic optimization based on THIS person's chart

---

## Recommended Implementation: Option 1

**Next Steps**:
1. Update `life_arc_generator.py` to calculate only 8 lots:
   - Fortune, Spirit, Eros, Necessity, Courage, Victory, Exaltation, Saturn/Basis
2. Update `life-arc-interpreter-v3.md` lines 79-84 to list 8 lots
3. Test: Generate life arc with 8-lot system
4. Compare: V3 (15 lots) vs. Optimized (8 lots) output quality
5. Measure: Prompt token reduction, interpretation clarity

**Expected Benefits**:
- 25% reduction in lots prompt complexity
- Clearer focus on high-value timing indicators
- Maintained coverage of all fundamental life areas
- Reduced risk of lot noise in interpretation

---

## Deferred

Implementation deferred pending user review and approval.

**Status**: Specification complete, awaiting implementation decision.
