# coding: UTF-8

'''
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
'''

import xml.etree.ElementTree as ET

tree = ET.parse("../data/nlp_sentence.txt.xml")
root = tree.getroot()
word_list = root.findall("document/sentences/sentence/tokens/token/word")
lemma_list = root.findall("document/sentences/sentence/tokens/token/lemma")
pos_list = root.findall("document/sentences/sentence/tokens/token/POS")

for word, lemma, pos in zip(word_list, lemma_list, pos_list):
    print "\t".join([word.text, lemma.text, pos.text])
