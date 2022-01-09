v = 2
u = 1
while v >= u:
    u = int(input("tvoje prve cislo je: "))
    v = int(input("tvoje druhe cislo je: "))
    a = 2 * u * v
    b = (u * u) - (v * v)
    c = (u * u) + (v * v)
    print("prve cislo musi byt vacsie, skus este raz")

print(" prvé pytagorejske cislo je ", a, ", druhé je ", b, " a tretie je ", c)