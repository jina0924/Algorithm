import sys
sys.stdin = open('input.txt')

X = int(input())
nums = [0] * (X + 1)
def calc(n):
    if n == 1:
        return 0
    if nums[n]:
        return nums[n]
    if n % 3 == 0:
        if n % 2:
            nums[n] = min(calc(n // 3) + 1, calc(n - 1) + 1)
        else:
            nums[n] = min(calc(n // 3) + 1, calc(n // 2) + 1)
    elif n % 3 == 1:
        if n % 2:
            nums[n] = calc(n - 1) + 1
        else:
            nums[n] = min(calc(n // 2) + 1, calc(n - 1) + 1)
    else:
        if n % 2:
            nums[n] = calc(n - 1) + 1
        else:
            nums[n] = min(calc(n // 2) + 1, calc(n - 1) + 1)
    return nums[n]
print(calc(X))