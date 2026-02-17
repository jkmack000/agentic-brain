# INDEX-MASTER
<!-- type: INDEX -->
<!-- updated: 2026-02-17 -->
<!-- total-files: 48 (33 in INDEX-MASTER + 15 in INDEX-claude-code) -->
<!-- Load this file at the start of every Claude Code session. -->

## How to Use This Index
1. Check for `SESSION-HANDOFF.md` first — if it exists, the previous session left unfinished work or undeposited knowledge.
2. Scan entries below to find what you need. Each summary should tell you whether to open the file or skip it.
3. If the project grows past ~75 files, entries here will point to sub-indexes in `indexes/` instead of individual files.
4. Use `brain.py` for keyword search OUTSIDE context when possible.
5. **Before ending any session**, write `SESSION-HANDOFF.md` to capture where you left off.

## Fat Index Entry Rules
Every entry MUST answer: **"Do I need to open this file?"**
1. **What** the file does/contains (one sentence)
2. **Key decisions** made inside it
3. **Interface/contract** — inputs and outputs
4. **Open issues** — so the LLM doesn't chase a file expecting answers it doesn't have

---

## Sub-Indexes

### claude-code (Sub-Index)
- **File:** indexes/INDEX-claude-code.md
- **Members:** 15 files (LEARN-004, 005, 006, 007, 008, 009, 010, 013, 014, 015, 016, 017, 018, 019, LOG-003)
- **Summary:** Claude Code internals — memory, skills, hooks, subagents, MCP, agent SDK, plugins, costs, workflows, architecture, brain integration. Load the sub-index when working on Claude Code integration tasks.
- **Squeeze point:** Active — 15 files with overlapping summaries, largest cluster (31% of brain)

---

## SPEC Files

### SPEC-000
- **Type:** SPEC
- **File:** specs/SPEC-000_project-brain-architecture.md
- **Tags:** architecture, overview, memory-system, fat-index, master-spec
- **Links:** _(foundational — linked by everything)_
- **Backlinks:** SPEC-001, SPEC-003, LEARN-001, LEARN-002, LEARN-003, LEARN-004, LEARN-005, LEARN-006, LEARN-007, LEARN-008, LEARN-009, LEARN-010, LEARN-011, LEARN-012, LEARN-013, LEARN-014, LEARN-015, LEARN-016, LEARN-017, LEARN-018, LEARN-019, LEARN-020, LEARN-021, LEARN-022, LEARN-023, LEARN-024, LEARN-025, LEARN-030, LEARN-031, LEARN-032, LEARN-033, LEARN-034, LOG-001, LOG-002, LOG-003 _(35 inbound — foundational hub)_
- **Summary:** Defines the entire Project Brain LLM memory system. Covers fat indexing methodology, file type system (SPEC/CODE/RULE/LEARN/LOG/RESET), directory structure, session workflows (search → reset → work), brain-search.py CLI spec, and the phase plan. First application target is a multi-timeframe Donchian trading bot. This is the root document — load it to understand how the memory system works.
- **Key decisions:** Fat index over thin index; standalone CLI over Obsidian plugin; search/work session split; typed file system with 6 types; hierarchical index navigation for scale.
- **Interface:** N/A (architecture spec, not code)
- **Known issues:** None open

### SPEC-001
- **Type:** SPEC
- **File:** specs/SPEC-001_prover-multi-brain-architecture.md
- **Tags:** prover, multi-brain, orchestrator, architecture, git-worktrees, sub-agents, coordination, backtesting
- **Links:** SPEC-000, LEARN-024, LEARN-025, LEARN-026, LEARN-027, LEARN-028, LEARN-029, LEARN-031, LEARN-009, LEARN-011, LEARN-015
- **Backlinks:** SPEC-002, LEARN-025, LEARN-026, LEARN-027, LEARN-028, LEARN-029
- **Summary:** Definitive architecture for Prover — the multi-brain backtesting system. Incorporates findings from LEARN-025 through LEARN-031. Defines 5 brains with roles. **Each agent = own project + own brain** (not brains within a shared project — token-efficient, each agent loads only its own brain). Three coordination options (worktrees/sub-agents/agent-teams) with recommended progression (B→A). CONTEXT-PACK v2 and RESULT v2 inter-brain protocol with YAML frontmatter, token budgets (~750/~1500 tokens), capability advertisement headers. Two-phase backtesting pipeline: VectorBT screening → Freqtrade validation → CPCV robust validation (PBO < 0.5 hard gate). Freqtrade IStrategy as AI-friendly strategy abstraction. Git worktree layout: bare repo with peer worktrees, `agent/<brain>/<task-id>` branch naming, `--no-ff` merges, orchestrator-only brain writes. Fan-out/fan-in orchestration with reducer merge, maker-checker quality gates, circuit breakers (3 failures → degrade). Six Prover guard rails as RULE files (max budget, PBO gate, thesis-before-search, fixed validation, convergence caps, narrative check). Coder brain design informed by Context7 (two-tool resolution, token-budgeted reads). Scaling thresholds from 50 to 1000+ files with consolidation cadence.
- **Key decisions:** Option B first, evolve to A; orchestrator-only brain writes; YAML+markdown for inter-brain protocol; VectorBT+Freqtrade+CPCV stack; PBO < 0.5 hard gate; economic thesis required before parameter search; centralized INDEX-MASTER (Gap 5 resolved); code-level orchestration + LLM flexibility in specialists.
- **Interface:** Defines CONTEXT-PACK v2 (orchestrator→specialist, ~750 tokens) and RESULT v2 (specialist→orchestrator, ~1500 tokens) message formats with YAML frontmatter.
- **Known issues:** Five open questions: frontend stack, Prover scope, data freshness, strategy versioning, inter-agent-project coordination. Agent teams experimental (7x cost). Subagents can't recurse. Freqtrade crypto-focused. Claude Code worktree support is feature request #24850.

### SPEC-003
- **Type:** SPEC
- **File:** specs/SPEC-003_quorum-capable-brain-implementation-plan.md
- **Tags:** quorum-sensing, implementation, INDEX-MASTER, brain-deposit, brain-status, backlinks, tensions, open-questions, clusters
- **Links:** LEARN-032, SPEC-000, LEARN-031, LEARN-003
- **Backlinks:** LEARN-032, LEARN-033, LEARN-034
- **Summary:** Prescriptive implementation plan for the 7-rule quorum sensing framework (LEARN-032). Four priority tiers — **ALL COMPLETE**. P0: Open Questions, Tensions, Backlinks. P1: deposit enforces min 3 links + open questions, status reports quiet files + clusters. P2: consolidation guide (maintenance vs synthesis modes), vitality scoring (inbound×3+outbound×1+tags×0.5), retirement workflow with archive/, CLUSTERS section (8 clusters). P3: first sub-index created (claude-code, 15 files), sub-index format spec, INDEX-MASTER restructured.
- **Key decisions:** P0→P3 ordering; backlinks as fat index field; 3 tension states; sub-index by squeeze point not count; topological vitality (no recency); RULEs exempt from low-vitality; archive/ not git-delete; CLUSTERS auto-generated by /brain-status; vitality < 2.0 review, < 1.0 retirement.
- **Interface:** INDEX-MASTER gains 4 sections (Sub-Indexes, Open Questions, Tensions, Clusters) + Backlinks field per entry. /brain-deposit gains link minimum + open questions prompt. /brain-status gains cluster + quiet-file + vitality + retirement candidate reporting.
- **Known issues:** All three original open questions resolved. Vitality formula may need threshold adjustment — tag component provides high floor (see P2.2 observation).

