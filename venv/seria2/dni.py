def vysklonujD(den):
    if den == 1: return "den"
    else: return "dni"

def vysklonujT(tyzden):
    if tyzden == 1: return "tyzden"
    if tyzden == 1 or tyzden == 2 or tyzden ==3: return "tyzdne"
    else: return "tyzdnov"

def vysklonujM(mesiac):
    if mesiac ==1: return "mesiac"
    if mesiac ==2 or mesiac == 3 or mesiac ==4: return "mesiace"
    else: return "mesiacov"

def vysklonujR(rok):
    if rok == 1: return "rok"
    if rok == 2 or rok == 3 or rok == 4: return "roky"
    else: return "rokov"


a = int(input("pocet dni: "))
r = a // 360
m = a % 360 // 30
t = a % 360 % 30 //7
d = a % 360 % 30 %7


print(str(r) + " " + vysklonujR(r) + ", " + str(m) + " " + vysklonujM(m) + ", " + str(t) + " " + vysklonujT(t) + " a " + str(d) + " " + vysklonujD(d))