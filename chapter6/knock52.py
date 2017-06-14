# coding: UTF-8

'''
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
'''

from nltk import stem
import knock50
import knock51


def stemming(words):
    stemmer = stem.PorterStemmer()
    for word in words:
        print "\t".join([word, stemmer.stem(word)])

if __name__ == '__main__':
    with open("../data/nlp.txt", "r") as f:
        text = f.readlines()
        sentences = knock50.separateIntoSentences(text)
        words = knock51.separateIntoWords(sentences)
        stemming(words)

