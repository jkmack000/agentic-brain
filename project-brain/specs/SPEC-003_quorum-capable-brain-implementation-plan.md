# SPEC-003 — Quorum-Capable Brain Implementation Plan
<!-- type: SPEC -->
<!-- tags: quorum-sensing, implementation, INDEX-MASTER, brain-deposit, brain-status, backlinks, tensions, open-questions, clusters -->
<!-- created: 2026-02-17 -->
<!-- status: ACTIVE -->
<!-- links: LEARN-032, SPEC-000, LEARN-031, LEARN-003 -->

## Context

LEARN-032 defines a 7-rule quorum sensing framework for LLM knowledge management. This spec is the prescriptive implementation plan — what changes, in what order, and how each change maps to the framework rules.

## Decision

Implement quorum sensing in 4 priority tiers (P0→P3), where each tier is independently valuable and builds on the previous. All changes are additive — no existing functionality is removed or broken.

## Implementation Plan

### P0 — Index Structure (Rules 3, 4, 2)
These changes make INDEX-MASTER.md the coordination medium.

#### P0.1: OPEN QUESTIONS section in INDEX-MASTER.md
- **Rule:** 3 (chemoattractant gradients)
- **What:** Add an `## Open Questions` section after the fat index entries. Each entry: question text, source file(s), date first raised, status (open/researched/answered).
- **Format:**
  ```markdown
  ## Open Questions
  | Question | Source | Raised | Status |
  |----------|--------|--------|--------|
  | Frontend stack preference? | SPEC-001 | 2026-02-16 | open |
  ```
- **Seed:** Populate from SESSION-HANDOFF.md "Open Questions (Carried Forward)" section.

#### P0.2: TENSIONS section in INDEX-MASTER.md
- **Rule:** 4 (contradiction preservation)
- **What:** Add a `## Tensions` section. Each entry: tension description, files on each side, state (OPEN/BLOCKING/RESOLVED), evidence summary.
- **Format:**
  ```markdown
  ## Tensions
  | Tension | Side A | Side B | State | Notes |
  |---------|--------|--------|-------|-------|
  | Temporal vs topological decay | (Grok, common practice) | LEARN-032 (connection-based) | RESOLVED | Topological chosen — relevance is relationships not recency |
  ```
- **Seed:** Scan existing files for any contradictions or disagreements.

#### P0.3: Backlinks in fat index entries
- **Rule:** 2 (maximize binding sites)
- **What:** Add a `Backlinks:` field to each fat index entry listing files that reference it. Currently entries have `Links:` (forward references) but no reverse.
- **Method:** Scan all files' `<!-- links: ... -->` frontmatter, build reverse map, add `Backlinks:` to each index entry.

### P1 — Deposit & Status Enhancements (Rules 2, 3, 5, 6)
These changes enforce the framework at deposit time and surface system health.

#### P1.1: Minimum 3 links per deposit
- **Rule:** 2 (maximize binding sites)
- **What:** Update `/brain-deposit` skill to require minimum 3 links (forward links + tags count). Skill should warn if under threshold and suggest connections.

#### P1.2: Required "what this doesn't answer" in deposit
- **Rule:** 3 (chemoattractant gradients)
- **What:** Update `/brain-deposit` skill to prompt for open questions. Add the responses to the file's content AND aggregate into INDEX-MASTER.md OPEN QUESTIONS section.

#### P1.3: Tag cluster detection in `/brain-status`
- **Rule:** 5 (cluster quorum)
- **What:** `/brain-status` should group files by shared tags, identify clusters with 5+ files, and flag clusters approaching "mental squeeze point" (where fat index summaries can't capture the distinctions).

#### P1.4: Quiet file detection in `/brain-status`
- **Rule:** 6 (topological decay)
- **What:** `/brain-status` should list files with 0 inbound links (backlinks). These are candidates for review: reconnect, confirm quiet, or retire.

### P2 — Consolidation & Vitality (Rules 5, 6, 7)
These changes support the ongoing health of the brain.

#### P2.1: Synthesis vs maintenance consolidation distinction
- **Rule:** 5 (cluster quorum)
- **What:** Document two consolidation modes: (1) **Maintenance** — dedup, fix broken links, tighten summaries (safe, routine). (2) **Synthesis** — merge cluster into new understanding, create higher-level file, retire source files (significant, needs review). Consolidation prompts should distinguish which mode.

#### P2.2: Vitality scoring + retirement workflow
- **Rule:** 6 (decay)
- **What:** Score each file: inbound links + outbound links + tag count + recency of last reference. Surface in `/brain-status`. Provide retirement workflow: archive file to `project-brain/archive/`, remove from INDEX-MASTER, add note to LOG-002.

#### P2.3: CLUSTERS section in INDEX-MASTER.md
- **Rule:** 7 (index is the medium)
- **What:** Add `## Clusters` section grouping related files by detected tag overlap. Each cluster: name, member files, link density, squeeze-point assessment.

### P3 — Sub-Index Design (Rule 7)

#### P3.1: Sub-index design along cluster boundaries
- **Rule:** 7 (index is the medium)
- **What:** When INDEX-MASTER exceeds mental squeeze point, split into sub-indexes aligned with detected clusters (not arbitrary alphabetical or type-based splits). INDEX-MASTER becomes a directory of cluster summaries. Cross-cluster links preserved in master.
- **Trigger:** Not file count — the "mental squeeze point" where INDEX-MASTER can no longer be scanned in one pass without losing important distinctions.

## Rationale

- **P0 first** because it's all additive structure in INDEX-MASTER — zero risk, immediate value, enables P1-P3.
- **P1 second** because it enforces quality at deposit time — every future file benefits.
- **P2 third** because it requires enough files + backlink data to be meaningful.
- **P3 last** because the brain is ~41 files — sub-indexes are premature until ~75+.

## Interface / Contract

- INDEX-MASTER.md gains 3 new sections: `## Open Questions`, `## Tensions`, `## Clusters`
- Fat index entries gain `Backlinks:` field
- `/brain-deposit` skill gains: link minimum check, open questions prompt
- `/brain-status` skill gains: cluster detection, quiet file detection, vitality scoring

## Constraints

- All changes must be backward-compatible — existing brain files remain valid
- No automatic decay or retirement — human review required for all removals
- Tensions are never auto-resolved — evidence accumulation only
- Sub-index split is never triggered by file count alone

## Open Questions

- Should CLUSTERS section be auto-generated by `/brain-status` or manually maintained?
- What vitality score threshold triggers the "review" flag?
- Should retired files be git-deleted or moved to `archive/` directory?

## Changelog

- 2026-02-17: Created from SESSION-HANDOFF.md design decisions
