# coding: UTF-8

# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
# （弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
# （参考: マークアップ早見表）．

import re
template = {}
kiso_flag = False

for line in open("documents/jawiki-country-uk.txt"):
    if re.search(r"基礎情報", line):
        kiso_flag = True
    if re.match(r"\}\}", line):
        kiso_flag = False
    if kiso_flag:
        match = re.search(r"(.*)\s=\s(.*)", line)
        if match:
            template.update({match.group(1):match.group(2).replace("'''''","").replace("'''","").replace("''","")})

for key, value in template.iteritems():
    print "%s = %s" %(key,value)