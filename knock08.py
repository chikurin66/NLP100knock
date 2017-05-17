#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(str1):
    str2 = ''
    for char in str1:
       str2 += chr(219-ord(char)) if char.islower() else char
    return str2

if __name__ == '__main__':
    str = raw_input()
    print cipher(str)
