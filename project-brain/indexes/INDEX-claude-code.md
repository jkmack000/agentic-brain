# INDEX — claude-code
<!-- type: SUB-INDEX -->
<!-- cluster-tag: claude-code -->
<!-- updated: 2026-02-17 -->
<!-- member-count: 16 -->
<!-- parent: INDEX-MASTER.md -->

## About This Sub-Index
This sub-index contains fat index entries for the `claude-code` cluster — 16 files covering Claude Code internals, memory, skills, hooks, subagents, MCP, agent SDK, plugins, costs, workflows, architecture, and brain integration patterns.

**When to load:** Load this sub-index when working on Claude Code integration tasks, brain delivery mechanisms, or any task involving Claude Code features.

**Cross-cluster links:** Files in this sub-index link to files in the main INDEX-MASTER. File IDs are globally unique — cross-references work regardless of which index contains the entry.

---

## LEARN Files

### LEARN-004
- **Type:** LEARN
- **File:** learnings/LEARN-004_context-engineering-for-claude-code.md
- **Tags:** context-engineering, claude-code, knowledge-files, token-management, research-workflow, CLAUDE-files
- **Links:** SPEC-000, LEARN-001, LEARN-002
- **Backlinks:** LEARN-005, LEARN-006, LEARN-017, LEARN-024
- **Vitality:** 18.0
- **Summary:** Distilled from Thomas Landgraf's Substack article on context engineering for Claude Code. Defines three pillars of context engineering: project architecture knowledge (CLAUDE files), product requirements (PRD files), and deep technical knowledge documents. Documents a concrete three-step research workflow: (1) OpenAI Deep Research for exhaustive breadth (25-36 pages, 100+ citations, 7-30min), (2) Claude Research for rapid refinement (~0% hallucination, 2-5min), (3) synthesis into master knowledge documents. Key best practices: rigorous expert review of knowledge files (one bad API pattern poisons all future sessions), strategic splitting at 50KB threshold, token management via `/compact` and `/clear`, and living documentation via `@path` code references. Token economics: front-loaded knowledge docs beat real-time research by orders of magnitude ($40-70 per research session vs. near-zero for pre-computed docs). Strongly validates our brain architecture — fat indexing, modular files, and session management all align with these emerging best practices.
- **Key decisions:** Three actionable items identified: (1) adopt `@path` code references in LEARN/SPEC files, (2) use 50KB as splitting threshold, (3) consider two-phase research workflow for `brain ingest`.
- **Interface:** N/A (learning, not code)
- **Known issues:** Article focuses on Claude Code specifically — some advice (CLAUDE files, /compact) is tool-specific and may not generalize to other LLM assistants.

### LEARN-005
- **Type:** LEARN
- **File:** learnings/LEARN-005_claude-code-official-best-practices.md
- **Tags:** claude-code, best-practices, context-management, CLAUDE-md, prompting, workflows, subagents, agent-sdk, hooks, skills, verification, session-management
- **Links:** SPEC-000, LEARN-004, LEARN-013, LEARN-014, LEARN-017, LEARN-018, LEARN-013, LEARN-014, LEARN-017, LEARN-018
- **Backlinks:** LEARN-006, LEARN-007, LEARN-008, LEARN-009, LEARN-010, LEARN-013, LEARN-014, LEARN-015, LEARN-016, LEARN-017, LEARN-018, LEARN-019, LEARN-024, LOG-003, RULE-002, RULE-003, LEARN-039 _(17 inbound — secondary hub)_
- **Vitality:** 60.0
- **Summary:** Comprehensive operational playbook from Anthropic's official Claude Code best practices. Core constraint: context window is #1 resource. Covers 9 areas: (1) Verification as highest-leverage practice; (2) Explore→Plan→Implement→Commit 4-phase workflow with Plan Mode (Shift+Tab toggle); (3) Specific context in prompts; (4) CLAUDE.md authoring — include/exclude rules, @path imports, pruning; (5) Environment config — permissions, CLI tools, MCP, hooks, skills, subagents, plugins; (6) Communication — codebase questions, interview pattern; (7) Session management — course-correct after 2 failures, compaction; (8) Agent SDK (formerly headless mode) — `claude -p`, fan-out, writer/reviewer; (9) Five anti-patterns. Seven brain takeaways. **Note:** Topics introduced here are expanded in depth by later LEARNs: MCP (013), Agent SDK (014), costs/settings (017), workflows (018).
- **Key decisions:** Seven actionable items. Most impactful: skills/CLAUDE.md @path as brain delivery mechanism; anti-patterns as depositworthy RULE file.
- **Interface:** N/A (learning, not code)
- **Known issues:** Source may update as Claude Code evolves. Later LEARNs supersede this on specific topics (MCP, SDK, costs, workflows) but this remains the best single-file operational overview.

