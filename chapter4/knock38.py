# coding: UTF-8

# 38. ヒストグラム
# 単語の出現頻度のヒストグラム
# （横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

import knock36
import matplotlib.pyplot as plt


freq_dict = knock36.Create_freq_dict("../data/neko.mecab")

labels = []
height = []
maxValue = sorted(freq_dict.values(), reverse=True)[0]

currentValue = 1
counter = 0
for key, value in sorted(freq_dict.items(), key=lambda x: x[1]):
    if currentValue != value:
        labels.append(currentValue)
        height.append(counter)
        currentValue = value
        counter = 0
    counter += 1
labels.append(currentValue)
height.append(counter)

n = raw_input('input # of group: ')
N = int(n)
g_labels = []
g_height = []
a = maxValue / N
b = maxValue % N
c = 0

print "maxValue:", maxValue
print a, "*", N, "+", b, "=", a*N+b

sum = 0
a += 1
th = a
g_labels.append(0)
for l, h in zip(labels, height):
    print l," ", h
    if l < th:
        sum += h
    else:
        while l >= th:
            print "group was changed"
            g_labels.append(th)
            th += a
            g_height.append(sum)
            sum = 0
        sum = h
g_height.append(sum)

plt.bar(g_labels, g_height, width=a)
plt.show()
