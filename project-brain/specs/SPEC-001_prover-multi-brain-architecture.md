# SPEC-001: Prover Multi-Brain Architecture
<!-- type: SPEC -->
<!-- created: 2026-02-17 -->
<!-- tags: prover, multi-brain, orchestrator, architecture, git-worktrees, sub-agents, coordination, backtesting -->
<!-- links: SPEC-000, LEARN-024, LEARN-009, LEARN-011, LEARN-015 -->

## Overview

Prover is a multi-brain backtesting system. Multiple specialist brains coordinate through an orchestrator brain to implement, test, and refine trading strategies. This SPEC defines the architecture, coordination patterns, and the gaps that must be closed to make it work.

## System Components

### Brains

| Brain | Role | Source | Status |
|---|---|---|---|
| **Agentic Brain** | Meta-brain — documents how brains work | This repo | Exists (31+ files) |
| **Orchestrator** | Fans out tasks, gathers results, coordinates | Fork/refinement of agentic-brain | Not built |
| **Donchian** | Trading domain — indicators, signals, execution | Existing brain | Exists, needs enrichment |
| **Coder** | Implementation — from context7 repo | context7 repository | Not built |
| **Frontend** | HMI/UI for backtest visualization | Stack TBD | Not built |

### Orchestrator Role

The orchestrator is the only brain that talks to the user directly. It:

1. Receives a task from the user (e.g., "backtest Donchian channel breakout on BTC daily")
2. Decomposes the task into specialist subtasks
3. Fans out to specialist brains with context packages
4. Gathers results and synthesizes
5. Returns a unified response or coordinates multi-step implementation

### Specialist Brain Role

