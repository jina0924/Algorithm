x = int(input())
n = 1
while x > n:
    x -= n
    n += 1

if n % 2 == 0:
    print('{0}/{1}'.format(x, n+1-x))
else:
    print('{0}/{1}'.format(n+1-x, x))