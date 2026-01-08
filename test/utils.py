import json
from datetime import datetime
from typing import List, Sequence

from nearorder.bisect_fallback import SearchState
from nearorder.math.metrics import disorder_metrics
from nearorder.types import Order


def parse_csv_datetimes(path: str) -> List[datetime]:
    result: List[datetime] = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            result.append(datetime.fromisoformat(s))

    show_disorder_metrics([int(t.timestamp()) for t in result], order="desc")

    return result


def get_disorder_metrics(xs: Sequence[int], *, order: Order = "asc") -> str:
    metrics = disorder_metrics(xs, order=order)
    return json.dumps(metrics, indent=2, ensure_ascii=False)


def show_disorder_metrics(xs: Sequence[int], *, order: Order = "asc") -> None:
    print(get_disorder_metrics(xs, order=order))


def get_disorder_metrics_with_state(
    xs: Sequence[int], state: SearchState, *, order: Order = "asc"
) -> str:
    metrics = disorder_metrics(xs, order=order)
    metrics["fallback_count"] = state.fallback_count
    metrics["cmp_count"] = state.cmp_count
    return json.dumps(metrics, indent=2, ensure_ascii=False)


def show_disorder_metrics_with_state(
    xs: Sequence[int], state: SearchState, *, order: Order = "asc"
) -> None:
    print(get_disorder_metrics_with_state(xs, state=state, order=order))