### SPEC-002
- **Type:** SPEC
- **File:** specs/SPEC-002_coder-brain-architecture.md
- **Tags:** coder-brain, prover, coding-agent, python, freqtrade, ccxt, context7, code-generation, testing, validation, guardrails
- **Links:** SPEC-001, LEARN-025, LEARN-028
- **Backlinks:** _(none)_
- **Summary:** Architecture for the Coder brain — a Python coding agent that receives designs from Architect/Planner agents and produces working, tested code for the trading infrastructure stack (Freqtrade, CCXT, ta-lib, VectorBT). Defines three-tier knowledge hierarchy (brain files → Context7 MCP → GitHub), 11 knowledge sources to ingest with priorities, full brain file structure (7 LEARNs, 5 CODEs, 4 RULEs seed files). Specifies input/output via CONTEXT-PACK/RESULT v2 formats. Write pipeline: brain search → Context7 query → few-shot → SCoT reasoning → template-fill (strategies) or full generation (other code). Test pipeline: unit + integration + property tests with pre-built fixtures. Validation pipeline: AST parse → import whitelist → pytest/dry-run, max 3 iteration rounds. Security: strict import whitelist for strategies (no network, filesystem, exec), relaxed for data pipelines. Three-phase ingestion plan: seed (Freqtrade, CCXT, ta-lib) → expand (VectorBT, Optuna, pytest) → accumulate (error patterns, validated snippets).
- **Key decisions:** Knowledge-first over guess-and-check; template-fill for IStrategy, full gen for non-strategy; whitelist-never-blacklist for imports; 30s timeout + 512MB memory limit; three-tier knowledge hierarchy; brain files as first source of truth over Context7.
- **Interface:** Receives CONTEXT-PACK (task_type: implement|test|fix|refactor, plan_ref from Architect/Planner). Returns RESULT (files written, validation evidence, discoveries).
- **Known issues:** 7 open questions (Architect/Planner communication, CCXT async/sync, short support, multi-timeframe, VectorBT template, GitHub ingestion method, CCXT exchange scope). Freqtrade dry-run requires installation. ta-lib problematic on Windows. VectorBT validation not yet designed.

---

## CODE Files
_None yet._

---

## RULE Files

### RULE-001
- **Type:** RULE
- **File:** rules/RULE-001_hooks-configuration-patterns.md
- **Tags:** tool-pattern, hooks, configuration, settings-json, windows, matcher, stop-hook
- **Links:** LEARN-008, LEARN-019
- **Backlinks:** RULE-004
- **Summary:** 11 concrete patterns for writing Claude Code hooks correctly. Covers: matcher must be string regex (not object), matcher-based format required (2.1.42+), Stop hooks must be command-type (prompt-type unreliable), `stop_hook_active` guard prevents infinite loops, prompt-type uses `ok`/`reason` while command-type uses `decision`, async hooks can't block, hooks snapshot at startup (restart to test), Windows path normalization with `chr(92)`, SessionStart stdout injection. Every "never" pattern was tested and confirmed broken.
- **Known issues:** PreCompact and SessionEnd hooks not yet tested in production.

### RULE-002
- **Type:** RULE
- **File:** rules/RULE-002_context-and-session-management.md
- **Tags:** tool-pattern, context-window, compaction, sessions, subagents, clear, plan-mode
- **Links:** LEARN-005, LEARN-010, LEARN-018
- **Backlinks:** _(none)_
- **Summary:** 9 patterns for protecting the context window and managing sessions. Key rules: externalize critical state before compaction hits, use subagents for investigation (keeps main context clean), skills save context vs always-on CLAUDE.md, `/clear` after 2 failed corrections (never 3), "ultrathink" is not a keyword (use `CLAUDE_CODE_EFFORT_LEVEL`), Plan Mode for read-only analysis, don't resume sessions in two terminals (use `--fork-session`), session permissions not restored on `--continue`, `--output-format json` for cost tracking.
- **Known issues:** Optimal compaction threshold for brain sessions still under evaluation.

### RULE-003
- **Type:** RULE
- **File:** rules/RULE-003_skills-and-claude-md-patterns.md
- **Tags:** tool-pattern, skills, SKILL-md, CLAUDE-md, configuration, visibility, context-budget
- **Links:** LEARN-005, LEARN-007, LEARN-018, LEARN-019
- **Backlinks:** _(none)_
- **Summary:** 6 patterns for skills and CLAUDE.md configuration. Key rules: `disable-model-invocation: true` makes skills completely invisible to Claude (not just user-only), skills in spaced paths fail CLI resolution (copy to `~/.claude/skills/`), bloated CLAUDE.md causes silent rule-ignoring (prune ruthlessly, move to skills/hooks), `@` references auto-load CLAUDE.md from target directory, 2% context budget for all skill descriptions combined, supporting files pattern for skills over 500 lines.
- **Known issues:** Optimal CLAUDE.md size threshold for brain projects needs measurement.

### RULE-004
- **Type:** RULE
- **File:** rules/RULE-004_hooks-safe-modification-workflow.md
- **Tags:** tool-pattern, hooks, settings-json, backup, rollback, safety
- **Links:** RULE-001, LEARN-008, LEARN-019
- **Backlinks:** _(none)_
- **Summary:** Workflow for safely modifying hooks: always `cp settings.local.json settings.local.json.backup` before changes, restart session, test that hooks still fire, rollback from backup if broken. Motivated by silent-disable failure mode where one bad field kills ALL hooks with no error message. Includes recovery steps and when to overwrite the backup.
- **Known issues:** Automating backup as a hook is chicken-and-egg — the backup hook itself could break.

### RULE-005
- **Type:** RULE
- **File:** rules/RULE-005_user-prime-directive-and-working-style.md
- **Tags:** user-preference, workflow, prioritization, scope-discipline, session-management
- **Links:** RULE-002, LEARN-034
- **Backlinks:** _(none)_
- **Summary:** User's prime directive: **organized, trackable, provable work > token efficiency.** When goals conflict, always choose committed artifacts over token savings. Lane discipline: user is multi-directional — enforce one-task-at-a-time, finish and commit before starting next, name lane changes explicitly, deposit tangents rather than pursuing them. Every session should produce at least one commit.
- **Key decisions:** Organized/trackable/provable > token efficiency. Smaller committed increments > ambitious multi-file changes.
- **Interface:** N/A (behavioral rule)
- **Known issues:** None.

---

## LEARN Files

### LEARN-001
- **Type:** LEARN
- **File:** learnings/LEARN-001_semantic-compression-context-extension.md
- **Tags:** context-window, compression, semantic-search, ingestion, supermemory, architecture
- **Links:** SPEC-000
- **Backlinks:** LEARN-002, LEARN-003, LEARN-004, LEARN-020
- **Summary:** Documents semantic compression (6-stage pipeline: segmentation → MiniLM embedding → spectral clustering → BART summarization → reassembly → injection) achieving ~6:1 compression at 90%+ retrieval accuracy. Also covers Supermemory's Infinite Chat (vector-scored conversation chunking). Key finding: compression is complementary to fat indexing, not a replacement — compression stuffs more in the window, fat indexing avoids loading at all. Identified as candidate architecture for automating `brain ingest` and as the paid-tier AI summarization feature from SPEC-000.
- **Known issues:** None open

