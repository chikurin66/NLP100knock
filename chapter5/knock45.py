# coding: UTF-8

'''
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

・動詞を含む文節において，最左の動詞の基本形を述語とする
・述語に係る助詞を格とする
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
    始める  で
    見る は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

・コーパス中で頻出する述語と格パターンの組み合わせ
・「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
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
                    kaku_dict[dest_v] = part
                else:
                    kaku_dict[dest_v] += " " + part

    for k, v in kaku_dict.items():
        print k + "\t" + v


