b = int(input())
q = int(input())
n = int(input())
print(b * q**(n - 1))

a = int(input())
print(a // 100)

print(int(input()) // 100)

n = int(input())
k = int(input())
print(k // n, k % n, sep="\n")

a = int(input())
b = (a % 2) / 2
print(int(a/2 + b))

a = int(input())
print(a, "мин - это", a // 60, "час", a % 60, "минут.")

n = int(input())
print(-(-n // 4))

n = int(input())
a = n % 10  # Находим единицы
b = (n // 10) % 10  # Находим десятки
с = n // 100  # Находим сотни
print("Сумма цифр =", a + b + с)
print("Произведение цифр =", a * b * с)

n = int(input())
c = n % 10  # Находим единицы
b = (n // 10) % 10  # Находим десятки
a = n // 100  # Находим сотни
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")

n = int(input())
d3 = (n // 10 ** 3) % 10  # Находим тысячи
d2 = (n // 10 ** 2) % 10  # Находим сотни
d1 = (n // 10 ** 1) % 10  # Находим десятки
d0 = (n // 10 ** 0) % 10  # Находим единицы
print("Цифра в позиции тысяч равна", d3)
print("Цифра в позиции сотен равна", d2)
print("Цифра в позиции десятков равна", d1)
print("Цифра в позиции единиц равна", d0)
