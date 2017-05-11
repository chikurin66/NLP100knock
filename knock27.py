# coding: UTF-8

# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
# テキストに変換せよ（参考: マークアップ早見表）．

import re
template = {}
kiso_flag = False

for line in open("documents/jawiki-country-uk.txt"):
    if re.search(r"基礎情報", line):
        kiso_flag = True
    if re.match(r"\}\}", line):
        kiso_flag = False
    if kiso_flag:
        match = re.search(r"\|(.*)\s=\s(.*)", line)
        if match:
            string = re.sub(r"(\[\[)|(\]\])", "", match.group(2).replace("'''''","").replace("'''","").replace("''",""))
            template.update({match.group(1):string})

for key, value in template.iteritems():
    print "%s = %s" %(key,value)