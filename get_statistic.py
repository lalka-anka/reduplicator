#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, осуществляющий подсчет статистики"""


def get_statistic(text, res_text):
    len_txt = len(text)
    count = 0
    for l in range(len_txt):
        if text[l] != res_text[l]:
            count += 1
    res = count / len_txt * 100
    return int(res)
