# coding: UTF-8

# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．


import knock36
import matplotlib.pyplot as plt


freq_dict = knock36.Create_freq_dict("documents/neko.mecab")

count = 0
v = []
k =[]
for key, value in sorted(freq_dict.items(), key=lambda x:x[1], reverse=True):
    print key,value
    k.append(key)
    v.append(value)
    count += 1
    if count >= 10:
        break

# unicodeに変換
# 普通ならu"文字列"で変換できるが、str型の変数には適応できなかったのでこのようにした。
for i in range(10):
    k[i] = unicode(k[i], 'utf-8')
    # k[i] = k[i].decode("unicode")
left = [i for i in range(10)] # 横軸(棒の左端の位置)
height = [val for val in v]
labels = [ke for ke in k]

plt.xticks(left, labels)
plt.bar(left, height, align='center')
plt.show()