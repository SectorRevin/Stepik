a = float(input())
b = float(input())
print(a * b * 0.5)

S = float(input())
v1 = float(input())
v2 = float(input())
print(S/(v1 + v2))

n = float(input())
if n == 0:
    print("Обратного числа не существует")
else:
    print(n**(-1))

t = float(input())
print((5/9) * (t-32))

n = float(input())
if n <= 2:
    print(n * 10.5)
else:
    print(21 + ((n-2) * 4))

n = float(input())
n = n * 10
print(int(n) % 10)

n = float(input())
print(n - int(n))

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print("Наименьшее число =", min(a, b, c, d, e))
print("Наибольшее число =", max(a, b, c, d, e))

a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c), (a+b+c) - max(a, b, c) -
      min(a, b, c), min(a, b, c), sep="\n")

n = int(input())
d2 = (n // 10 ** 2) % 10  # Находим сотни
d1 = (n // 10 ** 1) % 10  # Находим десятки
d0 = (n // 10 ** 0) % 10  # Находим единицы
if max(d0, d1, d2) - min(d0, d1, d2) == (d0 + d1 + d2) - max(d0, d1, d2) - min(d0, d1, d2):
    print("Число интересное")
else:
    print("Число неинтересное")

a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())
print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))

a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
print(abs(a1-b1) + abs(a2-b2))
