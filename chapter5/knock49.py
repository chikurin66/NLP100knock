# coding: UTF-8

'''
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiiとjj（i<ji<j）のとき，係り受けパスは以下の仕様を満たすものとする．

・問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
・文節iiとjjに含まれる名詞句はそれぞれ，XとYに置換する

また，係り受けパスの形状は，以下の2通りが考えられる．

・文節iiから構文木の根に至る経路上に文節jjが存在する場合: 文節iiから文節jjのパスを表示
・上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kkで交わる場合: 文節iiから文節kkに至る直前のパスと文節jjから文節kkに至る直前までのパス，文節kkの内容を"|"で連結して表示

例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
'''

import CaboCha


def find_same_chunk(x_list, y_list):
    for x in x_list:
        for y in y_list:
            if x == y:
                return x
    return None

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
    noun = "None"
    print cabocha_data

    for line in cabocha_data.splitlines():
        if line == "EOS":
            word_dest.append([section, dest_num, noun])
        elif str(line[0]) == "*":
            if section != "":
                word_dest.append([section, dest_num, noun])
                section = ""
                noun = "None"
            dest_num = int(line.split(" ")[2].rstrip('D'))
        else:
            if noun == "None" and line.split("\t")[1].split(',')[0] == "名詞":
                noun = line.split("\t")[1].split(',')[6]
                section = section + noun
            else:
                section = section + line.split("\t")[0]


    for x in word_dest:
        print x[0], x[1], x[2]
    print ""
    '''
    word_destの中身：
        吾輩は 5 吾輩
        ここで 2 ここ
        始めて 3 None
        人間という 4 人間
        ものを 5 もの
        見た -1 None
    '''
    output_temp = list()
    output_list = list()
    for chunk, dest, noun in word_dest:
        if noun != "None":
            print chunk, "->",
            output_temp.append(chunk)
            while 1:
                print word_dest[dest][0],
                output_temp.append(word_dest[dest][0])
                dest = word_dest[dest][1]
                if dest == -1:
                    break
                print "->",
            print ""
        output_list.append(output_temp)
        output_temp = list()

    print "output_list: "
    for x in output_list:
        print "\t",
        for y in x:
            print y,
        print ""

    for i, x_path in enumerate(output_list):
        if x_path:
            for j, y_path in enumerate(output_list[i+1:]):
                if y_path:
                    # find same chunk in x_path and y_path
                    root_chunk = find_same_chunk(x_path, y_path)
                    if y_path[0] == root_chunk:  # |がいらない
                        print x_path[0].replace(word_dest[i][2], 'X'),
                        for x in x_path[1:]:
                            if x != root_chunk:
                                print "->", x,
                            else:
                                break
                        print "->", y_path[0].replace(word_dest[i+j+1][2], 'Y')

                    else:  # |がいる
                        print x_path[0].replace(word_dest[i][2], 'X'),
                        for x in x_path[1:]:
                            if x != root_chunk:
                                print "->", x,
                            else:
                                break
                        print "|",
                        print y_path[0].replace(word_dest[i+j+1][2], 'Y'),
                        for y in y_path[1:]:
                            if y != root_chunk:
                                print "->", y,
                            else:
                                break
                        print "|", root_chunk
