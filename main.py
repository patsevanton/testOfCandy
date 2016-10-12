#!usr/bin/env python
# -*- encoding: utf-8 -*-
import itertools
import random


def xorAllList(list):
    out = list[0]
    for i in range(1, len(list)):
        out = int(out) ^ int(list[i])
    return out


numberTestOfCase = random.randint(1, 10) # количество тестовых наборов
# numberTestOfCase = int(input("Введите количество тестовых наборов\n"))
for i in range(int(numberTestOfCase)):
    # numberOfCandy = int(input("Введите количество конфет\n"))
    numberOfCandy = random.randint(1, 10)
    # weightOfCandyInList = [int(x) for x in input("Введите веса конфет\n").split()]
    weightOfCandyInList = [random.randint(1, 10) for x in range(numberTestOfCase)]  # Введите веса конфет
    # print(numberTestOfCase)
    # print(weightOfCandyInList)
    for j in range(2, numberOfCandy):
        listOfList = list(itertools.combinations(weightOfCandyInList, j))
        CiList = []
        for k in listOfList:
            otherList = list(set(weightOfCandyInList).difference(k))
            if xorAllList(k) == xorAllList(otherList):
                CiList.append(sum([int(i) for i in k]))
        print("Case {0} {1}".format(int(i), max(int(i) for i in CiList)))
