#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
 
if __name__ == '__main__':
    a = list(map(float, input().split()))
    print("Индекс минимального элемента:", a.index(min(a)))
    mass = [1,2,-4,5,4,3,-2,1,-3,2]
indx = [mass.index(i) for i in mass if i<0]
result = [i for i in mass[indx[0]+1: indx[1]]]
print(f'{sum(result)} - сумма.')