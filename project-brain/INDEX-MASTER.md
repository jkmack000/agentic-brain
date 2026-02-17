# INDEX-MASTER
<!-- type: INDEX -->
<!-- updated: 2026-02-14 -->
<!-- total-files: 31 -->
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
_None yet. Sub-indexes will be created when file count exceeds ~75._
<!-- When sub-indexes exist, list them here:
- [INDEX-indicators.md](indexes/INDEX-indicators.md) — Donchian, ATR, etc.
- [INDEX-signals.md](indexes/INDEX-signals.md) — Entry/exit signal logic
- [INDEX-execution.md](indexes/INDEX-execution.md) — Order routing, position management
- [INDEX-learnings.md](indexes/INDEX-learnings.md) — Discovered knowledge, edge cases
-->

---

## SPEC Files

### SPEC-000
- **Type:** SPEC
- **File:** specs/SPEC-000_project-brain-architecture.md
- **Tags:** architecture, overview, memory-system, fat-index, master-spec
- **Links:** _(foundational — linked by everything)_
- **Summary:** Defines the entire Project Brain LLM memory system. Covers fat indexing methodology, file type system (SPEC/CODE/RULE/LEARN/LOG/RESET), directory structure, session workflows (search → reset → work), brain-search.py CLI spec, and the phase plan. First application target is a multi-timeframe Donchian trading bot. This is the root document — load it to understand how the memory system works.
- **Key decisions:** Fat index over thin index; standalone CLI over Obsidian plugin; search/work session split; typed file system with 6 types; hierarchical index navigation for scale.
- **Interface:** N/A (architecture spec, not code)
- **Known issues:** None open

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
- **Summary:** 11 concrete patterns for writing Claude Code hooks correctly. Covers: matcher must be string regex (not object), matcher-based format required (2.1.42+), Stop hooks must be command-type (prompt-type unreliable), `stop_hook_active` guard prevents infinite loops, prompt-type uses `ok`/`reason` while command-type uses `decision`, async hooks can't block, hooks snapshot at startup (restart to test), Windows path normalization with `chr(92)`, SessionStart stdout injection. Every "never" pattern was tested and confirmed broken.
- **Known issues:** PreCompact and SessionEnd hooks not yet tested in production.

### RULE-002
- **Type:** RULE
- **File:** rules/RULE-002_context-and-session-management.md
- **Tags:** tool-pattern, context-window, compaction, sessions, subagents, clear, plan-mode
- **Links:** LEARN-005, LEARN-010, LEARN-018
- **Summary:** 9 patterns for protecting the context window and managing sessions. Key rules: externalize critical state before compaction hits, use subagents for investigation (keeps main context clean), skills save context vs always-on CLAUDE.md, `/clear` after 2 failed corrections (never 3), "ultrathink" is not a keyword (use `CLAUDE_CODE_EFFORT_LEVEL`), Plan Mode for read-only analysis, don't resume sessions in two terminals (use `--fork-session`), session permissions not restored on `--continue`, `--output-format json` for cost tracking.
- **Known issues:** Optimal compaction threshold for brain sessions still under evaluation.

### RULE-003
- **Type:** RULE
- **File:** rules/RULE-003_skills-and-claude-md-patterns.md
- **Tags:** tool-pattern, skills, SKILL-md, CLAUDE-md, configuration, visibility, context-budget
- **Links:** LEARN-005, LEARN-007, LEARN-018, LEARN-019
- **Summary:** 6 patterns for skills and CLAUDE.md configuration. Key rules: `disable-model-invocation: true` makes skills completely invisible to Claude (not just user-only), skills in spaced paths fail CLI resolution (copy to `~/.claude/skills/`), bloated CLAUDE.md causes silent rule-ignoring (prune ruthlessly, move to skills/hooks), `@` references auto-load CLAUDE.md from target directory, 2% context budget for all skill descriptions combined, supporting files pattern for skills over 500 lines.
- **Known issues:** Optimal CLAUDE.md size threshold for brain projects needs measurement.

### RULE-004
- **Type:** RULE
- **File:** rules/RULE-004_hooks-safe-modification-workflow.md
- **Tags:** tool-pattern, hooks, settings-json, backup, rollback, safety
- **Links:** RULE-001, LEARN-008, LEARN-019
- **Summary:** Workflow for safely modifying hooks: always `cp settings.local.json settings.local.json.backup` before changes, restart session, test that hooks still fire, rollback from backup if broken. Motivated by silent-disable failure mode where one bad field kills ALL hooks with no error message. Includes recovery steps and when to overwrite the backup.
- **Known issues:** Automating backup as a hook is chicken-and-egg — the backup hook itself could break.

---

## LEARN Files

### LEARN-001
- **Type:** LEARN
- **File:** learnings/LEARN-001_semantic-compression-context-extension.md
- **Tags:** context-window, compression, semantic-search, ingestion, supermemory, architecture
- **Links:** SPEC-000
- **Summary:** Documents semantic compression (6-stage pipeline: segmentation → MiniLM embedding → spectral clustering → BART summarization → reassembly → injection) achieving ~6:1 compression at 90%+ retrieval accuracy. Also covers Supermemory's Infinite Chat (vector-scored conversation chunking). Key finding: compression is complementary to fat indexing, not a replacement — compression stuffs more in the window, fat indexing avoids loading at all. Identified as candidate architecture for automating `brain ingest` and as the paid-tier AI summarization feature from SPEC-000.
- **Known issues:** None open

