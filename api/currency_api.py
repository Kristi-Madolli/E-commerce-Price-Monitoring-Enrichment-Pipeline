import requests
from typing import Dict, Optional

FRANKFURTER_LATEST = "https://api.frankfurter.dev/v1/latest"
ERAPI_LATEST = "https://open.er-api.com/v6/latest"


def _get_rates_frankfurter(base: str) -> Optional[Dict[str, float]]:
    try:
        r = requests.get(FRANKFURTER_LATEST, params={"base": base.upper()}, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("rates")
    except requests.RequestException as e:
        print(f"[currency_api] Frankfurter error: {e}")
        return None
    except ValueError as e:
        print(f"[currency_api] Frankfurter JSON error: {e}")
        return None


def _get_rates_erapi(base: str) -> Optional[Dict[str, float]]:
    # Example: https://open.er-api.com/v6/latest/GBP
    try:
        r = requests.get(f"{ERAPI_LATEST}/{base.upper()}", timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("rates")
    except requests.RequestException as e:
        print(f"[currency_api] ERAPI error: {e}")
        return None
    except ValueError as e:
        print(f"[currency_api] ERAPI JSON error: {e}")
        return None


def get_latest_rates(base: str = "GBP") -> Optional[Dict[str, float]]:
    """
    Tries Frankfurter first; if it fails (e.g., 521), falls back to open.er-api.com.
    """
    rates = _get_rates_frankfurter(base)
    if rates:
        return rates

    return _get_rates_erapi(base)


def convert_amount(amount: float, base: str, target: str) -> Optional[float]:
    rates = get_latest_rates(base=base)
    if not rates:
        return None

    rate = rates.get(target.upper())
    if rate is None:
        print(f"[currency_api] Missing rate for {target.upper()}")
        return None

    return round(float(amount) * float(rate), 2)
