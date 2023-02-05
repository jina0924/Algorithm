import sys

n = int(input())
count = n
for i in range(n):
    word = sys.stdin.readline()
    for j in range(len(word)-1):
        if word.find(word[j]) > word.find(word[j+1]):
            count -= 1
            break
            
print(count)