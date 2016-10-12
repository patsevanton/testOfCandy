#!usr/bin/env python3
# -*- encoding: utf-8 -*-
from functools import reduce
from itertools import combinations
from operator import xor
from random import randint

import sys


def xorAllList(list):
    if len(list)> 1:
        return reduce(xor, list)
    else:
        return list[0]


def printCase(list, out=sys.stdout):
    if list:
        out.write("Case #{0}: {1}\n".format(int(i), max(list)))
    else:
        out.write("Case #{0}: NO\n".format(int(i)))


def subtraction(generalList, partOfList):
    return list(set(generalList).difference(partOfList))


def randomOfCandy(start, end):
    return randint(start, end)


def randomWeightOfCandyInList(start, end, numberOfCandy):
    return [randint(start, end) for x in range(numberOfCandy)]


if __name__ == "__main__":
    numberTestOfCase = randint(1, 10)  # количество тестовых наборов
    # numberTestOfCase = int(input("Введите количество тестовых наборов\n"))
    for i in range(numberTestOfCase):
        # print(i, "i")
        # numberOfCandy = int(input("Введите количество конфет\n"))
        numberOfCandy = randomOfCandy(1, 10)
        # print(numberOfCandy, "numberOfCandy")
        # weightOfCandyInList = [int(x) for x in input("Введите веса конфет\n").split()]
        weightOfCandyInList = randomWeightOfCandyInList(1, 100, numberOfCandy)  # Введите веса конфет
        # print(numberTestOfCase, "numberTestOfCase")
        # print(weightOfCandyInList, "weightOfCandyInList")
        listOfCi = []
        for j in range(2, numberOfCandy):
            listOfList = list(combinations(weightOfCandyInList, j))
            # print(listOfList, "listOfList")
            for k in listOfList:
                otherList = subtraction(weightOfCandyInList, k)
                # print(otherList, "otherList")
                # print(k, "k")
                if (len(k) > 0 and len(otherList) > 0):
                    if (xorAllList(k) == xorAllList(otherList)):
                        listOfCi.append(sum([int(i) for i in k]))
                        # print(listOfCi, "listOfCi")
        printCase(listOfCi)
        listOfCi = None
