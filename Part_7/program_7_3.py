from math import log
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        count += 1
print(count)

n = int(input())
summ = 0
for _ in range(n):
    a = int(input())
    summ += a
print(summ)

n = int(input())
summ = 1
znam = 2
for _ in range(n - 1):
    summ += 1/znam
    znam += 1
summ -= log(n)
print(summ)

n = int(input())
summ = 0
for i in range(1, n + 1):
    if i**2 % 10 == 2:
        summ += i
    elif i**2 % 10 == 5:
        summ += i
    elif i**2 % 10 == 8:
        summ += i
print(summ)

n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

itog = 1
for i in range(10):
    n = int(input())
    if n != 0:
        itog *= n
print(itog)

n = int(input())
summ = 0
for i in range(1, n + 1):
    if n % i == 0:
        summ += i
print(summ)

n = int(input())
summ = 0
for i in range(1, n + 1):
    summ += ((-1) ** (i+1)) * i
print(summ)

n = int(input())
max_1 = 0
max_2 = 0
for _ in range(n):
    i = int(input())
    if i >= max_1:
        max_1 = i
    if max_1 >= max_2:
        max_2, max_1 = max_1, max_2
print(max_2, max_1, sep="\n")

flag = True
for _ in range(10):
    n = int(input())
    if n % 2 != 0:
        flag = False
if flag == False:
    print("NO")
else:
    print("YES")

n = int(input())
a = 0
b = 1
for i in range(n):
    if i == 0:
        print(b, end=" ")
    else:
        print(a + b, end=" ")
        a, b = b, a + b
