# coding: UTF-8

# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

# 改善する必要あり

import math

f = open('../data/hightemp.txt')
lines = f.readlines()
f.close()

n = raw_input('input N : ')
N = float(n)

num_row = len(lines)

sp = math.ceil(num_row / N)

inc = 0
lar = 0
for i in range(0, num_row):
    inc += 1
    print lines[i],
    if inc%sp == 0:
        print ""
        lar += 1
        if lar == num_row % N:
            inc = 0
            sp -= 1
