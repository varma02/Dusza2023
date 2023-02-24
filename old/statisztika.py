import db


def statisztika():
    foglalasok = []
    lemondasok = [] #F4
    varolista = [] #F3
    sikeresVarolista = [] #F3.2
    elutasítottFoglalas = []

    for sor in db.readFoglalasok():
        if sor["tipus"] == "F":
            foglalasok.append(sor)
        else: lemondasok.append(sor)

    for sor in foglalasok:
        if -1 in sor["asztalok"]:
            varolista.append(sor)

    for sor in foglalasok:
        for sorCheck in varolista:
            if sorCheck["nev"] == sor["nev"]:
                if sorCheck["tipus"] == sor["tipus"]:
                    if sorCheck["kezdet"] == sor["kezdet"]:
                        if sorCheck["befejezes"] == sor["befejezes"]:
                            if sorCheck["szekek"] == sor["szekek"]:
                                if -1 not in sor["asztalok"]:
                                    sikeresVarolista.append(sor)

    for sor in foglalasok:
        if -2 in sor["asztalok"]:
            elutasítottFoglalas.append(sor)

    igaziFoglalasok = len(foglalasok) - len(sikeresVarolista) #F1
    sikertelenFoglalasok = len(elutasítottFoglalas) + (len(varolista) - len(sikeresVarolista)) #F5
    instantFoglalasok = len(foglalasok) - len(varolista) - sikertelenFoglalasok #F2
    
    return print(f"""    Foglalási igények: {igaziFoglalasok}
    Egyből teljesített foglalások: {instantFoglalasok}
    Várólistás foglalások: {len(varolista)}
    Várólistás teljesített foglalások: {len(sikeresVarolista)}
    Lemondott foglalások: {len(lemondasok)}
    Sikertelen foglalások: {sikertelenFoglalasok}""")

