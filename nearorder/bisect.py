from typing import Sequence, TypeVar

T = TypeVar("T")


def binary_search(
    xs: Sequence[T],
    k,
    *,
    cmp=lambda a, b: a - b,
    window_size: int = 1,
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
        # print("window: {}".format(xs[window_left:window_right]))

        c = 0
        for i in range(window_left, window_right):
            rt = cmp(xs[i], k)
            if rt == 0:
                return i
            elif rt > 0:
                c -= 1
            else:
                c += 1

        if c > 0:
            left = mid + 1
        else:
            right = mid - 1

    return None
