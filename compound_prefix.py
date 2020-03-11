#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, осуществляющий преобразование текста"""
from get_register import get_word_with_register
VOWEL = 'аоуыеяиэёю'


def get_new_text(text, prefix):
    """Метод, осуществляющий преобразование текста"""
    res = ''
    for word in text:
        key = 0
        first_up = word[0].isupper() and word[-1].islower()
        all_up = word[0].isupper() and word[int(len(word)/2)].isupper()
        word = word.lower()
        for let in word:
            if let not in VOWEL:
                key += 1
        if key == len(word):
            word = word
        else:
            if get_prefix(word)[1] < prefix[1] or prefix[1] > len(get_prefix(word)[0]) or len(prefix[0]) + 2 >= len(
                    word) \
                    or len(get_prefix(word)[0]) < len(prefix[0]) - 1:
                prefix_word = get_prefix(word)[0]
                prefix_len = len(get_prefix(word)[0])
                suffix = word[prefix_len:]
                word = get_word_with_register(first_up, all_up, prefix_word, suffix)
            else:
                prefix_len = len(get_prefix(word)[0])
                suffix = word[prefix_len:]
                if suffix[0] == 'е':
                    suffix = 'о' + suffix[1:]
                word = get_word_with_register(first_up, all_up, prefix[0], suffix)
        res += word + ' '
    return res[:-1]


def get_pieces_be4_vowel(word):
    """Метод, осуществляющий работу с частями слова"""
    pieces = []
    piece = ''
    i = 0
    for w in word:
        if w not in VOWEL:
            piece += w
        else:
            piece += w
            pieces.append(piece)
            piece = ''

    pieces.append(word[i-1:])
    return pieces


def get_prefix(word):
    """Метод, осуществляющий работу с приставкой"""
    pieces = get_pieces_be4_vowel(word)
    if len(pieces[0]) <= 2:
        pre = pieces[0] + pieces[1]
        syllables = 2
    else:
        pre = pieces[0]
        syllables = 1
    return pre[:-1], syllables


def return_res_compound_pre(words, prefix):
    """Метод, возвращающий результат"""
    pre = get_prefix(prefix)
    res = get_new_text(words, pre)
    return res
