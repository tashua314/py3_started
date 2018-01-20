# -*- coding: utf-8 -*-
import sys


# dividend: 被除数
# divisor: 除数
def devide(dividend, divisor):
    try:
        return int(dividend) / int(divisor)
    except ZeroDivisionError:
        return "infinite"


if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) not in [2, 3]:
        print("数値を1つ入力してください")
        sys.exit(1)
    res = devide(argvs[1], argvs[2])
    print(res)
