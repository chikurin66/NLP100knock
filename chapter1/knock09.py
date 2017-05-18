#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def typoglycemia(string):
    words_list = string.split()
    new_words_list = []
    for word in words_list:
        if len(word) <= 4:
            new_words_list.append(word)
        else:
            middle_char_list = list(word[1:-1])
            random.shuffle(middle_char_list)
            new_words_list.append(word[0] + ''.join(middle_char_list) + word[-1])

    return ' '.join(new_words_list)


if __name__ == '__main__':

    string = "I couldn't believe that I could actually understand " \
             "what I was reading : the phenomenal power of the human mind ."
    print typoglycemia(string)


