from typing import List, Dict
from api.currency_api import convert_amount


def enrich_books_with_currency(books: List[Dict], targets=("EUR", "ALL")) -> List[Dict]:
    """
    Adds converted prices to each book dict (price_eur, price_all).
    If conversion fails, fields are set to None.
    """
    enriched = []

    for b in books:
        price_gbp = b.get("price_gbp")
        out = dict(b)

        if isinstance(price_gbp, (int, float)):
            for t in targets:
                out[f"price_{t.lower()}"] = convert_amount(price_gbp, "GBP", t)
        else:
            for t in targets:
                out[f"price_{t.lower()}"] = None

        enriched.append(out)

    return enriched
