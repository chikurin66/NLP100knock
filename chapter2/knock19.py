# coding: UTF-8

# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．


str_list = []
for line in open('../ata/hightemp.txt', 'r'):
    str_list.append(line.split('\t')[0])

result = {}
for key in set(str_list):
    result[key] = str_list.count(key)

for y in sorted(result.items(), key=lambda x: x[1], reverse=True):  # ソートするコラムを指定できる
    print y[0], y[1]

print ''

for y in sorted(result.items(), reverse=True):  # 単純にかけば最初の要素からの多重ソートになる
    print y[0], y[1]
