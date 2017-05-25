# coding: UTF-8

# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル
# （例えば"== セクション名 =="なら1）を表示せよ．

import re
pattern = r"^(=+)(.*?)(=+)"
repattern = re.compile(pattern)
for line in open('../data/jawiki-country-uk.txt','r'):
    match = repattern.search(line)
    if match:
        elements = match.groups()
        print "%s %s" % (len(elements[0]), elements[1])

print ""
print ""

import re
# ()でくくることでグループとしている
pattern = r"=(=+)([^=]*)(=+)"

repattern = re.compile(pattern)
for line in open('../data/jawiki-country-uk.txt','r'):
    match = repattern.search(line)
    if match:
        elements = match.groups()
        print "%s %s" % (len(elements[0]), elements[1])
