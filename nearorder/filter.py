from nearorder.types import Cmp


def filter_window(xs, k, index: int, *, window_size: int, cmp: Cmp = lambda a, b: a - b):
    start = max(index - window_size // 2, 0)
    end = min(index + window_size // 2, len(xs) - 1)
    return [xs[i] for i in range(start, end + 1) if cmp(xs[i], k) == 0]
