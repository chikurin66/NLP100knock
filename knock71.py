# coding: UTF-8

# 71. ストップワード
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
# さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
# それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．

import re
from nltk.corpus import stopwords

def isInStoplist(sentence):
    words = [word.lower() for word in re.sub("[\.\,\!\?;\:\(\)\[\]\'\"]$", '', sentence.rstrip()).split()]
    for x in [word.lower() for word in re.sub("[\.\,\!\?;\:\(\)\[\]\'\"]$", '', sentence.rstrip()).split()]:
        print x
    result = set(words).intersection(set(stopwords.words('english')))
    print stopwords.words('english')
    return True if len(result) != 0 else False

if __name__ == '__main__':

    print isInStoplist("I have a Muhanmad. I have a radzi. -> Munhanmad radzi")
