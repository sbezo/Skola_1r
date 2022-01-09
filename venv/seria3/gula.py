import math

p = int(input("priemer je v m: "))
v = round((4 / 3) * math.pi * (p / 2) ** 3, 2)
print("objem v metroch kubických je ", v)
vx = v * 1000
print("v litroch je objem ", vx)
