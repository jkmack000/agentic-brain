#!/usr/bin/env python3
"""AMP inbox checker — PostToolUse hook for Write tool.

Checks other agents' outboxes for new messages addressed to this agent.
Identity is set via AMP_ID environment variable. If unset, exits silently (0 tokens).

Usage in hook: uv run python amp/check-inbox.py
Env var: AMP_ID=alpha (or bravo, etc.)
"""
import os
import re
import sys
from pathlib import Path


def main():
    my_id = os.environ.get("AMP_ID")
    if not my_id:
        sys.exit(0)  # Not an AMP participant — silent, 0 tokens

    amp_root = Path(os.environ.get("AMP_ROOT", os.path.join(os.path.dirname(__file__))))
    agents_dir = amp_root / "agents"

    if not agents_dir.exists():
        sys.exit(0)

    # Track last-seen sequence per other agent
    tracker_file = amp_root / f".last_seen_{my_id}"
    last_seen = {}
    if tracker_file.exists():
        for line in tracker_file.read_text(encoding="utf-8").strip().split("\n"):
            if "=" in line:
                agent, seq = line.split("=", 1)
                try:
                    last_seen[agent] = int(seq)
                except ValueError:
                    pass

    new_messages = []

    for agent_dir in sorted(agents_dir.iterdir()):
        if not agent_dir.is_dir():
            continue
        other_id = agent_dir.name
        if other_id == my_id:
            continue

        last = last_seen.get(other_id, 0)

        # Find numbered message files
        for msg_file in sorted(agent_dir.glob("*.md")):
            try:
                seq = int(msg_file.stem)
            except ValueError:
                continue

            if seq <= last:
                continue

            content = msg_file.read_text(encoding="utf-8")

            # Check if addressed to me or broadcast
            to_match = re.search(r"<!--\s*to:\s*(\S+)\s*-->", content)
            if to_match:
                to_val = to_match.group(1)
                if to_val != my_id and to_val != "*":
                    continue

            new_messages.append((other_id, seq, content))
            last_seen[other_id] = max(last_seen.get(other_id, 0), seq)

    # Update tracker
    if last_seen:
        with open(tracker_file, "w", encoding="utf-8") as f:
            for agent, seq in sorted(last_seen.items()):
                f.write(f"{agent}={seq}\n")

    # Print new messages to stdout (injected into conversation)
    if new_messages:
        print(f"[AMP] {len(new_messages)} new message(s) in inbox:")
        for other_id, seq, content in new_messages:
            print(f"\n--- {other_id}/{seq:03d} ---")
            print(content.strip())
            print(f"--- end {other_id}/{seq:03d} ---")


if __name__ == "__main__":
    main()
