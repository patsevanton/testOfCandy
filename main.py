#!usr/bin/env python
# -*- encoding: utf-8 -*-
import itertools
import operator
import random
from functools import reduce


def xorAllList(list):
    if len(list)> 1:
        return reduce(operator.xor, list)
    else:
        return list[0]

numberTestOfCase = random.randint(1, 100) # количество тестовых наборов
# numberTestOfCase = int(input("Введите количество тестовых наборов\n"))
for i in range(numberTestOfCase):
    # print(i, "i")
    # numberOfCandy = int(input("Введите количество конфет\n"))
    numberOfCandy = random.randint(1, 100)
    # print(numberOfCandy, "numberOfCandy")
    # weightOfCandyInList = [int(x) for x in input("Введите веса конфет\n").split()]
    weightOfCandyInList = [random.randint(1, 1000000) for x in range(numberOfCandy)]  # Введите веса конфет
    # print(numberTestOfCase, "numberTestOfCase")
    # print(weightOfCandyInList, "weightOfCandyInList")
    listOfCi = []
    for j in range(2, numberOfCandy):
        listOfList = list(itertools.combinations(weightOfCandyInList, j))
        # print(listOfList, "listOfList")
        for k in listOfList:
            otherList = list(set(weightOfCandyInList).difference(k))
            # print(otherList, "otherList")
            # print(k, "k")
            if (len(k) > 0 and len(otherList) > 0):
                if (xorAllList(k) == xorAllList(otherList)):
                    listOfCi.append(sum([int(i) for i in k]))
        # print(listOfCi, "listOfCi")
    if listOfCi:
        print("Case #{0}: {1}".format(int(i), max(listOfCi)))
    else:
        print("Case #{0}: NO".format(int(i)))
    listOfCi = None
