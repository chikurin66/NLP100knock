#!/usr/bin/env python
# -*- coding: utf-8 -*-

import knock005 as kn5

n = 2
mode = 'char'
string1 = "paraparaparadise"
string2 = "paragraph"

bigram_set1 = set(kn5.ngram(string1, n, mode))
bigram_set2 = set(kn5.ngram(string2, n, mode))
print bigram_set1
print bigram_set2

print "sum set -> %s" % (bigram_set1 | bigram_set2)
print "product set -> %s" % (bigram_set1 & bigram_set2)
print "difference set (1)-(2) -> %s" % (bigram_set1 - bigram_set2)
print "difference set (2)-(1) -> %s" % (bigram_set2 - bigram_set1)

print 'se' in bigram_set1
print 'se' in bigram_set2


