rychlost = int(input("ako rýchlo ides v km/h? "))
cas = int(input("ako dlho ides v hodinach?"))
draha = rychlost * cas
jedenKM = int(input("aka je tvoja spotrebav litroch na 1OO km?"))
spotreba = jedenKM/100 * draha
print("prejdes ", draha, " kilomertrov a tvoja spotreba bude ", spotreba, "litrov")
