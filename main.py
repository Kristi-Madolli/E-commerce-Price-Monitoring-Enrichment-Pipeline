from scraping.books_scraper import scrape_books
from processing.transformer import enrich_books_with_currency


def run_pipeline(limit: int = 10):
    books = scrape_books(limit=limit)
    enriched = enrich_books_with_currency(books, targets=("EUR", "ALL"))

    # For now: just print results (storage + security in next steps)
    for item in enriched:
        print(item)


if __name__ == "__main__":
    run_pipeline(limit=5)