### LEARN-006
- **Type:** LEARN
- **File:** learnings/LEARN-006_claude-code-memory-system.md
- **Tags:** claude-code, CLAUDE-md, auto-memory, memory-hierarchy, rules, imports, configuration
- **Links:** SPEC-000, LEARN-004, LEARN-005
- **Backlinks:** LEARN-007, LEARN-010, LEARN-011, LEARN-017, LEARN-019, LOG-003
- **Vitality:** 24.5
- **Summary:** Deep dive into Claude Code's memory system from official docs. Two memory types: auto memory (Claude writes for itself, 200-line MEMORY.md index + topic files) and CLAUDE.md (user-written instructions). Full 6-level hierarchy with priority order: managed policy → project memory → project rules → user memory → project local → auto memory. Covers `@path` import syntax (relative resolution, max depth 5, approval dialog), `.claude/rules/*.md` modular rules with path-specific conditional rules (YAML frontmatter `paths` field with glob patterns), user-level rules at `~/.claude/rules/`, symlinks for cross-project sharing, and `--add-dir` for multi-directory access. Key finding: auto memory's architecture (200-line index + topic files loaded on demand) independently converges on our fat-index pattern — strong validation. Path-specific rules could scope brain knowledge to relevant code areas.
- **Key decisions:** Five brain-relevant takeaways: auto memory parallels brain system; `.claude/rules/*.md` maps to our RULE files; `@path` imports as brain delivery mechanism; path-specific rules for context-scoped knowledge; symlinks for cross-project brain sharing.
- **Interface:** N/A (learning, not code)
- **Known issues:** Auto memory is still rolling out gradually (opt-in via `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0`). Relationship between auto memory and brain system needs practical testing.

### LEARN-007
- **Type:** LEARN
- **File:** learnings/LEARN-007_claude-code-skills-system.md
- **Tags:** claude-code, skills, SKILL-md, slash-commands, workflows, configuration
- **Links:** SPEC-000, LEARN-005, LEARN-006
- **Backlinks:** LEARN-008, LEARN-009, LEARN-016, LEARN-019, LOG-003, RULE-003
- **Vitality:** 24.0
- **Summary:** Comprehensive reference for Claude Code's skills system from official docs. Skills = SKILL.md files with YAML frontmatter + markdown instructions. Two content types: reference (knowledge applied to current work, runs inline) and task (step-by-step workflows, often manual-only). Full frontmatter reference: name, description, argument-hint, disable-model-invocation, user-invocable, allowed-tools, model, context (fork for subagent execution), agent, hooks. Invocation control matrix: default (both user+Claude), disable-model-invocation (user only), user-invocable:false (Claude only). String substitutions ($ARGUMENTS, $N, ${CLAUDE_SESSION_ID}). Dynamic context injection via `!`command`` preprocessing. Supporting files pattern (SKILL.md under 500 lines, details in separate files). Context budget: 2% of window for skill descriptions (fallback 16K chars). Follows Agent Skills open standard (agentskills.io).
- **Key decisions:** Six brain-relevant takeaways: skills ARE the delivery mechanism for brain knowledge; `disable-model-invocation` for brain workflows; supporting files pattern maps to brain architecture; dynamic context injection for brain search; context budget constrains how many skills can exist; `context:fork` for isolated brain operations.
- **Interface:** N/A (learning, not code)
- **Known issues:** Context budget (2% of window) limits total skill count. Brain system needs to be selective about which knowledge becomes a skill vs. stays as a brain file.

