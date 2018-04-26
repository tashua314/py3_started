# -*- coding: utf-8 -*-
import sys
from statistics import mean
from random import randint


# 平均値を求める
def average(nums):
    return mean(nums)
    # return sum(nums) / len(nums)


# 乱数リストを生成
# params:
#   countt: 標本数
#   max_value: 乱数の最大値
def rand_nums(count, max_value):
    arr = []
    for num in range(count):
        arr.append(randint(1, max_value))
    return arr


if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) not in [3]:
        print("標本数と乱数の最大値を入力してください")
        sys.exit(1)
    arr = rand_nums(int(argvs[1]), int(argvs[2]))
    m = average(arr)
    print(arr)
    print(m)
