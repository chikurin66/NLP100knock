# coding: UTF-8

# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．

import knock30

result = knock30.morpho("../data/neko.mecab")
for sentence in result:
    for morph_dict in sentence:
        if morph_dict['pos1'] == "サ変接続":
            print morph_dict['surface']


