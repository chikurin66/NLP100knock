#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．


f = open('../data/hightemp.txt')
data = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

data2 = data.replace('\t', " ")  # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)
print data2
