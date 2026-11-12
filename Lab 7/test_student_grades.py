from hypothesis import given, strategies as st
from student_grades import average_marks, parse_srn, short_name


# Test 1: average_marks
@given(st.text() | st.none())
def test_average_marks_no_crash(s):
    try:
        average_marks(s)
    except Exception as e:
        assert False, f"average_marks crashed with input {s!r}: {e}"


# Test 2: parse_srn
@given(st.text() | st.none())
def test_parse_srn_no_crash(s):
    try:
        parse_srn(s)
    except Exception as e:
        assert False, f"parse_srn crashed with input {s!r}: {e}"


# Test 3: short_name
@given(st.text() | st.none())
def test_short_name_no_crash(s):
    try:
        short_name(s)
    except Exception as e:
        assert False, f"short_name crashed with input {s!r}: {e}"