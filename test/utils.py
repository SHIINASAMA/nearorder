import json
from datetime import datetime
from typing import List, Sequence

from nearorder.bisect_fallback import SearchState
from nearorder.math import (
    displacement_sum,
    inversion_count,
    local_inversion_ratio,
    max_monotonic_run,
)
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


def disorder_metrics(xs: Sequence[int], order: Order = "asc") -> dict:
    """
    Aggregate disorder metrics.
    """
    n = len(xs)
    max_inv = n * (n - 1) // 2

    inv = inversion_count(xs, order=order)

    return {
        "n": n,
        "inversion_count": inv,
        "inversion_ratio": inv / max_inv if max_inv else 0.0,
        "local_inversion_ratio": local_inversion_ratio(xs, order=order),
        "max_monotonic_run": max_monotonic_run(xs, order=order),
        "displacement_sum": displacement_sum(xs, order=order),
    }


def show_disorder_metrics(xs: Sequence[int], *, order: Order = "asc") -> None:
    metrics = disorder_metrics(xs, order=order)
    print(json.dumps(metrics, indent=2, ensure_ascii=False))


def show_disorder_metrics_with_state(
    xs: Sequence[int], state: SearchState, *, order: Order = "asc"
) -> None:
    metrics = disorder_metrics(xs, order=order)
    metrics["fallback_count"] = state.fallback_count
    metrics["cmp_count"] = state.cmp_count
    print(json.dumps(metrics, indent=2, ensure_ascii=False))
