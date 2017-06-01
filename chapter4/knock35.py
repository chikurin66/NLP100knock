# coding: UTF-8

# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．


import knock30

result = knock30.morpho("../data/neko.mecab")
continue_flag = False
for sentence in result:
    for i in range(len(sentence)-1):
        if sentence[i]['pos'] == "名詞" and sentence[i+1]['pos'] == "名詞":
            continue_flag = True
            print sentence[i]['surface'],
        if sentence[i]['pos'] == "名詞" and sentence[i+1]['pos'] != "名詞" and continue_flag is True:
            continue_flag = False
            print sentence[i]['surface']

