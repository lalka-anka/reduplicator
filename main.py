#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Модуль, осуществляющий запуск программы"""
import argparse
from get_text_from_type_pre import get_text
from process_encode import get_decode_text
from get_statistic import get_statistic
from fetch import get_page_code
from get_new_html_page import create_new_html_page
from handle import create_server
import os.path


def parsing():
    """Метод, осуществляющий парсинг и выводящий результат"""
    parser = argparse.ArgumentParser(description='Lexical reduplication')
    parser.add_argument('-txt', '--text', type=str, metavar='', help='Text for reduplication')
    parser.add_argument('-opt', '--option', type=str, metavar='', help='Type of reduplication')
    parser.add_argument('-doc', '--document', type=str, metavar='', help='Document with text and type for '
                                                                         'reduplication\n(1 line-text, 2 line-type)')
    parser.add_argument('-save', '--save', type=str, metavar='', help='The path of the file in which to save result '
                                                                      'text')

    parser.add_argument('-html', '--html', type=str, metavar='', help='Option to work with html page')
    args = parser.parse_args()
    text = args.text
    option = args.option
    doc = args.document
    save = args.save
    html = args.html
    if html is not None:
        if option is not None:
            opt = option
        else:
            opt = input('Введите приставку для редупликации: ')
        get_page_code(html)
        create_new_html_page(opt)
        create_server()
    else:
        if text is not None and option is not None:
            txt = text.split()
            opt = option
        elif doc is not None and text is None and option is None:
            opt = get_decode_text(doc)[1]
            txt = get_decode_text(doc)[0].split()
        else:
            txt = input('Введите текст: ').split()
            opt = input('Введите приставку для редупликации: ')

        if txt == '' and opt == '':
            result = 'Повторите попытку'
        else:
            result = get_text(opt, txt)
        statistic = get_statistic(txt, result)
        if save is None:
            print(result)
            print('Процент редуплицированного текста составляет: {}%'.format(str(statistic)))
        else:
            with open(save, 'w') as f:
                f.write(result)
                f.write('Процент редуплицированного текста составляет: {}%'.format(str(statistic)))


if __name__ == '__main__':
    parsing()
    path = os.path.dirname(os.path.realpath(__file__))
    new_html_page = path + '/page_code.html'
    path_2_delete = os.path.join(os.path.abspath(os.path.dirname(__file__)), new_html_page)
    if os.path.exists(path_2_delete):
        os.remove(path_2_delete)
