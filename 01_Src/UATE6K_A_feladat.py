'''
[Készítő: Szy László Csongor (UATE6K)
Objektum-orientált programozás, A feladat
Főmodul]
'''

import autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles
from datetime import date, datetime

'''- Autó bérlése
  - Bérlés lemondása
  - Bérlések listázása'''

kolcsonzo = autokolcsonzo.Autokolcsonzo("Badzsit Autókölcsönző")

#Az alkalmazás főmenüje
def menu():
    while True:
        print("[" + kolcsonzo.nev + " - Autókölcsönző nyilvántartás]")
        print("\n\t1 - Autó bérlése")
        print("\t2 - Bérlés lemondása")
        print("\t3 - Bérlések listázása")
        print("\t0 - Kilépés")

        choice = int(input("Kérem, válasszon műveletet: ").strip())

        match choice:
            case 0: #Kilépés
                print("Kilépés.")
                exit()
                break
            case 1: #Autó bérlése
                choiceRent = input("Rendszám, kategória vagy típus alapján válasszunk autót? [R, K vagy T, vissza: X]:").upper()
                match choiceRent:
                    case "R": #Rendszámszerinti keresés
                        rendszamIn = input("Rendszám: ")
                        datumIn = input("Dátum (éééé-hh-nn): ")
                        try:
                            datumIn = datetime.strptime(datumIn, "%Y-%m-%d").date()
                            print(kolcsonzo.ujBerles(rendszamIn, datumIn))
                        except(ValueError):
                            print("Hibás dátum! Kérem, használja a következő formátumot: éééé-hh-nn")
                            continue    
                        break
                    case "K":
                        #TODO: kategóriaszerinti keresés
                        break
                    case "T":
                        #TODO: típusszerinti keresés
                        break
                    case "X": #Kilépés
                        break
                    case _:
                        print("Kérem, válasszon a fenti lehetőségek közül!")
                        continue
            case 2: #Bérlés lemondása
                rendszamIn = input("Rendszám: ")
                datumIn = input("Dátum (éééé-hh-nn): ")
                try:
                    datumIn = datetime.strptime(datumIn, "%Y-%m-%d").date()
                    print(kolcsonzo.berlesLemondas(rendszamIn, datumIn))
                except(ValueError):
                    print("Hibás dátum! Kérem, használja a következő formátumot: éééé-hh-nn")
                    continue    
                break
            case 3: #Bérlések listázása
                print(kolcsonzo.berlesekLista())
                break
            case _: #Default
                print("Kérem, válasszon a fenti lehetőségek közül!")
                continue
    menu()

#A kezdeti értékek beállítása
def initValues():
    kolcsonzo.autok = [Teherauto("THR-123", "Iveco Palfinger", 25000), Teherauto("TEH-456", "Mercedes-Benz Actros", 37500), Szemelyauto("SZE-789", "Trabant 601", 12500)]
    
    kolcsonzo.berlesek = [Berles("THR-123", date(2026, 5, 21)), Berles("THR-123", date(2026, 8, 23)), Berles("TEH-456", date(2025, 1, 2)), Berles("SZE-789", date(2026, 5, 23))]
    
#Belépési pont
if __name__ == "__main__":    
    initValues()
    menu()