### LEARN-002
- **Type:** LEARN
- **File:** learnings/LEARN-002_competitive-landscape-memory-indexing-systems.md
- **Tags:** competitive-analysis, memory-systems, indexing, MCP, RAPTOR, GraphRAG, Letta, Mem0, context-engineering
- **Links:** SPEC-000, LEARN-001, LOG-001
- **Backlinks:** LEARN-004, LEARN-011, LEARN-020, LEARN-021, LEARN-022, LEARN-023, LEARN-024, LEARN-026, LEARN-028, LEARN-031, LEARN-032
- **Summary:** Feb 2026 survey of LLM memory/indexing systems. Key finding: Letta's Context Repositories independently converged on our architecture (git-backed, file-based, progressive disclosure) — strong validation. Our 44:1 compression beats automated approaches (6-20x). Top 3 actionable improvements: (1) **MCP server wrapper for brain.py** — biggest gap, entire ecosystem converging on MCP; (2) **Formalize consolidation as ADD/UPDATE/DELETE/NOOP** — from Mem0; (3) **Git-commit every deposit** — from Letta. Also covers RAPTOR (tree-of-summaries), GraphRAG, Zep (temporal provenance), ACE (context collapse prevention), and "lost in the middle" research (critical info at top/bottom of context). Brain Hub concept (LOG-001) validated by MemOS and OpenMemory market demand.
- **Key decisions:** MCP wrapper is #1 priority for brain system after Donchian bot MVP. Top 10 improvements ranked by impact/effort.
- **Interface:** N/A (learning, not code)
- **Known issues:** All improvements deferred until Donchian bot proves core concept.

### LEARN-003
- **Type:** LEARN
- **File:** learnings/LEARN-003_qualitative-research-methods-for-knowledge-systems.md
- **Tags:** qualitative-research, triangulation, progressive-focusing, concept-mapping, methodology, Stake
- **Links:** SPEC-000, LEARN-001, LEARN-002
- **Backlinks:** SPEC-003, LEARN-031, LEARN-032
- **Summary:** Transfers 6 concepts from Stake's qualitative research methodology to brain system design: (1) **Triangulation** — multi-source confirmation, formalize confidence levels (unconfirmed/corroborated/validated) in fat index entries; (2) **Progressive focusing** — start broad, narrow to emerging issues across sessions, don't lock structure too early; (3) **Concept mapping** — spatial representation of how knowledge relates, addresses cross-referencing gaps; (4) **Member checking** — present findings for user review before committing; (5) **Progressive recoding** — file types may need reclassification as projects mature; (6) **Data storage tips** — our SESSION-HANDOFF, fat index, and "Known issues" fields already implement Stake's recommendations. Three actionable improvements: add confidence indicator to index entries, consider FOCUS file type, concept map overlay for INDEX-MASTER.
- **Key decisions:** None yet — three improvements identified but deferred.
- **Interface:** N/A (learning, not code)
- **Known issues:** Academic framework, not directly about LLM memory — transferability needs validation through practice.

<!-- LEARN-004 through LEARN-010: Moved to indexes/INDEX-claude-code.md (claude-code sub-index) -->

### LEARN-011
- **Type:** LEARN
- **File:** learnings/LEARN-011_fat-index-convergence-validation.md
- **Tags:** validation, architecture, fat-index, convergence, auto-memory, subagents, context-repositories
- **Links:** SPEC-000, LEARN-002, LEARN-006, LEARN-009
- **Backlinks:** LEARN-024, LEARN-032, SPEC-001, LEARN-033
- **Summary:** Cross-cutting finding: three independently-designed systems converge on our fat-index architecture. (1) Claude Code auto memory (200-line MEMORY.md index + topic files), (2) subagent persistent memory (same pattern, three scopes), (3) Letta Context Repositories (git-backed, file-based, progressive disclosure). All use the same core principle: a summary layer that answers "do I need to open this?" without paying token cost. Strong external validation of brain system's core design. Implications for interoperability, marketing positioning, and architecture confidence.
- **Key decisions:** None — strategic validation finding. Carry forward into product positioning.
- **Interface:** N/A (learning, not code)
- **Known issues:** None open

### LEARN-012
- **Type:** LEARN
- **File:** learnings/LEARN-012_brain-operational-drift-and-sync.md
- **Tags:** operational, drift, sync, templates, INIT-md, multi-brain, maintenance
- **Links:** SPEC-000, LOG-002
- **Backlinks:** LEARN-031
- **Summary:** Documents two operational edge cases: (1) **Template drift** — brain.py init generates INIT.md from a hardcoded template that has fallen behind the manually-evolved INIT.md (now includes timeline rules, dedup rules, shorthand commands, handoff triggers). New brains start with stale operational knowledge. (2) **Multi-brain sync** — when multiple brains exist, INIT.md improvements in one don't propagate to others (e.g., Donchian brain missing timeline rule). Two fix approaches identified: single-source versioned template with `brain sync`, or split INIT.md into project-specific + shared operational rules.
- **Key decisions:** None yet — flagged for resolution. Low priority until third brain created.
- **Interface:** N/A (learning, not code)
- **Known issues:** Both problems will worsen as more brains are created. Needs resolution before any public release.

<!-- LEARN-013 through LEARN-019: Moved to indexes/INDEX-claude-code.md (claude-code sub-index) -->

