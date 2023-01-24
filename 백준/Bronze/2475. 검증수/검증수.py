data = list(map(int, input().split()))
checksum = 0
for num in data:
    checksum += num ** 2
checksum %= 10
print(checksum)