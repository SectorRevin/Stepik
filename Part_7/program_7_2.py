m = int(input())
n = int(input())
for i in range(m, n + 1):
    print(i)

m = int(input())
n = int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

m = int(input())
n = int(input())
for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)

m = int(input())
n = int(input())
for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif (i // 10 ** 0) % 10 == 9:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)

n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
