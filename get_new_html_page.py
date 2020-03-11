from get_text_from_type_pre import get_text
import re
import os


def create_new_html_page(prefix):
    """Метод, создающий редуплицированную html-страницу"""
    rus_alpha = 'йцукеёнгшщзхъэждлорпавыфячсмитьбюЙЦУКЕЁНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
    result_text = ''
    path = os.path.dirname(os.path.realpath(__file__))
    text_path = path + '/page_code.txt'
    new_html_page = path + '/page_code.html'
    with open(text_path, 'r') as f:
        for line in f.readlines():
            new_line = line
            word = ''
            i = 0
            for letter in line:
                if letter in rus_alpha:
                    word += letter
                    if line[i+1] not in rus_alpha:
                        new_red_word = get_text(prefix, [word])
                        new_check_red_word = check_the_word(new_red_word, prefix)
                        new_line = re.sub(word, new_check_red_word, new_line)
                        word = ''
                i += 1
            result_text += new_line

    with open(new_html_page, 'w') as res_file:
        res_file.write(result_text)

    path_2_delete = os.path.join(os.path.abspath(os.path.dirname(__file__)), text_path)
    os.remove(path_2_delete)


def check_the_word(word, prefix):
    """Метод, проверяющий правильность редупликации"""
    while word[:len(prefix)] == word[len(prefix):2*len(prefix)]:
        word = word[len(prefix):]
    return word
