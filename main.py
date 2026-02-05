from storage.save import save_json, save_csv
from scraping.books_scraper import scrape_books
from processing.transformer import enrich_books_with_currency
from security.encryption import encrypt_text


def run_pipeline(limit: int = 10):
    books = scrape_books(limit=limit)
    enriched = enrich_books_with_currency(books, targets=("EUR", "ALL"))

    for item in enriched:
        item["title_encrypted"] = encrypt_text(item["title"])
        del item["title"]

save_json(enriched, "output.json")
save_csv(enriched, "output.csv")
print("Saved: output.json and output.csv")

        print(item)


if __name__ == "__main__":
    run_pipeline(limit=5)
