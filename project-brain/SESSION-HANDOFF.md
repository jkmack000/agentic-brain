# SESSION-HANDOFF
<!-- written: 2026-02-17 -->
<!-- session-type: WORK -->
<!-- trigger: context-limit — 80% usage, 3% free -->

## What Was Being Done
Cleanup tasks, coder-brain scaffolding, Sandbox Agent SDK research + deposit, SPEC-001 update with Option D, and first knowledge migration from agentic-brain to coder-brain (retirement workflow).

## Current State
- **Status:** COMPLETED (this session's tasks) / READY for next phase
- **What's done:**
  - Deleted `coder.agent.project.md` (superseded by SPEC-002)
  - Fixed `pyproject.toml`: `brain_search` → `brain` in scripts/setuptools
  - Verified brain.py sub-index support already working
  - Scaffolded `coder-brain/` project (CLAUDE.md + brain.py init + capability ads in INDEX-MASTER)
  - Researched Sandbox Agent SDK → deposited as LEARN-037
  - Added Option D (Sandbox Agent + Rivet actors) to SPEC-001 coordination architecture
  - Migrated LEARN-035 → coder-brain LEARN-001 (Freqtrade IStrategy reference)
  - Migrated LEARN-036 → coder-brain LEARN-002 (LLM code generation patterns)
  - Originals retired to `project-brain/archive/` (first use of SPEC-003 retirement workflow)
  - Agentic-brain: 49 → 47 files. Coder-brain: 0 → 2 files.
  - All committed and pushed (4 commits: 3465d99, 7a98944, 6a06910)
- **What's left:**
  - **Coder brain Phase 1 ingestion** — next priority:
    - LEARN-003: Freqtrade bot config (config.json, exchange setup, dry-run vs live)
    - LEARN-004: Freqtrade bot lifecycle (startup, trading loop, shutdown, data refresh)
    - LEARN-005: Freqtrade data handling (pairs, timeframes, downloading, custom data)
    - LEARN-006: Freqtrade backtesting CLI (commands, parameters, result interpretation)
    - LEARN-007: ta-lib indicator reference (function signatures, gotchas)
    - CODE-001: IStrategy template with fill slots
    - CODE-002: Test scaffolding (conftest.py, fixtures, strategy test patterns)
    - CODE-003: Sample validated strategy (known-working example)
    - RULE-001: Import whitelist
    - RULE-002: Code style conventions
    - RULE-003: Testing requirements
    - SPEC-001: Coder brain architecture (adapted from agentic-brain SPEC-002)
  - Vitality threshold tuning (deferred)
  - `/brain-checkpoint` skill (deferred)

## Uncommitted Decisions
- None — all deposited and committed

## Discoveries Not Yet Deposited
- None — LEARN-037 deposited, SPEC-001 updated

## Open Questions (Carried Forward)
- All tracked in INDEX-MASTER Open Questions table (26 items)

## Files Modified This Session
- `coder.agent.project.md` — DELETED
- `project-brain/pyproject.toml` — fixed module references
- `project-brain/INDEX-MASTER.md` — LEARN-037 entry, LEARN-035/036 retired, SPEC-001 summary updated, file count 48→47, OQs #25/#26 added
- `project-brain/indexes/INDEX-claude-code.md` — LEARN-014 backlinks updated
- `project-brain/specs/SPEC-001_prover-multi-brain-architecture.md` — Option D added, links updated
- `project-brain/learnings/LEARN-037_sandbox-agent-sdk-remote-coding-agent-execution.md` — Rivet section added
- `project-brain/SESSION-HANDOFF.md` — this file
- `project-brain/logs/LOG-002_project-timeline.md` — timeline entries

## Files Added to Brain This Session
- `project-brain/learnings/LEARN-037` — Sandbox Agent SDK research
- `coder-brain/CLAUDE.md` — Coder agent project configuration
- `coder-brain/project-brain/` — full brain scaffold
- `coder-brain/project-brain/learnings/LEARN-001` — Freqtrade IStrategy (migrated)
- `coder-brain/project-brain/learnings/LEARN-002` — LLM code gen patterns (migrated)

## Files Retired This Session
- `LEARN-035` → `archive/` (migrated to coder-brain LEARN-001)
- `LEARN-036` → `archive/` (migrated to coder-brain LEARN-002)

## Dead Ends
- None

## Recommended Next Session
- **Type:** INGESTION
- **Load:** SESSION-HANDOFF.md, coder-brain/project-brain/INDEX-MASTER.md
- **First action:**
  1. Launch 2-3 parallel research agents against freqtrade.io docs for deep ingestion
  2. Deposit as coder-brain LEARN-003 through LEARN-007
  3. Then create CODE-001 (IStrategy template), CODE-002 (test scaffold), CODE-003 (sample strategy)
  4. Then create RULE-001/002/003 and SPEC-001
  5. Run coder-brain `brain.py status` to verify health
