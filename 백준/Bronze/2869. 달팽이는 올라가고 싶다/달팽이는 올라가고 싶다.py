a, b, v = map(int, input().split())
up = a - b

if (v-b) % up == 0:
    print((v-b) // up)
else:
    print((v-b) // up + 1)