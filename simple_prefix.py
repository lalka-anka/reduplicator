#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, осуществляющий преобразование текста"""
from get_register import get_word_with_register
VOWEL = 'аоуыеяиэёю'


def return_res_simple_pre(text, red_type):
    """Метод, осуществляющий преобразование текста"""
    res = ''
    for d in text:
        key = 0
        i = 0
        first_up = d[0].isupper() and d[-1].islower()
        all_up = d[0].isupper() and d[int(len(d)/2)].isupper()
        d = d.lower()
        if len(d) >= 3:
            for let in d:
                if let not in VOWEL:
                    key += 1
            if key == len(d):
                d = d
            else:
                if d[0] in VOWEL:
                    d = get_word_with_register(first_up, all_up, red_type, d)
                else:
                    a = d
                    key = 0
                    while a[i] not in VOWEL:
                        a = a[i + 1:]
                        key += 1
                    if key <= 2:
                        d = a
                    d = get_word_with_register(first_up, all_up, red_type, d)
        else:
            d = get_word_with_register(first_up, all_up, d[0], d[1:])
        res += d + ' '
    return res[:-1]
