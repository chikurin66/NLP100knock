# coding: UTF-8

# 本章では，Bo Pang氏とLillian Lee氏が公開しているMovie Review Dataのsentence polarity dataset v1.0を用い，
# 文を肯定的（ポジティブ）もしくは否定的（ネガティブ）に分類するタスク（極性分析）に取り組む．

# 70. データの入手・整形
# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．
#
# rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

import random



def labeling():
    neg = ["-1 %s" % line.rstrip() for line in open('data/rt-polarity.neg','r')]
    pos = ["+1 %s" % line.rstrip() for line in open('data/rt-polarity.pos','r')]
    pol = neg + pos
    random.shuffle(pol)
    return pol

if __name__ == '__main__':

    pol = labeling()

    output = open('data/sentiment.txt','w')

    for item in pol:
        output.write("%s\n" % item)

    output.close()

    print "pos: %s" % len(filter(lambda x: x[:2] == '+1', pol))
    print "neg: %s" % len(filter(lambda x: x[:2] == '-1', pol))