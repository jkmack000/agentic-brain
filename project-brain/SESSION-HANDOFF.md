# SESSION-HANDOFF
<!-- written: 2026-02-17 -->
<!-- session-type: RESEARCH + DESIGN -->
<!-- trigger: user-requested — preparing for tagged commit + restart -->

## What Was Being Done
Two tracks: (1) SPEC-002 deferred to architect agent in separate terminal. (2) Quorum sensing framework for LLM knowledge management — full creative exploration, Grok comparison, gap analysis, implementation plan, and detailed Q&A refining the design.

## Current State
- **Status:** DESIGN COMPLETE — ready to implement
- **What's done:**
  - 7 rules for quorum-capable knowledge (full framework)
  - Grok vs Claude comparison analysis
  - Gap analysis: all 7 rules mapped against current brain
  - P0-P3 prioritized implementation plan
  - User Q&A refining: binding sites clarified, token overhead assessed (~10K/5% current), contradiction handling refined (adversarial evidence accumulation, 3 states: OPEN/BLOCKING/RESOLVED), decay clarified (human-reviewed only, never automatic, topological not temporal), sub-index workflow impact assessed (one extra hop, transparent to skills), branching strategy confirmed (git branches + tags, not parallel brains)
- **What's left:** Implement the plan (next session)

## Design Decisions Made This Session

### Quorum Sensing Framework — 7 Rules
1. Every packet must emit signal (fat index entry required)
2. Maximize binding sites (links, tags, backlinks — minimum 3 links per deposit)
3. Declare open questions as chemoattractant gradients (required field, aggregated in INDEX-MASTER)
4. Deposit contradictions, don't resolve prematurely (adversarial evidence accumulation)
5. Consolidate at cluster quorum, not arbitrary count (synthesis ≠ dedup)
6. Let decay work — topological not temporal, human-reviewed only (quiet → review → reconnect/confirm/retire)
7. Index is the medium (INDEX-MASTER gets OPEN QUESTIONS, TENSIONS, CLUSTERS sections)

### Contradiction Handling (Refined)
- Tensions have 3 states: OPEN (accumulating evidence), BLOCKING (on critical path, triggers research), RESOLVED (one side won through weight)
- Resolution is earned through asymmetric accretion, not premature consolidation
- Losing side retired with full provenance ("we used to think X because A,B but Y proved correct because C,D,E,F,G")
- BLOCKING tensions are research triggers — the system tells you where to spend tokens

### Decay Mechanism (Refined)
- Never automatic — `/brain-status` flags quiet files (0 inbound links), human reviews
- Three review outcomes: reconnect (add missing links), confirm quiet (mark, leave in index), retire (archive, remove from index)
- Topological not temporal — a 6-month file with 5 inbound links is alive, a yesterday file with 0 is decaying
- Files only, never whole brains (dormancy ≠ irrelevance)

### Sub-Index Strategy (Confirmed)
- INDEX-MASTER becomes directory of cluster summaries (~50-100 lines)
- Each sub-index is 200-300 lines
- One extra hop in workflow, transparent to skills
- Split triggered by "mental squeeze point" not arbitrary file count
- Cross-cluster links preserved in master index

### Safety Strategy
- Git branching for structural experiments
- Tagged commits before irreversible operations (e.g., `pre-quorum-implementation`)
- No parallel brains — git history is the undo buffer

## Prioritized Implementation Plan

| Priority | Change | Rule |
|----------|--------|------|
| P0 | OPEN QUESTIONS section in INDEX-MASTER | 3 |
| P0 | TENSIONS section in INDEX-MASTER | 4 |
| P0 | Backlinks in fat index entries | 2 |
| P1 | Min 3 links per deposit (update /brain-deposit skill) | 2 |
| P1 | Required "what this doesn't answer" in deposit | 3 |
| P1 | Tag cluster detection in /brain-status | 5 |
| P1 | Quiet file detection in /brain-status | 6 |
| P2 | Synthesis vs maintenance consolidation distinction | 5 |
| P2 | Vitality scoring + retirement workflow | 6 |
| P2 | CLUSTERS section in INDEX-MASTER | 7 |
| P3 | Sub-index design along cluster boundaries | 7 |

## Undeposited Knowledge
- Full quorum sensing framework (7 rules + biological mapping) — deposit as LEARN-032
- Grok comparison insights — include in LEARN-032
- Gap analysis + implementation plan — deposit as SPEC-003 (prescriptive design changes)

## Open Questions (Carried Forward)
- Frontend stack preference?
- Is Prover the whole system or just the backtester?
- Data freshness — how does OHLCV data get refreshed?
- Strategy versioning — git tags? Dedicated VERSION file?
- Each agent = own project + own brain (not yet in SPEC-001)
- Should quorum sensing framework be LEARN-032 or SPEC-003? (Recommend: LEARN for the framework, SPEC for the implementation plan)

## Files Modified This Session
- None (all output conversational)

## Files Added to Brain This Session
- None

## Dead Ends
- Plan mode entered for SPEC-002, never used — deferred to architect agent

## Recommended Next Session
- **Type:** WORK (deposit + implement)
- **Load:** SESSION-HANDOFF.md, INDEX-MASTER.md
- **First action:**
  1. Tagged commit exists at `pre-quorum-implementation`
  2. Deposit LEARN-032 (quorum sensing framework + Grok comparison)
  3. Deposit SPEC-003 (quorum-capable brain implementation plan)
  4. Implement P0: add OPEN QUESTIONS, TENSIONS, backlinks to INDEX-MASTER
  5. Implement P1: update /brain-deposit skill, /brain-status skill
  6. Update INDEX-MASTER with new entries
  7. Check architect agent output for SPEC-002
