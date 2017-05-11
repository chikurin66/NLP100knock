# coding: UTF-8

# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
# 素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．

import re
from nltk.corpus import stopwords
import nltk


def stemming(sentence):
    lemmatizer = nltk.WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word.lower()) for word in re.sub("[\.\,\!\?;\:\(\)\[\]\'\"]$", '', sentence.rstrip()).split()]
    result = set(words) - set(stopwords.words('english'))
    return result


def extractFeatures(filename):
    # 特徴をディクショナリー型で抽出．リストで集めつので単語の重複も考慮される．
    pos_features = []
    neg_features = []
    for line in open('documents/' + filename + '.txt', 'r'):
        label = line[:2]
        try:
            if label == '+1':
                for word in stemming(line[3:]):
                    pos_features.append(word)
            elif label == '-1':
                for word in stemming(line[3:]):
                    neg_features.append(word)
        except:
            continue

    features_dic = {'+1': pos_features, '-1': neg_features}
    print "pos_features:", len(features_dic['+1'])
    print "neg_features:", len(features_dic['-1'])
    return features_dic


if __name__ == '__main__':
    filename = "sentiment"
    extractFeatures(filename)