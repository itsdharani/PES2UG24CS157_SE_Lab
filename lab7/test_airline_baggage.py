from hypothesis import given, strategies as st
from airline_baggage import parse_booking, total_weight, tag_label


@given(st.one_of(st.text(), st.none()))
def test_parse_booking_no_crash(s):
    try:
        parse_booking(s)
    except Exception as e:
        assert False, f"parse_booking crashed with {s!r}: {e}"


@given(st.one_of(st.text(), st.none()))
def test_total_weight_no_crash(s):
    try:
        total_weight(s)
    except Exception as e:
        assert False, f"total_weight crashed with {s!r}: {e}"


@given(st.one_of(st.text(), st.none()))
def test_tag_label_no_crash(s):
    try:
        tag_label(s)
    except Exception as e:
        assert False, f"tag_label crashed with {s!r}: {e}"


def test_parse_booking_valid():
    assert parse_booking("AI-203-12A") == ("AI", 203, "A")


def test_parse_booking_invalid():
    assert parse_booking("AI-203") is None


def test_total_weight_valid():
    assert total_weight("12.5,7,23") == 42.5


def test_total_weight_invalid():
    assert total_weight("12,abc") is None


def test_tag_label_valid():
    assert tag_label("John Smith") == "J. SMITH"


def test_tag_label_invalid():
    assert tag_label("John") is None

