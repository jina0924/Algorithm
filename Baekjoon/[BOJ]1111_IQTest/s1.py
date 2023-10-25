# 백준 1111번 IQ Test - 3%

import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
if n <= 1:
    print('A')
elif n == 2:
    # X Y
    if arr[0] != arr[1]:
        print('A')
    # X X
    else:
        print(arr[0])
else:
    d1, d2 = arr[1] - arr[0], arr[2] - arr[1]
    if d1 == 0:
        # X X Y
        for i in range(1, n):
            if arr[i] - arr[i - 1]:
                print('B')
                break
        # X X X
        else:
            print(arr[0])
    else:
        a = d2 / d1
        if a == int(a):
            for i in range(3, n):
                d1 = d2
                d2 = arr[i] - arr[i - 1]
                # X X Y
                if d1 == 0 and d2 != 0:
                    print('B')
                    break
                # X Y.2 Z
                if d1 and d2 / d1 != a:
                    print('B')
                    break
            # X Y Z
            else:
                b = arr[1] - arr[0] * a
                print(int(arr[n - 1] * a + b))
        # X.1 Y.2 Z.3
        else:
            print('B')