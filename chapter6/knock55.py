# coding: UTF-8

'''
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
'''

import xml.etree.ElementTree as ET

tree = ET.parse("../data/nlp_sentence.txt.xml")
root = tree.getroot()
word_list = root.findall("document/sentences/sentence/tokens/token/word")
ner_list = root.findall("document/sentences/sentence/tokens/token/NER")

for word, ner in zip(word_list, ner_list):
    if ner.text == "PERSON":
        print word.text
