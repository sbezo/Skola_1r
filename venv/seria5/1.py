vyska = float(input("zadaj vyske v metroch: "))
hmotnost = float(input("zadaj vahu v kilogramoch: "))
bmi = round(hmotnost / (vyska ** 2), 2)
print("tvoje bmi je", bmi)