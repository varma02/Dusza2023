import db
import datetime



    
"""def foglalas_torles(vendeg, start):
    foglalasok = db.readRawFoglalasok()
    foglalas = list(filter(lambda x: x[0] == vendeg, foglalasok))[0]
    foglalas[1] = "L"
    db.appendFoglalasok(*foglalas)

print(db.getSzabadAsztalok(6, 30, 16, 40,))"""

def foglalas_torles():
    nev = input("Adja meg a nevét!: ")
    while True:
        try:
            kezdet = input("Adja meg a foglalás kezdetét! [Hónap-Nap Óra:Perc]: ")
            hónap = (kezdet.split(" ")[0].split("-")[0])
            nap = (kezdet.split(" ")[0].split("-")[1])
            óra = (kezdet.split(" ")[1].split(":")[0])
            perc = (kezdet.split(" ")[1].split(":")[1])
            datetime.datetime(2022, int(hónap), nap, óra, perc)
            break
        except ValueError:
            print("Hibás adat!:")

    check = False
    for sor in db.readRawFoglalasok():
        if sor[0].lower() == nev.lower():
            if sor[2] == f"{hónap}-{nap} {óra}:{perc}":
                db.appendFoglalasok(sor["nev"], "L", *sor[2:])
                check = True
    if not check:
        print("Nincs ilyen foglalás!")
    else: print("Foglalás sikeresen törölve.")