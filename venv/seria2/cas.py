def vysklonuj(cislo):
    if cislo == 1: return 'a'
    elif cislo == 2 or cislo == 3 or cislo == 4: return 'y'
    else: return ''



a = int(input("kolko sekund: "))
h = a // 3600
m = (a % 3600) // 60
s = (a % 3600) % 60

print("je to " + str(h) + " hodin" + vysklonuj(h) + " " + str(m) + " minut" + vysklonuj(m) + " " + str(s) + " sekund" + vysklonuj(s))