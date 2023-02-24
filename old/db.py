import datetime
from re import A

def readAsztalok():
    with open("data/asztalok.txt", "r") as f:
        asztalok =  {}
        for sor in f.readlines():
            sor = sor.strip().split(";")
            asztalok[sor[0]] = sor[1:]
        return asztalok

# def writeAsztalok():
#     with open("data/asztalok.txt", "r") as f:
#         asztalok =  {}
#         for sor in f.readlines():
#             sor = sor.strip().split(";")
#             asztalok[sor[0]] = sor[1:]
#         print(asztalok)

def readRawFoglalasok():
    with open("data/foglalasok.txt", "r", encoding="utf-8") as f:
        arr = []
        for line in f.readlines():
            arr.append(line.strip().split(";"))
        return arr

def readFoglalasok():
    foglalasok =  []
    with open("data/foglalasok.txt", "r", encoding="utf-8") as f:
        for sor in f.readlines():
            try:
                sor = sor.strip().split(";")
                foglalasok.append({
                    "nev": sor[0],
                    "tipus": sor[1],
                    "kezdet": {
                        "honap": int(sor[2].split(" ")[0].split("-")[0]),
                        "nap": int(sor[2].split(" ")[0].split("-")[1]),
                        "ora": int(sor[2].split(" ")[1].split(":")[0]),
                        "perc": int(sor[2].split(" ")[1].split(":")[1]),
                    },
                    "befejezes": {
                        "ora": int(sor[3].split(":")[0]),
                        "perc": int(sor[3].split(":")[1]),
                    },
                    "szekek": int(sor[4]),
                    "asztalok": [int(x) for x in sor[5:]],
                })
            except:
                print(f"Hiba az egyik sorban: {sor}")
    return foglalasok

def readRealFoglalasok():
    foglalasok = readFoglalasok()

    lemondott = list(filter(lambda x: x["tipus"] == "L", foglalasok))
    return list(filter(lambda x: x not in lemondott, foglalasok))

def getSzabadAsztalok(honap, nap, ora, perc):
    asztalok = readAsztalok()
    foglalasok = readRealFoglalasok()
    # print(foglalasok)

    nemszabad = []
    szabad = []

    # PS H:\Csapat\Csapat2\h> py
    # Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
    # Type "help", "copyright", "credits" or "license" for more information.
    # >>> import datetime
    # >>> a = datetime.datetime(month=5, day=4, hour=10, minute=20)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: function missing required argument 'year' (pos 1)
    # >>> a = datetime.datetime(year=2022, month=5, day=4, hour=10, minute=20)
    # >>> a.timesamp()
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # AttributeError: 'datetime.datetime' object has no attribute 'timesamp'
    # >>> a.timestamp()
    # 1651652400.0
    # >>>
    for Foglalas in list(filter(lambda i: datetime.datetime(year=2022, month=i["kezdet"]["honap"], day=i["kezdet"]["nap"], hour=i["kezdet"]["ora"], minute=i["kezdet"]["perc"]).timestamp() < datetime.datetime(year=2022, month=honap, day=nap, hour=ora, minute=perc).timestamp() and datetime.datetime(year=2022, month=honap, day=nap, hour=ora, minute=perc).timestamp() < datetime.datetime(year=2022, month=i["kezdet"]["honap"], day=i["kezdet"]["nap"], hour=i["befejezes"]["ora"], minute=i["befejezes"]["perc"]).timestamp(), foglalasok)):
        if Foglalas["tipus"] == "F" and -1 not in Foglalas["asztalok"]:
            for l in Foglalas["asztalok"]:
                nemszabad.append(l)
    
    for key, val in asztalok.items():
        if int(key) not in nemszabad:
            szabad.append([int(key), *asztalok[key]])
    
    return szabad


def appendFoglalasok(name, fogl, start, end, szekek, *asztalok) -> None:
    with open("data/foglalasok.txt", 'a') as f:
        f.write(f"\n{name};{fogl};{start};{end};{szekek};{';'.join(asztalok)}")