from datetime import datetime
from typing import List


def parse_csv_datetimes(path: str) -> List[datetime]:
    result: List[datetime] = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            result.append(datetime.fromisoformat(s))

    return result
