import requests
import re
from bs4 import BeautifulSoup
from typing import List, Dict


BASE_URL = "https://books.toscrape.com/"


def scrape_books(limit: int = 20) -> List[Dict]:
    """
    Scrapes book data from the BooksToScrape website.

    Args:
        limit (int): Maximum number of books to scrape.

    Returns:
        List[Dict]: List of scraped book data.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; DataPipelineBot/1.0)"
    }

    books = []

    try:
        response = requests.get(BASE_URL, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return books

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="product_pod")

    for article in articles[:limit]:
        try:
            title = article.h3.a["title"]
            price_text = article.find("p", class_="price_color").get_text(strip=True)
            price_clean = re.sub(r"[^0-9.]", "", price_text)   # heq £, Â, etj.
            price = float(price_clean)

            availability = article.find("p", class_="instock availability").text.strip()

            books.append({
                "title": title,
                "price_gbp": price,
                "availability": availability,
                "source": "BooksToScrape"
            })
        except Exception as e:
            print(f"Error parsing book data: {e}")

    return books


if __name__ == "__main__":
    data = scrape_books(5)
    for book in data:
        print(book)
