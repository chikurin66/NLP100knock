# coding: UTF-8

'''
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，
文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

(代表参照表現) ((参照表現))とする．

'''

import xml.etree.ElementTree as ET

tree = ET.parse("../data/nlp_sentence.txt.xml")
root = tree.getroot()
sent_list = root.findall("document/sentences/sentence")
coref_list = root.findall(".//coreference/coreference")

sentence = []
sentences = []
# list of list expressing sentences
for i, sent in enumerate(sent_list):
    word_list = sent.findall("tokens/token/word")
    for j, word in enumerate(word_list):
        sentence.append(word.text)
    sentences.append(sentence)
    sentence = []

repr_dict = {}
repr_sent = ""
# make dictionary that has representative as key and original expression as value
for l in coref_list:
    m = l.findall("mention")
    for n in m:
        if "representative" in n.attrib:
            repr_sent = n.find("text").text
            if repr_sent not in repr_dict:
                repr_dict[repr_sent] = list()
        else:
            repr_dict[repr_sent].append([n.find("sentence").text, n.find("start").text, n.find("text").text])

# insert representative like (representative) ((original expression))
for key, value in repr_dict.items():
    for elem in value:
        sent_num, start_num, mention = elem
        # ここはミスってる．一文に二つの今日参照があった場合，ずれてしまう．
        # printで制御すべきか？
        sentences[int(sent_num)-1].insert(int(start_num)-1+len(mention.split(" ")), "}")
        sentences[int(sent_num)-1].insert(int(start_num)-1, "("+key+") {")

for sent in sentences:
    for word in sent:
        print word,
    print ""

