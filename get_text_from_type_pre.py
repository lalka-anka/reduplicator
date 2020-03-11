#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from compound_prefix import return_res_compound_pre
from simple_prefix import return_res_simple_pre
"""Модуль, осуществляющий работу с приставкой"""
VOWEL = 'аоуыеяиэёю'


def not_contain_vowel(pre):
    """Метод, работающий с типом приставки"""
    key = 0
    for i in pre:
        if i in VOWEL:
            key += 1
    return key == 0


def get_text(prefix, text):
    """Метод, возвращающий результат в зависимости от сложности приставки"""
    if not_contain_vowel(prefix):
        return return_res_simple_pre(text, prefix)
    else:
        return return_res_compound_pre(text, prefix)
