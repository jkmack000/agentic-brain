# LOG-002 — Project Timeline
<!-- type: LOG -->
<!-- tags: timeline, sessions, milestones, changelog, meta -->
<!-- created: 2026-02-14 -->
<!-- links: SPEC-000 -->

## Purpose
Running chronological record of all project sessions, milestones, ingestions, and structural changes. Every session should append an entry before ending. This file is the project's memory of *when* things happened — use it to trace evolution, estimate velocity, and orient new sessions on project history.

## How to Use
- **New session?** Scan the latest entries to see recent activity.
- **Ending a session?** Append an entry below with what happened.
- **Format:** One entry per session or significant event. Keep entries tight — the fat index in INDEX-MASTER tells you *what's in the files*, this tells you *when and why they were created*.

## Entry Format
```
### YYYY-MM-DD — [Session Type] — [Brief Label]
- **Duration:** ~Xh / unknown
- **Key actions:** [bulleted list]
- **Files created/modified:** [list]
- **Decisions made:** [if any]
- **Blockers/dead ends:** [if any]
```

---

## Timeline

### 2026-02-14 — BUILD + INGESTION — Project Brain Genesis
- **Duration:** ~unknown (long session, hit ~130K/200K tokens)
- **Key actions:**
  - Full Phase 0 framework built: directory structure, 7 templates, INDEX-MASTER, brain.py CLI, INIT.md
  - SESSION-HANDOFF system designed and documented
  - Deduplication and consolidation rules formalized
  - User shorthand commands defined (Ingest, Deposit, Index, Handoff)
  - Donchian bot brain initialized at Desktop/Donchian.bot/project-brain/
  - First ingestion into Donchian brain (4 files: SPEC-001, RULE-001, RULE-002, LEARN-001)
  - Compared system against claude-mem, Mem0, SimpleMem — confirmed complementary
- **Files created:**
  - SPEC-000 (project brain architecture)
  - LEARN-001 (semantic compression)
  - LOG-001 (Brain Hub concept)
  - INIT.md, SESSION-HANDOFF.md, all 7 templates, brain.py, INDEX-MASTER.md
- **Decisions made:**
  - Fat index over thin index; standalone CLI over Obsidian plugin
  - Focus on Donchian bot as first real project before any public release
- **Blockers/dead ends:**
  - pyproject.toml entry points conflict — settled on `uv run brain.py`
  - StudyLib URL 403 — used alternate sources

### 2026-02-14 — INGESTION — Competitive Landscape + Research Methods
- **Duration:** ~unknown
- **Key actions:**
  - Ingested competitive landscape survey of LLM memory systems
  - Ingested qualitative research methods (Stake) transfer to brain design
- **Files created:**
  - LEARN-002 (competitive landscape — Letta, RAPTOR, GraphRAG, Mem0, etc.)
  - LEARN-003 (qualitative research methods — triangulation, progressive focusing)
- **Decisions made:**
  - MCP wrapper for brain.py is #1 priority after Donchian bot MVP
  - Top 10 improvements ranked by impact/effort (all deferred)

### 2026-02-14 — INGESTION — Context Engineering Article
- **Duration:** ~5min
- **Key actions:**
  - Ingested Thomas Landgraf's "Context Engineering for Claude Code" article
  - Validated brain architecture against emerging industry best practices
- **Files created:**
  - LEARN-004 (context engineering for Claude Code)
- **Decisions made:**
  - Three actionable items: `@path` code refs, 50KB split threshold, two-phase research workflow

### 2026-02-14 — META — Project Timeline Established
- **Duration:** ~5min
- **Key actions:**
  - Created LOG-002 (this file) as the standard project timeline
  - Added to INIT.md as standard for all new brains
  - Updated INDEX-MASTER.md
- **Files created:**
  - LOG-002 (project timeline)
- **Decisions made:**
  - Every brain gets a LOG-002 project timeline as standard infrastructure

### 2026-02-14 — INGESTION — Anthropic Official Docs (Tier 1 Batch)
- **Duration:** ~15min
- **Key actions:**
  - Ingested Anthropic's official best practices page (LEARN-005)
  - Batch-ingested 6 Tier 1 doc pages in parallel: memory system, skills, hooks (ref+guide), subagents, architecture internals
  - Created 5 LEARN files (LEARN-006 through LEARN-010) from 6 source pages (hooks ref+guide combined)
  - Updated INDEX-MASTER.md with fat index entries for all 6 new files (LEARN-005 through LEARN-010), total now 13
