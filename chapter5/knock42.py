# coding: UTF-8

# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

import re
import knock41

class Morph:

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:

    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

def CreateDependency(sentences):
    dependencies = []
    str1 = []
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != '-1':
                for word in chunk.morphs:
                    if word.surface != "、" and word.surface != "。":
                        str1.append(word.surface)
                str1.append('\t')
                for word in sentence[int(chunk.dst)].morphs:
                    if word.surface != "、" and word.surface != "。":
                        str1.append(word.surface)
                dependencies.append(''.join(str1))
                str1 = []
        dependencies.append('\n')
    return dependencies

if __name__ == '__main__':
    sentences = knock41.CreateChunkList('data/neko.cabocha')

    dependencies = CreateDependency(sentences)

    for dependency in dependencies:
        print dependency
