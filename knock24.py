# coding: UTF-8

# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import re
pattern = r"(File:([^|]*))|(ファイル:([^|]*))"
repattern = re.compile(pattern)
for line in open("documents/jawiki-country-uk.txt"):
    match = repattern.search(line)
    if match:
        print match.group(1) if match.group(3) is None else match.group(3)