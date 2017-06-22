# coding: UTF-8

'''
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

以下コマンド
java -cp "/usr/local/lib/stanford-corenlp-full-2014-08-27/*"
-Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP
-annotators tokenize,ssplit,pos,lemma,ner,depparse,dcoref
-file /Users/yutoTakebayashi/PycharmProjects/NLP100Knock/data/nlp_sentence.txt
'''


import xml.etree.ElementTree as ET

tree = ET.parse("../data/nlp_sentence.txt.xml")
root = tree.getroot()
words = root.findall("document/sentences/sentence/tokens/token/word")
# words = root.findall(".//word")

for word in words:
    print word.text
