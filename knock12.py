#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．


f = open('documents/hightemp.txt')
lines = f.readlines()  # ファイル終端まで全て読んだデータを返す
f.close()

str1 = ''
str2 = ''
for line in lines:
    str0 = line.split('\t')
    str1 += str0[0] + '\n'
    str2 += str0[1] + '\n'

f1 = open('documents/col1.txt', 'w')
f2 = open('documents/col2.txt', 'w')
f1.write(str1)
f2.write(str2)
f1.close()
f2.close()

print "made documents"


