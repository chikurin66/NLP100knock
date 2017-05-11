# coding: UTF-8

# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import sys

f = open('documents/hightemp.txt')
line = f.readline()


n = raw_input('imput N : ')
N = int(n)

for i in range(0, N):
    sys.stdout.write(line)
    line = f.readline()

f.close()





