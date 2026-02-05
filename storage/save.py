import json
import csv
from typing import List, Dict


def save_json(data: List[Dict], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_csv(data: List[Dict], path: str) -> None:
    if not data:
        return

    fieldnames = sorted({k for row in data for k in row.keys()})

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