### LEARN-008
- **Type:** LEARN
- **File:** learnings/LEARN-008_claude-code-hooks-system.md
- **Tags:** claude-code, hooks, automation, lifecycle, deterministic, configuration
- **Links:** SPEC-000, LEARN-005, LEARN-007, LEARN-015, LEARN-016
- **Backlinks:** LEARN-013, LEARN-016, LEARN-019, LOG-003, RULE-001, RULE-004
- **Vitality:** 26.0
- **Summary:** Combined reference + guide for Claude Code's hooks system from official docs. 14 lifecycle events (SessionStart through SessionEnd), three hook types (command, prompt, agent), full JSON input/output schemas, exit code protocol (0=proceed, 2=block, other=log), and decision control patterns per event. Detailed coverage of: PreToolUse decision control (allow/deny/ask + updatedInput), matcher patterns (regex on tool names, session sources, notification types), async hooks (background execution, no blocking), MCP tool matching (mcp__server__tool pattern), SessionStart environment persistence (CLAUDE_ENV_FILE), prompt-based hooks (single-turn LLM evaluation, ok/reason response), agent-based hooks (multi-turn subagent with tools, up to 50 turns). Six hook locations by scope (user → project → local → managed → plugin → skill/agent frontmatter). Practical patterns: desktop notifications, auto-format after edits, block protected files, re-inject context after compaction.
- **Key decisions:** Seven brain-relevant takeaways: SessionStart hooks for brain loading; PreCompact hooks for brain preservation; PostToolUse hooks for auto-deposit after commits; Stop hooks as quality gates for session handoff; SessionEnd hooks for auto-handoff; UserPromptSubmit for brain-aware context routing; async hooks for background brain indexing.
- **Interface:** N/A (learning, not code)
- **Known issues:** Hooks snapshot at startup — mid-session changes need review in /hooks menu. Prompt/agent hooks add latency. Stop hooks can loop infinitely without stop_hook_active guard.

### LEARN-009
- **Type:** LEARN
- **File:** learnings/LEARN-009_claude-code-subagents-system.md
- **Tags:** claude-code, subagents, delegation, context-isolation, custom-agents, persistent-memory
- **Links:** SPEC-000, LEARN-005, LEARN-007
- **Backlinks:** LEARN-011, LEARN-015, LEARN-016, LEARN-026, LEARN-027, SPEC-001, LEARN-039
- **Vitality:** 24.0
- **Summary:** Full subagent system reference from official docs. Built-in agents: Explore (Haiku, read-only, fast), Plan (inherits, read-only), general-purpose (inherits, all tools), Bash, statusline-setup, Claude Code Guide. Custom agents via `.claude/agents/*.md` with YAML frontmatter: name, description, tools/disallowedTools, model, permissionMode (6 modes), maxTurns, skills (preloaded), mcpServers, hooks, memory. Four storage locations with priority: CLI flag → project → user → plugin. Key feature: **persistent memory** with three scopes (user/project/local) — MEMORY.md index (200 lines loaded) + topic files, independently converging on our fat-index architecture. Foreground vs background execution (Ctrl+B to background). Resumable subagents (preserves full conversation history). CLI-defined agents via `--agents` JSON for session-only testing. Task tool restrictions for controlling which subagents can be spawned. Subagents cannot spawn other subagents.
- **Key decisions:** Six brain-relevant takeaways: brain-searcher subagent (Explore/Haiku for cheap lookups); persistent memory parallels brain system; brain-depositor subagent (Write access, Haiku); skills preloading for brain-aware agents; background subagents for brain maintenance; CLI-defined agents for brain CI/CD automation.
- **Interface:** N/A (learning, not code)
- **Known issues:** Subagents can't spawn subagents — limits recursive brain operations. Background subagents can't use MCP tools. Context from many completed subagents can bloat main conversation. **Custom agents (.claude/agents/) cannot be spawned via Task tool** — user-invoked only; workaround: inject custom agent prompt into general-purpose Task. **Background subagents denied Write permissions** in default mode — must resume in foreground or extract output from main agent.

