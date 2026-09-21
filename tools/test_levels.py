import copy
import pathlib

import pytest
import yaml

from levels import max_level, required_controls
from validate import _to_json, check

ROOT = pathlib.Path(__file__).resolve().parent.parent


def answers(**overrides):
    a = {f"Q{i}": 0 for i in range(1, 9)}
    a.update(overrides)
    return a


@pytest.mark.parametrize("score,level", [(0, "L5"), (3, "L5"), (4, "L4"), (6, "L4"),
                                         (7, "L3"), (9, "L3"), (10, "L2"), (12, "L2"),
                                         (13, "L1"), (16, "L1")])
def test_thresholds(score, level):
    a = answers()
    remaining = score
    for q in a:
        a[q] = min(2, remaining)
        remaining -= a[q]
    # keep the Q1+Q7 cap out of the threshold test
    if a["Q1"] == 2 and a["Q7"] == 2 and level in ("L4", "L5"):
        pytest.skip("cap case covered separately")
    assert max_level(a) == (score, level)


def test_irreversible_action_on_people_caps_at_l3():
    assert max_level(answers(Q1=2, Q7=2)) == (4, "L3")


def test_invalid_answer_rejected():
    with pytest.raises(ValueError):
        max_level(answers(Q3=3))


def test_required_controls_cumulative_and_l1_only_rule():
    assert "AL-05" in required_controls("L1")
    assert "AL-05" not in required_controls("L2")
    assert len(required_controls("L5")) == 15
    assert set(required_controls("L3")) < set(required_controls("L4"))


def load_example():
    return _to_json(yaml.safe_load((ROOT / "templates" / "certificate.example.yaml").read_text()))


def test_example_certificate_is_valid():
    assert check(load_example()) == []


def test_missing_control_fails():
    cert = load_example()
    cert["controls"]["in_place"].remove("AL-11")
    assert any("AL-11" in e for e in check(cert))


def test_level_above_max_fails():
    cert = load_example()
    cert["level"] = "L5"
    cert["controls"]["in_place"] += ["AL-14", "AL-15", "AL-16"]
    assert any("exceeds max_level" in e for e in check(cert))


def test_l1_with_writes_fails():
    cert = copy.deepcopy(load_example())
    cert["level"] = "L1"
    cert["controls"]["in_place"] = required_controls("L1")
    assert any("AL-05" in e for e in check(cert))
