import sys
import re

from scrape import DarazScraper
from senti import SentimentAnalyzer
from trust import TrustMeter


# ---------------------------------------------------------------------------
# Standalone functions (CS50P requirement: 3+ at module level, all testable)
# ---------------------------------------------------------------------------

def parse_url(url: str) -> str:
    """
    Strip query-string parameters from a Daraz product URL.

    >>> parse_url("https://www.daraz.com.bd/products/-i123.html?spm=abc")
    'https://www.daraz.com.bd/products/-i123.html'
    >>> parse_url("https://www.daraz.com.bd/products/-i123.html")
    'https://www.daraz.com.bd/products/-i123.html'
    """
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string.")
    url = url.strip()
    if "?" in url:
        url = url.split("?")[0]
    return url


def calculate_trust_score(rating: float, review_count: int) -> float:
    """
    Calculate a simple trust score (0–100) from rating and review count.

    Formula:
        score = (rating / 5) * 70  +  min(review_count, 1000) / 1000 * 30

    >>> calculate_trust_score(5, 1000)
    100.0
    >>> calculate_trust_score(0, 0)
    0.0
    """
    if rating < 0 or rating > 5:
        raise ValueError("Rating must be between 0 and 5.")
    if review_count < 0:
        raise ValueError("Review count cannot be negative.")

    score = (rating / 5) * 70 + min(review_count, 1000) / 1000 * 30
    return round(score, 2)


def classify_trust(score: float) -> str:
    """
    Return a human-readable trust label for a score in the range 0–100.

    >>> classify_trust(90)
    'High Trust'
    >>> classify_trust(65)
    'Moderate Trust'
    >>> classify_trust(20)
    'Low Trust'
    """
    if score >= 80:
        return "High Trust"
    elif score >= 50:
        return "Moderate Trust"
    else:
        return "Low Trust"


def format_result(title: str, price, rating, trust_score: float, trust_label: str) -> str:
    """
    Format the final analysis result as a human-readable string.

    >>> result = format_result("Test Product", 999, 4.5, 82.0, "High Trust")
    >>> "Test Product" in result and "High Trust" in result
    True
    """
    return (
        f"Product : {title}\n"
        f"Price   : ৳{price}\n"
        f"Rating  : {rating}/5\n"
        f"Trust   : {trust_score}/100 — {trust_label}"
    )


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    """
    Entry point.

    Usage:
        python project.py <daraz_product_url>

    Scrapes the given Daraz URL, runs sentiment analysis on reviews,
    computes a composite trust score, and prints a summary.
    """
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py <daraz_product_url>")

    raw_url = sys.argv[1]

    try:
        url = parse_url(raw_url)
    except ValueError as e:
        sys.exit(str(e))

    print(f"Analysing: {url}\n")

    # --- scrape ---
    scraper = DarazScraper(url)
    result = scraper.scrape()

    # --- sentiment ---
    analyzer = SentimentAnalyzer()
    comments = result.get("comments", [])
    if comments:
        sentiment = analyzer.sentiment_percentage(comments)
    else:
        sentiment = {"positive": 0, "negative": 0, "neutral": 0}

    # --- trust ---
    trust_meter = TrustMeter()
    trust = trust_meter.calculate_trust_score(
        rating=result["rating"],
        total_reviews=result["total_reviews"],
        sentiment_dict=sentiment,
    )

    # --- output ---
    output = format_result(
        title=result.get("title", "N/A"),
        price=result.get("price", 0),
        rating=result.get("rating", 0),
        trust_score=trust["trust_score"],
        trust_label=trust["trust_label"],
    )
    print(output)
    print("\nSentiment breakdown:", sentiment)


if __name__ == "__main__":
    main()