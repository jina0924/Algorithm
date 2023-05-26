# 백준 17413번 단어 뒤집기2

import sys
sys.stdin = open('input.txt')

s = input()
word = ''
isTag = False
for char in s:
    if char == '>':
        print(word + '>', end='')
        word = ''
        isTag = False
    elif char == ' ' and not isTag:
        print(word[::-1] + ' ', end='')
        word = ''
    elif char == '<':
        if word:
            print(word[::-1], end='')
        word = char
        isTag = True
    else:
        word += char
if word:
    print(word[::-1])