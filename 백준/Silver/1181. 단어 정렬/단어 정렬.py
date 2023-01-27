#1181 단어 정렬
n = int(input())
words_set = set()
words = []

for i in range(n):
    words_set.add(input())

for w in words_set:
    words.append([len(w), w])

words.sort()

for i in range(len(words)):
    print(words[i][1])