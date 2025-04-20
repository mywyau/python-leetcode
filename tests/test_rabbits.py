# tests/test_rabbits.py
from ward import test

from rabbits import num_rabbits

@test("basic case returns 5")
def _():
    assert num_rabbits([1, 1, 2]) == 5

@test("all zeroes return exact count")
def _():
    assert num_rabbits([0, 0, 0]) == 3

@test("multiple groups of same answer")
def _():
    assert num_rabbits([1, 1, 1, 1]) == 6

@test("empty input returns 0")
def _():
    assert num_rabbits([]) == 0

@test("single rabbit who says 0")
def _():
    assert num_rabbits([0]) == 1