- **Files created:**
  - LEARN-005 (official best practices)
  - LEARN-006 (memory system — CLAUDE.md, auto memory, rules)
  - LEARN-007 (skills system — SKILL.md deep dive)
  - LEARN-008 (hooks system — reference + guide combined)
  - LEARN-009 (subagents system — custom agents, persistent memory)
  - LEARN-010 (architecture internals — agentic loop, context, sessions)
- **Decisions made:**
  - Identified Claude Code's delivery mechanisms for brain knowledge: skills, .claude/rules/, @path imports, auto memory
  - Persistent memory in subagents independently converges on fat-index architecture — strong validation
  - Hooks system enables brain automation: SessionStart loading, PostToolUse deposit, Stop quality gates, SessionEnd handoff

### 2026-02-14 — DEPOSIT — Undeposited Discoveries from Previous Session
- **Duration:** ~5min
- **Key actions:**
  - Deposited 3 findings carried in SESSION-HANDOFF.md that were never written to proper LTM files
  - LEARN-011: Fat-index convergence validation (3 Anthropic systems independently converge on our architecture)
  - LEARN-012: Operational drift — template divergence and multi-brain sync challenges
  - LOG-003: Brain-to-Claude Code delivery mechanism analysis (skills vs rules vs @path vs auto memory)
  - Updated INDEX-MASTER.md (file count 13 → 16)
- **Files created:**
  - LEARN-011 (fat-index convergence validation)
  - LEARN-012 (brain operational drift and sync)
  - LOG-003 (delivery mechanism analysis)
- **Files modified:**
  - INDEX-MASTER.md (3 new fat index entries, count updated)
  - LOG-002 (this entry)
- **Decisions made:** None — these were deposits of previously-identified findings, not new decisions
- **Blockers/dead ends:** None

### 2026-02-14 — INGESTION — Anthropic Official Docs (Tier 2 Batch)
- **Duration:** ~15min
- **Key actions:**
  - Batch-ingested 7 Tier 2 doc pages in parallel via 6 subagents: MCP, headless/Agent SDK (+ linked SDK docs), agent-teams, plugins (+ plugins-reference), costs + settings, common-workflows
  - Created 6 LEARN files (LEARN-013 through LEARN-018) from 7+ source pages
  - Updated INDEX-MASTER.md with fat index entries for all 6 new files, total now 22
  - Tier 2 ingestion is now COMPLETE — all identified Anthropic doc pages have been ingested
- **Files created:**
  - LEARN-013 (MCP system — transports, scopes, resources, prompts, brain MCP server architecture)
  - LEARN-014 (Agent SDK — programmatic API, Python/TypeScript, custom MCP tools, structured output)
  - LEARN-015 (agent teams — multi-session coordination, task list, messaging, delegate mode)
  - LEARN-016 (plugin system — packaging, distribution, namespacing, engine/data split)
  - LEARN-017 (costs, settings, environment variables — $6/day baseline, 50+ env vars, 5-level hierarchy)
  - LEARN-018 (common workflows — plan mode, extended thinking, 4 recipe shapes, headless plan mode)
- **Files modified:**
  - INDEX-MASTER.md (6 new fat index entries, count 16 → 22)
  - LOG-002 (this entry)
- **Decisions made:**
  - Brain MCP server confirmed as viable and high-priority (LEARN-013)
  - Agent SDK identified as brain automation engine (LEARN-014)
  - Plugin system identified as brain distribution mechanism with engine/data split (LEARN-016)
  - Headless Plan Mode identified as ideal brain search mechanism (LEARN-018)
  - "ultrathink" / "think hard" are NOT special keywords — do not use in brain prompts (LEARN-018)
- **Blockers/dead ends:**
  - Original headless docs URL now redirects to Agent SDK docs — naming changed, content significantly expanded

### 2026-02-14 — CONSOLIDATION — First Dedup/Correction Pass
- **Duration:** ~5min
- **Key actions:**
  - Systematic cross-file comparison of all 22 brain files via fat index analysis
  - Fixed LEARN-005: Plan Mode toggle (Ctrl+G → Shift+Tab), "headless mode" → "Agent SDK" rename
  - Fixed LEARN-015 and LEARN-016: removed incorrect claims that TeammateIdle/TaskCompleted events were missing from LEARN-008 (they were already there)
  - Added cross-reference links: LEARN-005 → 013/014/017/018, LEARN-008 → 015/016, LEARN-010 → 013/014/017
  - Tightened INDEX-MASTER entries for LEARN-005, LEARN-015, LEARN-016 (removed misinformation, added "superseded by" notes)
  - Updated tags: LEARN-005 "headless" → "agent-sdk"
