# coding: UTF-8

'''
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．

・項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
・述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを
'''


import CaboCha

if __name__ == '__main__':

    parser = CaboCha.Parser()

    sentence = "吾輩はここで始めて人間というものを見た"

    tree = parser.parse(sentence)
    cabocha_data = tree.toString(CaboCha.FORMAT_LATTICE)
    word_dest = list()  # 1節文の文字列と修飾先の数字，助詞，動詞を格納
    dest_num = -1
    section = ""
    kaku_dict = {}
    part = "None"
    verb = "None"
    for line in cabocha_data.splitlines():
        if line == "EOS":
            word_dest.append([section, dest_num, part, verb])
            part = "None"
            verb = "None"
        elif str(line[0]) == "*":
            if section != "":
                word_dest.append([section, dest_num, part, verb])
                section = ""
                part = "None"
                verb = "None"
            dest_num = int(line.split(" ")[2].rstrip('D'))
        else:
            section = section + line.split("\t")[0]
            lattice = line.split("\t")[1].split(',')
            if lattice[0] == "助詞":
                if part == "None":
                    part = lattice[6]
                else:
                    part += " " + lattice[6]
            if verb == "None" and lattice[0] == "動詞":
                verb = lattice[6]

    for w, x, y, z in word_dest:
        print w, x, y, z
    print ""
    '''
    word_destの中身：
        吾輩は 5 は None
        ここで 2 で None
        始めて 3 て 始める
        人間という 4 という None
        ものを 5 を None
        見た -1 None 見る
    '''
    for chunk, dest, part, verb in word_dest:
        if part != "None":
            dest_v = word_dest[dest][3]
            if dest_v != "None":
                if dest_v not in kaku_dict:
                    kaku_dict[dest_v] = list()
                    kaku_dict[dest_v].append((part, chunk))
                else:
                    kaku_dict[dest_v].append((part, chunk))

    for verb, tuple_list in kaku_dict.items():
        print verb + "\t",
        for part, chunk in tuple_list:
            print part,
        print "\t",
        for part, chunk in tuple_list:
            print chunk,
        print ""
