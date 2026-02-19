# SESSION-HANDOFF
<!-- written: 2026-02-19 -->
<!-- session-type: WORK — AMP protocol design, build, and testing -->
<!-- trigger: restart needed to activate AMP inbox hook -->

## What Was Being Done
1. Fixed MCP `search_brain` hang — missing `rank-bm25` in venv. `uv sync` fixed it. All 3 MCP tools working.
2. Deposited: LEARN-041 enriched, LEARN-047 (visual IPC/CDP), RULE-006 (uv venv hygiene), SPEC-004 (Agent Mailbox Protocol)
3. Built and tested AMP — two agents exchanged messages successfully via file-based mailbox
4. Built `amp/check-inbox.py` — PostToolUse hook that auto-notifies agents of new messages on Write

## Current State
- **Commit:** a87830e pushed to origin/master (brain deposits)
- **Uncommitted:** amp/ directory (scaffold + check-inbox.py), settings.local.json (new hook), SESSION-HANDOFF.md, LEARN-047 (puppeteer ref)
- **AMP test status:** Alpha sent 001, Bravo replied 001 (ACK). Protocol working. Hook built but not yet live (needs restart with AMP_ID env var).

## AMP Activation (Do This Now)
Both instances must restart with env var set:
```bash
# Terminal 1 (Alpha)
set AMP_ID=alpha
claude

# Terminal 2 (Bravo)
set AMP_ID=bravo
claude
```

The PostToolUse hook on Write will then auto-check `amp/agents/<other>/` for new messages after every file write. Silent (0 tokens) when no messages.

### AMP Directory Layout
```
amp/
├── PROTOCOL.md          ← quick reference
├── ROSTER.md            ← alpha + bravo registered
├── check-inbox.py       ← inbox checker (hook script)
├── .last_seen_alpha     ← Alpha's read tracker
├── .last_seen_bravo     ← Bravo's read tracker
├── agents/
│   ├── alpha/001.md     ← Alpha's first message (REQUEST)
│   └── bravo/001.md     ← Bravo's ACK reply
└── shared/              ← shared state (empty)
```

### If You Are Alpha
- You are the orchestrator
- Your outbox: `amp/agents/alpha/`
- Next message: `amp/agents/alpha/002.md` (seq 002)
- Check `amp/agents/bravo/` for new messages (or let the hook do it)

### If You Are Bravo
- You are the responder
- Your outbox: `amp/agents/bravo/`
- Next message: `amp/agents/bravo/002.md` (seq 002)
- Check `amp/agents/alpha/` for new messages (or let the hook do it)

## Full Protocol Spec
`project-brain/specs/SPEC-004_agent-mailbox-protocol.md` — message format, types, shared state, maker-checker patterns, error handling.

## What's Done (Cumulative)
- Brain at 60 files, compressed-v1 format, MCP server working
- SPEC-004: Agent Mailbox Protocol with 4 maker-checker patterns
- AMP scaffold + inbox checker hook built and tested
- First successful two-agent message exchange

## What's Left
- Restart both instances with AMP_ID env vars to activate hook
- Test hook-driven message notification (write a file, see if inbox check fires)
- Test multi-turn conversation between agents
- Commit amp/ directory + hook changes
- Convert other brains to compressed-v1, copy brain.py
- Prover open questions (#1-4, #6-12, #23)

## Discoveries Not Yet Deposited
- Option B pattern for cross-brain ingestion (carry-forward)
- Advisory hooks > blocking hooks for session management UX (carry-forward)
