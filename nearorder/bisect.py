from typing import Callable, Literal, Sequence, TypeVar

T = TypeVar("T")

Order = Literal["asc", "desc"]


def binary_search(
    xs: Sequence[T],
    k,
    *,
    cmp: Callable[[T, T], int] = lambda a, b: a - b,
    window_size: int = 1,
    order: Order = "asc",
):
    if window_size <= 0:
        raise ValueError("window_size must be > 0")

    left = 0
    right = len(xs) - 1

    while left <= right:
        mid = (left + right) // 2

        # 1. Hit
        if cmp(xs[mid], k) == 0:
            return mid

        # 2. Search in window
        window_left = max(0, mid - window_size)
        window_right = min(len(xs), mid + window_size + 1)

        c = 0
        for i in range(window_left, window_right):
            rt = cmp(xs[i], k)
            if rt == 0:
                return i
            if order == "asc":
                # xs[i] < k -> k in right side
                if rt < 0:
                    c += 1
                else:
                    c -= 1
            else:  # desc
                # xs[i] > k -> k in right side
                if rt > 0:
                    c += 1
                else:
                    c -= 1

        # 3. Shrink range
        if c > 0:
            left = mid + 1
        else:
            right = mid - 1

    return None
