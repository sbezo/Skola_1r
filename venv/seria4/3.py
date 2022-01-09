min = 16
ukoncene = 3
dlzka = int(input("kolko sekund si volal? "))
cena = ((dlzka - 60) // 10) * ukoncene
Vcena = cena + min
print("bude ta to stat: ", Vcena, " centov")