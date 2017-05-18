# coding: UTF-8

# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

import knock30

result = knock30.morpho("data/neko.mecab")
for sentence in result:
    for i in range(len(sentence)-2):
        if sentence[i]['pos'] == "名詞" and sentence[i+1]['surface'] == "の" and sentence[i+2]['pos'] == "名詞":
            print sentence[i]['surface'],sentence[i+1]['surface'],sentence[i+2]['surface']