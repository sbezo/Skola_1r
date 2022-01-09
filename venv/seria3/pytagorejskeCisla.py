b = 2
a = 1

while b >= a:
    a = int(input(" tvoje cislo je: "))
    b = int(input(" tvoje druhe cislo je: "))
    c = (a**2 + b**2)**(1/2)
    print("prve cislo musi byt vacsie ako druhe, skus este raz")

print("tretie pytagorejske cislo je: ", c)