### LEARN-002
- **Type:** LEARN
- **File:** learnings/LEARN-002_competitive-landscape-memory-indexing-systems.md
- **Tags:** competitive-analysis, memory-systems, indexing, MCP, RAPTOR, GraphRAG, Letta, Mem0, context-engineering
- **Links:** SPEC-000, LEARN-001, LOG-001
- **Summary:** Feb 2026 survey of LLM memory/indexing systems. Key finding: Letta's Context Repositories independently converged on our architecture (git-backed, file-based, progressive disclosure) — strong validation. Our 44:1 compression beats automated approaches (6-20x). Top 3 actionable improvements: (1) **MCP server wrapper for brain.py** — biggest gap, entire ecosystem converging on MCP; (2) **Formalize consolidation as ADD/UPDATE/DELETE/NOOP** — from Mem0; (3) **Git-commit every deposit** — from Letta. Also covers RAPTOR (tree-of-summaries), GraphRAG, Zep (temporal provenance), ACE (context collapse prevention), and "lost in the middle" research (critical info at top/bottom of context). Brain Hub concept (LOG-001) validated by MemOS and OpenMemory market demand.
- **Key decisions:** MCP wrapper is #1 priority for brain system after Donchian bot MVP. Top 10 improvements ranked by impact/effort.
- **Interface:** N/A (learning, not code)
- **Known issues:** All improvements deferred until Donchian bot proves core concept.

### LEARN-003
- **Type:** LEARN
- **File:** learnings/LEARN-003_qualitative-research-methods-for-knowledge-systems.md
- **Tags:** qualitative-research, triangulation, progressive-focusing, concept-mapping, methodology, Stake
- **Links:** SPEC-000, LEARN-001, LEARN-002
- **Summary:** Transfers 6 concepts from Stake's qualitative research methodology to brain system design: (1) **Triangulation** — multi-source confirmation, formalize confidence levels (unconfirmed/corroborated/validated) in fat index entries; (2) **Progressive focusing** — start broad, narrow to emerging issues across sessions, don't lock structure too early; (3) **Concept mapping** — spatial representation of how knowledge relates, addresses cross-referencing gaps; (4) **Member checking** — present findings for user review before committing; (5) **Progressive recoding** — file types may need reclassification as projects mature; (6) **Data storage tips** — our SESSION-HANDOFF, fat index, and "Known issues" fields already implement Stake's recommendations. Three actionable improvements: add confidence indicator to index entries, consider FOCUS file type, concept map overlay for INDEX-MASTER.
- **Key decisions:** None yet — three improvements identified but deferred.
- **Interface:** N/A (learning, not code)
- **Known issues:** Academic framework, not directly about LLM memory — transferability needs validation through practice.

### LEARN-004
- **Type:** LEARN
- **File:** learnings/LEARN-004_context-engineering-for-claude-code.md
- **Tags:** context-engineering, claude-code, knowledge-files, token-management, research-workflow, CLAUDE-files
- **Links:** SPEC-000, LEARN-001, LEARN-002
- **Summary:** Distilled from Thomas Landgraf's Substack article on context engineering for Claude Code. Defines three pillars of context engineering: project architecture knowledge (CLAUDE files), product requirements (PRD files), and deep technical knowledge documents. Documents a concrete three-step research workflow: (1) OpenAI Deep Research for exhaustive breadth (25-36 pages, 100+ citations, 7-30min), (2) Claude Research for rapid refinement (~0% hallucination, 2-5min), (3) synthesis into master knowledge documents. Key best practices: rigorous expert review of knowledge files (one bad API pattern poisons all future sessions), strategic splitting at 50KB threshold, token management via `/compact` and `/clear`, and living documentation via `@path` code references. Token economics: front-loaded knowledge docs beat real-time research by orders of magnitude ($40-70 per research session vs. near-zero for pre-computed docs). Strongly validates our brain architecture — fat indexing, modular files, and session management all align with these emerging best practices.
- **Key decisions:** Three actionable items identified: (1) adopt `@path` code references in LEARN/SPEC files, (2) use 50KB as splitting threshold, (3) consider two-phase research workflow for `brain ingest`.
- **Interface:** N/A (learning, not code)
- **Known issues:** Article focuses on Claude Code specifically — some advice (CLAUDE files, /compact) is tool-specific and may not generalize to other LLM assistants.

### LEARN-005
- **Type:** LEARN
- **File:** learnings/LEARN-005_claude-code-official-best-practices.md
- **Tags:** claude-code, best-practices, context-management, CLAUDE-md, prompting, workflows, subagents, agent-sdk, hooks, skills, verification, session-management
- **Links:** SPEC-000, LEARN-004, LEARN-013, LEARN-014, LEARN-017, LEARN-018, LEARN-013, LEARN-014, LEARN-017, LEARN-018
- **Summary:** Comprehensive operational playbook from Anthropic's official Claude Code best practices. Core constraint: context window is #1 resource. Covers 9 areas: (1) Verification as highest-leverage practice; (2) Explore→Plan→Implement→Commit 4-phase workflow with Plan Mode (Shift+Tab toggle); (3) Specific context in prompts; (4) CLAUDE.md authoring — include/exclude rules, @path imports, pruning; (5) Environment config — permissions, CLI tools, MCP, hooks, skills, subagents, plugins; (6) Communication — codebase questions, interview pattern; (7) Session management — course-correct after 2 failures, compaction; (8) Agent SDK (formerly headless mode) — `claude -p`, fan-out, writer/reviewer; (9) Five anti-patterns. Seven brain takeaways. **Note:** Topics introduced here are expanded in depth by later LEARNs: MCP (013), Agent SDK (014), costs/settings (017), workflows (018).
- **Key decisions:** Seven actionable items. Most impactful: skills/CLAUDE.md @path as brain delivery mechanism; anti-patterns as depositworthy RULE file.
- **Interface:** N/A (learning, not code)
- **Known issues:** Source may update as Claude Code evolves. Later LEARNs supersede this on specific topics (MCP, SDK, costs, workflows) but this remains the best single-file operational overview.

