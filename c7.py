# -*- coding: utf-8 -*-
import sys


def arr2tuple(arr):
    indexes = range(1, len(arr) + 1)

    res = []
    for (index, str) in zip(indexes, arr):
        res.append((index, str))
    return res


if __name__ == '__main__':
    # 入力は対応外
    arr = ['hoge', 'foo', 'bar']
    res = arr2tuple(arr)
    print(res)
