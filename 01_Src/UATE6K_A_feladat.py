'''
[Készítő: Szy László Csongor (UATE6K)
Objektum-orientált programozás, A feladat
Főmodul]
'''

import autokolcsonzo, szemelyauto, teherauto, berles
from datetime import date

'''- Autó bérlése
  - Bérlés lemondása
  - Bérlések listázása'''

kolcsonzo = autokolcsonzo.Autokolcsonzo()

#Az alkalmazás főmenüje
def menu():
    while True:
        print("Autókölcsönző\n " + kolcsonzo.nev)
        print("\t1 - Autó bérlése")
        print("\t2 - Bérlés lemondása")
        print("\t3 - Bérlések listázása")
        print("\t0 - Kilépés")

        choice = input("Válassz műveletet: ").strip()

        if choice == "0":
            print("Kilépés.")
            break

        match choice:
            case 1: #Autó bérlése
                pass
            case 2: #Bérlés lemondása
                pass
            case 3: #Bérlések listázása
                pass
            case _: #Default
                print("Kérem, válasszon a fenti számok közül!")
                continue

#A kezdeti értékek beállítása
def initValues():
    kolcsonzo.autok = [teherauto("THR-123", "Iveco Palfinger", 25000), teherauto("TEH-456", "Mercedes-Benz Actros", 37500), szemelyauto("SZE-789", "Trabant 601", 12500)]
    
    kolcsonzo.berlesek = [berles("THR-123", date(2026, 5, 21)), berles("THR-123", date(2026, 8, 23)), berles("TEH-456", date(2025, 1, 2)), berles("SZE-789", date(2026, 5, 23))]
    
#Belépési pont
if __name__ == "__main__":    
    initValues()
    menu()