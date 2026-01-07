from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple

from .types import Cmp, Order, T


@dataclass
class SearchState:
    fallback_count: int = -1
    cmp_count: int = 0
    search_route: List[Tuple[int, int, bool]] = field(default_factory=list)


def binary_search_with_fallback(
    xs: Sequence[T],
    k: T,
    *,
    cmp: Cmp = lambda a, b: a - b,
    order: Order = "asc",
    state: SearchState = None,
) -> Optional[int]:
    stack = [(0, len(xs) - 1, False)]  # fallback stack

    # normalize direction: asc = +1, desc = -1
    order_sign = 1 if order == "asc" else -1

    while stack:
        left, right, is_fallback = stack.pop()
        if state is not None:
            if is_fallback:
                state.fallback_count += 1
            state.search_route.append((left, right, is_fallback))

        if left > right:
            continue

        mid = (left + right) // 2

        c = cmp(xs[mid], k)
        if state is not None:
            state.cmp_count += 1
        if c == 0:
            return mid

        # normalized binary decision
        cmp_mid = c * order_sign

        if cmp_mid < 0:
            # k in right half
            stack.append((left, mid - 1, True))  # fallback
            left = mid + 1  # main path
        else:
            # k in left half
            stack.append((mid + 1, right, True))  # fallback
            right = mid - 1  # main path

        # continue main path
        if left <= right:
            stack.append((left, right, False))

    return None
