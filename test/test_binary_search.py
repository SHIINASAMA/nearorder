import pytest

from nearorder.bisect import binary_search


def test_mid_hit_dirty_data():
    nums = [1, 2, 3, 5, 8, 6, 7, 10, 9]
    index = binary_search(nums, 10)
    assert index == 7


def test_mid_hit_normal_data():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = binary_search(nums, 1)
    assert index == 0


def test_mid_hit_k():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = binary_search(nums, 5)
    assert index == 4


def test_invalid_window_size():
    nums = []
    with pytest.raises(ValueError):
        binary_search(nums, 1, window_size=-1)


def test_no_exist_data():
    nums = []
    index = binary_search(nums, 1)
    assert index is None
