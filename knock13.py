# coding: UTF-8

# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

f1 = open('documents/col1.txt')
f2 = open('documents/col2.txt')

data1 = f1.readlines()
data2 = f2.readlines()

f1.close()
f2.close()

str = ''
for line1, line2 in zip(data1, data2):
    a = line1.replace('\n','')
    str += a + '\t' + line2 + '\n'

f = open('documents/col.txt', 'w')
f.write(str)
f.close()

print "documents was made"





