from typing import Optional, Sequence

from .types import Cmp, Order, T


def binary_search_with_fallback(
    xs: Sequence[T],
    k: T,
    *,
    cmp: Cmp = lambda a, b: a - b,
    window_size: int = 1,
    order: Order = "asc",
) -> Optional[int]:
    if window_size <= 0:
        raise ValueError("window_size must be > 0")

    stack = [(0, len(xs) - 1)]  # fallback stack

    # normalize direction: asc = +1, desc = -1
    order_sign = 1 if order == "asc" else -1

    while stack:
        left, right = stack.pop()

        if left > right:
            continue

        mid = (left + right) // 2

        # window hit first
        window_left = max(left, mid - window_size)
        window_right = min(right + 1, mid + window_size + 1)
        for i in range(window_left, window_right):
            if cmp(xs[i], k) == 0:
                return i

        # normalized binary decision
        cmp_mid = cmp(xs[mid], k) * order_sign

        if cmp_mid < 0:
            # xs[mid] < k (semantic asc)
            stack.append((left, mid - 1))  # fallback
            left = mid + 1  # main path
        else:
            # xs[mid] >= k (semantic asc)
            stack.append((mid + 1, right))  # fallback
            right = mid - 1  # main path

        # continue main path
        if left <= right:
            stack.append((left, right))

    return None
