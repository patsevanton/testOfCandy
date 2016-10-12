#!usr/bin/env python3
# -*- encoding: utf-8 -*-
from functools import reduce
from operator import xor
from random import randint

from main import xorAllList, subtraction, randomOfCandy, randomWeightOfCandyInList


def test_xorAllList():
    assert xorAllList([50,10]) == 56

def test_subtraction():
    assert subtraction([1,2,3,4,5], [1,2]) == [3,4,5]

def test_randomOfCandy():
    assert randomOfCandy(1, 1) == randint(1, 1)

def test_randomWeightOfCandyInList():
    assert randomWeightOfCandyInList(1, 1, 5) == [randint(1, 1) for x in range(5)]