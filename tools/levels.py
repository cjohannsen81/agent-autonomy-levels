"""Shared definitions for the Autonomy Levels framework (FRAMEWORK.md)."""

LEVELS = ["L1", "L2", "L3", "L4", "L5"]
QUESTIONS = [f"Q{i}" for i in range(1, 9)]

# Level at which each control becomes required (FRAMEWORK.md section 4).
# AL-05 (no writes) applies to L1 only.
CONTROL_FROM = {
    "AL-01": "L1", "AL-02": "L1", "AL-03": "L1", "AL-04": "L1", "AL-05": "L1",
    "AL-06": "L2", "AL-07": "L2", "AL-08": "L2",
    "AL-09": "L3", "AL-10": "L3",
    "AL-11": "L4", "AL-12": "L4", "AL-13": "L4",
    "AL-14": "L5", "AL-15": "L5", "AL-16": "L5",
    "AL-17": "L1",
}
L1_ONLY = {"AL-05"}


def required_controls(level: str) -> list[str]:
    idx = LEVELS.index(level)
    return sorted(
        c for c, frm in CONTROL_FROM.items()
        if LEVELS.index(frm) <= idx and not (c in L1_ONLY and level != "L1")
    )


def max_level(answers: dict[str, int]) -> tuple[int, str]:
    """Return (score, maximum level) per FRAMEWORK.md section 5."""
    missing = [q for q in QUESTIONS if q not in answers]
    if missing:
        raise ValueError(f"missing answers: {', '.join(missing)}")
    for q in QUESTIONS:
        if answers[q] not in (0, 1, 2):
            raise ValueError(f"{q} must be 0, 1 or 2, got {answers[q]!r}")
    score = sum(answers[q] for q in QUESTIONS)
    if score <= 3:
        level = "L5"
    elif score <= 6:
        level = "L4"
    elif score <= 9:
        level = "L3"
    elif score <= 12:
        level = "L2"
    else:
        level = "L1"
    # Irreversible actions on people cap the use case at L3.
    if answers["Q1"] == 2 and answers["Q7"] == 2 and LEVELS.index(level) > LEVELS.index("L3"):
        level = "L3"
    return score, level
