# coding: UTF-8

# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import re
template = {}
kiso_flag = False

for line in open("data/jawiki-country-uk.txt"):
    if re.search(r"基礎情報", line):
        kiso_flag = True
    if re.match(r"\}\}", line):
        kiso_flag = False
    if kiso_flag:
        match = re.search(r"\|(.*)\s=\s(.*)", line)
        if match:
            template.update({match.group(1):match.group(2)})

for key, value in template.iteritems():
    print "%s = %s" %(key,value)
