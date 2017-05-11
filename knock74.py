# coding: UTF-8

# 74. 予測
# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
# その予測確率を計算するプログラムを実装せよ．

import numpy
from knock72 import extractFeatures,stemming
from knock73 import LogisticRegressionModel
from sklearn import linear_model


if __name__ == '__main__':
    filename = "sentiment"
    features = extractFeatures(filename)
    knock73_instance = LogisticRegressionModel(features)
    words = knock73_instance[0]
    logit_model = knock73_instance[1]

    print logit_model

    sentence = "the story feels more like a serious read , filled with heavy doses of always enticing sayles dialogue ."
    input_vec = numpy.zeros(len(words))

    for word in stemming(sentence):
        try:
            index = words.index(word)
            input_vec[index] += 1
            print word
        except:
            continue
    print logit_model.predict(input_vec)
    print logit_model.predict_proba(input_vec)