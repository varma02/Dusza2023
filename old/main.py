# KANDO-MRB csapat
# Vincze Roland, Váradi Marcell, Matuza Balázs
# © Copyright 2022-2022, KSZC Kandó Kálmán Technikum


import foglalas
import foglalas_torles
import statisztika


commands = [foglalas.foglalas, foglalas_torles.foglalas_torles, statisztika.statisztika, exit]

def menu():
    while True:
        print("Foglalás - 1\nFoglalás törlése - 2\nStatisztika - 3\nKilépés - 4")
        try:
            id = int(input("Id: "))
            if id not in range(1, 5):
                print("Hibás adat!" + "\n" * 4)
                continue
            break
        except ValueError:
            print("Hibás adat!" + "\n" * 4)
    commands[id-1]()

menu()