### LEARN-010
- **Type:** LEARN
- **File:** learnings/LEARN-010_claude-code-architecture-internals.md
- **Tags:** claude-code, architecture, agentic-loop, tools, context-window, sessions, checkpoints
- **Links:** SPEC-000, LEARN-005, LEARN-006, LEARN-013, LEARN-014, LEARN-017
- **Backlinks:** LEARN-013, LEARN-014, LEARN-017, LEARN-018, RULE-002, LEARN-034, LEARN-039
- **Vitality:** 27.5
- **Summary:** Claude Code architecture overview from official docs. Agentic loop: gather context → take action → verify results (phases blend, Claude chains dozens of actions). Claude Code = the agentic harness providing tools, context management, and execution environment. Five tool categories: file operations, search, execution, web, code intelligence (plugins). Session model: each session starts fresh (no cross-session memory except auto memory + CLAUDE.md), sessions tied to directory, branch-aware (switch branches = new files same history), resume/fork support. Context window management: auto-compaction clears old tool outputs then summarizes, preserves requests + key code, may lose early instructions → put persistent rules in CLAUDE.md. Skills load on demand, subagents get fresh context. Two safety mechanisms: checkpoints (every edit snapshots, Esc+Esc to rewind, local to session, separate from git) and permissions (4 modes via Shift+Tab: default, auto-accept edits, plan mode, delegate mode).
- **Key decisions:** Six brain-relevant takeaways: agentic loop validates search→work separation; session independence is why brains exist; compaction = information loss (validates SESSION-HANDOFF); checkpoints as safety net for brain operations; fork sessions for brain experiments; MCP context cost monitoring important for brain MCP wrapper.
- **Interface:** N/A (learning, not code)
- **Known issues:** Checkpoints only cover Claude's file changes, not external processes. Session-scoped permissions not restored on resume.

