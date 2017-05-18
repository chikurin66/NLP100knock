# coding: UTF-8

# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．


import numpy
from knock72 import extractFeatures
from sklearn import linear_model


def LogisticRegressionModel(features):

    words = list(set(features['+1'] + features['-1']))

    pos_vec = numpy.zeros(len(words))
    neg_vec = numpy.zeros(len(words))

    for feature in features['+1']:
        pos_vec[words.index(feature)] += 1
    for feature in features['-1']:
        neg_vec[words.index(feature)] += 1

    logit_model = linear_model.LogisticRegression()
    logit_model.fit([pos_vec, neg_vec], [1, -1])

    return (words, logit_model)

def aaa(features):
    fe = []
    for x in features['+1']:
        fe.append(['+1', x])
    for x in features['-1']:
        fe.append(['-1', x])
    return fe

if __name__ == '__main__':
    filename = "sentiment"
    logit = linear_model.LogisticRegression()
    features = extractFeatures(filename)
    LogisticRegressionModel(features)