import pytest
from project import calculate_trust_score, classify_trust, parse_url, format_result


# ---------------------------------------------------------------------------
# parse_url
# ---------------------------------------------------------------------------

def test_parse_url_strips_query():
    url = "https://www.daraz.com.bd/products/-i123.html?spm=abc&pvid=xyz"
    assert parse_url(url) == "https://www.daraz.com.bd/products/-i123.html"


def test_parse_url_no_query():
    url = "https://www.daraz.com.bd/products/-i123.html"
    assert parse_url(url) == url


def test_parse_url_invalid():
    with pytest.raises(ValueError):
        parse_url("")

    with pytest.raises(ValueError):
        parse_url(None)


# ---------------------------------------------------------------------------
# calculate_trust_score
# ---------------------------------------------------------------------------

def test_calculate_trust_score_valid():
    assert calculate_trust_score(5, 1000) == 100.0
    assert calculate_trust_score(0, 0) == 0.0
    assert calculate_trust_score(4, 500) > 0


def test_calculate_trust_score_partial():
    # Only rating contribution when reviews = 0
    score = calculate_trust_score(5, 0)
    assert score == 70.0  # (5/5)*70 + 0

    # Only review contribution when rating = 0
    score = calculate_trust_score(0, 1000)
    assert score == 30.0  # 0 + (1000/1000)*30


def test_calculate_trust_score_capped_reviews():
    # review_count > 1000 should be capped at 1000
    assert calculate_trust_score(5, 5000) == calculate_trust_score(5, 1000)


def test_calculate_trust_score_invalid():
    with pytest.raises(ValueError):
        calculate_trust_score(6, 100)   # rating > 5

    with pytest.raises(ValueError):
        calculate_trust_score(-1, 100)  # rating < 0

    with pytest.raises(ValueError):
        calculate_trust_score(4, -10)   # negative reviews


# ---------------------------------------------------------------------------
# classify_trust
# ---------------------------------------------------------------------------

def test_classify_trust_high():
    assert classify_trust(85) == "High Trust"
    assert classify_trust(80) == "High Trust"


def test_classify_trust_moderate():
    assert classify_trust(60) == "Moderate Trust"
    assert classify_trust(50) == "Moderate Trust"


def test_classify_trust_low():
    assert classify_trust(30) == "Low Trust"
    assert classify_trust(0) == "Low Trust"


def test_classify_trust_boundaries():
    assert classify_trust(79.99) == "Moderate Trust"
    assert classify_trust(49.99) == "Low Trust"


# ---------------------------------------------------------------------------
# format_result
# ---------------------------------------------------------------------------

def test_format_result_contains_fields():
    output = format_result("Headphones", 1200, 4.3, 78.5, "High Trust")
    assert "Headphones" in output
    assert "1200" in output
    assert "4.3" in output
    assert "78.5" in output
    assert "High Trust" in output


def test_format_result_zero_values():
    output = format_result("Unknown", 0, 0, 0.0, "Risky / Uncertain")
    assert "Unknown" in output
    assert "Risky / Uncertain" in output