#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''


def n_gram(n, sentence, opt):
    if opt == 'word':
        seq = sentence.split(" ")
        s = " "
    elif opt == 'char':
        seq = sentence
        s = ""
    ngram_list = list()
    temp_list = list()
    for index in range(len(seq)-n+1):
        for j in range(n):
            temp_list.append(seq[index + j])
        ngram_list.append(s.join(temp_list))
        temp_list = list()
    return ngram_list

if __name__ == '__main__':
    sentence = "I am an NLPer"
    print n_gram(2, sentence, "word")
    print n_gram(2, sentence, "char")

