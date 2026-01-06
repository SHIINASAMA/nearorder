import pytest

from nearorder.bisect_fallback import binary_search_with_fallback


def test_worst_case_1():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    index = binary_search_with_fallback(nums, k=0)
    assert index == 9


def test_worst_case_2():
    nums = [1, 9, 8, 7, 6, 5, 4, 3, 2, 0]
    index = binary_search_with_fallback(nums, k=1, order="desc")
    assert index == 0


def test_invalid_window_size():
    nums = []
    with pytest.raises(ValueError):
        binary_search_with_fallback(nums, k=1, window_size=0)


def test_k_not_found():
    nums = [1, 2, 3, 4, 5]
    index = binary_search_with_fallback(nums, k=6)
    assert index is None
