objem = float(input("v ml je objem: "))
cena = float(input("a stál: "))
jcena = 1 / (objem / 1000) * cena
print("jednotkova cena je: ", jcena, "eur za liter")