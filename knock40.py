# coding: UTF-8

# 第5章: 係り受け解析
# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
# その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

import CaboCha

def prepare_CaboChaFile(sourcefile, outputfile):
    c = CaboCha.Parser()
    result = []
    for sentence in open(sourcefile,'r'):
        tree = c.parse(sentence)
        result += tree.toString(CaboCha.FORMAT_LATTICE)
    w = open(outputfile, 'w')
    w.write(''.join(result))
    w.close()

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．
# このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
# をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
# 各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

import re

class Morph:

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

if __name__ == '__main__':

    # prepare_CaboChaFile('documents/neko.txt', 'documents/neko.cabocha')

    pattern = r'\*'
    repattern = re.compile(pattern)
    words = []
    sentence = []
    for line in open('data/neko.cabocha','r'):
        if line != 'EOS\n':
            a = repattern.match(line)
            if a != None:
                if a.start() == 0:
                    continue
            str1 = re.split(r'\t|,', line)
            words.append(Morph(str1[0], str1[6], str1[1], str1[2]))
        else:
            if len(words) > 0:
                sentence.append(words)
                words = []

    for x in sentence[3]:
        print x.surface,