#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 12:27
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : earthquake.py
# @Software: PyCharm

import xlrd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def get_data_from_excel():
    """
    从excel中获取数据
    :return:
    """
    # work_book = xlrd.open_workbook(r'./data/earthquake_data.xls')
    work_book = xlrd.open_workbook(r'./data/地震波参数4项_改.xls')
    sheet = work_book.sheet_by_name('13')
    datetime_list = sheet.col_values(2)
    epicentral_distance_list = sheet.col_values(4)
    level_list = sheet.col_values(5)
    positive_and_negative_list = sheet.col_values(6)

    data_len = sum([1 if len(str(i).strip()) > 0 else 0 for i in datetime_list])

    datetime_list = [datetime.datetime.strptime(str(int(i)), '%Y%m%d').date() for i in datetime_list[1:data_len]]
    epicentral_distance_list = epicentral_distance_list[1:data_len]
    level_list = [float(i) for i in level_list[1:data_len]]
    positive_and_negative_list = [check_positive_and_negative(i) for i in positive_and_negative_list[1:data_len]]

    data = {
        'datetime': datetime_list,
        'epicentral_distance': epicentral_distance_list,
        'positive_and_negative': positive_and_negative_list,
        'level': level_list
    }

    print(data)

    return data


def check_positive_and_negative(value: str):
    """
    检查正负值
    :param value:
    :return:
    """
    for i in value:
        if i == '+':
            return '+'
        if i == '-':
            return '-'
    return ''


def plot_data(data_dict):
    """
    可视化数据
    :param data_dict:
    :return:
    """
    x = data_dict.get('datetime')
    y = data_dict.get('epicentral_distance')
    markers = data_dict.get('positive_and_negative')

    print(len(x), len(y), len(markers))

    x_p = list()
    y_p = list()

    x_n = list()
    y_n = list()

    for x_i, y_i, m_i in zip(x, y, markers):
        if m_i == '+':
            x_p.append(x_i)
            y_p.append(y_i)
        elif m_i == '-':
            x_n.append(x_i)
            y_n.append(y_i)

    print(len(x_p), x_p)
    print(len(y_p), y_p)

    print(len(x_n), x_n)
    print(len(y_n), y_n)

    plt.figure(figsize=(15, 5))
    plt.subplots_adjust(bottom=0.2, top=0.95,
                        left=0.05, right=0.95)

    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率

    p1 = plt.scatter(x_p, y_p, marker='+', c='k', s=50)
    p2 = plt.scatter(x_n, y_n, marker='_', c='k', s=50)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # 設置x軸主刻度顯示格式（日期）
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # 設置x軸主刻度間距

    plt.gca().spines['top'].set_visible(False)  # 去掉上边框
    plt.gca().spines['right'].set_visible(False)  # 去掉右边框

    plt.xticks(rotation=90, fontsize=15)
    # plt.legend([p1, p2], ['波动向上', '波动向下'], loc='best')

    # plt.ylim(0, max(y))
    # plt.xlim(min(x), max(x))
    # plt.xticks(range(len(x)), x, rotation=90, fontsize=8)
    #
    # plt.scatter(range(len(x)), y, s=10)

    plt.savefig('plot1.png', dpi=100)  # 指定分辨率保存
    plt.show()


def plot_data_level(data_dict):
    """
    画图，震级大小
    :return:
    """
    x = data_dict.get('datetime')
    y = data_dict.get('epicentral_distance')
    level_list = data_dict.get('level')

    print(len(x), len(y), len(level_list))

    plt.figure(figsize=(15, 5))
    plt.subplots_adjust(bottom=0.2, top=0.95, left=0.05, right=0.95)

    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率

    # p1 = plt.scatter(x_p, y_p, marker='+', c='k', s=50)
    # p2 = plt.scatter(x_n, y_n, marker='_', c='k', s=50)

    print(max(level_list))

    for x_i, y_i, l_i in zip(x, y, level_list):
        if 1 <= l_i < 2:
            plt.scatter(x_i, y_i, marker='o', color='', edgecolors='k', s=10)
        elif 2 <= l_i < 3:
            plt.scatter(x_i, y_i, marker='o', color='', edgecolors='k', s=40)
        elif 3 <= l_i < 4:
            plt.scatter(x_i, y_i, marker='o', color='', edgecolors='k', s=150)
        elif 4 <= l_i < 5:
            plt.scatter(x_i, y_i, marker='o', color='', edgecolors='k', s=350)
        else:
            raise ValueError('error level value')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # 設置x軸主刻度顯示格式（日期）
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # 設置x軸主刻度間距

    plt.xticks(rotation=90, fontsize=15)

    plt.gca().spines['top'].set_visible(False)  # 去掉上边框
    plt.gca().spines['right'].set_visible(False)  # 去掉右边框

    # plt.ylim(0, max(y))
    # plt.xticks(range(len(x)), x, rotation=90, fontsize=8)
    #
    # plt.scatter(range(len(x)), y, s=10)

    plt.savefig('plot2.png', dpi=100)  # 指定分辨率保存
    plt.show()


if __name__ == '__main__':
    data = get_data_from_excel()
    plot_data(data)
    plot_data_level(data)