### LEARN-006
- **Type:** LEARN
- **File:** learnings/LEARN-006_claude-code-memory-system.md
- **Tags:** claude-code, CLAUDE-md, auto-memory, memory-hierarchy, rules, imports, configuration
- **Links:** SPEC-000, LEARN-004, LEARN-005
- **Summary:** Deep dive into Claude Code's memory system from official docs. Two memory types: auto memory (Claude writes for itself, 200-line MEMORY.md index + topic files) and CLAUDE.md (user-written instructions). Full 6-level hierarchy with priority order: managed policy → project memory → project rules → user memory → project local → auto memory. Covers `@path` import syntax (relative resolution, max depth 5, approval dialog), `.claude/rules/*.md` modular rules with path-specific conditional rules (YAML frontmatter `paths` field with glob patterns), user-level rules at `~/.claude/rules/`, symlinks for cross-project sharing, and `--add-dir` for multi-directory access. Key finding: auto memory's architecture (200-line index + topic files loaded on demand) independently converges on our fat-index pattern — strong validation. Path-specific rules could scope brain knowledge to relevant code areas.
- **Key decisions:** Five brain-relevant takeaways: auto memory parallels brain system; `.claude/rules/*.md` maps to our RULE files; `@path` imports as brain delivery mechanism; path-specific rules for context-scoped knowledge; symlinks for cross-project brain sharing.
- **Interface:** N/A (learning, not code)
- **Known issues:** Auto memory is still rolling out gradually (opt-in via `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0`). Relationship between auto memory and brain system needs practical testing.

### LEARN-007
- **Type:** LEARN
- **File:** learnings/LEARN-007_claude-code-skills-system.md
- **Tags:** claude-code, skills, SKILL-md, slash-commands, workflows, configuration
- **Links:** SPEC-000, LEARN-005, LEARN-006
- **Summary:** Comprehensive reference for Claude Code's skills system from official docs. Skills = SKILL.md files with YAML frontmatter + markdown instructions. Two content types: reference (knowledge applied to current work, runs inline) and task (step-by-step workflows, often manual-only). Full frontmatter reference: name, description, argument-hint, disable-model-invocation, user-invocable, allowed-tools, model, context (fork for subagent execution), agent, hooks. Invocation control matrix: default (both user+Claude), disable-model-invocation (user only), user-invocable:false (Claude only). String substitutions ($ARGUMENTS, $N, ${CLAUDE_SESSION_ID}). Dynamic context injection via `!`command`` preprocessing. Supporting files pattern (SKILL.md under 500 lines, details in separate files). Context budget: 2% of window for skill descriptions (fallback 16K chars). Follows Agent Skills open standard (agentskills.io).
- **Key decisions:** Six brain-relevant takeaways: skills ARE the delivery mechanism for brain knowledge; `disable-model-invocation` for brain workflows; supporting files pattern maps to brain architecture; dynamic context injection for brain search; context budget constrains how many skills can exist; `context:fork` for isolated brain operations.
- **Interface:** N/A (learning, not code)
- **Known issues:** Context budget (2% of window) limits total skill count. Brain system needs to be selective about which knowledge becomes a skill vs. stays as a brain file.

### LEARN-008
- **Type:** LEARN
- **File:** learnings/LEARN-008_claude-code-hooks-system.md
- **Tags:** claude-code, hooks, automation, lifecycle, deterministic, configuration
- **Links:** SPEC-000, LEARN-005, LEARN-007, LEARN-015, LEARN-016
- **Summary:** Combined reference + guide for Claude Code's hooks system from official docs. 14 lifecycle events (SessionStart through SessionEnd), three hook types (command, prompt, agent), full JSON input/output schemas, exit code protocol (0=proceed, 2=block, other=log), and decision control patterns per event. Detailed coverage of: PreToolUse decision control (allow/deny/ask + updatedInput), matcher patterns (regex on tool names, session sources, notification types), async hooks (background execution, no blocking), MCP tool matching (mcp__server__tool pattern), SessionStart environment persistence (CLAUDE_ENV_FILE), prompt-based hooks (single-turn LLM evaluation, ok/reason response), agent-based hooks (multi-turn subagent with tools, up to 50 turns). Six hook locations by scope (user → project → local → managed → plugin → skill/agent frontmatter). Practical patterns: desktop notifications, auto-format after edits, block protected files, re-inject context after compaction.
- **Key decisions:** Seven brain-relevant takeaways: SessionStart hooks for brain loading; PreCompact hooks for brain preservation; PostToolUse hooks for auto-deposit after commits; Stop hooks as quality gates for session handoff; SessionEnd hooks for auto-handoff; UserPromptSubmit for brain-aware context routing; async hooks for background brain indexing.
- **Interface:** N/A (learning, not code)
- **Known issues:** Hooks snapshot at startup — mid-session changes need review in /hooks menu. Prompt/agent hooks add latency. Stop hooks can loop infinitely without stop_hook_active guard.

