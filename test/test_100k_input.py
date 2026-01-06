from datetime import datetime

from nearorder.bisect import binary_search
from nearorder.bisect_fallback import binary_search_with_fallback

from .utils import parse_csv_datetimes

data = parse_csv_datetimes("test_data/datetime_2020~2025.csv")
k = datetime(
    year=2025,
    month=8,
    day=7,
    hour=23,
    minute=29,
    second=59,
)


def cmp(a: datetime, b: datetime) -> int:
    rt = a.timestamp() - b.timestamp()
    return int(rt)


def test_binary_search_fallback():
    index = binary_search_with_fallback(data, k, cmp=lambda a, b: cmp(a, b))
    assert index == 6991


# This test is expected to return None because this algorithm cannot fall back
def test_binary_search_precise():
    index = binary_search(data, k, cmp=lambda a, b: cmp(a, b), window_size=5)
    assert index is None
