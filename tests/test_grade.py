from app.main import grade


def test_grade_pass():
    assert grade(60) == "pass"
    assert grade(95) == "pass"


def test_grade_fail():
    assert grade(59) == "fail"
    assert grade(0) == "fail"

