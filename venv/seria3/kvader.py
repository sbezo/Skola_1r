a = int(input("hrana a v cm je dlha: "))
b = int(input("hrana b v cm je dlha: "))
c = int(input("hrana c v cm je dlha: "))
povrch = (a * b * 2) + (b * c * 2) + (c * a *2)
objem = a * b * c
print("povrch v centimeroch stvorcovych je ", povrch, " a objem v centimetroch kubickych je ", objem)