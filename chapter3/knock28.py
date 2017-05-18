# coding: UTF-8

# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値から
# MediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

import re
template = {}
kiso_flag = False
string = ""

for line in open("data/jawiki-country-uk.txt"):
    if re.search(r"基礎情報", line):
        kiso_flag = True
    if re.match(r"\}\}", line):
        kiso_flag = False
    if kiso_flag:
        match = re.search(r"(.*)\s=\s(.*)", line)
        if match:
            string = re.sub(r"(\[\[)|(\]\])", "", match.group(2).replace("'''''", "").replace("'''", "").replace("''", ""))
            string = string.replace("<br","").replace("/>","")
            string2 = re.search(r"(.*)<ref(.*)", string)
            if string2:
                string = string2.group(1)
            template.update({match.group(1).replace("|",""):string})

for key, value in template.iteritems():
    print "%s = %s" %(key,value)