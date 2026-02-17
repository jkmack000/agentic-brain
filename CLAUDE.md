# Project Brain — Claude Code Integration

This workspace contains a **Project Brain** — a persistent long-term memory system for LLM sessions.

## Bootstrap

@project-brain/INIT.md

## Brain Location
All brain files live in `project-brain/`. The brain currently has 22+ knowledge files covering the brain system architecture, Claude Code internals, and integration patterns.

## Quick Reference
- **Start of session:** Check SESSION-HANDOFF.md, then load INDEX-MASTER.md
- **Find knowledge:** Scan fat index entries in INDEX-MASTER.md — don't open files speculatively
- **Deposit knowledge:** Create typed .md file (LEARN/LOG/SPEC/CODE/RULE) + update INDEX-MASTER.md
- **End of session:** Write SESSION-HANDOFF.md + append LOG-002 timeline entry

## File Types
| Type | Purpose | Directory |
|------|---------|-----------|
| SPEC | Design decisions, architecture | `project-brain/specs/` |
| CODE | Implementation documentation | `project-brain/code/` |
| RULE | Business rules, constraints | `project-brain/rules/` |
| LEARN | Discovered knowledge, insights | `project-brain/learnings/` |
| LOG | Decision rationale, timeline | `project-brain/logs/` |
| RESET | Pre-built context packages | `project-brain/reset-files/` |

## Brain Skills
- `/brain-search <query>` — Search fat indexes, return ranked results without opening files
- `/brain-deposit [TYPE] [desc]` — Guided deposit with dedup check
- `/brain-handoff` — Write SESSION-HANDOFF.md immediately
- `/brain-status` — File counts, orphans, index health

## Rules
Session hygiene, fat-index discipline, and ingestion dedup are enforced via `.claude/rules/`. These load automatically every session — no manual action needed.
