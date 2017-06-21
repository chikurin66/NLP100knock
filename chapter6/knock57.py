# coding: UTF-8

'''
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''

from graphviz import Digraph
import xml.etree.ElementTree as ET


def make_dependency_tree(sent_num):
    G = Digraph(format='svg')
    # 属性(attribute)の設定: nodeの形をcircleに
    G.attr('node', shape='circle')

    tree = ET.parse("../data/nlp_sentence.txt.xml")
    root = tree.getroot()
    # get collapsed-dependencies list
    depe_list = [d for d in root.findall(".//dependencies") if d.get('type') == 'collapsed-dependencies']
    # focus on one sentence
    dependencies = depe_list[sent_num]

    # nodes_set = set()
    for dep in dependencies.findall('dep'):
        # make edge from governor to dependent
        # put id to avoid that same words are regarded as same node
        from_edge = dep.find('governor').get('idx') + "_" + dep.find('governor').text
        to_edge = dep.find('dependent').get('idx') + "_" + dep.find('dependent').text
        G.edge(from_edge, to_edge)
        # nodes_set.add(from_edge)
        # nodes_set.add(to_edge)

    # G.body.append('{rank=same; "' + '"; "'.join(list(nodes_set)) + '";}')
    print G.source
    G.render('../data/knock57_tree.gv', view=True)

if __name__ == '__main__':
    make_dependency_tree(1)
