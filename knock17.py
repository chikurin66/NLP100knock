# coding: UTF-8

# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

import sys
import math

f = open('documents/hightemp.txt')
lines = f.readlines()
f.close()
str_set = set([])
for line in lines:
    str_set.add(line.split('\t')[0])

for x in str_set:
    print x












