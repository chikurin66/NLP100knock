# coding: UTF-8

'''
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
ただし，主語，述語，目的語の定義は以下を参考にせよ．

述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）

'''

from graphviz import Digraph
import xml.etree.ElementTree as ET


def Extract_SVO(tree, sent_num):

    root = tree.getroot()
    # get collapsed-dependencies list
    depe_list = [d for d in root.findall(".//dependencies") if d.get('type') == 'collapsed-dependencies']
    # focus on one sentence
    dependencies = depe_list[sent_num]

    nsubj = []
    dobj = []

    for dep in dependencies.findall('dep'):
        if dep.get("type") == "nsubj":
            governor = dep.find("governor")
            dependent = dep.find("dependent")
            nsubj.append([governor.text, dependent.text, governor.get("idx")])

        if dep.get("type") == "dobj":
            governor = dep.find("governor")
            dependent = dep.find("dependent")
            dobj.append([governor.text, dependent.text, governor.get("idx")])

    print nsubj
    print dobj

    output = []
    # search same idx
    # v is s_g (= o_g)
    for s_g, s_d, s_idx in nsubj:
        for o_g, o_d, o_idx in dobj:
            if s_idx == o_idx:
                output.append("\t".join([s_d, s_g, o_d]))
    for line in output:
        print line


if __name__ == '__main__':
    tree = ET.parse("../data/nlp_sentence.txt.xml")
    for i in range(10):
        print i
        Extract_SVO(tree, i)
