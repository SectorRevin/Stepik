x = int(input())
if -1 < x < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")

x = int(input())
if x <= -3 or x >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")

x = int(input())
if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")

a, b, c = int(input()), int(input()), int(input())
if a + b > c and b + c > a and a + c > b:
    print('YES')
else:
    print("NO")

y = int(input())
if (y % 4 == 0 and not (y % 100 == 0)) or y % 400 == 0:
    print("YES")
else:
    print("NO")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (-1 <= (x1 - x2) <= 1) and (-1 <= (y1 - y2) <= 1):
    print("YES")
else:
    print("NO")
