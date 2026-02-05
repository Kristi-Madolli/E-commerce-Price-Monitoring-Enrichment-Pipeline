import requests
from typing import Dict, Optional

FRANKFURTER_BASE_URL = "https://api.frankfurter.dev"


def get_latest_rates(base: str = "GBP") -> Optional[Dict[str, float]]:
    """
    Fetch latest exchange rates with given base currency.
    Returns dict like {"EUR": 1.17, "ALL": ...} or None on failure.
    """
    url = f"{FRANKFURTER_BASE_URL}/latest"
    params = {"base": base.upper()}

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("rates", None)
    except requests.RequestException as e:
        print(f"[currency_api] Request error: {e}")
        return None
    except ValueError as e:
        print(f"[currency_api] JSON parse error: {e}")
        return None


def convert_amount(amount: float, base: str, target: str) -> Optional[float]:
    """
    Converts amount from base currency to target currency using latest rates.
    """
    rates = get_latest_rates(base=base)
    if not rates:
        return None

    rate = rates.get(target.upper())
    if rate is None:
        print(f"[currency_api] Missing rate for {target.upper()}")
        return None

    return round(amount * float(rate), 2)
