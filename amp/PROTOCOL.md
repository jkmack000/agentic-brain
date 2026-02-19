# Agent Mailbox Protocol (AMP)
<!-- See SPEC-004 in project-brain for full specification -->

## Quick Rules
1. Write ONLY to your own outbox: `agents/<your-id>/`
2. Read others' outboxes to receive messages
3. Messages are individual .md files, numbered sequentially (001.md, 002.md, ...)
4. Check ROSTER.md for active agents
5. Use shared/ for coordinated state (claim before writing)

## Message Format
```markdown
<!-- amp-version: 1 -->
<!-- from: <your-id> -->
<!-- to: <recipient-id or * for broadcast> -->
<!-- seq: <NNN> -->
<!-- type: REQUEST|RESPONSE|STATUS|HANDOFF|ACK|ERROR|DONE -->
<!-- timestamp: <ISO 8601> -->
<!-- re: <agent-id/seq> (optional, reference to previous message) -->

## Subject
<one-line summary>

## Body
<full message content>
```
