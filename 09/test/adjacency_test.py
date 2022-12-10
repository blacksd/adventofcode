import pytest
from solution1 import *


def test_is_adjacent():

    #    0 1
    # 0  b .
    # 1  a .
    assert is_adjacent((1, 0), (0, 0)), "vertical up"

    #    0 1
    # 0  a b
    # 1  . .
    assert is_adjacent((0, 0), (0, 1)), "horizontal right"

    #   0 1
    # 0 b a
    # 1 . .
    assert is_adjacent((0, 1), (0, 0)), "horizontal left"

    #   0 1
    # 0 a .
    # 1 b .
    assert is_adjacent((0, 0), (1, 0)), "vertical down"

    #   0 1
    # 0 . b
    # 1 a .
    assert is_adjacent((0, 1), (1, 0)), "diagonal up-right"

    #   0 1
    # 0 b .
    # 1 . a
    assert is_adjacent((1, 1), (0, 0)), "diagonal up-left"

    #   0 1
    # 0 a .
    # 1 . b
    assert is_adjacent((0, 0), (1, 1)), "diagonal down-right"

    #   0 1
    # 0 . a
    # 1 b .
    assert is_adjacent((1, 0), (0, 1)), "diagonal down-left"

    #   0  1
    # 0 ab .
    # 1 .  .
    assert is_adjacent((0, 0), (0, 0)), "overlapping"


def test_is_not_adjacent():

    assert not is_adjacent((2, 0), (0, 0)), "vertical over"

    assert not is_adjacent((2, 0), (2, 4)), "horizontal over"
