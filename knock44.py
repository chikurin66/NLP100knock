# coding: UTF-8

# 44. 係り受け木の可視化
# 与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

from graphviz import Digraph
import CaboCha

if __name__ == '__main__':
    G = Digraph(format='png')
    G.attr('node', shape='circle')
    parser = CaboCha.Parser()

    sentence = "その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。"

    tree = parser.parse(sentence)
    cabocha_data = tree.toString(CaboCha.FORMAT_LATTICE)
    modify = []  # 1節文の文字列と修飾先の数字を格納
    modify_num = -1
    section = ""
    for line in cabocha_data.splitlines():
        if line == "EOS":
            modify.append([section, modify_num])
        elif str(line[0]) == "*":
            if section != "":
                modify.append([section, modify_num])
                section = ""
            modify_num = int(line.split(" ")[2].replace('D', ''))
        else:
            section = section + line.split("\t")[0]

    for chunk in modify:
        if chunk[1] != -1:
            G.edge(unicode(chunk[0], 'utf-8'), unicode(modify[chunk[1]][0], 'utf-8'))

    print(G.source)
    G.render('knock_tree.gv', view=True)

