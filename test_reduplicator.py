#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль с тестами"""
import unittest
from simple_prefix import return_res_simple_pre
from compound_prefix import get_pieces_be4_vowel
from compound_prefix import get_prefix
from compound_prefix import return_res_compound_pre
from get_register import get_word_with_register
from get_statistic import get_statistic
import os
from get_new_html_page import check_the_word
from get_text_from_type_pre import not_contain_vowel
from get_text_from_type_pre import get_text
from get_new_html_page import create_new_html_page


class Tests(unittest.TestCase):
    def test_for_anytask_1(self):
        """Чтобы запустились тесты на таске"""
        self.assertEqual(1, 1)

    def test_for_anytask_2(self):
        self.assertEqual(2, 2)

    def test_get_word_with_reg_1(self):
        word = 'самолёт'
        begin = 'долб'
        end = 'олёт'
        first_up = word[0].isupper() and word[-1].islower()
        all_up = word[-1].isupper()
        result = get_word_with_register(first_up, all_up, begin, end)
        self.assertEqual('долболёт', result)

    def test_get_word_with_reg_2(self):
        word = 'Самолёт'
        begin = 'долб'
        end = 'олёт'
        first_up = word[0].isupper() and word[-1].islower()
        all_up = word[-1].isupper()
        result = get_word_with_register(first_up, all_up, begin, end)
        self.assertEqual('Долболёт', result)

    def test_get_word_with_reg_3(self):
        word = 'САМОЛЁТ'
        begin = 'долб'
        end = 'олёт'
        first_up = word[0].isupper() and word[-1].islower()
        all_up = word[-1].isupper()
        result = get_word_with_register(first_up, all_up, begin, end)
        self.assertEqual('ДОЛБОЛЁТ', result)

    def test_get_pieces_be4_vowel_1(self):
        word = 'хомяк'
        result = get_pieces_be4_vowel(word)
        self.assertEqual(['хо', 'мя', 'к'], result)

    def test_get_pieces_be4_vowel_2(self):
        word = 'привет'
        result = get_pieces_be4_vowel(word)
        self.assertEqual(['при', 'ве', 'т'], result)

    def test_get_prefix_1(self):
        raw_prefix = 'долбить'
        result = get_prefix(raw_prefix)[0]
        self.assertEqual('долб', result)

    def test_get_prefix_2(self):
        raw_prefix = 'пилить'
        result = get_prefix(raw_prefix)[0]
        self.assertEqual('пил', result)

    def test_get_len_prefix_1(self):
        raw_prefix = 'долбить'
        result = get_prefix(raw_prefix)[1]
        self.assertEqual(2, result)

    def test_get_len_prefix_2(self):
        raw_prefix = 'пилить'
        result = get_prefix(raw_prefix)[1]
        self.assertEqual(2, result)

    def test_right_convert_words_1(self):
        words = ['шашлык']
        opt = 'м'
        result = return_res_simple_pre(words, opt)
        self.assertEqual('машлык', result)

    def test_right_convert_words_2(self):
        words = ['танцы']
        opt = 'шм'
        result = return_res_simple_pre(words, opt)
        self.assertEqual('шманцы', result)

    def test_right_convert_words_3(self):
        words = ['я', 'и', 'шашлык', 'друзья']
        opt = 'м'
        new_text = 'я и машлык музья'
        result = return_res_simple_pre(words, opt)
        self.assertEqual(new_text, result)

    def test_right_convert_words_4(self):
        words = ['я', 'собралась', 'на', 'танцы']
        opt = 'шм'
        new_text = 'я шмобралась на шманцы'
        result = return_res_simple_pre(words, opt)
        self.assertEqual(new_text, result)

    def test_right_convert_words_5(self):
        text = 'Я сегодня чудесным ВЕЧЕРОМ иду на танцы! А после за шашлычками!!!!'.split()
        opt = 'шм'
        new_text = 'Я шмегодня шмудесным ШМЕЧЕРОМ шмиду на шманцы! А шмосле за шмашлычками!!!!'
        result = return_res_simple_pre(text, opt)
        self.assertEqual(new_text, result)

    def test_right_convert_words_6(self):
        text = 'был ЧУДЕСНЫЙ день!!! Я видела САМОЛЁТ.....'.split()
        opt = 'долбить'
        new_text = 'был ДОЛБОСНЫЙ день!!! Я видела ДОЛБОЛЁТ.....'
        result = return_res_compound_pre(text, opt)
        self.assertEqual(new_text, result)

    def test_right_convert_words_7(self):
        text = 'Это очень интересный сказ о птицах... Как говорил один таксист птицы это круто'.split()
        opt = 'пилить'
        new_text = 'Это очень пилоресный сказ о птицах... Как пилорил один пилист птицы это круто'
        result = return_res_compound_pre(text, opt)
        self.assertEqual(new_text, result)

    def test_right_convert_words_8(self):
        text = 'какой-то текст очень интересный, да, такой вот необычный СЛОГ у меня'.split()
        opt = 'пилить'
        new_text = 'пилой-то текст очень пилоресный, да, такой вот пилобычный СЛОГ у меня'
        result = return_res_compound_pre(text, opt)
        self.assertEqual(new_text, result)

    def test_get_statistic_1(self):
        text = 'привет друг!!!'
        new_text = 'шмивет друг!!!'
        result = get_statistic(text, new_text)
        exp = 14
        self.assertEqual(exp, result)

    def test_get_statistic_2(self):
        text = 'Я видела САМОЛЁТ'
        new_text = 'Я видела ДОЛБОЛЁТ'
        result = get_statistic(text, new_text)
        exp = 43
        self.assertEqual(exp, result)

    def test_get_statistic_3(self):
        text = 'я иду на танцы'
        new_text = 'я иду на шманцы'
        result = get_statistic(text, new_text)
        exp = 35
        self.assertEqual(exp, result)

    def test_right_word_1(self):
        word = 'шмшмшмязык'
        exp = 'шмязык'
        res = check_the_word(word, 'шм')
        self.assertEqual(exp, res)

    def test_right_word_2(self):
        word = 'долбдолболет'
        exp = 'долболет'
        res = check_the_word(word, 'долб')
        self.assertEqual(exp, res)

    def test_is_not_contain_vowel_1(self):
        res = not_contain_vowel('шм')
        self.assertEqual(True, res)

    def test_is_not_contain_vowel_2(self):
        res = not_contain_vowel('долбить')
        self.assertEqual(False, res)

    def test_get_text_1(self):
        res = get_text('шм', 'шашлык'.split())
        exp = 'шмашлык'
        self.assertEqual(exp, res)

    def test_get_text_2(self):
        res = get_text('долбить', 'самолет'.split())
        exp = 'долболет'
        self.assertEqual(exp, res)
