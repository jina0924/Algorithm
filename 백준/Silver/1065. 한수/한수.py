n = int(input())

def han(x):
    count = 0
    for i in range(1, x+1):
        if i % 10 == i or i % 100 == i:
            count += 1
        else:
            if (i // 100) - ((i  // 10) % 10) == ((i  // 10) % 10) - (i % 10):
                count += 1
    return count

print(han(n))