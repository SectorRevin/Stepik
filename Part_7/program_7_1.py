for i in range(10):
    print("Python is awesome!")

for i in range(6):
    print("AAA")
for i in range(5):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")

text = input()
n = int(input())
for i in range(n):
    print(text)

n = int(input())
for i in range(n):
    print("*" * 19)

s = input()
for i in range(10):
    print(i, s)

n = int(input())
for i in range(n):
    print("Квадрат числа", i, "равен", i**2)
print("Квадрат числа", n, "равен", n**2)

n = int(input())
for i in range(n):
    print("*" * (n-i))

m = int(input())
p = int(input())
n = int(input())
print("1", float(m))
for i in range(n - 1):
    print(i + 2, m + m * (p/100))
    m = m + m * (p/100)
