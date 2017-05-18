# coding: UTF-8

# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

import knock36
import matplotlib.pyplot as plt

freq_dict = knock36.Create_freq_dict("data/neko.mecab")

rank = 1
labels = []
height = []
for key, value in sorted(freq_dict.items(), key=lambda x:x[1], reverse=True):
    labels.append(rank)
    height.append(value)
    rank += 1

plt.loglog(labels, height)
plt.show()