# -*- coding: utf-8 -*-
import sys
import math


# 素数チェック
def check_prime(val, type=1):
    try:
        val = int(val)

        if val <= 1:
            return False

        if int(type) == 1:
            if is_prime1(val):
                return True
        elif int(type) == 2:
            if is_prime2(val):
                return True
        return False
    except ValueError:
        print("ERROR: 数値を入力してください")


# 1つずつ回してく
def is_prime1(val, is_print=True):
    for i in range(2, val):
        if val % i == 0:
            if is_print:
                print("{}で割れました".format(i))
            return False
    return True


# 高速化Ver
def is_prime2(val, is_print=True):
    if val == 2:
        return True
    if val % 2 == 0:
        return False

    sqrt = math.sqrt(val)
    i = 3
    while i <= sqrt:
        if val % i == 0:
            if is_print:
                print("{}で割れました".format(i))
            return False
        i = i + 2
    return True


if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) not in [2, 3]:
        print("数値を1つ入力してください")
    else:
        res = check_prime(argvs[1], argvs[2])
        if res:
            print("素数")
