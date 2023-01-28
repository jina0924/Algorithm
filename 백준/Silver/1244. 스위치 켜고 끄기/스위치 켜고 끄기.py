# 백준 1244번 스위치 켜고 끄기

def switch_boy(arr, pos):
    for i in range(pos-1, len(arr), pos):
        if arr[i]:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr

def switch_girl(arr, pos):
    left = right = pos-1
    while left >= 0 and right < len(arr):
        if arr[left] and arr[right]:
            arr[left] = 0
            arr[right] = 0
            left -= 1
            right += 1
        elif arr[left] == 0 and arr[right] == 0:
            arr[left] = 1
            arr[right] = 1
            left -= 1
            right += 1
        else:
            break
    return arr

n = int(input())
switch = list(map(int, input().split()))
for _ in range(int(input())):
    gender, position = map(int, input().split())
    if gender == 1:
        switch = switch_boy(switch, position)
    else:
        switch = switch_girl(switch, position)

for i in range(0, n, 20):
    print(*switch[i:i+20])
