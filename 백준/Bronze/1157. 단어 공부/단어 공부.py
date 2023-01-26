word = input().upper()
w_set = list(set(word))
count = []
for w in w_set:
    cnt = word.count(w)
    count.append(cnt)

if count.count(max(count)) > 1:
    print('?')
else:
    print(w_set[count.index(max(count))])