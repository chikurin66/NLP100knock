# coding: UTF-8

'''
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，
1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
'''

import knock50


def separateIntoWords(sentences):
    words = []
    for sentence in sentences:
        words_temp = sentence.split(' ')
        for word in words_temp:
            words.append(word.rstrip(',.'))  # コンマとピリオドは消す
        words.append("")
    return words

if __name__ == '__main__':
    with open("../data/nlp.txt", "r") as f:
        text = f.readlines()
        sentences = knock50.separateIntoSentences(text)
        words = separateIntoWords(sentences)
    with open("../data/nlp_word.txt", "w") as g:
        g.writelines(words)

    for word in words:
         print word

