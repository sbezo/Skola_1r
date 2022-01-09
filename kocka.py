import random


a = 0
b = 0
c = 0
i = 0

x = int(input(("zadaj číslo: ")))
y = int(input("zadaj 2 číslo: "))
z = int(input("zadaj 3 číslo: "))
while not (a == x and b == y and c == z):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    i = i + 1
    print(a, b, c, i)

print('tri sestky padli na ', i, ' pokus.')