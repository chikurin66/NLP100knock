# coding: UTF-8

# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import sys

f = open('documents/hightemp.txt')
lines = f.readlines()
f.close()

n = raw_input('imput N : ')
N = int(n)

for i in range(1, N+1):
    sys.stdout.write(lines[-i])







