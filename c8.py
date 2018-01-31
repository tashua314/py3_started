# -*- coding: utf-8 -*-
import sys


def fizz_buzz(max_num):
    return [make_fizz_buzz(n) for n in range(1, max_num + 1)]


def make_fizz_buzz(num):
    return (num % 3 == 0) * 'Fizz' + (num % 5 == 0) * 'Buzz' or num


if __name__ == '__main__':
    num = input('FizzBuzz判定する最大値を入力してください：')
    try:
        num = int(num)
    except ValueError:
        print('ERROR: 整数を入力してください')
        sys.exit(1)

    res = fizz_buzz(num)
    print(res)
