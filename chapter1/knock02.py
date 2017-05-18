#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

str1 = u"パトカー"
str2 = u"タクシー"
print "".join([p + t for p, t in zip(str1, str2)])

