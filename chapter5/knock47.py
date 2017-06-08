# coding: UTF-8

'''
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．
・「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
・述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
・述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
・コーパス中で頻出する述語（サ変接続名詞+を+動詞）
・コーパス中で頻出する述語と助詞パターン
'''


import CaboCha

if __name__ == '__main__':

    parser = CaboCha.Parser()

    sentence = "別段くるにも及ばんさと、主人は手紙に返事をする。"

    tree = parser.parse(sentence)
    cabocha_data = tree.toString(CaboCha.FORMAT_LATTICE)
    word_dest = list()  # 1節文の文字列と修飾先の数字，サ変接続＋助詞（を），動詞を格納
    dest_num = -1
    section = ""
    kaku_dict = {}
    part = "None"
    verb = "None"
    shn = "None"
    shn_flag = False

    print cabocha_data

    for line in cabocha_data.splitlines():
        if line == "EOS":
            word_dest.append([section, dest_num, part, verb, shn])
            part = "None"
            verb = "None"
            shn = "None"
        elif str(line[0]) == "*":
            if section != "":
                word_dest.append([section, dest_num, part, verb, shn])
                section = ""
                part = "None"
                verb = "None"
                shn = "None"
            dest_num = int(line.split(" ")[2].rstrip('D'))
        else:
            section = section + line.split("\t")[0]
            lattice = line.split("\t")[1].split(',')

            if shn_flag and lattice[6] == "を":
                shn += lattice[6]
            shn_flag = False
            if lattice[0] == "助詞":
                # if part == "None":
                #     part = lattice[6]
                # else:
                #     part += " " + lattice[6]
                part = lattice[6]  # 最後の助詞を取得
            elif verb == "None" and lattice[0] == "動詞":
                verb = lattice[6]
            elif lattice[1] == "サ変接続":
                shn = lattice[6]
                shn_flag = True

    for v, w, x, y, z in word_dest:
        print "       ", v, w, x, y, z
    print ""
    '''
    word_destの中身：
        別段 1 None None None
        くるにも 2 に も くる None
        及ばんさと、 6 さ と 及ぶ None
        主人は 6 は None None
        手紙に 6 に None None
        返事を 6 を None 返事を
        する。 -1 None する None
    '''
    for i, wor_des in enumerate(word_dest):
        chunk, dest, part, verb, shn = wor_des
        if shn != "None":
            if word_dest[dest][3] != "None":
                word_dest[i][0] = shn + word_dest[dest][3]
                word_dest[i][4] = shn + word_dest[dest][3]
                word_dest[i][1] = -1
                word_dest[dest] = word_dest[i]


    for v, w, x, y, z in word_dest:
        print "       ", v, w, x, y, z
    print ""
    '''
        word_destの中身：
            別段 1 None None None
            くるにも 2 も くる None
            及ばんさと、 6 と 及ぶ None
            主人は 6 は None None
            手紙に 6 に None None
            返事をする -1 を None 返事をする
            返事をする -1 を None 返事をする
        '''

    for chunk, dest, part, verb, shn in word_dest:
        if part != "None":
            if dest == -1:
                break
            dest_s = word_dest[dest][4]
            if dest_s != "None":
                if dest_s not in kaku_dict:
                    kaku_dict[dest_s] = list()
                    kaku_dict[dest_s].append((part, chunk))
                else:
                    kaku_dict[dest_s].append((part, chunk))

    for verb, tuple_list in kaku_dict.items():
        print verb + "\t",
        for part, chunk in tuple_list:
            print part,
        print "\t",
        for part, chunk in tuple_list:
            print chunk,
        print ""
