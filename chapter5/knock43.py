# coding: UTF-8

# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．


import knock41


if __name__ == '__main__':
    sentences = knock41.CreateChunkList('../data/neko.cabocha')

    dependencies = []
    str1 = []
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != '-1':
                haveNoun = False
                haveVerb = False
                for word in chunk.morphs:
                    if word.pos == '名詞':
                        haveNoun = True
                for word in sentence[int(chunk.dst)].morphs:
                    if word.pos == '動詞':
                        haveVerb = True
                if haveNoun and haveVerb:
                    for word in chunk.morphs:
                        if word.surface != "、" and word.surface != "。":
                            str1.append(word.surface)
                    str1.append('\t')
                    for word in sentence[int(chunk.dst)].morphs:
                        if word.surface != "、" and word.surface != "。":
                            str1.append(word.surface)
                    dependencies.append(''.join(str1))
                    str1 = []

    for dependency in dependencies:
        print dependency