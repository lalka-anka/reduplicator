#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, осуществляющий работу с регистром"""


def get_word_with_register(first_up, all_up, begin, end):
    if first_up:
        word = begin[0].upper() + begin[1:] + end
    elif all_up:
        word = (begin + end).upper()
    else:
        word = begin + end
    return word
