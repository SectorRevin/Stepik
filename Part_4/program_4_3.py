n = int(input())
k = int(input())
if n > k:
    print("NO")
elif n < k:
    print("YES")
else:
    print("Don't know")

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif a == b or b == c or a == c:
    print("Равнобедренный")
else:
    print("Разносторонний")

a, b, c = int(input()), int(input()), int(input())
if a < b < c or c < b < a:
    print(b)
elif b < c < a or a < c < b:
    print(c)
else:
    print(a)

n = int(input())
if n == 2:
    print("28")
elif n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print("31")
else:
    print("30")

n = int(input())
if n < 60:
    print("Легкий вес")
elif 60 <= n < 64:
    print("Первый полусредний вес")
elif 64 <= n < 69:
    print("Полусредний вес")

a = int(input())
b = int(input())
action = input()
if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "/":
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        print(a / b)
else:
    print("Неверная операция")

a = input()
b = input()
if a == b and (a == "красный" or a == "синий" or a == "желтый"):
    print(a)
elif a == "красный" or b == "красный":
    if a == "синий" or b == "синий":
        print("фиолетовый")
    elif a == "желтый" or b == "желтый":
        print("оранжевый")
    else:
        print("ошибка цвета")
elif a == "синий" or b == "синий":
    if a == "желтый" or b == "желтый":
        print("зеленый")
    else:
        print("ошибка цвета")
else:
    print("ошибка цвета")

n = int(input())
if n == 0:
    print("зеленый")
elif 1 <= n <= 10:
    if n % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 11 <= n <= 18:
    if n % 2 != 0:
        print("черный")
    else:
        print("красный")
elif 19 <= n <= 28:
    if n % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 29 <= n <= 36:
    if n % 2 != 0:
        print("черный")
    else:
        print("красный")
else:
    print("ошибка ввода")

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print("пустое множество")
elif a2 <= a1 <= b1 <= b2:
    print(a1, b1)
elif a1 <= a2 <= b2 <= b1:
    print(a2, b2)
elif b1 == a2:
    print(a2)
elif a1 == b2:
    print(b2)
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
