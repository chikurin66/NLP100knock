# coding: UTF-8

# 44. 係り受け木の可視化
# 与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

from graphviz import Digraph
import CaboCha

if __name__ == '__main__':
    G = Digraph(format='png')
    # 属性(attribute)の設定: nodeの形をcircleに
    G.attr('node', shape='circle')
    parser = CaboCha.Parser()

    sentence = "その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。"

    tree = parser.parse(sentence)
    cabocha_data = tree.toString(CaboCha.FORMAT_LATTICE)
    word_dest = list()  # 1節文の文字列と修飾先の数字を格納
    dest_num = -1
    section = ""

    '''
    word_destの中身：
    その後 3
    猫にも 3
    だいぶ 3
    逢ったが 9
    こんな 5
    片輪には 9
    一度も 7
    出会わし 9
    た事が 9
    ない。 -1
    '''

    for line in cabocha_data.splitlines():
        if line == "EOS":
            word_dest.append([section, dest_num])
        elif str(line[0]) == "*":
            if section != "":
                word_dest.append([section, dest_num])
                section = ""
            dest_num = int(line.split(" ")[2].rstrip('D'))
        else:
            section = section + line.split("\t")[0]

    for chunk in word_dest:
        if chunk[1] != -1:
            # 係り受け元->係り受け先
            G.edge(unicode(chunk[0], 'utf-8'), unicode(word_dest[chunk[1]][0], 'utf-8'))

    print(G.source)
    G.render('../data/knock_tree.gv', view=True)