### LEARN-009
- **Type:** LEARN
- **File:** learnings/LEARN-009_claude-code-subagents-system.md
- **Tags:** claude-code, subagents, delegation, context-isolation, custom-agents, persistent-memory
- **Links:** SPEC-000, LEARN-005, LEARN-007
- **Summary:** Full subagent system reference from official docs. Built-in agents: Explore (Haiku, read-only, fast), Plan (inherits, read-only), general-purpose (inherits, all tools), Bash, statusline-setup, Claude Code Guide. Custom agents via `.claude/agents/*.md` with YAML frontmatter: name, description, tools/disallowedTools, model, permissionMode (6 modes), maxTurns, skills (preloaded), mcpServers, hooks, memory. Four storage locations with priority: CLI flag → project → user → plugin. Key feature: **persistent memory** with three scopes (user/project/local) — MEMORY.md index (200 lines loaded) + topic files, independently converging on our fat-index architecture. Foreground vs background execution (Ctrl+B to background). Resumable subagents (preserves full conversation history). CLI-defined agents via `--agents` JSON for session-only testing. Task tool restrictions for controlling which subagents can be spawned. Subagents cannot spawn other subagents.
- **Key decisions:** Six brain-relevant takeaways: brain-searcher subagent (Explore/Haiku for cheap lookups); persistent memory parallels brain system; brain-depositor subagent (Write access, Haiku); skills preloading for brain-aware agents; background subagents for brain maintenance; CLI-defined agents for brain CI/CD automation.
- **Interface:** N/A (learning, not code)
- **Known issues:** Subagents can't spawn subagents — limits recursive brain operations. Background subagents can't use MCP tools. Context from many completed subagents can bloat main conversation.

### LEARN-010
- **Type:** LEARN
- **File:** learnings/LEARN-010_claude-code-architecture-internals.md
- **Tags:** claude-code, architecture, agentic-loop, tools, context-window, sessions, checkpoints
- **Links:** SPEC-000, LEARN-005, LEARN-006, LEARN-013, LEARN-014, LEARN-017
- **Summary:** Claude Code architecture overview from official docs. Agentic loop: gather context → take action → verify results (phases blend, Claude chains dozens of actions). Claude Code = the agentic harness providing tools, context management, and execution environment. Five tool categories: file operations, search, execution, web, code intelligence (plugins). Session model: each session starts fresh (no cross-session memory except auto memory + CLAUDE.md), sessions tied to directory, branch-aware (switch branches = new files same history), resume/fork support. Context window management: auto-compaction clears old tool outputs then summarizes, preserves requests + key code, may lose early instructions → put persistent rules in CLAUDE.md. Skills load on demand, subagents get fresh context. Two safety mechanisms: checkpoints (every edit snapshots, Esc+Esc to rewind, local to session, separate from git) and permissions (4 modes via Shift+Tab: default, auto-accept edits, plan mode, delegate mode).
- **Key decisions:** Six brain-relevant takeaways: agentic loop validates search→work separation; session independence is why brains exist; compaction = information loss (validates SESSION-HANDOFF); checkpoints as safety net for brain operations; fork sessions for brain experiments; MCP context cost monitoring important for brain MCP wrapper.
- **Interface:** N/A (learning, not code)
- **Known issues:** Checkpoints only cover Claude's file changes, not external processes. Session-scoped permissions not restored on resume.

### LEARN-011
- **Type:** LEARN
- **File:** learnings/LEARN-011_fat-index-convergence-validation.md
- **Tags:** validation, architecture, fat-index, convergence, auto-memory, subagents, context-repositories
- **Links:** SPEC-000, LEARN-002, LEARN-006, LEARN-009
- **Summary:** Cross-cutting finding: three independently-designed systems converge on our fat-index architecture. (1) Claude Code auto memory (200-line MEMORY.md index + topic files), (2) subagent persistent memory (same pattern, three scopes), (3) Letta Context Repositories (git-backed, file-based, progressive disclosure). All use the same core principle: a summary layer that answers "do I need to open this?" without paying token cost. Strong external validation of brain system's core design. Implications for interoperability, marketing positioning, and architecture confidence.
- **Key decisions:** None — strategic validation finding. Carry forward into product positioning.
- **Interface:** N/A (learning, not code)
- **Known issues:** None open

### LEARN-012
- **Type:** LEARN
- **File:** learnings/LEARN-012_brain-operational-drift-and-sync.md
- **Tags:** operational, drift, sync, templates, INIT-md, multi-brain, maintenance
- **Links:** SPEC-000, LOG-002
- **Summary:** Documents two operational edge cases: (1) **Template drift** — brain.py init generates INIT.md from a hardcoded template that has fallen behind the manually-evolved INIT.md (now includes timeline rules, dedup rules, shorthand commands, handoff triggers). New brains start with stale operational knowledge. (2) **Multi-brain sync** — when multiple brains exist, INIT.md improvements in one don't propagate to others (e.g., Donchian brain missing timeline rule). Two fix approaches identified: single-source versioned template with `brain sync`, or split INIT.md into project-specific + shared operational rules.
- **Key decisions:** None yet — flagged for resolution. Low priority until third brain created.
- **Interface:** N/A (learning, not code)
- **Known issues:** Both problems will worsen as more brains are created. Needs resolution before any public release.

