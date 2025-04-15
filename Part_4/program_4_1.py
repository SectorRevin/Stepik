pass1 = input()
pass2 = input()
if pass1 == pass2:
    print("Пароль принят")
else:
    print("Пароль не принят")

n = int(input())
if n % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

n = int(input())
d3 = (n // 10 ** 3) % 10  # Находим тысячи
d2 = (n // 10 ** 2) % 10  # Находим сотни
d1 = (n // 10 ** 1) % 10  # Находим десятки
d0 = (n // 10 ** 0) % 10  # Находим единицы
if d3 + d0 == d2 - d1:
    print("ДА")
else:
    print("НЕТ")

n = int(input())
if n < 18:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")

a, b, c = int(input()), int(input()), int(input())
if b - a == c - b:
    print("YES")
else:
    print("NO")

n1, n2 = int(input()), int(input())
if n1 < n2:
    print(n1)
if n1 > n2:
    print(n2)
else:
    print("Числа равны")

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b:
    ab = a
if a > b:
    ab = b
if a == b:
    ab = a
if c < d:
    cd = c
if c > d:
    cd = d
if c == d:
    cd = c
if ab < cd:
    print(ab)
else:
    print(cd)

n = int(input())
if n <= 13:
    print("детство")
if 13 < n <= 24:
    print("молодость")
if 24 < n <= 59:
    print("зрелость")
if 59 < n:
    print("старость")

a, b, c = int(input()), int(input()), int(input())
summ = 0
if a > 0:
    summ = summ + a
if b > 0:
    summ = summ + b
if c > 0:
    summ = summ + c
print(summ)
