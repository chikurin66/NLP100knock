# coding: UTF-8

'''
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
入力された文書を1行1文の形式で出力せよ．
'''

import re

def separateIntoSentences(text):
    sentences = []

    for line in text:
        if line != "\n":
            items = re.sub(r"(\.|;|:|\?|!) ([A-Z])", r"\1\n\2", line.rstrip())
            items = items.split("\n")
            for item in items:
                sentences.append(item)
    return sentences


if __name__ == '__main__':
    with open("../data/nlp.txt", "r") as f:
        text = f.readlines()
        sentences = separateIntoSentences(text)
    with open("../data/nlp_sentence.txt", "w") as g:
        g.write("\n".join(sentences))
    for sentence in sentences:
        print sentence

