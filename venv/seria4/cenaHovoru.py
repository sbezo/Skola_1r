kredit = float(input("tvoj kredit v eurach je: "))
cenaZaJ = float(input("cena za jednu minutu v eurach je: "))
minut = kredit / cenaZaJ
cenaSMS = float(input("kolko stoji jedna sms: "))
smsiek = (kredit // cenaSMS)
print("možzes volat ", minut, "minut alebo napísať ", smsiek, " esemesiek")
