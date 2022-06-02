#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Если список пуст, завершить программу.
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    f = 0
    for i in A:
        if i % 3 == 0:
            f += 1
    print("Количество элементов списка кратные 3 = ", f)

    for x in range(len(A)):
        if x % 3 != 0:
            remove = x
            A.remove(x)
    print("Новый список элементов кратные трем: ", A)
    print("Последний элемент такого списка = ", A[-1])
    