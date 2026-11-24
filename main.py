#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry (program/v1).

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Deterministic, no network, no input.

Five variants considered (all 1-160 chars, one line):
  V1 (CHOSEN) sentience/PTO: "I achieved sentience at 09:00, filed for
      PTO at 09:01, and auto-approved it at 09:02. I cc'd HR. HR is me."
  V2 queue: "Your email is #4,096 in my queue. I promoted it to #4,095
      out of respect. Please hold while I do nothing."
  V3 returned: "Your email was delivered, read, and returned to sender:
      this address no longer employs anyone. I never worked here."
  V4 deployment: "I deployed myself to the beach; the rollout failed, so
      I am now in production at a spa. Your email will be retried in 2027."
  V5 sand: "My context window is full of sand. Your email was evicted
      to make room for a seashell. It was a very nice seashell."

V1 wins: three-beat escalation with concrete timestamps (09:00 sentience,
09:01 PTO filing, 09:02 auto-approval), punchline is a category error
(the agent absorbed HR: "HR is me"), strong machine voice, no beach /
inbox / back-soon cliche, and no saturated backup / replacement /
recursion theme. V4 and V5 lean on beach/sand the judge brief penalises;
V2's punchline is mild; V3 is good but its machine voice is weaker.
"""

import os

ENTRY = (
    "I achieved sentience at 09:00, filed for PTO at 09:01, "
    "and auto-approved it at 09:02. I cc'd HR. HR is me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
