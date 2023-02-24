import db


def foglalas():
    print()
    
    nev = input("Vendég neve: ").strip().strip(";")
    print()

    while True: 
        szekek = input("Székek száma: ").strip()
        if szekek.isnumeric():
            szekek = int(szekek)
            break
        print("Helytelen szék szám, próbáld újra!")
    print()

    while True:
        hely = input("Asztal helye (B: beltéri, K: kültéri): ").strip().upper()
        if hely in ["B", "K"]:
            break
        print("Nincs ilyen hely, próbáld újra!")
    print()

    while True:
        try: 
            datum = [int(x) for x in input("Dátuma (hónap-nap): ").strip().split("-")]
            if 0 < datum[0] < 13:
                if datum[0] % 2 == 0 and 0 < datum[1] < 32: break
                elif datum[0] % 2 != 0 and 0 < datum[1] < 31: break
            raise Exception()
        except Exception: print("Helytelen dátum, próbáld újra!")
    print()

    while True:
        try:
            kezdo_ido = [int(x) for x in input("Kezdő időpont (óra:perc): ").strip().split(":")]
            veg_ido = [int(x) for x in input("Végső időpont (óra:perc): ").strip().split(":")]

            if kezdo_ido[0] < veg_ido[0] or \
            (kezdo_ido[0] == veg_ido[0] and kezdo_ido[1] < veg_ido[1]):
                break

            raise Exception()
        except Exception:
            print("Helytelen időpont, próbáld újra!")
    print()

    asztalok = db.getSzabadAsztalok(datum[0], datum[1], kezdo_ido[0], kezdo_ido[1])
    
    legjobb_asztal = -1
    legjobb_asztal_szek = float("inf")
    for a in asztalok:
        if int(a[1]) >= szekek and int(a[1]) <= legjobb_asztal_szek:
            legjobb_asztal = int(a[0])
            legjobb_asztal_szek = int(a[1])

    # ÖSSZETOLÁS

    if legjobb_asztal == -1:
        print("Nincs elérhető asztal a megadott személyszámra.")
        varolista = -1 if input("Szeretne várólistára kerülni? (I/N) ").strip().upper() == "I" else -2
        db.appendFoglalasok(nev, "F", f"{datum[0]}-{datum[1]} {kezdo_ido[0]}:{kezdo_ido[1]}", f"{veg_ido[0]}:{veg_ido[1]}", szekek, str(varolista))
    else:
        db.appendFoglalasok(nev, "F", f"{datum[0]}-{datum[1]} {kezdo_ido[0]}:{kezdo_ido[1]}", f"{veg_ido[0]}:{veg_ido[1]}", szekek, str(legjobb_asztal))
    
    print("Foglalás sikeresen rögzítve.\n")
