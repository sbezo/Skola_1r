import math

p = int(input("priemer je v m: "))
osadnici = int(input("na pusti ich je: "))
v = round((4 / 3) * math.pi * (p / 2) ** 3, 2)
vx = v * 1000
naDni = vx / (10 * osadnici)
print("v litroch je objem ", vx, "a voda im vydrží na ", naDni, "dní" )
