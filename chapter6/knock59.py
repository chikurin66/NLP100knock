# coding: UTF-8

'''
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．
入れ子になっている名詞句もすべて表示すること．
'''

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