### LEARN-013
- **Type:** LEARN
- **File:** learnings/LEARN-013_claude-code-mcp-system.md
- **Tags:** claude-code, MCP, model-context-protocol, transports, tools, resources, prompts, brain-server
- **Links:** SPEC-000, LEARN-002, LEARN-005, LEARN-008, LEARN-010
- **Backlinks:** LEARN-005, LEARN-010, LEARN-014, LEARN-016, LEARN-023, LEARN-028, LEARN-040, CODE-001, LEARN-041
- **Vitality:** 27.0
- **Summary:** Comprehensive MCP reference from official docs. Three transport types (HTTP recommended, SSE deprecated, stdio for local). Three scoping levels (local > project > user) with `.mcp.json` format supporting `${VAR:-default}` env var expansion. OAuth 2.0 and header-based auth. Output limits (10K warning, 25K max, `MAX_MCP_OUTPUT_TOKENS` override). Tool Search auto-activates at 10% context to defer MCP tools (requires Sonnet 4+/Opus 4+). MCP Resources as @-mentionable attachments (`@server:protocol://path`). MCP Prompts as slash commands (`/mcp__server__prompt`). `claude mcp serve` exposes Claude as MCP server. Plugin-bundled servers with `${CLAUDE_PLUGIN_ROOT}`. Enterprise managed MCP with allowlist/denylist. Anthropic MCP Registry API. **Brain MCP server architecture fully viable:** stdio transport, tools (search/read/index), resources (@-mentionable brain files), prompts (slash-command workflows), user-scoped cross-project.
- **Key decisions:** Brain MCP server confirmed as high-priority implementation target (validates LEARN-002 #1 ranking).
- **Interface:** N/A (learning, not code)
- **Known issues:** Brain MCP responses should stay under 10K tokens. Windows stdio servers using npx need `cmd /c` wrapper (Python avoids this).

### LEARN-014
- **Type:** LEARN
- **File:** learnings/LEARN-014_claude-code-agent-sdk.md
- **Tags:** claude-code, agent-sdk, headless, programmatic, automation, python, typescript, MCP-tools
- **Links:** SPEC-000, LEARN-005, LEARN-010, LEARN-013
- **Backlinks:** LEARN-005, LEARN-010, LEARN-018, LEARN-037, LEARN-039
- **Vitality:** 17.0
- **Summary:** Full Agent SDK reference (renamed from "Claude Code SDK"). Two packages: `pip install claude-agent-sdk` (Python), `npm install @anthropic-ai/claude-agent-sdk` (TypeScript). Two interfaces: `query()` (one-shot, no hooks/MCP) vs `ClaudeSDKClient` (multi-turn, hooks, custom MCP tools, interrupts). Key options: `system_prompt` preset+append, `setting_sources` (defaults to None — SDK does NOT load CLAUDE.md unless explicit), `max_turns`/`max_budget_usd` for cost caps, `output_format` for JSON schema validation, `agents` for programmatic subagents, `can_use_tool` for permission callbacks with input modification. In-process custom MCP tools via `@tool` decorator + `create_sdk_mcp_server()`. Programmatic hooks as Python callbacks (not shell scripts). `ResultMessage` includes `total_cost_usd` for cost tracking. 1M context beta via `betas=["context-1m-2025-08-07"]`. SDK is the correct infrastructure for brain automation.
- **Key decisions:** Agent SDK identified as brain automation engine. Critical constraint: `setting_sources` defaults to None.
- **Interface:** N/A (learning, not code)
- **Known issues:** Python hooks missing SessionStart/SessionEnd/Notification events (TypeScript only). "Headless mode" officially renamed to "Agent SDK."

### LEARN-015
- **Type:** LEARN
- **File:** learnings/LEARN-015_claude-code-agent-teams.md
- **Tags:** claude-code, agent-teams, coordination, multi-agent, task-list, messaging, experimental
- **Links:** SPEC-000, LEARN-005, LEARN-009
- **Backlinks:** LEARN-008, LEARN-026, LEARN-027, SPEC-001
- **Vitality:** 18.5
- **Summary:** Agent teams are full independent Claude Code sessions (not subagent child processes) connected by shared task list + inter-agent mailbox. Four components: team lead, teammates, file-locked task list (pending/in-progress/completed with dependency tracking), and mailbox (direct or broadcast messaging). Teammates form a mesh (any-to-any), unlike subagents (child-to-parent only). Delegate mode restricts lead to coordination-only. Plan approval gates require teammate plans before implementation. Team-specific hook events (TeammateIdle, TaskCompleted — already in LEARN-008) only fire during team sessions. Context critical: teammates do NOT inherit lead's conversation — all context via spawn prompt or CLAUDE.md/skills. Experimental: requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Uses ~7x tokens vs standard sessions.
- **Key decisions:** Agent teams identified as coordination layer for complex brain operations (parallel ingestion, multi-area search, maintenance). High cost (7x) limits to high-value operations.
- **Interface:** N/A (learning, not code)
- **Known issues:** Experimental feature. No session resumption with in-process teammates. Task status can lag. No nested teams. Split panes not on Windows Terminal. ~7x token cost limits to high-value operations.

### LEARN-016
- **Type:** LEARN
- **File:** learnings/LEARN-016_claude-code-plugin-system.md
- **Tags:** claude-code, plugins, packaging, distribution, plugin-json, namespacing, marketplace
- **Links:** SPEC-000, LEARN-005, LEARN-007, LEARN-008, LEARN-009, LEARN-013
- **Backlinks:** LEARN-008
- **Vitality:** 12.5
- **Summary:** Complete plugin system for packaging skills, agents, hooks, MCP servers, and LSP servers as distributable units. Plugin = directory with `.claude-plugin/plugin.json` manifest (only `name` required). Components go at plugin root (NOT inside `.claude-plugin/` — silent failure gotcha). Auto-namespacing: `/<plugin-name>:<skill-name>`. Four installation scopes (user/project/local/managed). Five distribution sources (path/npm/pip/github/url). Plugins cached — do NOT run in-place, use `${CLAUDE_PLUGIN_ROOT}` for all paths. Plugin MCP servers auto-start. CLI: `--plugin-dir` for dev testing. Migration from `.claude/` to plugin is straightforward. **Architecture split for brain**: engine (templates, skills, hooks, agents) in cached plugin vs data (learnings, specs, logs) project-local. Distribution aligns with Brain Hub concept (LOG-001).
- **Key decisions:** Plugin system is the distribution mechanism for brain system. Engine/data split is a key architecture decision.
- **Interface:** N/A (learning, not code)
- **Known issues:** Plugin caching breaks path traversal — `${CLAUDE_PLUGIN_ROOT}` must be used everywhere. 2% context budget limits total skill count in plugins.

### LEARN-017
- **Type:** LEARN
- **File:** learnings/LEARN-017_claude-code-costs-settings-environment.md
- **Tags:** claude-code, costs, settings, environment-variables, configuration, token-management, optimization
- **Links:** SPEC-000, LEARN-004, LEARN-005, LEARN-006, LEARN-010
- **Backlinks:** LEARN-005, LEARN-010, LEARN-018
- **Vitality:** 17.5
- **Summary:** Quantitative cost baseline: $6/dev/day average, 90% under $12, ~$100-200/dev/month API, agent teams ~7x overhead, background sessions $0.04. Rate limits by team size (200-300k TPM solo → 10-15k TPM at 500+ users). Complete 5-level settings hierarchy: managed → CLI → local → shared → user, with precise file paths for all OS. Full settings.json key reference including `model`, `availableModels`, `cleanupPeriodDays`, `env`, `fileSuggestion`, `respectGitignore`. 50+ environment variables for model/token/cost/feature control. Key vars: `CLAUDE_CODE_EFFORT_LEVEL` (low/med/high), `CLAUDE_CODE_SUBAGENT_MODEL`, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` (~95% default), `ENABLE_TOOL_SEARCH`. Complete permissions syntax with `additionalDirectories` for cross-directory brain access. Cost strategies: CLAUDE.md under ~500 lines, prompt caching benefits static brain files maximally, subagent model selection.
- **Key decisions:** Brain operations quantifiably budgetable. Key optimizations: effort_level=low for maintenance, subagent_model=haiku for lookups, never disable prompt caching for brain projects.
- **Interface:** N/A (learning, not code)
- **Known issues:** Rate limits are org-level — brain automation competes with interactive usage. CLAUDE_AUTOCOMPACT_PCT_OVERRIDE default confirmed ~95%.

### LEARN-018
- **Type:** LEARN
- **File:** learnings/LEARN-018_claude-code-common-workflows-and-patterns.md
- **Tags:** claude-code, workflows, plan-mode, extended-thinking, recipes, automation, patterns
- **Links:** SPEC-000, LEARN-005, LEARN-010, LEARN-014, LEARN-017
- **Backlinks:** LEARN-005, LEARN-029, RULE-002, RULE-003
- **Vitality:** 20.5
- **Summary:** Concrete operational recipes and details from common-workflows docs. Plan Mode mechanics: Shift+Tab cycles modes, `--permission-mode plan` flag, **headless Plan Mode** (`claude --permission-mode plan -p "query"`) for zero-risk read-only analysis (ideal for brain search). Extended thinking: enabled by default, Opus 4.6 uses adaptive reasoning (effort levels), `MAX_THINKING_TOKENS` env var, Alt+T toggle, **"think"/"ultrathink" are NOT special keywords**. Four reusable workflow recipe shapes: Explore (overview→architecture→models→component), Debug (error→options→fix→verify), Refactor (find→recommend→apply→verify), Test (uncovered→scaffold→edge cases→verify). PR creation via `/commit-push-pr` skill with auto-Slack-posting, `--from-pr <number>` session linking. `@` references auto-load CLAUDE.md from referenced file's directory — zero-config brain discoverability. Git worktrees for parallel brain sessions. `--output-format json` includes cost+duration metadata.
- **Key decisions:** Headless Plan Mode identified as ideal brain search mechanism. Four RESET template variants identified but not yet created.
- **Interface:** N/A (learning, not code)
- **Known issues:** Plan Mode Ctrl+G (editor export) vs Shift+Tab (mode cycling) are different functions — LEARN-005 conflates slightly.

### LEARN-019
- **Type:** LEARN
- **File:** learnings/LEARN-019_claude-code-brain-integration-layers-1-3.md
- **Tags:** claude-code, integration, CLAUDE-md, rules, skills, hooks, automation, brain-delivery, testing, windows, matcher-format
- **Links:** SPEC-000, LEARN-005, LEARN-006, LEARN-007, LEARN-008, LOG-003
- **Backlinks:** RULE-001, RULE-003, RULE-004, LEARN-034, LEARN-041
- **Vitality:** 23.5
- **Summary:** Documents implementation AND test results of Claude Code native integration (Layers 1-3). Eight files: CLAUDE.md (@path import of INIT.md), 3 rules, 4 skills, 4 hooks. **Tested:** Layer 1 (CLAUDE.md + rules) fully working including @path with spaces in Windows paths. Layer 2 (skills) all 4 working after fixing `disable-model-invocation: true → false`; skills also fail CLI `/` resolution when project path contains spaces — workaround is copying to user-level `~/.claude/skills/`. Layer 3 (hooks) **CRITICAL FIX:** `matcher` must be a string regex or omitted — using JSON objects (`{}`, `{"tools": [...]}`) causes a Settings Error that silently disables ALL hooks. Stop hook FAILED due to this — session exited without blocking. Fixed: PostToolUse matcher changed to `"Edit|Write"` string; all other matchers omitted. Contains gotchas section covering: `disable-model-invocation` visibility, `chr(92)` pattern, hooks snapshot at startup, hooks format migration (corrected), and skills spaces-in-path bug.
- **Key decisions:** @path imports INIT.md (not INDEX-MASTER — too large); `disable-model-invocation: false`; PostToolUse uses `"Edit|Write"` string matcher + `chr(92)` path normalization; hooks use matcher-based format with **string matchers only**; skills copied to user-level `~/.claude/skills/` for CLI resolution.
- **Interface:** N/A (learning, not code)
- **Known issues:** Prompt-type hooks unreliable for Stop events — use command-type with exit codes. PreCompact hook not testable on demand (simple echo, trivially correct). All other components fully tested and passing as of 2026-02-15 cleanup session. Duplicate skills resolved (project-level copies removed).

### LEARN-039
- **Type:** LEARN
- **File:** learnings/LEARN-039_anthropic-agent-sdk-practical-design-patterns.md
- **Tags:** anthropic, agent-sdk, agents, feedback-loop, context-gathering, verification, tool-design, code-generation, evaluation, practical-patterns
- **Links:** LEARN-038, LEARN-014, LEARN-010, LEARN-005, LEARN-009
- **Backlinks:** _(none)_
- **Vitality:** 8.0
- **Summary:** Anthropic's practical guide for building agents with the Claude Agent SDK. Complements LEARN-038 (what pattern) with HOW to implement. Four-stage feedback loop (gather → act → verify → iterate). **Context gathering hierarchy** ranked: agentic search (bash/grep, start here) > semantic search (fast, opaque) > subagents (parallel, isolated) > compaction (prevents exhaustion). File system structure IS context engineering. **Verification taxonomy** ranked: rules-based (linting, TypeScript) > visual (screenshots, Playwright) > LLM-as-judge (fuzzy, latency). **Tool prominence = prioritization** — position in context affects agent usage. Code generation > natural language for precise, composable, reusable outputs. Agent evaluation checklist: sufficient info? appropriate tools? creative alternatives? representative tests?
- **Key decisions:** None — ingested knowledge. Context gathering hierarchy and verification taxonomy are most actionable for brain/Prover agent design.
- **Interface:** N/A (learning, not code)
- **Known issues:** WebFetch returned summarized content — full code examples not captured. Article may evolve with SDK.

---

## LOG Files

### LOG-003
- **Type:** LOG
- **File:** logs/LOG-003_brain-to-claude-code-delivery-mechanisms.md
- **Tags:** integration, delivery, skills, rules, imports, claude-code, architecture
- **Links:** SPEC-000, LEARN-005, LEARN-006, LEARN-007, LEARN-008
- **Backlinks:** LEARN-019
- **Vitality:** 11.5
- **Summary:** Analysis of four mechanisms for delivering brain knowledge into Claude Code sessions: (1) `.claude/skills/` — on-demand via slash commands, best for task-specific brain operations, constrained by 2% context budget; (2) `.claude/rules/*.md` — always loaded, path-scoped, best for session hygiene rules, lowest effort; (3) `@path` imports in CLAUDE.md — selective, stable references, best for architecture specs; (4) auto memory — Claude-controlled, not for structured domain knowledge. Concludes mechanisms are complementary, not competing. Layered architecture: rules for always-on hygiene, skills for on-demand operations, @path for stable knowledge, auto memory for Claude's own housekeeping. Open question: which to implement first (skills = highest impact/effort, rules = lowest effort/power).
- **Key decisions:** Not yet made — analysis only. Likely first step: rules (trivial) then skills (impactful). May need `brain export --target claude-code` command.
- **Interface:** N/A (decision log, not code)
- **Known issues:** Revisit when starting Phase 2 implementation and when auto memory exits opt-in.
