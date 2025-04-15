from math import *
from math import floor, ceil
from math import sin, cos, tan, radians, pow
from math import sqrt, pow
from math import pi, pow
import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))

R = float(input())
print(pi * pow(R, 2))
print(2 * pi * R)

a = float(input())
b = float(input())
print((a+b) / 2)
print(sqrt(a * b))
print((2*a*b) / (a+b))
print(sqrt((pow(a, 2) + pow(b, 2)) / 2))

r = float(input())
r = radians(r)
print(sin(r) + cos(r) + pow(tan(r), 2))

n = float(input())
print(floor(n) + ceil(n))

a = float(input())
b = float(input())
c = float(input())
D = pow(b, 2) - 4 * a * c
if D > 0:
    x1 = (-b - sqrt(D)) / 2 * a
    x2 = (-b + sqrt(D)) / 2 * a
    if x1 < x2:
        print(x1, x2, sep='\n')
    else:
        print(x2, x1, sep='\n')
elif D == 0:
    x = -(b / 2*a)
    print(x)
else:
    print('Нет корней')

n = int(input())
a = float(input())
s1 = n * pow(a, 2)
s2 = 4 * tan(pi / n)
print(s1 / s2)
