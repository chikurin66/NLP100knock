# coding: UTF-8

# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
# その結果をneko.mecabというファイルに保存せよ．
# このファイルを用いて，以下の問に対応するプログラムを実装せよ．

# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
# をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import MeCab

def CreateMecabFile():
    m = open("documents/neko.mecab","w")
    text = ""
    me = MeCab.Tagger('mecabrc')
    for line in open("documents/neko.txt","r"):
        text += me.parse(line)
    m.write(text)
    m.close()



import re

def morpho(data_path):
    result = []
    sentence = []
    morph_dict = {}
    for line in open(data_path,"r"):
        if line == "EOS\n":
            result.append(sentence)
            sentence = []

        else:
            morph = re.split(r",|\t", line)
            morph_dict = {
                'surface':morph[0],
                'base':morph[7],
                'pos':morph[1],
                'pos1':morph[2]
            }
            sentence.append(morph_dict)

    return result

if __name__ == '__main__':
    # preparation for 30
    CreateMecabFile()

    sentence_morph_list = morpho("documents/neko.mecab")
    print len(sentence_morph_list)
    for i in range(20):
        for j in sentence_morph_list[i]:
            print j['surface'],
        print ""


