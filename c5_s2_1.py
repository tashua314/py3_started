# -*- coding: utf-8 -*-
import sys
import math

METHOD_TYPE = 1


# 素数チェック
def check_prime(val, type=1):
    val = int(val)

    if val <= 1 or val == 1:
        return False

    if int(type) == 1:
        if is_prime1(val):
            return True
    elif int(type) == 2:
        if is_prime2(val):
            return True
    return False


# 1つずつ回してく
def is_prime1(val):
    for i in range(2, val):
        if val % i == 0:
            return False
    return True


# 高速化Ver
def is_prime2(val):
    if val == 2:
        return True
    if val % 2 == 0:
        return False

    sqrt = math.sqrt(val)
    i = 3
    while i <= sqrt:
        if val % i == 0:
            return False
        i = i + 2
    return True


if __name__ == '__main__':
    argvs = sys.argv
    if not len(argvs) == 2:
        print("素数かどうかを調べる数値を1つ入力してください。")
    else:
        try:
            is_prime = check_prime(argvs[1], METHOD_TYPE)

            if is_prime:
                print("素数です")
            else:
                print("素数じゃないです。")
        except ValueError:
            print("ERROR: 数値を入力してください")
