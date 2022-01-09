print("**  **  **\n" 
      "**********\n"
      "   *  *   \n"
      "   *  *\n"
      "   *  *\n"
      "   *  *\n"
      "   *  *\n"
      "   *  *\n"
      " ***  ***\n"
      "*        *\n"
      "**********\n"
      "**********\n")


#cenaPoštovného = int(input(" aká je cena poštovného: "))
#cenaKs = int(input("cena za ks: "))
#pocetKs = int(input("pocet ks je: "))
#celkom = cenaPoštovného + cenaKs * pocetKs
#print("zapatíš:", celkom)

#meno = input("ako sa voláš: ")
#rok = int(input("Kedy si sa narodil: " ))
#rokT = int(2021)
#vek = rokT -rok
#print("Voláš sa:", meno)
#
#print("mas", vek, "rokov")


meno = input("ako sa voláš: ")
rokN = int(input("kedy si sa narodi: "))
sk = int(input("do školy si šiel 6/7 ročný: "))
rokT = int(2021)
vek = rokT -rokN
if sk == 6:
      skZ = 6
elif sk == 7:
      skZ = 7


print("volas sa: ", meno)
print("narodil si sa v:", rokN)
print("teraz mas: ", vek)
print("do školy si začal chodiť ako: ", skZ)
print("na strednu si zacal chodiť v:", skZ +9)
print("maturovat budeš v ", skZ + 9 +4)
print("vysoku skoncis v:", skZ +9+4+5)