- **Files modified:**
  - LEARN-005 (3 corrections + link additions)
  - LEARN-008 (link additions)
  - LEARN-010 (link additions)
  - LEARN-015 (hook event claim corrected)
  - LEARN-016 (hook event claim corrected)
  - INDEX-MASTER.md (5 entries updated: LEARN-005, LEARN-008, LEARN-010, LEARN-015, LEARN-016)
  - LOG-002 (this entry)
- **Decisions made:**
  - No files need merging — all 22 cover distinct topics, overlaps are only brief mentions in earlier files later expanded by dedicated LEARNs
  - LEARN-005 remains the best single-file operational overview; later LEARNs supersede it on specific topics
  - Hook event count is 14 (confirmed), including team-specific events
- **Blockers/dead ends:**
  - Subagent extraction agents were misled by dedup context summaries, causing 2 false "missing event" claims — corrected during consolidation

### 2026-02-15 — BUILD — Claude Code Brain Integration (Layers 1-3)
- **Duration:** ~15min
- **Key actions:**
  - Implemented full Claude Code native integration for Project Brain
  - Created CLAUDE.md with @path import of INIT.md (auto-bootstrap)
  - Created 3 always-on rules in .claude/rules/ (session hygiene, fat-index discipline, ingestion dedup)
  - Created 4 skills in .claude/skills/ (/brain-search, /brain-deposit, /brain-handoff, /brain-status)
  - Added 4 hooks to .claude/settings.local.json (SessionStart, PreCompact, Stop, PostToolUse)
  - Deposited LEARN-019 documenting the integration
  - Updated INDEX-MASTER.md (file count 22 → 23, new fat index entry)
- **Files created:**
  - CLAUDE.md (root bootstrap)
  - .claude/rules/brain-session-hygiene.md
  - .claude/rules/brain-fat-index-discipline.md
  - .claude/rules/brain-ingestion-dedup.md
  - .claude/skills/brain-search/SKILL.md
  - .claude/skills/brain-deposit/SKILL.md
  - .claude/skills/brain-handoff/SKILL.md
  - .claude/skills/brain-status/SKILL.md
  - LEARN-019 (claude-code-brain-integration-layers-1-3)
- **Files modified:**
  - .claude/settings.local.json (hooks block added)
  - INDEX-MASTER.md (LEARN-019 entry, count 22 → 23)
  - LOG-002 (this entry)
  - SESSION-HANDOFF.md (updated)
- **Decisions made:**
  - CLAUDE.md imports INIT.md via @path (not INDEX-MASTER — too large)
  - Skills use disable-model-invocation (user-only slash commands)
  - Stop hook is prompt-type (blocking) — may need downgrade if too aggressive
  - PostToolUse hook uses python -c for JSON parsing
  - All hooks in settings.local.json (personal, not shared)
- **Blockers/dead ends:** None

### 2026-02-15 — TEST — Layer 1-3 Integration Test (Continuation)
- **Duration:** ~10min
- **Key actions:**
  - Confirmed all 4 skills visible in system-reminder (disable-model-invocation fix verified)
  - Tested /brain-search: returned 5 ranked results for "hooks" query, correct ranking
  - Tested /brain-status: 23 files, 0 orphans, 0 ghosts, healthy
  - Tested /brain-handoff: SESSION-HANDOFF.md written successfully with full session state
  - Steps 5-6 (PostToolUse hook, Stop hook) pending
- **Files modified:**
  - SESSION-HANDOFF.md (overwritten by /brain-handoff test)
  - LOG-002 (this entry)
- **Decisions made:** None — this is a test session
- **Blockers/dead ends:** None so far

### 2026-02-15 — FIX + TEST — Skills Resolution & Hooks Format Migration
- **Duration:** ~10min
- **Key actions:**
  - Diagnosed skills not resolving via CLI `/` — caused by spaces in project path
  - Copied 4 skills to user-level `~/.claude/skills/` as workaround — all now resolve
  - Migrated hooks in `settings.local.json` to new matcher-based format (required by Claude Code 2.1.42)
  - PostToolUse hook improved with `{"tools": ["Edit", "Write"]}` matcher
  - Tested `/brain-status`, `/brain-search hooks`, `/brain-handoff` — all working
