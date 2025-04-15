print('"Python is a great language!", said Fred. "I don' +
      "'t ever remember having this much fun" + ' before."')

print('''Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

print("\"Python is a great language!\", said Fred. \"I don\'t ever remember having this much fun before.\"")

name = input()
surname = input()
print("Hello", " ", name, " ", surname,
      "! You have just delved into Python", sep="")

fk = input()
print("Футбольная команда", fk, "имеет длину", len(fk), "символов")

name1 = input()
name2 = input()
name3 = input()
if len(name1) < len(name2) and len(name1) < len(name3):
    short_name = name1
elif len(name2) < len(name1) and len(name2) < len(name3):
    short_name = name2
elif len(name3) < len(name1) and len(name3) < len(name2):
    short_name = name3
if len(name1) > len(name2) and len(name1) > len(name3):
    dlin_name = name1
elif len(name2) > len(name1) and len(name2) > len(name3):
    dlin_name = name2
elif len(name3) > len(name1) and len(name3) > len(name2):
    dlin_name = name3
print(short_name)
print(dlin_name)

stroka1 = input()
stroka2 = input()
stroka3 = input()
a = int(len(stroka1))
b = int(len(stroka2))
c = int(len(stroka3))
sred_len = (a + b + c) - max(a, b, c) - min(a, b, c)
if sred_len + (sred_len - min(a, b, c)) == max(a, b, c):
    print("YES")
else:
    print("NO")

s = input()
if "синий" in s:
    print("YES")
else:
    print("NO")

s = input()
if 'суббота' in s or 'воскресенье' in s:
    print("YES")
else:
    print("NO")

mail = input()
if '@' in mail and '.' in mail:
    print("YES")
else:
    print("NO")