Each specialist brain:
- Owns a domain (trading logic, code patterns, UI components)
- Receives a scoped task + context package from the orchestrator
- Returns a condensed result (target: 1-2K tokens per LEARN-024 finding #10)
- Does NOT talk to other specialists directly — all coordination through orchestrator

## Coordination Architecture

### Option A: Git Worktree Isolation (from Letta)

Each specialist brain operates in its own git worktree of a shared repo:

```
prover/
├── .git/                          # Shared git history
├── main/                          # Orchestrator worktree
│   └── project-brain/
├── worktrees/
│   ├── donchian/                  # Donchian specialist worktree
│   │   └── project-brain/
│   ├── coder/                     # Coder specialist worktree
│   │   └── project-brain/
│   └── frontend/                  # Frontend specialist worktree
│       └── project-brain/
```

- Specialists work in isolation (no merge conflicts during work)
- Results merge back to main via git merge
- Git conflict resolution handles contradictions
- **Pro:** True isolation, auditable history, familiar tooling
- **Con:** Merge overhead, requires git discipline, setup complexity

### Option B: Sub-Agent with Context Packages (Claude Code native)

Use Claude Code's built-in sub-agent system (LEARN-009):

```
Orchestrator (main session)
├── Task tool → Donchian subagent (Explore type, brain files pre-loaded)
├── Task tool → Coder subagent (general-purpose, code access)
└── Task tool → Frontend subagent (general-purpose, UI patterns)
```

- Each subagent gets a fresh context window with only relevant brain files
- Returns condensed summary to orchestrator
- **Pro:** Native to Claude Code, no git overhead, parallel execution
- **Con:** Subagents can't spawn subagents, no persistent state between calls, context from many subagents bloats main conversation

### Option C: Agent Teams (LEARN-015, experimental)

Full independent Claude Code sessions connected by shared task list + mailbox:

- Teammates form a mesh (any-to-any messaging)
- Persistent task list with dependency tracking
- **Pro:** Most flexible, teammates have full capabilities
- **Con:** Experimental, ~7x token cost, no session resumption with teammates, Windows terminal limitations

### Recommended: Option B first, Option A for persistence

Start with **Option B** (sub-agents) because:
- Zero infrastructure to build
- Native to Claude Code
- Adequate for single-session backtesting tasks

Evolve to **Option A** (worktrees) when:
- Multi-session tasks require persistent specialist state
- Results need to be auditable/diffable
- Multiple specialists need to work on the same files

Option C deferred until agent teams exits experimental.

## Inter-Brain Communication Format

### Context Package (Orchestrator → Specialist)

```markdown
# CONTEXT-PACK: [task-id]
## Task
[Scoped description of what this specialist should do]

## Relevant Brain Files
[Fat index entries for files the specialist needs — not full files]

## Constraints
[Budget, scope limits, what NOT to do]

## Expected Output
[Format and size target for the response]
```

### Result Package (Specialist → Orchestrator)

```markdown
# RESULT: [task-id]
## Status
[complete | partial | blocked]

## Output
[1-2K token condensed result]

## Discoveries
[New knowledge found during work — candidate for deposit]

## Blockers
[What prevented completion, if any]
```

## Task Routing

Three strategies identified (from SESSION-HANDOFF uncommitted decisions):

1. **Hardcoded routing** — Orchestrator has a static map: trading → Donchian, implementation → Coder, UI → Frontend. Simple, works now.
2. **Fat-index capability ads** — Each specialist brain's INDEX-MASTER advertises what it knows. Orchestrator scans indexes to route. Self-maintaining.
3. **Learned RULE-based routing** — After enough tasks, deposit routing rules as RULE files based on observed patterns.

**Recommendation:** Start with #1, evolve to #2 as brains grow. #3 is aspirational.

## Gaps to Close

Derived from LEARN-024 gap analysis, scoped to what Prover needs:

### Gap 1: Git Worktree Multi-Agent Isolation
- **Need:** Specialists working on shared codebase without conflicts
- **Effort:** Medium — git worktree commands are straightforward, orchestration logic is the hard part
- **Priority:** P2 — not needed for Option B, needed for Option A evolution
- **Blocker:** None

### Gap 2: Background Reflection / Auto-Deposit
- **Need:** Specialists auto-depositing discoveries during long tasks, not just at session end
- **Effort:** Medium — requires periodic hook or timer mechanism
- **Priority:** P3 — nice-to-have, manual deposit works initially
- **Blocker:** Claude Code hooks are event-driven, not timer-driven. Would need a background subagent polling pattern.

### Gap 3: Formalized Defragmentation
- **Need:** After multiple backtest iterations, specialist brains accumulate redundant/contradictory results. Need structured cleanup.
- **Effort:** Low-Medium — define triggers (file count threshold, contradiction count), process (merge/retire/tighten), and metrics (index coverage, orphan count)
- **Priority:** P2 — becomes critical after ~50 files per brain
- **Triggers:**
  - File count exceeds 50 in any specialist brain
  - More than 3 files flagged with contradictions in Known Issues
  - Fat index entries exceed 200 lines
  - User explicitly requests consolidation

### Gap 4: Concurrent Initialization
- **Need:** Bootstrapping a new specialist brain from a large source (e.g., context7 repo) is slow if serial
- **Effort:** Medium — use parallel subagents to explore different parts of source, merge deposits
- **Priority:** P1 — needed immediately for building Coder and Frontend brains
- **Implementation:** Fan out N subagents, each exploring a different directory/topic, each deposits to a staging area, orchestrator deduplicates and commits

### Gap 5: Per-File Frontmatter vs Centralized Index
- **Need:** Decide whether Prover brains use per-file YAML frontmatter (Letta style) or centralized INDEX-MASTER (our style)
- **Effort:** Low — design decision, not implementation
- **Priority:** P1 — must decide before building new brains
- **Recommendation:** Keep centralized INDEX-MASTER. Reasons:
  - Saves tokens (one file load vs many)
  - Already proven in agentic-brain (31+ files, works well)
  - Per-file frontmatter requires opening files to discover them — defeats the purpose
  - Trade-off: requires index maintenance discipline (already enforced via rules)

## Backtest Results — Where They Go

Open question from SESSION-HANDOFF. Proposed answer:

- **Raw results** → Not stored in brain (too large, ephemeral)
- **Insights from results** → LEARN files in Donchian brain (e.g., "Donchian 20/10 outperforms 55/20 on BTC daily in trending markets")
- **Parameter decisions** → SPEC or RULE files in Donchian brain
- **Implementation notes** → CODE files in Coder brain
- **Visualization patterns** → LEARN files in Frontend brain

## Cross-Brain Conflict Resolution

Open question from SESSION-HANDOFF. Proposed answer:

When two specialists return contradictory information:
1. Orchestrator flags the conflict explicitly
2. Both claims deposited with `[CONFLICT]` tag in Known Issues
3. User decides (orchestrator presents the conflict, doesn't resolve autonomously)
4. Winning claim updated, losing claim retired with rationale

## Open Questions

- What is context7? (repo link needed to build Coder brain)
- Frontend stack preference? (React? Svelte? Plain HTML/JS?)
- Is Prover the whole system or just the backtester?
- Iterative vs single fan-out orchestration? (can orchestrator do multiple rounds?)

## Known Issues
- Agent teams (Option C) is experimental and ~7x token cost — not viable yet
- Subagents can't spawn subagents — limits recursive orchestration depth to 1
- Context from many completed subagents can bloat orchestrator's context window
- No timer-driven hooks in Claude Code — background reflection requires workaround
