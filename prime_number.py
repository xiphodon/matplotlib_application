#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 14:46
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : prime_number.py
# @Software: PyCharm
import json
from math import sqrt

import os

prime_number_list = list()


def is_prime(n):
    """
    是否为素数
    :param n:
    :return:
    """
    if n == 1:
        return False
    else:
        sqrt_n = int(sqrt(n)) + 1

        # for i in range(2, sqrt_n):
        #     if n % i == 0:
        #         return False
        # return True

        if len(prime_number_list) == 0:
            for i in range(2, sqrt_n):
                if n % i == 0:
                    return False
            return True
        else:
            for i in prime_number_list:
                if i <= sqrt_n:
                    if n % i == 0:
                        return False
                else:
                    return True
            return True


def start():
    """
    入口
    :return:
    """
    n = 5 * 1000 * 10000
    prime_number_json_path = r'./data/prime_number.json'

    global prime_number_list

    if os.path.exists(prime_number_json_path):
        with open(prime_number_json_path, 'r', encoding='utf8') as fp:
            prime_number_list = json.load(fp)

    if len(prime_number_list) > 0:
        last_prime = prime_number_list[-1]
        if last_prime > n:
            return
        else:
            for i in range(last_prime + 1, n + 1):
                if is_prime(i):
                    print(i)
                    prime_number_list.append(i)

    print('total: ', len(prime_number_list))

    with open(prime_number_json_path, 'w', encoding='utf8') as fp:
        json.dump(prime_number_list, fp)


if __name__ == '__main__':
    start()
