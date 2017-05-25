# coding: UTF-8

# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import re
import urllib
import json
template = {}
kiso_flag = False
string = ""

for line in open("../data/jawiki-country-uk.txt"):
    if re.search(r"基礎情報", line):
        kiso_flag = True
    if re.match(r"\}\}", line):
        kiso_flag = False
    if kiso_flag:
        match = re.search(r"(.*)\s=\s(.*)", line)
        if match:
            string = re.sub(r"(\[\[)|(\]\])", "", match.group(2).replace("'''''", "").replace("'''", "").replace("''", ""))
            string = string.replace("<br","").replace("/>", "")
            string2 = re.search(r"(.*)<ref(.*)", string)
            if string2:
                string = string2.group(1)
            template.update({match.group(1).replace("|", ""): string})


print "https://upload.wikimedia.org/wikipedia/en/a/ae/" + template["国旗画像"].replace(" ", "_")
# 苦し紛れに上記の方法で実行した...
# 下記の手法の方がよさそうだが意味がわからない。
url = "http://ja.wikipedia.org/w/api.php?format=json&action=query&titles=Image:%s&prop=imageinfo&iiprop=url"
response = urllib.urlopen(url % template["国旗画像"]).read()
jres = json.loads(response)
print jres['query']['pages']['-1']["imageinfo"][0]["url"].encode("utf-8")
