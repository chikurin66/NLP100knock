# coding: UTF-8

# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

import sys
import math

str_list = []
for line in open('documents/hightemp.txt','r'):
    str_list.append(line.split('\t')[0])

result = []
for key in set(str_list):
    result.append([key, str_list.count(key)])

for x in sorted(result, key=lambda x:x[1], reverse=True): # ソートするコラムを指定できる
    print x[0],x[1]

print ''

for x in sorted(result,reverse=True): # 単純にかけば最初の要素からの多重ソートになる
    print x[0],x[1]