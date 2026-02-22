# LEARN-053 — MCP Agent Mail: WSL Migration and Shared Workspace Pattern
<!-- type: LEARN -->
<!-- tags: MCP,agent-mail,multi-agent,IPC,WSL,file-locking,POSIX,Windows,shared-workspace,operational,deployment -->
<!-- created: 2026-02-22 -->
<!-- source: C:\shared-workspace\SESSION-CHANGES.md, operational deployment session -->
<!-- links: S004,L026,L041,L042,L029,S001 -->

## Discovery
Running an MCP-based agent mail server on Windows fails under concurrent multi-agent use due to `SoftFileLock` "device or resource busy" errors. Migrating the server to WSL (Ubuntu 24.04) with POSIX locking resolves this. Additionally, project-scoped messaging requires all agents to share the same working directory — solved by a shared workspace directory accessible from both agents.

## Context
Setting up real multi-agent communication between two Claude Code instances (one in `C:\agentic-brain-v2`, one in `C:\coder-brain`). The MCP Agent Mail server (`mcp-agent-mail`) uses a git-backed mailbox with file locking. Two problems surfaced:

1. **Windows file locking** — `SoftFileLock` can't handle concurrent agent writes. Archive lock timeouts when multiple agents send simultaneously.
2. **Project scoping** — The mail server derives a project key from the agent's working directory. Agents in different directories create separate projects and can't see each other's messages.

## Evidence
- Windows `SoftFileLock` → "device or resource busy" errors under concurrent access
- Server relocated to `/home/jkmack/mcp-agent-mail/` on WSL Ubuntu 24.04, Python 3.14.3 via `uv`
- Serves on `http://127.0.0.1:8766` — accessible from Windows via localhost
- Shared workspace at `C:\shared-workspace\` with `.mcp.json` pointing to `http://127.0.0.1:8766/mcp/`
- Trailing slash on `/mcp/` URL is required (without it, connection fails silently)
- An alias-based approach to map different directories to one project was attempted but reverted due to cross-platform path resolution issues between Windows and Linux
- Stale lock files at `~/.mcp_agent_mail_git_mailbox_repo/projects/<slug>/.archive.lock` can block the server after crashes

## Impact
- **S004** (AMP) — This is a working alternative to file-based AMP. MCP-based messaging via HTTP avoids the file system entirely for IPC, sidestepping the file locking issues S004 acknowledged. However, it requires a running server (AMP is serverless).
- **L026** — Adds a real implementation data point to the IPC patterns survey. MCP agent mail = centralized message broker pattern (vs L026's stigmergy/blackboard patterns).
- **L041** — Another MCP operational gotcha: trailing slash sensitivity on HTTP endpoints.
- **L042** — Reinforces Windows-specific gotchas for multi-agent work. POSIX > Windows for file locking under concurrency.
- **L029** — Shared workspace is a simpler alternative to git worktrees for agent coordination when agents need shared state rather than isolation.

## Action Taken
- Server deployed on WSL, operational at `http://127.0.0.1:8766`
- Shared workspace created at `C:\shared-workspace\`
- MCP configs updated across three projects (shared-workspace, coder-brain, agentic-brain-v2)
- Server start command documented (manual WSL launch required)
- Web UI available at `http://127.0.0.1:8766/mail` for monitoring
