#!/usr/bin/env python3
"""Модуль, осуществляющий работу с различными кодировками"""
from chardet.universaldetector import UniversalDetector


def get_decode_text(file):
    """Метод, осуществляющий преобразование текстового файла"""
    detector = UniversalDetector()
    with open(file, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
        detector.close()

    encode = detector.result['encoding']
    encode_file = file.encode(encode)
    decode = 'utf-8'
    decode_file = encode_file.decode(decode)

    with open(decode_file, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
        detector.close()

    with open(decode_file, 'r') as new_f:
        lines = new_f.readlines()
        text = lines[0]
        red_type = lines[1]
    return text[:-1], red_type
