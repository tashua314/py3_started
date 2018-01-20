# -*- coding: utf-8 -*-
from c5_s2_1 import is_prime2 as is_prime
import sys
import math
import pdb


# 指定した値までの素数を出力
def loop_print_prime(max):
    try:
        max = int(max)
        print(2)
        i = 3
        result = []
        while i <= max:
            if is_prime(i, False):
                result.append(i)
            i = i + 2
        return result
    except ValueError:
        print("ERROR: 数値を入力してください")


if __name__ == '__main__':
    argvs = sys.argv
    print(argvs)
    if len(argvs) != 2:
        print("数値を1つ入力してください")
        sys.exit()

    result = loop_print_prime(argvs[1])
    print(result)