### LEARN-021
- **Type:** LEARN
- **File:** learnings/LEARN-021_langchain-langgraph-architecture-memory-retrieval.md
- **Tags:** langchain, langgraph, deep-agents, memory, persistence, retrieval, RAG, middleware, competitive-analysis, architecture-patterns
- **Links:** LEARN-002, LEARN-020, SPEC-000
- **Backlinks:** LEARN-023, LEARN-026, LEARN-030
- **Summary:** Full architectural analysis of LangChain/LangGraph ecosystem (Feb 2026 reorganization). Three layered products: DeepAgents (auto-compression, virtual filesystem) → LangChain Agents (middleware system) → LangGraph (stateful graphs). Memory adopts CoALA taxonomy: semantic (LEARN/SPEC), episodic (LOG), procedural (RULE). Store uses namespace tuples + key-value + optional semantic search — maps to our directory structure. Six middleware hooks including novel transient vs persistent context distinction. Priority-ranked retrieval improvements: BM25 (#1, low effort), content hashing dedup (#2), multi-query (#3), self-query filtering (#4), hybrid BM25+vector (#5). ParentDocumentRetriever independently converges on fat index pattern. LangChain Indexing API with content hashing solves our dedup problem systematically. DeepAgents (new, post-May 2025) most directly competitive to brain system — virtual filesystem + auto-compression for autonomous agents.
- **Key decisions:** None — competitive intelligence. BM25 search identified as #1 low-effort improvement. Content hashing as #2.
- **Interface:** N/A (learning, not code)
- **Known issues:** DeepAgents docs couldn't be fully fetched (new section). LangChain evolves rapidly — analysis is point-in-time Feb 2026.

### LEARN-020
- **Type:** LEARN
- **File:** learnings/LEARN-020_mem0-dspy-llm-driven-memory-crud.md
- **Tags:** mem0, dspy, react-agent, memory-crud, qdrant, vector-search, competitive-analysis, architecture-patterns
- **Links:** LEARN-002, LEARN-001, SPEC-000
- **Backlinks:** LEARN-021, LEARN-022
- **Summary:** Full architecture analysis of avbiswas/mem0-dspy — a from-scratch Mem0 reimplementation (~300 lines) using DSPy ReAct agents + Qdrant. Core pattern: two LLM agents in sequence — Agent 1 (ResponseGenerator) answers user with optional memory search + outputs `save_memory` boolean; Agent 2 (UpdateMemory) sees conversation + existing memories and decides ADD/UPDATE/DELETE/NOOP via tool calls. Uses 64-dim OpenAI embeddings (24x smaller than default), DOT product, category faceting via Qdrant. Includes detailed comparison table with Project Brain (vector vs fat-index, LLM-driven vs rule-based CRUD, lossy vs lossless compression). Found 4 bugs in the repo. Five brain-relevant takeaways: LLM-driven CRUD as automation path for `/brain-deposit`, category faceting maps to our type system, `save_memory` boolean pattern for PostToolUse hook, 64-dim embeddings viable for small stores, DSPy Signatures as agent contract pattern.
- **Key decisions:** None — competitive intelligence. LLM-driven dedup identified as candidate enhancement for `/brain-deposit`.
- **Interface:** N/A (learning, not code)
- **Known issues:** Analysis is point-in-time (Feb 2026). Repo has 4 bugs including broken delete tool.

### LEARN-022
- **Type:** LEARN
- **File:** learnings/LEARN-022_dspy-optimizers-teleprompters.md
- **Tags:** dspy, optimizers, teleprompters, prompt-tuning, bootstrapping, compilation, bayesian-optimization, few-shot, fine-tuning, MIPROv2
- **Links:** LEARN-020, SPEC-000, LEARN-002
- **Backlinks:** _(none)_
- **Summary:** Complete technical reference for DSPy's optimizer system (formerly "teleprompters", renamed DSPy 2.0 mid-2024). Covers all 15 optimizers across 5 categories: few-shot (LabeledFewShot, BootstrapFewShot, RandomSearch, Optuna, KNNFewShot), instruction (COPRO, MIPROv2, SIMBA, GEPA, InferRules), weight (BootstrapFinetune, GRPO), combined (BetterTogether), and utility (Ensemble, AvatarOptimizer). Deep dives on: BootstrapFewShot mechanics (teacher runs → metric filters → traces become demos), MIPROv2 three-stage process (bootstrap → propose instructions → Bayesian optimization via Optuna TPE), SIMBA self-reflective rules, GEPA evolutionary search, InferRules rule induction. Covers metrics system (`trace` parameter for strict-during-optimization), assertions (`dspy.Assert`/`Suggest`), teacher-student distillation, save/load (JSON format), and compilation model. Practical guidance: when to use which optimizer, min data sizes, cost estimates, 9 common pitfalls. Seven brain-relevant takeaways including: SIMBA rules parallel brain RULE files, InferRules could mine LOGs for rules, teacher-student distillation for brain search optimization.
- **Key decisions:** None — ingested knowledge. Seven improvement ideas identified but all deferred.
- **Interface:** N/A (learning, not code)
- **Known issues:** DSPy API evolves rapidly — analysis is point-in-time Feb 2026. SIMBA/GEPA/InferRules/GRPO are newer and less battle-tested. BetterTogether requires experimental flag.

### LEARN-023
- **Type:** LEARN
- **File:** learnings/LEARN-023_qmd-local-hybrid-search-engine.md
- **Tags:** qmd, search, BM25, vector-search, reranking, hybrid-search, MCP, local-first, competitive-analysis, sqlite, node-llama-cpp
- **Links:** LEARN-002, LEARN-021, LEARN-013, SPEC-000
- **Backlinks:** LEARN-028, LEARN-030
- **Summary:** Full architecture analysis of QMD (tobi/qmd) — local-first CLI hybrid search engine for markdown by Shopify founder Tobi Lütke. MIT, v0.9.9, 8K+ stars. Three-layer pipeline: BM25 (FTS5) + vector (300M embedding-gemma) + LLM reranker (0.6B qwen3), all on-device via node-llama-cpp GGUF models (~2.1GB total). Novel patterns not in existing brain files: (1) typed query expansion (lex/vec/hyde variants via grammar-constrained decoding), (2) position-aware score blending preventing reranker from destroying high-confidence retrieval results, (3) smart signal detection skipping expansion when BM25 is confident, (4) two-table content-addressable storage (immutable content by SHA-256, mutable documents as filesystem mapping), (5) dynamic MCP instruction injection (collection metadata in system prompt). Ships MCP server (stdio + HTTP daemon). Confirms LEARN-021 patterns: BM25 (#1), content hashing (#2), multi-query (#3), hybrid+RRF (#5). "96% token savings" claim flagged as **unverified** — single Twitter anecdote, not apples-to-apples comparison. QMD is usable as a complement to brain.py (collection add over project-brain/).
- **Key decisions:** None — competitive intelligence. QMD identified as both competitor and potential search backend complement.
- **Interface:** N/A (learning, not code)
- **Known issues:** Pre-1.0, sqlite-vec alpha, 96% savings unverified, evolving rapidly (74 PRs/month).

### LEARN-025
- **Type:** LEARN
- **File:** learnings/LEARN-025_backtesting-engine-architecture-research.md
- **Tags:** backtesting, architecture, event-driven, vectorized, data-pipeline, strategy-abstraction, optimization, overfitting, prover
- **Links:** SPEC-001, SPEC-000
- **Backlinks:** SPEC-001, SPEC-002
- **Summary:** Comprehensive research synthesis on production backtesting engine architectures for Prover. Covers 7 areas: (1) Core architecture — event-driven vs vectorized, streaming vs batch, hybrid two-phase pipeline (vectorized screening → event-driven validation) as industry best practice; NautilusTrader Rust-core actor model as performance gold standard. (2) Data pipeline — raw→clean→resample→strategy-ready flow, Parquet as industry-standard format, multi-timeframe alignment rules (higher TF values only after period closes), partition strategies. (3) Strategy abstraction — 4 patterns compared: class inheritance (Backtrader/Zipline), DataFrame methods (Freqtrade, recommended for LLM generation), vectorized composition (VectorBT), handler interfaces (LEAN). (4) Result storage — Parquet for data + JSON for metadata, 12 key performance metrics, directory structure pattern. (5) Parameter optimization — grid/random/Bayesian(Optuna)/walk-forward/CPCV compared; 3-phase pipeline recommended (vectorized sweep → Bayesian refinement → CPCV validation with PBO < 0.5 gate). (6) Framework reference — 6 frameworks compared (Backtrader, Zipline, VectorBT, LEAN, Freqtrade, NautilusTrader) with architecture details. (7) Pitfalls — look-ahead bias, survivorship bias, overfitting, transaction costs, data snooping, plus 4 Prover-specific pitfalls (infinite search, narrative fabrication, compounding bias, meta-overfitting). Recommends VectorBT (Phase 1) + Freqtrade (Phase 2) stack. Full data flow diagram through Prover brains.
- **Key decisions:** Freqtrade IStrategy recommended for AI-generated strategies (DataFrame methods are LLM-friendly); VectorBT for screening, Freqtrade for validation; CPCV with PBO < 0.5 as hard gate; validation methodology fixed in RULE file (not modifiable by AI agents); economic thesis required before parameter search.
- **Interface:** N/A (learning, not code)
- **Known issues:** NautilusTrader not hands-on tested; VectorBT PRO not evaluated; CPCV Python library assessment needed; Freqtrade crypto-focused (equity/futures may need different framework); 5 open design questions for Prover (execution service, data freshness, strategy versioning, multi-asset, MVP timeframe).

### LEARN-026
- **Type:** LEARN
- **File:** learnings/LEARN-026_inter-agent-communication-patterns.md
- **Tags:** multi-agent, IPC, communication, context-passing, message-formats, serialization, shared-memory, token-efficiency, A2A, MCP, AutoGen, CrewAI, LangGraph, Claude-Code, OpenAI-Swarm, blackboard, stigmergy
- **Links:** SPEC-001, LEARN-009, LEARN-015, LEARN-024, LEARN-002, LEARN-021
- **Backlinks:** LEARN-027
- **Summary:** Comprehensive research synthesis on inter-process communication patterns for LLM/AI multi-agent systems. Covers 9 areas: (1) Context passing — full dump vs summary/compression vs delta/incremental, with compression ratios (10-20x Anthropic subagents, 70% Claude Code reduction, 73% protocol compression, 26-54% Acon). (2) Message formats — Google A2A (JSON-RPC 2.0, Agent Cards, typed Parts), AutoGen (GroupChatMessage, HandoffMessage with context list), CrewAI (Pydantic output schemas), LangGraph (TypedDict state + reducers), OpenAI Swarm (stateless, context vars). (3) Serialization — markdown (LLM-native), JSON with schema validation, YAML frontmatter + markdown body as optimal hybrid. (4) Shared memory — blackboard pattern (maps to INDEX-MASTER), stigmergy (maps to file deposits), file-based (our architecture), database-backed (Mem0/Zep), in-memory (LangGraph). (5) Token-efficient techniques — context filtering (highest impact), protocol compression, structured output constraints, summary distillation, tiered memory. (6) Real implementations — Anthropic research system (90.2% improvement, 15x cost, Opus+Sonnet), Claude Code subagents (70% reduction, 20K overhead), AutoGen/CrewAI/LangGraph/Swarm/tick-md details. (7) MCP vs A2A protocol landscape. (8) Improved CONTEXT-PACK v2 and RESULT v2 templates with YAML frontmatter, token budgets, and capability advertisement headers. (9) Eight key takeaways including: context isolation beats sharing, 1-2K token returns are standard, markdown+git is legitimate, Agent Card pattern should be adopted.
- **Key decisions:** Recommends YAML frontmatter + markdown body for CONTEXT-PACK/RESULT v2 formats; capability advertisement headers in INDEX-MASTER for automated routing; LangGraph-style reducer pattern for merging concurrent specialist results; token budget envelope (~750 tokens CONTEXT-PACK, ~1100-1500 tokens RESULT).
- **Interface:** N/A (learning, not code). Defines proposed v2 message templates for SPEC-001 inter-brain communication.
- **Known issues:** A2A protocol still evolving (v0.3); MCP agent-to-agent extensions on 2026 roadmap only; Acon/SDE are academic; 15x token overhead is Anthropic's number for research tasks, may differ for our use case.

### LEARN-027
- **Type:** LEARN
- **File:** learnings/LEARN-027_multi-agent-orchestration-patterns.md
- **Tags:** multi-agent, orchestration, choreography, fan-out, fan-in, task-decomposition, aggregation, error-handling, context-management, LangGraph, CrewAI, AutoGen, OpenAI, prover
- **Links:** SPEC-001, LEARN-009, LEARN-015, LEARN-026, LEARN-024
- **Backlinks:** _(none)_
- **Summary:** Research synthesis of multi-agent orchestration patterns from 6 production frameworks (LangGraph, CrewAI, AutoGen, OpenAI Agents SDK, Microsoft Agent Framework, Google ADK). Covers 8 areas: (1) Fan-out/fan-in — LangGraph superstep semantics (atomic failure, reducers), 137x speedup benchmark, Microsoft anti-pattern (no shared mutable state). (2) Choreography vs orchestration — hybrid consensus as industry best practice ("orchestrate via code, delegate to LLM"), framework positioning table. (3) Task decomposition — 4 strategies: role-based (CrewAI), graph-based (LangGraph), dynamic task ledger (Microsoft Magentic), conversation-based (AutoGen); Microsoft complexity hierarchy (direct call → single agent → multi-agent). (4) Result aggregation — 5 strategies (voting, weighted, LLM synthesis, concat+dedup, conflict agent); maker-checker with iteration caps; **41-86.7% failure rate** for unstructured coordination. (5) Framework details — OpenAI Agents SDK (manager+handoff), LangGraph (state+reducers+checkpoints), CrewAI (Crews+Flows), AutoGen (GroupChat+speaker selection), Microsoft (5 declarative patterns), Google ADK. (6) Error handling — 7 patterns: retry+backoff, circuit breakers (Salesforce 40%/60s), failure classification, graceful degradation, output validation, timeouts, checkpointing. (7) Context management — 6 strategies: context isolation (Manus, highest impact), observation masking (JetBrains, as good as LLM summarization), compaction, blackboard (=INDEX-MASTER), system prompt swapping, hierarchical. (8) Prover-specific takeaways: code orchestration + LLM reasoning, fan-out with reducer merge, circuit breakers, observation masking over summarization, context isolation as #1 principle.
- **Key decisions:** Recommends code-level orchestration for Prover workflow graph with LLM flexibility within specialists; fan-out with append reducers; maker-checker with iteration caps; circuit breakers for specialist failures; observation masking preferred over LLM summarization; complexity hierarchy (start single-agent, escalate to multi-brain only when needed).
- **Interface:** N/A (learning, not code)
- **Known issues:** Framework APIs evolve rapidly (point-in-time Feb 2026); 41-86.7% failure statistic methodology not deeply evaluated; observation masking is one study; no hands-on benchmarking.

### LEARN-028
- **Type:** LEARN
- **File:** learnings/LEARN-028_context7-architecture-analysis.md
- **Tags:** context7, MCP, library-docs, architecture, search, reranking, coder-brain, upstash, vector-search
- **Links:** LEARN-013, LEARN-002, LEARN-023, SPEC-001
- **Backlinks:** SPEC-002
- **Summary:** Architecture analysis of Context7 (Upstash) — MCP server providing up-to-date library docs to AI coding assistants. 33K+ libraries indexed on 10-15 day rolling crawl. Split architecture: thin open-source MCP client (2 tools, ~2 files of logic) + thick proprietary backend (crawling, parsing, LLM enrichment, Upstash Vector multi-model embeddings, c7score 5-metric reranker, Redis cache). Two MCP tools: `resolve-library-id` (maps to fat-index search) and `get-library-docs` (maps to brain file read, with token budget parameter). 5-stage data pipeline: parse → enrich (LLM adds explanations) → vectorize (adaptive models by content complexity) → rerank (c7score) → cache. Recent architecture update achieved 65% token reduction and 38% latency reduction by moving filtering from LLM to backend. Seven patterns transferable to Coder brain: two-tool resolution, token-budgeted responses, query-aware reranking, enrichment at index time (=fat index), backend filtering > LLM filtering, adaptive embeddings, rolling freshness. **Context7 and Coder brain are complementary**: Context7 answers "how does this library work?" while brain answers "how does OUR project use it and why?" Ideal: both as MCP servers to same AI assistant.
- **Key decisions:** Context7 validates brain MCP server design (two-tool pattern, token budgets, pre-enrichment). Recommended integration: Context7 for external library docs + Coder brain for project-specific knowledge. Six concrete next steps for brain MCP server informed by Context7 patterns.
- **Interface:** N/A (learning, not code)
- **Known issues:** Backend is proprietary (can't inspect internals); c7score uses Vertex AI/Gemini (vendor-locked); "96% token savings" claim unverified; pre-1.0 MCP server.

### LEARN-024
- **Type:** LEARN
- **File:** learnings/LEARN-024_context-repositories-and-context-engineering-patterns.md
- **Tags:** context-repositories, context-engineering, letta, memgpt, anthropic, memory-architecture, git-worktrees, progressive-disclosure, compaction, sub-agents
- **Links:** LEARN-002, LEARN-004, LEARN-005, LEARN-011, SPEC-000
- **Backlinks:** LEARN-026, LEARN-027, LEARN-029, SPEC-001
- **Summary:** Deep dive into Letta's Context Repositories blog post + embedded links (Anthropic context engineering framework, MemGPT paper, Letta Code docs/repo). Extends LEARN-002/011 with 17 specific new patterns not previously deposited. Letta implementation details: git worktrees for multi-agent isolation, background reflection (auto-deposit), memory defragmentation as first-class operation, `system/` always-loaded directory, YAML frontmatter per file, concurrent subagent initialization. Anthropic framework details: attention budget as n² cost, context rot as gradient (not cliff), compaction art (recall vs precision), sub-agent 10-20x compression ratio (1-2K token returns), Goldilocks zone for system prompts, hybrid pre-load + JIT approach. MemGPT: interrupt-based control flow, virtual context illusion. Includes full comparison table (our brain vs Letta vs Anthropic patterns) and 5-item gap analysis: git worktree isolation, background reflection, formalized defrag, concurrent init, per-file frontmatter.
- **Key decisions:** None — research synthesis. Five gaps identified for future work.
- **Interface:** N/A (learning, not code)
- **Known issues:** Letta Code is TypeScript (may not transfer to Python brain.py). MemGPT paper (Oct 2023) predates current Letta evolution.

### LEARN-029
- **Type:** LEARN
- **File:** learnings/LEARN-029_git-worktree-workflows-for-parallel-agents.md
- **Tags:** git, worktrees, parallel-agents, isolation, multi-brain, concurrent, prover
- **Links:** SPEC-001, LEARN-024, LEARN-018
- **Backlinks:** _(none)_
- **Summary:** Comprehensive research on git worktree workflows for parallel AI agent sessions. Covers worktree mechanics (shared objects/refs, per-worktree HEAD/index, branch exclusivity constraint), 4 real-world systems (Letta Context Repos, ccswarm, Crystal, incident.io), concurrent safety analysis (lock files, object DB safety, 6-scenario risk matrix), Claude Code integration (multi-terminal sessions, `--add-dir` flag, branch awareness, programmatic launch). Practical Prover patterns: `agent/<brain-name>/<task-id>` branch naming, standard vs bare-repo directory layouts, complete orchestrator shell script, merge strategies (`--no-ff` for audit trail, test-before-merge). Three brain file coordination strategies evaluated — recommends Option C (orchestrator-only brain writes) aligned with SPEC-001 CONTEXT-PACK/RESULT pattern. Covers Windows gotchas (long paths, file locking, antivirus), submodule incompleteness, stale worktree detection, runtime isolation limits.
- **Key decisions:** Recommends worktrees with branch-per-agent + orchestrator-only brain writes for Prover Phase 1; `--no-ff` merges for audit trail; bare-repo layout for many worktrees; automated cleanup after each session.
- **Interface:** N/A (learning, not code)
- **Known issues:** Claude Code native worktree support is an open feature request (#24850). Submodule support is incomplete. Runtime environment (ports, DBs, env vars) NOT isolated by worktrees.

### LEARN-030
- **Type:** LEARN
- **File:** learnings/LEARN-030_bm25-hybrid-search-implementation-patterns.md
- **Tags:** BM25, search, hybrid-search, vector-search, ranking, Python, brain-py, implementation, RRF, reranking, SQLite-FTS5
- **Links:** LEARN-021, LEARN-023, SPEC-000
- **Backlinks:** _(none)_
- **Summary:** Research synthesis for improving brain.py search. Covers BM25 fundamentals (scoring formula, k1/b tuning for short docs: k1=1.0, b=0.4), 6 Python library comparison (rank-bm25, bm25s, SQLite FTS5, Whoosh-Reloaded, tantivy-py, lunr.py) with decision matrix. Field boosting strategy (tags 5x, ID 4x, title 3x, summary 1x). Hybrid search: RRF implementation (k=60, complete Python code), weighted blending alternative, minimal vector stack (fastembed + sqlite-vec + FTS5). Query expansion (pseudo-relevance feedback with code, HyDE, multi-query). Reranking (FlashRank 4-80MB options). Small-corpora patterns: BM25 alone sufficient when vocabulary is shared, add vectors for cross-brain search. 3-phase roadmap: (1) improve tokenizer now (stemming, stopwords, hyphen expansion), (2) migrate to SQLite FTS5 at 50-100 files for native field boosting, (3) add hybrid search at 100+ files or MCP server.
- **Key decisions:** rank-bm25 adequate for current 37 files; SQLite FTS5 is best next step (zero deps, native field boosting, persistence); vector search premature at current scale; RRF over weighted blending for hybrid fusion.
- **Interface:** N/A (learning, not code). Contains ready-to-use Python code for RRF, PRF, tokenizer, FTS5 schema.
- **Known issues:** FTS5 k1/b hardcoded at 1.2/0.75 (not tunable). bm25s requires numpy/scipy. FlashRank reranking adds latency. All recommendations are for current scale (37 files) — reassess at 100+.

### LEARN-031
- **Type:** LEARN
- **File:** learnings/LEARN-031_file-based-knowledge-management-at-scale.md
- **Tags:** zettelkasten, obsidian, logseq, knowledge-management, scaling, consolidation, graph, MOC, atomic-notes, progressive-summarization, maintenance
- **Links:** SPEC-000, LEARN-002, LEARN-003, LEARN-012
- **Backlinks:** SPEC-001, SPEC-003, LEARN-032, LEARN-033
- **Summary:** Research synthesis of file-based knowledge management patterns for LLM memory systems. Covers Zettelkasten (5 core principles, fleeting/literature/permanent pipeline, emergence from cross-domain links, digital adaptations — 40% retrieval improvement), Obsidian (vault structure, MOCs with "mental squeeze point" trigger, Dataview metadata querying, scaling thresholds up to 40K+ notes — graph view is bottleneck, not file operations), Logseq (outliner model, block-level linking, namespaces, journal-first workflow — we correctly chose Obsidian/page model for LLM consumption). Scaling thresholds: 50-100 (fat index essential), 100-300 (first consolidation), 300-500 (sub-indexes), 500-1000 (Evernote Effect danger zone), 1000+ (automated search required). Knowledge graph patterns: link density benchmarks (2-3 minimum, 4-6 good), hub note priority maintenance, clustering for auto-organization. LLM-optimized adaptations: fat index = MOC equivalent, A-MEM NeurIPS 2025 academic validation, RAG chunking alignment (fat entries at optimal 50-150 tokens), context positioning (INDEX-MASTER early, task files last). Consolidation: Forte's 5-layer progressive summarization mapped to brain, gardening metaphors, maintenance cadence (time/event/metric triggers), merge vs split vs archive decision table. Prioritized improvements table and scaling roadmap from 37 to 1000+ files.
- **Key decisions:** Architecture validated by A-MEM (NeurIPS 2025), Letta, Claude auto memory (4th independent convergence). Sub-index creation triggered by "mental squeeze point" not arbitrary file count. Evernote Effect is biggest long-term risk — consolidation every 20-30 files is correct.
- **Interface:** N/A (learning, not code)
- **Known issues:** A-MEM is academic (not production-tested at scale). Obsidian scaling data is community-reported (not benchmarked). Progressive summarization touch-count tracking not yet implemented. File size guideline (<1000 tokens) conflicts with current LEARN files (most are 500-2000 tokens).

### LEARN-032
- **Type:** LEARN
- **File:** learnings/LEARN-032_quorum-sensing-framework-for-knowledge-management.md
- **Tags:** quorum-sensing, knowledge-management, biological-analogy, framework, indexing, contradictions, decay, consolidation, brain-architecture
- **Links:** SPEC-000, SPEC-003, LEARN-002, LEARN-003, LEARN-011, LEARN-031
- **Backlinks:** SPEC-003, LEARN-033, LEARN-034
- **Summary:** Seven rules for quorum-capable LLM knowledge management, derived from biological quorum sensing analogy. Rules: (1) every file must emit signal (fat index required), (2) maximize binding sites (min 3 links per deposit), (3) declare open questions as chemoattractant gradients, (4) deposit contradictions with 3-state tracking (OPEN/BLOCKING/RESOLVED), (5) consolidate at cluster quorum not arbitrary count, (6) topological decay not temporal (connections matter, not age — human-reviewed only), (7) index is the medium (INDEX-MASTER gains OPEN QUESTIONS, TENSIONS, CLUSTERS sections). Includes Grok comparison (convergent on signal emission + contradictions, divergent on decay — we chose topological), token overhead assessment (~10K/5% current context), sub-index workflow impact (one extra hop, transparent to skills), and safety strategy (git branches + tags, no parallel brains).
- **Key decisions:** Topological over temporal decay; 3-state tension tracking; adversarial evidence accumulation for contradictions; mental squeeze point triggers consolidation; INDEX-MASTER becomes coordination medium not just lookup table.
- **Interface:** N/A (framework, not code). Implementation plan in SPEC-003.
- **Known issues:** Framework is theoretical — not yet validated through implementation. Token overhead estimate needs verification after P0 implementation.

### LEARN-034
- **Type:** LEARN
- **File:** learnings/LEARN-034_knowledge-capture-gap-and-chat-log-review-pattern.md
- **Tags:** knowledge-capture, chat-logs, session-management, deposit-workflow, meta-insight, brain-architecture, usability
- **Links:** LEARN-032, SPEC-003, LEARN-019, SPEC-000, LEARN-010
- **Backlinks:** _(none)_
- **Summary:** Identifies a critical knowledge capture gap: at production pace, manual deposit discipline fails — insights generated in conversation evaporate unless someone remembers to deposit them. Documents three-layer solution: (1) deposit-as-you-go rule (implemented as `.claude/rules/` file, 7 triggers for immediate deposit), (2) chat log review (Claude Code stores local transcripts — recoverable knowledge source for post-session extraction), (3) automated `/brain-checkpoint` skill (not yet built — would scan conversation for undeposited knowledge before session end). Also validates stop hook fired successfully in production (caught stale handoff). Shifts brain capture model from "pull" (user remembers) to "push" (system prompts).
- **Key decisions:** Three-layer capture solution; deposit-as-you-go as Layer 1 (cheapest, immediate); chat log review as Layer 2 (recovery); /brain-checkpoint as Layer 3 (deferred).
- **Interface:** N/A (learning, not code). Layer 1 is `.claude/rules/brain-deposit-as-you-go.md`.
- **Known issues:** ~~Chat log location/format not documented~~ — **RESOLVED**: logs at `~/.claude/projects/<project>/<session>.jsonl`, JSONL format documented in file. Layer 1 may slow fast sessions. Layer 3 not designed. First measurement: ~4 items undeposited per session average (33 across 8 sessions).

### LEARN-033
- **Type:** LEARN
- **File:** learnings/LEARN-033_brain-graph-topology-first-backlink-analysis.md
- **Tags:** graph-topology, backlinks, hub-structure, quiet-files, link-density, quorum-sensing, empirical
- **Links:** LEARN-032, SPEC-003, LEARN-031, LEARN-011, SPEC-000
- **Backlinks:** _(none)_
- **Summary:** First empirical topology data from the brain's link graph after P0.3 backlink implementation. Hub-and-spoke structure: SPEC-000 (33 inbound, foundational hub), LEARN-005 (16 inbound, secondary hub), LEARN-002 (11 inbound, tertiary). 8 quiet files (0 inbound) cluster by type: 75% of RULEs are quiet (leaf-type — they consume knowledge but aren't referenced), 12.5% of LEARNs are quiet (recent research not yet consumed). Average ~3.5 forward links/file, median ~2 inbound. Largest tag cluster: `claude-code` at 14 files. Validates LEARN-032 Rule 6 (topological decay detection works). RULEs may need different quiet-file treatment since they're structurally terminal.
- **Key decisions:** None — empirical observation. RULEs flagged as potentially leaf-type by nature (not decaying). SPEC-002 flagged for link enrichment.
- **Interface:** N/A (learning, not code)
- **Known issues:** Open question: does hub structure change after consolidation? Preliminary finding: RULEs are structurally leaf-type (not decaying). `claude-code` cluster (14 files) is first sub-index candidate.

### LEARN-035
- **Type:** LEARN
- **File:** learnings/LEARN-035_freqtrade-istrategy-technical-reference.md
- **Tags:** freqtrade, IStrategy, trading, code-generation, python, callbacks, hyperopt, signals, coder-brain
- **Links:** SPEC-002, SPEC-001, LEARN-025
- **Backlinks:** LEARN-036
- **Summary:** Complete technical reference for Freqtrade's IStrategy interface — the target abstraction for AI-generated strategies. Covers: 3 required methods (populate_indicators/entry_trend/exit_trend) with exact signatures, DataFrame OHLCV columns, 15+ optional callback methods with full signatures (custom_stoploss, custom_exit, adjust_trade_position, leverage, etc.), parameter optimization interface (IntParameter/DecimalParameter/BooleanParameter/CategoricalParameter with constructor args), signal column conventions, trailing stop mechanics, ROI table format, indicator libraries (TA-Lib, technical, pandas-ta), complete minimal strategy example, and 10 code generation constraints. This is the seed knowledge for the Coder brain's planned LEARN-001 (SPEC-002 Phase 1).
- **Key decisions:** Template-fill for IStrategy (fill only populate method bodies); hyperopt parameters cannot be used in populate_indicators; always include volume > 0 guard.
- **Interface:** N/A (reference, not code). Consumed by Coder brain write pipeline.
- **Known issues:** TA-Lib problematic on Windows. Freqtrade crypto-focused. Recovered from subagent transcript — may need verification against latest Freqtrade docs.

### LEARN-036
- **Type:** LEARN
- **File:** learnings/LEARN-036_llm-code-generation-patterns-for-trading-strategies.md
- **Tags:** code-generation, LLM, trading, validation, security, sandbox, prompting, few-shot, SCoT, competitive-analysis, coder-brain
- **Links:** SPEC-002, SPEC-001, LEARN-035, LEARN-025
- **Backlinks:** _(none)_
- **Summary:** Quantitative research synthesis on LLM code generation for trading strategies. Prompting: SCoT +13.79% Pass@1, few-shot ~80% over zero-shot, prompt format varies 40%. Iteration: LLMLOOP pass@1 71%→80.85%, Self-Refine -30% errors, 3-5 iterations optimal, GPT-4o-mini 53%→75%, Gemini-flash 57%→89%. Validation: AST hallucination detection, Bandit security linting, smolagents LocalPythonExecutor (AST interpreter, best fit for strategy validation), 4-tier sandbox hierarchy (RestrictedPython < smolagents < gVisor < Firecracker). **Cross-project finding: LLM API hallucination is the consistent failure mode — every successful project required a validation layer.** NexusTrade JSON-out pattern (24K users, LLM never generates executable code). 5 open-source strategy generation projects + EMNLP 2025 paper (53.17% return on SSE50). Template-based generation recommended (eliminates structural errors, limits bugs to logic only).
- **Key decisions:** Knowledge-first beats guess-and-check (empirically validated); template-fill eliminates largest error classes; whitelist imports never blacklist; smolagents as validation model.
- **Interface:** N/A (learning, not code). Informs Coder brain write + validation pipeline (SPEC-002).
- **Known issues:** Academic benchmarks may differ from real-world. smolagents HuggingFace-specific. All framework APIs point-in-time Feb 2026.

---

## LOG Files

### LOG-001
- **Type:** LOG
- **File:** logs/LOG-001_brain-hub-shared-repository-idea.md
- **Tags:** product-direction, brain-hub, repository, crowdsourced, meta-brain, monetization
- **Links:** SPEC-000
- **Backlinks:** LEARN-002
- **Summary:** Captures the concept of "Brain Hub" — a shared public repository where users publish, browse, and pull fat-indexed knowledge files across domains. Global fat index enables discovery without downloading. Crowdsourced knowledge compounds value (one person's LEARN benefits all). Monetization: free browse/pull/push, paid for private brains, AI quality scoring, curated domain packs. Competitive moat is the data itself — millions of LLM-readable indexed knowledge entries. No competitor has this format.
- **Key decisions:** Concept captured, not yet committed to building. Revisit after local brain proven on 2-3 projects.
- **Known issues:** Needs trust/reputation system, global deduplication, privacy controls. Format stability required since it becomes an interchange format.

<!-- LOG-003: Moved to indexes/INDEX-claude-code.md (claude-code sub-index) -->

### LOG-002
- **Type:** LOG
- **File:** logs/LOG-002_project-timeline.md
- **Tags:** timeline, sessions, milestones, changelog, meta
- **Links:** SPEC-000
- **Backlinks:** LEARN-012
- **Summary:** Running chronological record of all project sessions, milestones, ingestions, and structural changes. Standard infrastructure file — every brain gets one. Contains dated entries for each session with: duration, key actions, files created/modified, decisions made, and blockers. Use to trace project evolution, estimate velocity, and orient on history. Currently covers: 2026-02-14 genesis session (Phase 0 build + Donchian brain init), competitive landscape + research methods ingestion, context engineering article ingestion, and timeline establishment.
- **Key decisions:** Every brain gets a project timeline as standard infrastructure. Every session appends an entry before ending.
- **Interface:** Append-only — add entries at the bottom using the entry format template in the file header.
- **Known issues:** Reconstructed retroactively from SESSION-HANDOFF — early entries may have imprecise durations.

---

## Open Questions
<!-- Rule 3: Chemoattractant gradients — aggregated from all files' unanswered questions -->
<!-- These tell future sessions where to spend tokens. Update when questions are answered. -->

| # | Question | Source | Raised | Status |
|---|----------|--------|--------|--------|
| 1 | Frontend stack preference for Prover? | SPEC-001 | 2026-02-16 | open |
| 2 | Is Prover the whole system or just the backtester? | SPEC-001 | 2026-02-16 | open |
| 3 | Data freshness — how does OHLCV data get refreshed? | SPEC-001 | 2026-02-16 | open |
| 4 | Strategy versioning — git tags? Dedicated VERSION file? | SPEC-001 | 2026-02-16 | open |
| 5 | Each agent = own project + own brain? (not yet in SPEC-001) | SESSION-HANDOFF | 2026-02-17 | **resolved** — deposited into SPEC-001 |
| 6 | Architect/Planner → Coder brain communication protocol details? | SPEC-002 | 2026-02-17 | open |
| 7 | CCXT async vs sync — which pattern for data pipelines? | SPEC-002 | 2026-02-17 | open |
| 8 | Short selling support in strategy abstraction? | SPEC-002 | 2026-02-17 | open |
| 9 | Multi-timeframe data alignment in IStrategy template? | SPEC-002 | 2026-02-17 | open |
| 10 | VectorBT validation template design? | SPEC-002 | 2026-02-17 | open |
| 11 | GitHub ingestion method for Coder brain seed knowledge? | SPEC-002 | 2026-02-17 | open |
| 12 | CCXT exchange scope — which exchanges to support first? | SPEC-002 | 2026-02-17 | open |
| 13 | Should CLUSTERS section be auto-generated or manually maintained? | SPEC-003 | 2026-02-17 | **resolved** — auto-generated by `/brain-status`, user pastes into INDEX-MASTER |
| 14 | Vitality score threshold for triggering review flag? | SPEC-003 | 2026-02-17 | **resolved** — vitality < 2.0 = review, < 1.0 = retirement candidate; RULEs exempt |
| 15 | Retired files: git-delete or move to archive/ directory? | SPEC-003 | 2026-02-17 | **resolved** — move to `project-brain/archive/` (preserves history, recoverable) |
| 16 | Optimal CLAUDE.md size threshold for brain projects? | RULE-003 | 2026-02-15 | open |
| 17 | Optimal compaction threshold for brain sessions? | RULE-002 | 2026-02-15 | open |
| 18 | Does hub structure change after consolidation? | LEARN-033 | 2026-02-17 | open |
| 19 | What backlink count separates "quiet" from "healthy"? | LEARN-033 | 2026-02-17 | open |
| 20 | Are quiet RULEs a structural pattern (leaf-type) or a problem? | LEARN-033 | 2026-02-17 | **preliminary finding** — leaf-type (see LEARN-033) |
| 21 | Where are Claude Code chat logs stored locally and what's their format? | LEARN-034 | 2026-02-17 | **resolved** — `~/.claude/projects/<project>/<session>.jsonl` (see LEARN-034) |
| 22 | How much knowledge typically goes undeposited per session? | LEARN-034 | 2026-02-17 | **partial** — first data: ~4 items/session (33 across 8) |
| 23 | How do independent agent-projects coordinate? Shared git repo with worktrees or separate repos with CONTEXT-PACK via filesystem/MCP? | SPEC-001 | 2026-02-17 | open |
| 24 | Should skill files be copied into the repo for version control? (currently at `~/.claude/skills/` outside git) | LEARN-019 | 2026-02-17 | open |

---

## Clusters
<!-- Auto-generated by /brain-status. Update by re-running the skill. -->
<!-- Last generated: 2026-02-17 -->

| Cluster | Files | Avg Vitality | Squeeze Point? | Sub-Index? |
|---------|-------|--------------|----------------|------------|
| claude-code | 15 | 23.5 | approaching | candidate |
| architecture | 8 | 29.9 | no | no |
| configuration | 6 | 18.0 | no | no |
| prover | 5 | 14.5 | no | no |
| hooks | 5 | 24.8 | no | no |
| skills | 5 | 25.3 | no | no |
| competitive-analysis | 5 | 19.1 | no | no |
| MCP | 5 | 22.4 | no | no |

**Notes:**
- `claude-code` at 15 files (31% of brain) is approaching squeeze point — summaries overlap significantly. First sub-index candidate.
- `prover` has lowest avg vitality (14.5) — newer research files not yet consumed by other files.
- No cluster besides `claude-code` is near squeeze point yet.

---

## Tensions
<!-- Rule 4: Deposit contradictions, don't resolve prematurely -->
<!-- States: OPEN (accumulating evidence), BLOCKING (on critical path), RESOLVED (one side won) -->

| # | Tension | Side A | Side B | State | Notes |
|---|---------|--------|--------|-------|-------|
| 1 | Temporal vs topological decay | Common practice, Grok (age-based relevance) | LEARN-032 (connection-based — vitality = inbound links) | RESOLVED | Topological chosen: a 6-month file with 5 inbound links is alive, yesterday's file with 0 is decaying. Relevance is relationships, not recency. |
| 2 | File size guideline | LEARN-031 (<1000 tokens recommended for atomic notes) | Current practice (most LEARNs are 500-2000 tokens) | OPEN | Brain files are more comprehensive than atomic notes. May need brain-specific guideline rather than Zettelkasten default. |
| 3 | Consolidation trigger | LEARN-031, SPEC-000 (every 20-30 files, count-based) | LEARN-032, SPEC-003 ("mental squeeze point", quality-based) | RESOLVED | Mental squeeze point chosen over arbitrary count. 20-30 is a heuristic, not a trigger — consolidate when fat index can't capture distinctions. |
| 4 | Brain delivery mechanism priority | LOG-003 (rules first — lowest effort) | LEARN-005, LEARN-007 (skills first — highest impact) | OPEN | Both valid. Rules already implemented. Skills implemented. Question is which to invest more in going forward. |
