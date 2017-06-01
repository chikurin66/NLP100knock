# coding: UTF-8

# 31. 動詞
# 動詞の表層形をすべて抽出せよ．

import knock30

result = knock30.morpho("../data/neko.mecab")
for sentence in result:
    for morph_dict in sentence:
        if morph_dict['pos'] == "動詞":
            print morph_dict['surface']