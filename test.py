from math import sqrt, pow
a = float(input())
b = float(input())
c = float(input())
D = pow(b, 2) - (4 * a * c)
print(D)
if D > 0:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    if x1 < x2:
        print(x1, x2, sep='\n')
    else:
        print(x2, x1, sep='\n')
elif D == 0:
    x = (-b) / (2*a)
    print(x)
else:
    print('Нет корней')
