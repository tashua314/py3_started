# -*- coding: utf-8 -*-
import numpy as np


def kuku():
    row = np.arange(1, 10)
    col = np.arange(1, 10)[:, np.newaxis]
    return row * col


def vector(start, goal):
    return np.linalg.norm(goal - start)


if __name__ == '__main__':
    ans = kuku()
    print(ans)

    p0 = np.array((1, 1))
    p1 = np.array((6, 4))
    print(vector(p0, p1))
