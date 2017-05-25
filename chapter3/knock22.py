# coding: UTF-8

# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re
pattern = r"Category:(?P<cat>.*)\]\]"
repattern = re.compile(pattern)
for line in open('../data/jawiki-country-uk.txt','r'):
    match = repattern.search(line)
    if match:
        print match.group('cat')