### LEARN-013
- **Type:** LEARN
- **File:** learnings/LEARN-013_claude-code-mcp-system.md
- **Tags:** claude-code, MCP, model-context-protocol, transports, tools, resources, prompts, brain-server
- **Links:** SPEC-000, LEARN-002, LEARN-005, LEARN-008, LEARN-010
- **Summary:** Comprehensive MCP reference from official docs. Three transport types (HTTP recommended, SSE deprecated, stdio for local). Three scoping levels (local > project > user) with `.mcp.json` format supporting `${VAR:-default}` env var expansion. OAuth 2.0 and header-based auth. Output limits (10K warning, 25K max, `MAX_MCP_OUTPUT_TOKENS` override). Tool Search auto-activates at 10% context to defer MCP tools (requires Sonnet 4+/Opus 4+). MCP Resources as @-mentionable attachments (`@server:protocol://path`). MCP Prompts as slash commands (`/mcp__server__prompt`). `claude mcp serve` exposes Claude as MCP server. Plugin-bundled servers with `${CLAUDE_PLUGIN_ROOT}`. Enterprise managed MCP with allowlist/denylist. Anthropic MCP Registry API. **Brain MCP server architecture fully viable:** stdio transport, tools (search/read/index), resources (@-mentionable brain files), prompts (slash-command workflows), user-scoped cross-project.
- **Key decisions:** Brain MCP server confirmed as high-priority implementation target (validates LEARN-002 #1 ranking).
- **Interface:** N/A (learning, not code)
- **Known issues:** Brain MCP responses should stay under 10K tokens. Windows stdio servers using npx need `cmd /c` wrapper (Python avoids this).

### LEARN-014
- **Type:** LEARN
- **File:** learnings/LEARN-014_claude-code-agent-sdk.md
- **Tags:** claude-code, agent-sdk, headless, programmatic, automation, python, typescript, MCP-tools
- **Links:** SPEC-000, LEARN-005, LEARN-010, LEARN-013
- **Summary:** Full Agent SDK reference (renamed from "Claude Code SDK"). Two packages: `pip install claude-agent-sdk` (Python), `npm install @anthropic-ai/claude-agent-sdk` (TypeScript). Two interfaces: `query()` (one-shot, no hooks/MCP) vs `ClaudeSDKClient` (multi-turn, hooks, custom MCP tools, interrupts). Key options: `system_prompt` preset+append, `setting_sources` (defaults to None — SDK does NOT load CLAUDE.md unless explicit), `max_turns`/`max_budget_usd` for cost caps, `output_format` for JSON schema validation, `agents` for programmatic subagents, `can_use_tool` for permission callbacks with input modification. In-process custom MCP tools via `@tool` decorator + `create_sdk_mcp_server()`. Programmatic hooks as Python callbacks (not shell scripts). `ResultMessage` includes `total_cost_usd` for cost tracking. 1M context beta via `betas=["context-1m-2025-08-07"]`. SDK is the correct infrastructure for brain automation.
- **Key decisions:** Agent SDK identified as brain automation engine. Critical constraint: `setting_sources` defaults to None.
- **Interface:** N/A (learning, not code)
- **Known issues:** Python hooks missing SessionStart/SessionEnd/Notification events (TypeScript only). "Headless mode" officially renamed to "Agent SDK."

### LEARN-015
- **Type:** LEARN
- **File:** learnings/LEARN-015_claude-code-agent-teams.md
- **Tags:** claude-code, agent-teams, coordination, multi-agent, task-list, messaging, experimental
- **Links:** SPEC-000, LEARN-005, LEARN-009
- **Summary:** Agent teams are full independent Claude Code sessions (not subagent child processes) connected by shared task list + inter-agent mailbox. Four components: team lead, teammates, file-locked task list (pending/in-progress/completed with dependency tracking), and mailbox (direct or broadcast messaging). Teammates form a mesh (any-to-any), unlike subagents (child-to-parent only). Delegate mode restricts lead to coordination-only. Plan approval gates require teammate plans before implementation. Team-specific hook events (TeammateIdle, TaskCompleted — already in LEARN-008) only fire during team sessions. Context critical: teammates do NOT inherit lead's conversation — all context via spawn prompt or CLAUDE.md/skills. Experimental: requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Uses ~7x tokens vs standard sessions.
- **Key decisions:** Agent teams identified as coordination layer for complex brain operations (parallel ingestion, multi-area search, maintenance). High cost (7x) limits to high-value operations.
- **Interface:** N/A (learning, not code)
- **Known issues:** Experimental feature. No session resumption with in-process teammates. Task status can lag. No nested teams. Split panes not on Windows Terminal. ~7x token cost limits to high-value operations.

### LEARN-016
- **Type:** LEARN
- **File:** learnings/LEARN-016_claude-code-plugin-system.md
- **Tags:** claude-code, plugins, packaging, distribution, plugin-json, namespacing, marketplace
- **Links:** SPEC-000, LEARN-005, LEARN-007, LEARN-008, LEARN-009, LEARN-013
- **Summary:** Complete plugin system for packaging skills, agents, hooks, MCP servers, and LSP servers as distributable units. Plugin = directory with `.claude-plugin/plugin.json` manifest (only `name` required). Components go at plugin root (NOT inside `.claude-plugin/` — silent failure gotcha). Auto-namespacing: `/<plugin-name>:<skill-name>`. Four installation scopes (user/project/local/managed). Five distribution sources (path/npm/pip/github/url). Plugins cached — do NOT run in-place, use `${CLAUDE_PLUGIN_ROOT}` for all paths. Plugin MCP servers auto-start. CLI: `--plugin-dir` for dev testing. Migration from `.claude/` to plugin is straightforward. **Architecture split for brain**: engine (templates, skills, hooks, agents) in cached plugin vs data (learnings, specs, logs) project-local. Distribution aligns with Brain Hub concept (LOG-001).
- **Key decisions:** Plugin system is the distribution mechanism for brain system. Engine/data split is a key architecture decision.
- **Interface:** N/A (learning, not code)
- **Known issues:** Plugin caching breaks path traversal — `${CLAUDE_PLUGIN_ROOT}` must be used everywhere. 2% context budget limits total skill count in plugins.

### LEARN-017
- **Type:** LEARN
- **File:** learnings/LEARN-017_claude-code-costs-settings-environment.md
- **Tags:** claude-code, costs, settings, environment-variables, configuration, token-management, optimization
- **Links:** SPEC-000, LEARN-004, LEARN-005, LEARN-006, LEARN-010
- **Summary:** Quantitative cost baseline: $6/dev/day average, 90% under $12, ~$100-200/dev/month API, agent teams ~7x overhead, background sessions $0.04. Rate limits by team size (200-300k TPM solo → 10-15k TPM at 500+ users). Complete 5-level settings hierarchy: managed → CLI → local → shared → user, with precise file paths for all OS. Full settings.json key reference including `model`, `availableModels`, `cleanupPeriodDays`, `env`, `fileSuggestion`, `respectGitignore`. 50+ environment variables for model/token/cost/feature control. Key vars: `CLAUDE_CODE_EFFORT_LEVEL` (low/med/high), `CLAUDE_CODE_SUBAGENT_MODEL`, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` (~95% default), `ENABLE_TOOL_SEARCH`. Complete permissions syntax with `additionalDirectories` for cross-directory brain access. Cost strategies: CLAUDE.md under ~500 lines, prompt caching benefits static brain files maximally, subagent model selection.
- **Key decisions:** Brain operations quantifiably budgetable. Key optimizations: effort_level=low for maintenance, subagent_model=haiku for lookups, never disable prompt caching for brain projects.
- **Interface:** N/A (learning, not code)
- **Known issues:** Rate limits are org-level — brain automation competes with interactive usage. CLAUDE_AUTOCOMPACT_PCT_OVERRIDE default confirmed ~95%.

### LEARN-018
- **Type:** LEARN
- **File:** learnings/LEARN-018_claude-code-common-workflows-and-patterns.md
- **Tags:** claude-code, workflows, plan-mode, extended-thinking, recipes, automation, patterns
- **Links:** SPEC-000, LEARN-005, LEARN-010, LEARN-014, LEARN-017
- **Summary:** Concrete operational recipes and details from common-workflows docs. Plan Mode mechanics: Shift+Tab cycles modes, `--permission-mode plan` flag, **headless Plan Mode** (`claude --permission-mode plan -p "query"`) for zero-risk read-only analysis (ideal for brain search). Extended thinking: enabled by default, Opus 4.6 uses adaptive reasoning (effort levels), `MAX_THINKING_TOKENS` env var, Alt+T toggle, **"think"/"ultrathink" are NOT special keywords**. Four reusable workflow recipe shapes: Explore (overview→architecture→models→component), Debug (error→options→fix→verify), Refactor (find→recommend→apply→verify), Test (uncovered→scaffold→edge cases→verify). PR creation via `/commit-push-pr` skill with auto-Slack-posting, `--from-pr <number>` session linking. `@` references auto-load CLAUDE.md from referenced file's directory — zero-config brain discoverability. Git worktrees for parallel brain sessions. `--output-format json` includes cost+duration metadata.
- **Key decisions:** Headless Plan Mode identified as ideal brain search mechanism. Four RESET template variants identified but not yet created.
- **Interface:** N/A (learning, not code)
- **Known issues:** Plan Mode Ctrl+G (editor export) vs Shift+Tab (mode cycling) are different functions — LEARN-005 conflates slightly.

### LEARN-019
- **Type:** LEARN
- **File:** learnings/LEARN-019_claude-code-brain-integration-layers-1-3.md
- **Tags:** claude-code, integration, CLAUDE-md, rules, skills, hooks, automation, brain-delivery, testing, windows, matcher-format
- **Links:** SPEC-000, LEARN-005, LEARN-006, LEARN-007, LEARN-008, LOG-003
- **Summary:** Documents implementation AND test results of Claude Code native integration (Layers 1-3). Eight files: CLAUDE.md (@path import of INIT.md), 3 rules, 4 skills, 4 hooks. **Tested:** Layer 1 (CLAUDE.md + rules) fully working including @path with spaces in Windows paths. Layer 2 (skills) all 4 working after fixing `disable-model-invocation: true → false`; skills also fail CLI `/` resolution when project path contains spaces — workaround is copying to user-level `~/.claude/skills/`. Layer 3 (hooks) **CRITICAL FIX:** `matcher` must be a string regex or omitted — using JSON objects (`{}`, `{"tools": [...]}`) causes a Settings Error that silently disables ALL hooks. Stop hook FAILED due to this — session exited without blocking. Fixed: PostToolUse matcher changed to `"Edit|Write"` string; all other matchers omitted. Contains gotchas section covering: `disable-model-invocation` visibility, `chr(92)` pattern, hooks snapshot at startup, hooks format migration (corrected), and skills spaces-in-path bug.
- **Key decisions:** @path imports INIT.md (not INDEX-MASTER — too large); `disable-model-invocation: false`; PostToolUse uses `"Edit|Write"` string matcher + `chr(92)` path normalization; hooks use matcher-based format with **string matchers only**; skills copied to user-level `~/.claude/skills/` for CLI resolution.
- **Interface:** N/A (learning, not code)
- **Known issues:** Prompt-type hooks unreliable for Stop events — use command-type with exit codes. PreCompact hook not testable on demand (simple echo, trivially correct). All other components fully tested and passing as of 2026-02-15 cleanup session. Duplicate skills resolved (project-level copies removed).

### LEARN-021
- **Type:** LEARN
- **File:** learnings/LEARN-021_langchain-langgraph-architecture-memory-retrieval.md
- **Tags:** langchain, langgraph, deep-agents, memory, persistence, retrieval, RAG, middleware, competitive-analysis, architecture-patterns
- **Links:** LEARN-002, LEARN-020, SPEC-000
- **Summary:** Full architectural analysis of LangChain/LangGraph ecosystem (Feb 2026 reorganization). Three layered products: DeepAgents (auto-compression, virtual filesystem) → LangChain Agents (middleware system) → LangGraph (stateful graphs). Memory adopts CoALA taxonomy: semantic (LEARN/SPEC), episodic (LOG), procedural (RULE). Store uses namespace tuples + key-value + optional semantic search — maps to our directory structure. Six middleware hooks including novel transient vs persistent context distinction. Priority-ranked retrieval improvements: BM25 (#1, low effort), content hashing dedup (#2), multi-query (#3), self-query filtering (#4), hybrid BM25+vector (#5). ParentDocumentRetriever independently converges on fat index pattern. LangChain Indexing API with content hashing solves our dedup problem systematically. DeepAgents (new, post-May 2025) most directly competitive to brain system — virtual filesystem + auto-compression for autonomous agents.
- **Key decisions:** None — competitive intelligence. BM25 search identified as #1 low-effort improvement. Content hashing as #2.
- **Interface:** N/A (learning, not code)
- **Known issues:** DeepAgents docs couldn't be fully fetched (new section). LangChain evolves rapidly — analysis is point-in-time Feb 2026.

### LEARN-020
- **Type:** LEARN
- **File:** learnings/LEARN-020_mem0-dspy-llm-driven-memory-crud.md
- **Tags:** mem0, dspy, react-agent, memory-crud, qdrant, vector-search, competitive-analysis, architecture-patterns
- **Links:** LEARN-002, LEARN-001, SPEC-000
- **Summary:** Full architecture analysis of avbiswas/mem0-dspy — a from-scratch Mem0 reimplementation (~300 lines) using DSPy ReAct agents + Qdrant. Core pattern: two LLM agents in sequence — Agent 1 (ResponseGenerator) answers user with optional memory search + outputs `save_memory` boolean; Agent 2 (UpdateMemory) sees conversation + existing memories and decides ADD/UPDATE/DELETE/NOOP via tool calls. Uses 64-dim OpenAI embeddings (24x smaller than default), DOT product, category faceting via Qdrant. Includes detailed comparison table with Project Brain (vector vs fat-index, LLM-driven vs rule-based CRUD, lossy vs lossless compression). Found 4 bugs in the repo. Five brain-relevant takeaways: LLM-driven CRUD as automation path for `/brain-deposit`, category faceting maps to our type system, `save_memory` boolean pattern for PostToolUse hook, 64-dim embeddings viable for small stores, DSPy Signatures as agent contract pattern.
- **Key decisions:** None — competitive intelligence. LLM-driven dedup identified as candidate enhancement for `/brain-deposit`.
- **Interface:** N/A (learning, not code)
- **Known issues:** Analysis is point-in-time (Feb 2026). Repo has 4 bugs including broken delete tool.

### LEARN-022
- **Type:** LEARN
- **File:** learnings/LEARN-022_dspy-optimizers-teleprompters.md
- **Tags:** dspy, optimizers, teleprompters, prompt-tuning, bootstrapping, compilation, bayesian-optimization, few-shot, fine-tuning, MIPROv2
- **Links:** LEARN-020, SPEC-000, LEARN-002
- **Summary:** Complete technical reference for DSPy's optimizer system (formerly "teleprompters", renamed DSPy 2.0 mid-2024). Covers all 15 optimizers across 5 categories: few-shot (LabeledFewShot, BootstrapFewShot, RandomSearch, Optuna, KNNFewShot), instruction (COPRO, MIPROv2, SIMBA, GEPA, InferRules), weight (BootstrapFinetune, GRPO), combined (BetterTogether), and utility (Ensemble, AvatarOptimizer). Deep dives on: BootstrapFewShot mechanics (teacher runs → metric filters → traces become demos), MIPROv2 three-stage process (bootstrap → propose instructions → Bayesian optimization via Optuna TPE), SIMBA self-reflective rules, GEPA evolutionary search, InferRules rule induction. Covers metrics system (`trace` parameter for strict-during-optimization), assertions (`dspy.Assert`/`Suggest`), teacher-student distillation, save/load (JSON format), and compilation model. Practical guidance: when to use which optimizer, min data sizes, cost estimates, 9 common pitfalls. Seven brain-relevant takeaways including: SIMBA rules parallel brain RULE files, InferRules could mine LOGs for rules, teacher-student distillation for brain search optimization.
- **Key decisions:** None — ingested knowledge. Seven improvement ideas identified but all deferred.
- **Interface:** N/A (learning, not code)
- **Known issues:** DSPy API evolves rapidly — analysis is point-in-time Feb 2026. SIMBA/GEPA/InferRules/GRPO are newer and less battle-tested. BetterTogether requires experimental flag.

### LEARN-023
- **Type:** LEARN
- **File:** learnings/LEARN-023_qmd-local-hybrid-search-engine.md
- **Tags:** qmd, search, BM25, vector-search, reranking, hybrid-search, MCP, local-first, competitive-analysis, sqlite, node-llama-cpp
- **Links:** LEARN-002, LEARN-021, LEARN-013, SPEC-000
- **Summary:** Full architecture analysis of QMD (tobi/qmd) — local-first CLI hybrid search engine for markdown by Shopify founder Tobi Lütke. MIT, v0.9.9, 8K+ stars. Three-layer pipeline: BM25 (FTS5) + vector (300M embedding-gemma) + LLM reranker (0.6B qwen3), all on-device via node-llama-cpp GGUF models (~2.1GB total). Novel patterns not in existing brain files: (1) typed query expansion (lex/vec/hyde variants via grammar-constrained decoding), (2) position-aware score blending preventing reranker from destroying high-confidence retrieval results, (3) smart signal detection skipping expansion when BM25 is confident, (4) two-table content-addressable storage (immutable content by SHA-256, mutable documents as filesystem mapping), (5) dynamic MCP instruction injection (collection metadata in system prompt). Ships MCP server (stdio + HTTP daemon). Confirms LEARN-021 patterns: BM25 (#1), content hashing (#2), multi-query (#3), hybrid+RRF (#5). "96% token savings" claim flagged as **unverified** — single Twitter anecdote, not apples-to-apples comparison. QMD is usable as a complement to brain.py (collection add over project-brain/).
- **Key decisions:** None — competitive intelligence. QMD identified as both competitor and potential search backend complement.
- **Interface:** N/A (learning, not code)
- **Known issues:** Pre-1.0, sqlite-vec alpha, 96% savings unverified, evolving rapidly (74 PRs/month).

---

## LOG Files

### LOG-001
- **Type:** LOG
- **File:** logs/LOG-001_brain-hub-shared-repository-idea.md
- **Tags:** product-direction, brain-hub, repository, crowdsourced, meta-brain, monetization
- **Links:** SPEC-000
- **Summary:** Captures the concept of "Brain Hub" — a shared public repository where users publish, browse, and pull fat-indexed knowledge files across domains. Global fat index enables discovery without downloading. Crowdsourced knowledge compounds value (one person's LEARN benefits all). Monetization: free browse/pull/push, paid for private brains, AI quality scoring, curated domain packs. Competitive moat is the data itself — millions of LLM-readable indexed knowledge entries. No competitor has this format.
- **Key decisions:** Concept captured, not yet committed to building. Revisit after local brain proven on 2-3 projects.
- **Known issues:** Needs trust/reputation system, global deduplication, privacy controls. Format stability required since it becomes an interchange format.

### LOG-003
- **Type:** LOG
- **File:** logs/LOG-003_brain-to-claude-code-delivery-mechanisms.md
- **Tags:** integration, delivery, skills, rules, imports, claude-code, architecture
- **Links:** SPEC-000, LEARN-005, LEARN-006, LEARN-007, LEARN-008
- **Summary:** Analysis of four mechanisms for delivering brain knowledge into Claude Code sessions: (1) `.claude/skills/` — on-demand via slash commands, best for task-specific brain operations, constrained by 2% context budget; (2) `.claude/rules/*.md` — always loaded, path-scoped, best for session hygiene rules, lowest effort; (3) `@path` imports in CLAUDE.md — selective, stable references, best for architecture specs; (4) auto memory — Claude-controlled, not for structured domain knowledge. Concludes mechanisms are complementary, not competing. Layered architecture: rules for always-on hygiene, skills for on-demand operations, @path for stable knowledge, auto memory for Claude's own housekeeping. Open question: which to implement first (skills = highest impact/effort, rules = lowest effort/power).
- **Key decisions:** Not yet made — analysis only. Likely first step: rules (trivial) then skills (impactful). May need `brain export --target claude-code` command.
- **Interface:** N/A (decision log, not code)
- **Known issues:** Revisit when starting Phase 2 implementation and when auto memory exits opt-in.

### LOG-002
- **Type:** LOG
- **File:** logs/LOG-002_project-timeline.md
- **Tags:** timeline, sessions, milestones, changelog, meta
- **Links:** SPEC-000
- **Summary:** Running chronological record of all project sessions, milestones, ingestions, and structural changes. Standard infrastructure file — every brain gets one. Contains dated entries for each session with: duration, key actions, files created/modified, decisions made, and blockers. Use to trace project evolution, estimate velocity, and orient on history. Currently covers: 2026-02-14 genesis session (Phase 0 build + Donchian brain init), competitive landscape + research methods ingestion, context engineering article ingestion, and timeline establishment.
- **Key decisions:** Every brain gets a project timeline as standard infrastructure. Every session appends an entry before ending.
- **Interface:** Append-only — add entries at the bottom using the entry format template in the file header.
- **Known issues:** Reconstructed retroactively from SESSION-HANDOFF — early entries may have imprecise durations.