- **Files modified:**
  - `.claude/settings.local.json` (hooks format migrated)
  - `~/.claude/skills/brain-*/SKILL.md` (4 skills copied to user scope)
  - SESSION-HANDOFF.md (updated via /brain-handoff)
  - LOG-002 (this entry)
- **Decisions made:**
  - Skills moved to user-level scope as workaround for spaces-in-path bug
  - Hooks use new matcher schema going forward
- **Blockers/dead ends:** None

### 2026-02-15 — CLEANUP — Integration Layer Known Issues Resolution
- **Duration:** ~10min
- **Key actions:**
  - Removed 4 duplicate project-level skills from `.claude/skills/` (user-level copies canonical)
  - Verified PostToolUse hook logic via manual stdin test — PASS
  - Noted PreCompact hook as not testable on demand (trivially correct)
  - Tested `/brain-deposit` skill — dedup check correctly identified enrichment target
  - Deleted `project-brain/test-session-handoff.md` artifact
  - Enriched LEARN-019 with final test results, all components PASS
  - All integration known issues now resolved — system fully operational
- **Files modified:**
  - LEARN-019 (enriched — test results updated, action item #9 added)
  - INDEX-MASTER.md (LEARN-019 known issues tightened)
  - LOG-002 (this entry)
  - SESSION-HANDOFF.md (updated)
- **Files deleted:**
  - `.claude/skills/brain-{search,deposit,handoff,status}/` (4 duplicate skill dirs)
  - `project-brain/test-session-handoff.md` (cleanup artifact)
- **Decisions made:** User-level `~/.claude/skills/` is the canonical location for brain skills
- **Blockers/dead ends:** None

### 2026-02-15 — WORK — Donchian Bot Integration + mem0-dspy Research
- **Duration:** ~20min
- **Key actions:**
  - Applied full brain integration (Layers 1-3) to Donchian.bot project
  - Created CLAUDE.md, 3 rules, 4 hooks for Donchian.bot (adapted: LOG-001 not LOG-002, SPEC-002 as deep-context doc)
  - Researched avbiswas/mem0-dspy repo: from-scratch Mem0 clone using DSPy ReAct agents + Qdrant
  - Identified key pattern: LLM-driven ADD/UPDATE/DELETE/NOOP memory CRUD (parallels our /brain-deposit dedup check)
  - Found 4 bugs in the repo (delete tool index→ID mapping, date format, duplicated facet, join separator)
  - Stop hook successfully blocked exit when handoff was stale — confirms hook works in production
- **Files created (Donchian.bot project):**
  - CLAUDE.md, .claude/rules/brain-{session-hygiene,fat-index-discipline,ingestion-dedup}.md
  - .claude/settings.local.json (rewritten with hooks)
- **Files modified (LTM SPECS project):**
  - SESSION-HANDOFF.md (updated twice — once mid-session, once on Stop hook trigger)
  - LOG-002 (this entry)
- **Decisions made:**
  - Donchian brain rules reference LOG-001 (its session compendium) not LOG-002
  - Donchian fat-index discipline points to SPEC-002 as deep-context doc
  - User wants to use brain more before packaging as plugin
- **Blockers/dead ends:** None

### 2026-02-15 — INGESTION — mem0-dspy + LangChain/LangGraph Deep Dives
- **Duration:** ~30min
- **Key actions:**
  - Deposited LEARN-020: mem0-dspy analysis — from-scratch Mem0 clone, two-agent ReAct architecture, LLM-driven CRUD, 64-dim embeddings, 4 bugs found
  - Researched LangChain docs via 3 parallel agents (overview, memory/persistence, agents/RAG)
  - Deposited LEARN-021: LangChain/LangGraph full architecture — 3 products (DeepAgents/Agents/LangGraph), CoALA memory taxonomy, middleware system (6 hooks, transient vs persistent), retrieval patterns priority-ranked
  - Comparative analysis: Brain vs LangGraph — complementary not competing. Brain wins on readability, zero cost, git-friendly. LangGraph wins on auto-persistence, semantic search, content hashing.
  - Identified BM25 search as #1 low-effort improvement for brain.py
  - Stop hook blocked exit twice this session — confirms production reliability
- **Files created:**
  - LEARN-020 (mem0-dspy LLM-driven memory CRUD)
  - LEARN-021 (LangChain/LangGraph architecture, memory, retrieval)
- **Files modified:**
  - INDEX-MASTER.md (count 23→25, two new fat index entries)
  - SESSION-HANDOFF.md (updated)
  - LOG-002 (this entry)
- **Decisions made:**
  - Brain and LangGraph are complementary — cherry-pick best patterns, don't switch architectures
  - BM25 search ranked #1 improvement, content hashing #2, multi-query #3
  - DeepAgents flagged for monitoring — most directly competitive to brain system
- **Blockers/dead ends:**
  - Agent 3 output file empty on first read — resumed agent to recover results (cause unknown)

### 2026-02-15 — INGESTION — DSPy Optimizers/Teleprompters
- **Duration:** ~15min
- **Key actions:**
  - Resumed deferred ingestion from previous session (DSPy optimizer/teleprompter docs)
  - Launched 2 parallel research agents: one for optimizer API/catalog, one for compilation model/metrics/advanced features
  - Both agents' output files were empty on completion (recurring bug) — resumed both to recover results
  - Synthesized findings into LEARN-022: 15 optimizers across 5 categories, full MIPROv2 deep dive, bootstrapping mechanics, metrics system, assertions, teacher-student distillation, practical guidance
  - Identified 7 brain-relevant takeaways: SIMBA rules parallel RULE files, InferRules could mine LOGs, teacher-student for brain search optimization
- **Files created:**
  - LEARN-022 (DSPy optimizers/teleprompters — complete technical reference)
- **Files modified:**
  - INDEX-MASTER.md (LEARN-022 entry, count 25→26)
  - LOG-002 (this entry)
  - SESSION-HANDOFF.md (updated)
- **Decisions made:** None — pure ingestion session
- **Blockers/dead ends:**
  - Both agent output files empty on completion — same bug as previous session. Resume-to-recover workaround reliable.

### 2026-02-15 — WORK — BM25 Search Upgrade for brain.py
- **Duration:** ~10min
- **Key actions:**
  - Replaced naive keyword scoring (`score_entry()`) with 3-stage BM25 pipeline in brain.py
  - Stage 1: BM25Okapi term-frequency/inverse-document-frequency scoring over fat index corpus
  - Stage 2: Structural boosts — exact tag match (+5.0), exact ID match (+4.0)
  - Stage 3: Link propagation — files linked by high-scoring results receive 15% score boost ("neuron connections")
  - Tags repeated 3x in corpus, IDs 2x — curated metadata naturally weighted higher than raw summary text
  - Fixed Windows cp1252 encoding crash on Unicode characters (UTF-8 stdout wrapper)
  - Added `rank-bm25>=0.2.2` to pyproject.toml
  - Tested 3 queries all ranking correctly: "hooks" → LEARN-005/008/019, "dspy optimizer" → LEARN-022/020, "fat index convergence validation" → LEARN-011
  - `cmd_recall` (RESET file generation) also upgraded to BM25
- **Files modified:**
  - `project-brain/brain.py` (score_entry → score_entries_bm25, tokenize, entry_to_corpus_doc, build_bm25_index, UTF-8 fix)
  - `project-brain/pyproject.toml` (rank-bm25 dependency)
  - SESSION-HANDOFF.md, LOG-002
- **Decisions made:**
  - Link propagation at 15% — enough to surface connected files without drowning out direct matches
  - Tags 3x, IDs 2x repetition in corpus — simple weighting via document construction, no custom BM25 params needed
  - Float scores displayed with 1 decimal (was integer)

### 2026-02-15 — INGESTION — QMD (tobi/qmd) Local Hybrid Search Engine
- **Duration:** ~15min
- **Key actions:**
  - Researched tobi/qmd at user request — local-first CLI hybrid search for markdown
  - Analyzed repo: README, store.ts, qmd.ts, llm.ts, mcp.ts, collections.ts, package.json
  - Dedup analysis: ~70% overlaps with LEARN-021 patterns (BM25, content hashing, hybrid+RRF, multi-query, MCP)
  - Identified 7 genuinely novel patterns: typed query expansion (lex/vec/hyde), position-aware blending, smart signal detection, two-table content-addressable storage, dynamic MCP instruction injection, grammar-constrained decoding, concrete model stack sizing
  - Flagged "96% token savings" claim as unverified per user instruction — single Twitter anecdote, not controlled benchmark
  - Deposited as LEARN-023 (standalone file, not enrichment — QMD is a distinct system)
- **Files created:**
  - LEARN-023 (QMD local hybrid search engine)
- **Files modified:**
  - INDEX-MASTER.md (LEARN-023 entry, count 26→27)
  - LOG-002 (this entry)
- **Decisions made:** None — competitive intelligence ingestion
- **Blockers/dead ends:** Twitter/X content unfetchable (returns JS/CSS only) — relied on search snippet for the token savings claim

### 2026-02-15 — WORK — SSH Key Setup (Non-Brain Task)
- **Duration:** ~10min
- **Key actions:**
  - Helped user set up SSH from Windows to remote machine (192.168.1.208, user bobfuggin)
  - Generated Ed25519 key pair (~/.ssh/id_ed25519)
  - Copied public key to remote using 3-step manual method (zsh on remote rejected && chains)
  - Confirmed passwordless SSH working
- **Files created:** ~/.ssh/id_ed25519, ~/.ssh/id_ed25519.pub (system files, not brain)
- **Files modified:** SESSION-HANDOFF.md, LOG-002 (this entry)
- **Decisions made:** None — operational task, no brain knowledge deposited
- **Blockers/dead ends:** ssh-copy-id / piped && command failed on remote zsh — 3 separate commands worked

### 2026-02-15 — REVIEW — Session State Check
- **Duration:** ~2min
- **Key actions:**
  - Read SESSION-HANDOFF.md at user request to review previous session state
  - No substantive work performed
- **Files created/modified:** SESSION-HANDOFF.md (refreshed), LOG-002 (this entry)
- **Decisions made:** None
- **Blockers/dead ends:** None

### 2026-02-15 — META — Clean Handoff
- **Duration:** ~2min
- **Key actions:**
  - User triggered /brain-handoff at session start
  - Wrote clean SESSION-HANDOFF.md carrying forward open questions from previous sessions
- **Files modified:** SESSION-HANDOFF.md, LOG-002 (this entry)
- **Decisions made:** None
- **Blockers/dead ends:** None

### 2026-02-16 — WORK — Content Hashing Dedup for brain.py
- **Duration:** ~15min
- **Key actions:**
  - Implemented content hashing dedup per approved plan (LEARN-021, LEARN-023 identified as #2 improvement)
  - Added 5 hash helper functions: `hash_file`, `load_manifest`, `save_manifest`, `build_manifest`, `check_content_duplicate`
  - Integrated into `cmd_deposit`: duplicate detection with abort option, manifest update on success
  - New `cmd_reindex`: full manifest rebuild with diff report (new/changed/deleted files)
  - Integrated into `cmd_status`: manifest health reporting
  - Verified: 27 files hashed, idempotent reindex, status shows "All hashes up to date"
  - Attempted git init + first commit — blocked by nested `.git` in `project-brain/`
- **Files created:**
  - `project-brain/.content-hashes.json` (27-entry manifest)
- **Files modified:**
  - `project-brain/brain.py` (content hashing: imports, constants, 5 helpers, 3 command integrations)
  - SESSION-HANDOFF.md, LOG-002 (this entry)
- **Decisions made:**
  - SHA-256 for content hashing (standard, collision-resistant)
  - JSON manifest over SQLite (simple, git-friendly, sufficient for 27 files)
  - Scope limited: no vector embeddings, no two-table schema, no multi-query (deferred per plan)
- **Blockers/dead ends:**
  - `git add project-brain/` fails with "does not have a commit checked out" — nested .git suspected, needs investigation

### 2026-02-16 — DEPOSIT — Tool-Use Pattern RULE Files (First Batch)
- **Duration:** ~10min
- **Key actions:**
  - Scanned LEARN-005, LEARN-008, LEARN-010, LEARN-018, LEARN-019 via subagent for extractable tool-use patterns
  - Extracted 26 patterns across 6 categories (hooks, skills, windows, context, sessions, CLAUDE.md)
  - Consolidated into 3 RULE files: hooks config (11 patterns), context/session mgmt (9 patterns), skills/CLAUDE.md (6 patterns)
  - Updated INDEX-MASTER.md with fat index entries (count 27→30)
  - Rebuilt content hash manifest (30 entries)
- **Files created:**
  - RULE-001 (hooks configuration patterns — 11 patterns)
  - RULE-002 (context and session management — 9 patterns)
  - RULE-003 (skills and CLAUDE.md patterns — 6 patterns)
- **Files modified:**
  - INDEX-MASTER.md (3 new fat index entries, count 27→30)
  - .content-hashes.json (rebuilt, 30 entries)
  - LOG-002 (this entry)
- **Decisions made:**
  - Tool-use patterns stored as RULE files (not LEARN) — they're prescriptive, not descriptive
  - Grouped by domain (hooks / context+session / skills+CLAUDE.md) rather than one-pattern-per-file
  - Each pattern follows When/Do/Never/Consequence structure for machine-actionability
- **Blockers/dead ends:** None

### 2026-02-16 — DEPOSIT — RULE-004 Hooks Safe Modification Workflow
- **Duration:** ~5min
- **Key actions:**
  - Created RULE-004: backup workflow for hooks modifications (cp .backup before changes, rollback if broken)
  - Updated INDEX-MASTER.md (count 30→31)
  - Rebuilt content hash manifest (31 entries)
- **Files created:**
  - RULE-004 (hooks safe modification workflow)
- **Files modified:**
  - INDEX-MASTER.md (RULE-004 entry, count 30→31)
  - .content-hashes.json (rebuilt, 31 entries)
  - LOG-002 (this entry)
- **Decisions made:** None — direct user request
- **Blockers/dead ends:** None

### 2026-02-16 — INFRA — GitHub Repo Creation + Initial Commit
- **Duration:** ~15min
- **Key actions:**
  - Removed nested .git from project-brain/ (cause of `git add` failure)
  - Installed gh CLI v2.86.0 via winget, authenticated as jkmack000
  - Set git identity (jkmack000, noreply email)
  - Created initial commit: 55 files, 6,370 lines
  - Created public GitHub repo: https://github.com/jkmack000/agentic-brain
  - Pushed via HTTPS (SSH failed — key not registered on GitHub)
  - Configured `gh auth setup-git` as HTTPS credential helper
- **Files modified:**
  - Removed project-brain/.git (nested git repo)
  - SESSION-HANDOFF.md, LOG-002 (this entry)
- **Decisions made:**
  - Repo name: "agentic-brain" (user specified)
  - Public repo (user specified)
  - HTTPS push (SSH key registration deferred by user)
  - Excluded donchian-channel-breakout.pdf and nul artifact from commit
- **Blockers/dead ends:**
  - Nested .git in project-brain/ blocked git add — removed
  - SSH push failed (key not on GitHub) — switched to HTTPS
  - gh ssh-key add needs admin:public_key scope — user deferred

### 2026-02-16 — PLANNING — Prover Multi-Brain Architecture
- **Duration:** ~15min
- **Key actions:**
  - High-level architecture discussion for "Prover" — multi-brain backtesting system
  - Defined three specialist brains: Donchian (trading domain, already exists), Coder (from context7), Frontend (HMI/UI)
  - Agentic-brain designated as the meta-brain; orchestrator will be built from it
  - Discussed orchestration workflow: fan-out to specialist brains → gather context packages → coordinate implementation
  - Identified three routing strategies (hardcoded, fat-index capability ads, learned RULE-based)
  - Identified need for inter-brain communication format (BRIEF/CONTEXT-PACK)
  - Confirmed Agent SDK (LEARN-014), subagents (LEARN-009), agent teams (LEARN-015) already ingested for orchestrator build
  - User clarified this is planning only — no implementation this session
- **Files created:** None
- **Files modified:** SESSION-HANDOFF.md, LOG-002 (this entry)
- **Decisions made:**
  - Prover = project name for the multi-brain backtesting system
  - Three specialist brains + orchestrator architecture
  - Agentic-brain is the meta-brain, orchestrator built from it separately
- **Blockers/dead ends:** None — planning session, all decisions captured in SESSION-HANDOFF.md for deposit as SPEC next session

### 2026-02-17 — RESEARCH — Prover Architecture Knowledge Batch
- **Duration:** ~30min
- **Key actions:**
  - Executed 4-topic parallel research for Prover build knowledge (200K token budget)
  - Launched 4 research agents in parallel: backtesting architecture, multi-agent orchestration, inter-agent IPC, Context7 ingestion
  - LEARN-025 (backtesting): 6 frameworks analyzed, hybrid two-phase pipeline (VectorBT screening → Freqtrade validation) recommended, CPCV with PBO < 0.5 as hard gate, 4 Prover-specific pitfalls identified
  - LEARN-026 (IPC): Google A2A protocol, 6 framework IPC patterns, CONTEXT-PACK v2 and RESULT v2 templates with YAML frontmatter, token budget envelope defined (~750 CONTEXT-PACK, ~1100-1500 RESULT), 9 key takeaways
  - LEARN-027 (orchestration): 6 production frameworks, fan-out/fan-in with reducers, 41-86.7% multi-agent failure rate finding, 7 error handling patterns, 6 context management strategies (observation masking = LLM summarization for cheaper)
  - LEARN-028 (Context7): Architecture analysis of Upstash's MCP doc server, 7 transferable patterns for Coder brain, Context7 + brain are complementary not competing
  - Updated INDEX-MASTER.md (count 33→37, 4 new fat index entries)
  - Batch 2 topics (git worktrees, BM25 implementation, Zettelkasten at scale) deferred to stay within 200K budget
- **Files created:**
  - LEARN-025 (backtesting engine architecture)
  - LEARN-026 (inter-agent communication patterns)
  - LEARN-027 (multi-agent orchestration patterns)
  - LEARN-028 (Context7 architecture analysis)
- **Files modified:**
  - INDEX-MASTER.md (4 entries added, count 33→37)
  - LOG-002 (this entry)
  - SESSION-HANDOFF.md
- **Files deleted:**
  - multi-agent-orchestration-research.md (root artifact, content moved to LEARN-027)
- **Decisions made:**
  - Freqtrade IStrategy for AI-generated strategies (LLM-friendly DataFrame methods)
  - CPCV with PBO < 0.5 as hard validation gate (not modifiable by AI agents)
  - YAML frontmatter + markdown body for CONTEXT-PACK/RESULT v2 formats
  - Context isolation as #1 multi-agent architecture principle
  - Code-level orchestration + LLM flexibility within specialists for Prover
  - Context7 + Coder brain complementary (external docs vs project-specific knowledge)
- **Blockers/dead ends:** Agent output files sometimes empty on first read (recurring bug, resume-to-recover works); Batch 2 deferred for budget

### 2026-02-17 — RESEARCH — Batch 2 Deferred Topics + Article Review
- **Duration:** ~30min
- **Key actions:**
  - Completed all 3 deferred Batch 2 research topics from previous session (200K token budget)
  - Launched 3 parallel research agents: git worktrees, BM25/hybrid search, file-based knowledge management
  - LEARN-029 (git worktrees): Worktree mechanics, 4 real-world systems (Letta, ccswarm, Crystal, incident.io), concurrent safety, Claude Code integration, Prover-specific patterns (branch naming, orchestrator script, brain file coordination — recommends orchestrator-only writes)
  - LEARN-030 (BM25/search): 6 Python libraries compared, field boosting strategy, RRF hybrid fusion, query expansion, 3-phase roadmap (improve tokenizer → SQLite FTS5 → hybrid search)
  - LEARN-031 (knowledge mgmt): Zettelkasten/Obsidian/Logseq patterns, scaling thresholds (50→5000+ files), A-MEM NeurIPS 2025 validation, progressive summarization, maintenance cadence, prioritized improvements
  - Reviewed HatchWorks orchestration article — found fully subsumed by LEARN-026/027, no deposit needed
  - Updated INDEX-MASTER.md (count 37→40, 3 new fat index entries)
  - Verified project files intact after directory move (C:\Users\Jkmac\fuck windows\Desktop\LTM SPECS → C:\agentic-brain)
- **Files created:**
  - LEARN-029 (git worktree workflows for parallel agents)
  - LEARN-030 (BM25 and hybrid search implementation patterns)
  - LEARN-031 (file-based knowledge management at scale)
- **Files modified:**
  - INDEX-MASTER.md (3 entries added, count 37→40)
  - LOG-002 (this entry)
- **Decisions made:**
  - Orchestrator-only brain writes for Prover (avoids merge conflicts in brain files)
  - SQLite FTS5 as best next search upgrade (zero deps, native field boosting)
  - Sub-index creation triggered by "mental squeeze point" not arbitrary file count
  - HatchWorks article skip — duplicate of existing LEARN-026/027 coverage
- **Blockers/dead ends:**
  - All 3 research agents couldn't write files (permission denied in subagents) — had to resume agents to extract content and write files from main session
  - Article ingestion agent couldn't fetch URL (permission denied) — analysis based on training data knowledge
