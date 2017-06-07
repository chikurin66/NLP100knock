# coding: UTF-8

'''
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
'''


import CaboCha

if __name__ == '__main__':

    parser = CaboCha.Parser()

    sentence = "吾輩はここで始めて人間というものを見た"
    # sentence = "その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。"

    tree = parser.parse(sentence)
    cabocha_data = tree.toString(CaboCha.FORMAT_LATTICE)
    word_dest = list()  # 1節文の文字列と修飾先の数字，名詞を含むかどうかを格納
    dest_num = -1
    section = ""
    kaku_dict = {}
    noun = False
    print cabocha_data

    for line in cabocha_data.splitlines():
        if line == "EOS":
            word_dest.append([section, dest_num, noun])
        elif str(line[0]) == "*":
            if section != "":
                word_dest.append([section, dest_num, noun])
                section = ""
                noun = False
            dest_num = int(line.split(" ")[2].rstrip('D'))
        else:
            section = section + line.split("\t")[0]
            if not noun and line.split("\t")[1].split(',')[0] == "名詞":
                noun = True

    for x in word_dest:
        print x[0], x[1], x[2]
    print ""
    '''
    word_destの中身：
        吾輩は 5 True
        ここで 2 True
        始めて 3 False
        人間という 4 True
        ものを 5 True
        見た -1 False
    '''
    for chunk, dest, noun in word_dest:
        if noun:
            print chunk, "->",
            while 1:
                print word_dest[dest][0],
                dest = word_dest[dest][1]
                if dest == -1:
                    break
                print "->",
            print ""

