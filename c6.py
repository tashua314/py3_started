# -*- coding: utf-8 -*-
import sys
from statistics import mean
from random import randint


def average(nums):
    return mean(nums)
    # return sum(nums) / len(nums)


def rand_nums(count, max=1000):
    arr = []
    for num in range(count):
        arr.append(randint(1, max))
    return arr

if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) not in [2, 3]:
        print("標本数と乱数の最大値を入力してください")
        sys.exit(1)
    arr = rand_nums(int(argvs[1]), int(argvs[2]))
    m = average(arr)
    print(arr)
    print(m)
