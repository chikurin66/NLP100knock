# coding: UTF-8

# 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラスChunkを実装せよ．
# このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
# 係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
# さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
# 8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．

import re
from knock40 import Morph

class Chunk:

    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def show(self):
        for morph in self.morphs:
            print morph.show_surface()
        print ""


def CreateChunkList(sourcefile):

    pattern = r'\*'
    repattern = re.compile(pattern)
    chunks = []
    sentence = []
    morphs = []
    srcs = {}
    for line in open(sourcefile, 'r'):
        if line != 'EOS\n':
            a = repattern.match(line)
            if a is None:
                str1 = re.split(r'\t|,', line)
                morphs.append(Morph(str1[0], str1[6], str1[1], str1[2]))

            else:
                if a.start() == 0:
                    if len(morphs) > 0:
                        if str2[1] in srcs:
                            chunks.append(Chunk(morphs, dst, srcs[str2[1]]))
                        else:
                            chunks.append(Chunk(morphs, dst, list()))
                        morphs = []

                    str2 = re.split(r'\s|\t', line)
                    dst = str2[2].rstrip('D')
                    if dst in srcs:
                        srcs[dst].append(int(str2[1]))
                    else:
                        srcs[dst] = [int(str2[1])]

        else:
            if len(morphs) > 0:
                if str2[1] in srcs:
                    chunks.append(Chunk(morphs, dst, srcs[str2[1]]))
                else:
                    chunks.append(Chunk(morphs, dst, list()))
                morphs = []
            if len(chunks) > 0:
                sentence.append(chunks)
                chunks = []
                srcs = {}

    return sentence

if __name__ == '__main__':

    sentences = CreateChunkList('../data/neko.cabocha')

    n = raw_input('input sentence # : ')
    N = int(n)

    for x in sentences[N]:
        for y in x.morphs:
            print y.surface,
        print "/",
    print ""
    for x in sentences[N]:
        print x.dst,
    print ""
    for x in sentences[N]:
        print x.srcs,
    print ""

    for chunk in sentences[N]:
        chunk.show()