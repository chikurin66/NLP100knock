# coding: UTF-8

# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import re
pattern = r"Category:"
repattern = re.compile(pattern)
for line in open('data/jawiki-country-uk.txt','r'):
    match = repattern.search(line)
    if match:
        print line,
