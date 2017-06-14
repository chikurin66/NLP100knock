# coding: UTF-8

'''
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
'''

import corenlp

def tokenize(filename, text):
    return 1

if __name__ == '__main__':
    parser = corenlp.StanfordCoreNLP()
    json_data = parser.parse("I am NLPer.")
    print json_data


