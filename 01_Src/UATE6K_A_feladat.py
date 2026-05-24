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
        print("\n\n\t\t\t[" + kolcsonzo.nev + " - Autókölcsönző nyilvántartás]")
        print("\n1 - Autó bérlése")
        print("2 - Bérlés lemondása")
        print("3 - Bérlések listázása")
        print("X - Kilépés")

        choice = input("Kérem, válasszon műveletet: ").strip().upper()

        match choice:
                        
            case '1': #Autó bérlése
                choiceRent = input("\nRendszám, kategória vagy típus alapján válasszunk autót? [R, K vagy T, visszalépés: X]:").upper()
                
                match choiceRent:
                    
                    case "R": #Rendszámszerinti keresés
                        rendszamIn = input("Rendszám: ")
                        datumIn = input("Dátum (éééé-hh-nn): ")
                        try:
                            datumIn = datetime.strptime(datumIn, "%Y-%m-%d").date()
                        except(ValueError):
                            print("Hibás dátum! Kérem, használja a következő formátumot: éééé-hh-nn")
                            continue    
                        
                        print(kolcsonzo.ujBerles(rendszamIn, datumIn))
                        break
                    
                    case "K": #Kategóriaszerinti bérlés
                        print("Kategória: \n\t1 - Személyautó \n\t2 - Teherautó \n\tX - Visszalépés")
                        kategoriaValIn = input("Kérem, válasszon kategóriát:").upper()
                        kategoriaIn = ""
                        
                        match kategoriaValIn:
                            case '1': #Személyautó
                                kategoriaIn = Szemelyauto
                            case '2': #Teherautó
                                kategoriaIn = Teherauto
                            case 'X': #Visszalépés
                                break
                            case _: #Default
                                print("Kérem, válasszon a fenti lehetőségek közül.")
                                continue
                                
                        datumIn = input("\tDátum (éééé-hh-nn): ")
                        
                        try:
                            datumIn = datetime.strptime(datumIn, "%Y-%m-%d").date()                            
                        except(ValueError):
                            print("Hibás dátum! Kérem, használja a következő formátumot: éééé-hh-nn")
                            continue    
                        
                        try:
                            berlendoAuto = kolcsonzo.kategoriaKeres(kategoriaIn, 0, datumIn)
                            print(kolcsonzo.ujBerles(berlendoAuto.rendszam, datumIn))
                        except:
                            print(str(datumIn) +" dátumon nincs szabad " + kategoriaValIn + " típusú autó.")
                            continue
                        break
                    
                    case "T": #Típusszerinti bérlés                     
                        tipusIn = input("\tTípus: ")
                        datumIn = input("\tDátum (éééé-hh-nn): ")
                        try:
                            datumIn = datetime.strptime(datumIn, "%Y-%m-%d").date()                            
                        except(ValueError):
                            print("Hibás dátum! Kérem, használja a következő formátumot: éééé-hh-nn")
                            continue    
                        
                        try:
                            berlendoAuto = kolcsonzo.tipusKeres(tipusIn, 0, datumIn)
                            print(kolcsonzo.ujBerles(berlendoAuto.rendszam, datumIn))
                        except:
                            print(str(datumIn) +" dátumon nincs szabad " + tipusIn + " típusú autó.")
                            continue
                        break
                    
                    case "X": #Visszalépés
                        break
                    
                    case _: #Default
                        print("\tKérem, válasszon a fenti lehetőségek közül!")
                        continue
                    
            case '2': #Bérlés lemondása
                rendszamIn = input("\tRendszám: ")
                datumIn = input("\tDátum (éééé-hh-nn): ")
                try:
                    datumIn = datetime.strptime(datumIn, "%Y-%m-%d").date()
                    print(kolcsonzo.berlesLemondas(rendszamIn, datumIn))
                except(ValueError):
                    print("Hibás dátum! Kérem, használja a következő formátumot: éééé-hh-nn")
                    continue    
                break
            
            case '3': #Bérlések listázása
                print(kolcsonzo.berlesekLista())
                break
            
            case 'X': #Kilépés
                print("Kilépés.")
                exit()
                break

            case _: #Default
                print("\tKérem, válasszon a fenti lehetőségek közül!")
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