# coding: UTF-8

# 75. 素性の重み
# 73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．

import numpy
from knock72 import extractFeatures


if __name__ == '__main__':
    filename = "sentiment"
    features = extractFeatures(filename)

    words = list(set(features['+1'] + features['-1']))

    pos_vec = numpy.zeros(len(words))
    neg_vec = numpy.zeros(len(words))

    for feature in features['+1']:
        pos_vec[words.index(feature)] += 1
    for feature in features['-1']:
        neg_vec[words.index(feature)] += 1

    print "pos_vec"
    counter = 0
    for index, value in sorted(enumerate(pos_vec), key=lambda x:x[1], reverse=False):
        print index, words[index], value
        counter += 1
        if counter >= 10:
            break
    print "neg_vec"
    counter = 0
    for index, value in sorted(enumerate(neg_vec), key=lambda x:x[1], reverse=False):
        print index, words[index], value
        counter += 1
        if counter >= 10:
            break