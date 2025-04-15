n = int(input())
if n % 100 == 0:
    print("YES")
else:
    print("NO")


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if ((a1 + b1) % 2 == 0) and ((a2 + b2) % 2 == 0):
    print("YES")
elif ((a1 + b1) % 2 != 0) and ((a2 + b2) % 2 != 0):
    print("YES")
else:
    print("NO")


a = int(input())
b = input()
if (10 <= a <= 15) and b == "f":
    print("YES")
else:
    print("NO")


n = int(input())
if n == 1:
    print("I")
elif n == 2:
    print("II")
elif n == 3:
    print("III")
elif n == 4:
    print("IV")
elif n == 5:
    print("V")
elif n == 6:
    print("VI")
elif n == 7:
    print("VII")
elif n == 8:
    print("VIII")
elif n == 9:
    print("IX")
elif n == 10:
    print("X")
else:
    print("ошибка")


n = int(input())
if not n % 2 == 0:
    print("YES")
elif (n % 2 == 0) and 2 <= n <= 5:
    print("NO")
elif (n % 2 == 0) and 6 <= n <= 20:
    print("YES")
elif (n % 2 == 0) and n > 20:
    print("NO")


a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a1 + b1 == a2 + b2) or (a1 - b1 == a2 - b2):
    print("YES")
else:
    print("NO")


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 + 2 == x2 or x1 - 2 == x2:
    if y1 + 1 == y2 or y1 - 1 == y2:
        print("YES")
    else:
        print("NO")
elif x1 + 1 == x2 or x1 - 1 == x2:
    if y1 + 2 == y2 or y1 - 2 == y2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a1 + b1 == a2 + b2) or (a1 - b1 == a2 - b2) or a1 == a2 or b1 == b2:
    print("YES")
else:
    print("NO")
