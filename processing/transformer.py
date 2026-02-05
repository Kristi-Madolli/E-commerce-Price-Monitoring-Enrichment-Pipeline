from typing import List, Dict
from api.currency_api import get_latest_rates


def enrich_books_with_currency(books: List[Dict], targets=("EUR", "ALL")) -> List[Dict]:
    rates = get_latest_rates(base="GBP") or {}
    enriched = []

    for b in books:
        price_gbp = b.get("price_gbp")
        out = dict(b)

        for t in targets:
            rate = rates.get(t)
            if isinstance(price_gbp, (int, float)) and rate is not None:
                out[f"price_{t.lower()}"] = round(float(price_gbp) * float(rate), 2)
            else:
                out[f"price_{t.lower()}"] = None

        enriched.append(out)

    return enriched
