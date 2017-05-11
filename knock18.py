# coding: UTF-8

# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

import sys
import math

f = open('documents/hightemp.txt')
lines = f.readlines()
f.close()

for i in range(0,len(lines)):
    for j in range(0,len(lines)-1-i):
        if lines[j].split('\t')[2] < lines[j+1].split('\t')[2]:
            a = lines.pop([j])
            lines.insert(j+1, a)

for line in lines:
    sys.stdout.write(line)















