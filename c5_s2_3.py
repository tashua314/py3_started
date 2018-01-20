# -*- coding: utf-8 -*-
import sys
import random
import string
import re


# パスワードを作成
# type: 2の場合は、空白や改行等特殊記号を除外
def make_password(length, type=1):
    try:
        result = []
        length = int(length)

        for i in range(0, length):
            key = string.printable[random.randint(0, 99)]
            if int(type) == 2:
                while 1:
                    if key in [' ', '\t', '\n', '\r', '\x0b', '\x0c']:
                        key = string.printable[random.randint(0, 99)]
                    else:
                        break
            result.append(key)
        print(result)
        return ''.join(result)

    except ValueError:
        print("ERROR: 数値を入力してください")


if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) not in [2, 3]:
        print("数値を1つ入力してください")
        sys.exit(1)
    password = make_password(argvs[1], argvs[2])
    print(password)
