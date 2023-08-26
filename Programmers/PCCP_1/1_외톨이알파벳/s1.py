import sys
sys.stdin = open('input3.txt')
from collections import defaultdict

def solution(input_string):
    answer = ''
    solo = set()
    isfound = defaultdict(int)
    
    for i in range(len(input_string)):
        char = input_string[i]
        if isfound[char]:
            if i > 0 and char != input_string[i - 1]:
                solo.add(char)
        else:
            isfound[char] = 1
    
    if solo:
        answer = ''.join(sorted(solo))
    else:
        answer = 'N'
    return answer

print(solution(input()))