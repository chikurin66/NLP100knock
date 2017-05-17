#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ

f = open('documents/hightemp.txt')
lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
                      # lines: リスト。要素は１行の文字列データ
f.close()
print len(lines)

print open('/Users/Takebayashi/Documents/Laboratory/NLP/hightemp.txt','r').read().count("\n")

