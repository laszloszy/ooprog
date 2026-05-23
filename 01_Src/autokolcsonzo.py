'''
[Készítő: Szy László Csongor (UATE6K)
Objektum-orientált programozás, A feladat]
- **Autokolcsonzo:** Tartalmazza az autókat és saját attribútumot is, például a kölcsönző nevét.
'''

from berles import Berles

class Autokolcsonzo(object):

    #Konstruktor    
    def __init__(self, nev="N/A"):
        self._nev = nev
        self._autok = []
        self._berlesek = []


#----------Property-k----------

    #Kölcsönző neve
    @property
    def nev(self):
        return self._nev

    @nev.setter
    def nev(self, value):        
        
        if value == "N/A":
            print("Kérem, adjon meg érvényes értéket a kölcsönző nevének!")    
            raise ValueError       
        
        else:
            self._nev = value
    
    #Autók a kölcsönzőben
    @property
    def autok(self):
        return self._autok    
    
    @autok.setter
    def autok(self, value):
        self._autok = value
    
    #Bérlések a kölcsönzőben
    @property
    def berlesek(self):
        return self._berlesek
    
    @berlesek.setter
    def berlesek(self, value):
        self._berlesek = value
    
#----------Metódusok----------
    
#Visszaadja a rendszámhoz tartozó autót, vagy StopIteration kivételt dob, ha nem található
    def rendszamKeres(self, rendszamIn):
        return next(x for x in self.autok if x.rendszam == rendszamIn) 
    
    
#Visszaadja az első szabad autót, aminek a típusa a keresettvagy StopIteration kivételt dob, ha nem található
    def szabadKeres(self, tipusIn="N/A", berletiDijMax=0):
        
        if (tipusIn != "N/A"):
            if (berletiDijMax == 0): #Keresés csak típus alapján
                return next(x for x in self._autok if x.tipus == tipusIn) 
            
            else: #Keresés típus és max. bérleti díj alapján
                return next(x for x in self._autok if (x.tipus == tipusIn and x.berletiDij <= berletiDijMax)) 
            
        elif (berletiDijMax > 0): #Keresés csak max. bérleti díj alapján
            return next(x for x in self._autok if x.berletiDij <= berletiDijMax)
        
        else:
             raise ValueError("Kérem, adjon meg típust, maximális bérleti díjat vagy mindkettőt!")             
         
         
#Lekérdezi, hogy az adott dátumra már ki van-e bérelve az autó
    #TODO: dátumvalidáció
    def berelveVan(self, rendszamIn, datumIn) -> bool:
        try:
            next(x for x in self._berlesek if x.rendszam == rendszamIn and x.kezdesDatum <= datumIn and x.vegDatum >= datumIn)
            return True
        except(StopIteration):
            return False
            
            
#Új bérlés rögzítése
    #TODO: dátumvalidáció
    def ujBerles(self, rendszamIn, datumIn) -> str:
        try:
            berlendoAuto = self.rendszamKeres(rendszamIn)
            if (self.berelveVan(rendszamIn, datumIn)):
               return "Az autó már ki van bérelve az adott napra." 
            else:
                if(input("Napi bérleti díj: " + str(berlendoAuto.berletiDij) + ". Rögzítsük a bérlést?[I/N]").upper() == "I"):
                    self._berlesek.append(Berles(rendszamIn, datumIn))
                    return "A(z) " + rendszamIn + " rendszámú, " + berlendoAuto.tipus + " típusú autó bérlése " + str(datumIn) + " dátumra rögzítve."    
                else:
                    return("A foglalás nincs rögzítve.")
                
        except(StopIteration):
            return "A megadott rendszámú autó nem található a nyilvántartásban."
        
        
#Bérlés lemondása
    #TODO: dátumvalidáció
    def berlesLemondas(self, rendszamIn, datumIn) -> str:
        try:
            self.rendszamKeres(rendszamIn)
            if (self.berelveVan(rendszamIn, datumIn)):
                self._berlesek.remove(next(x for x in self._berlesek if x.rendszam == rendszamIn and x.kezdesDatum <= datumIn and x.vegDatum >= datumIn))
                return "A(z) " + rendszamIn + " rendszámú autó bérlése " + str(datumIn) + " dátumról törölve."    
            else:
                return("Nem található bérlés a(z) " + rendszamIn + " rendszámú autóra " + datumIn + " dátumra.")
        except:
            return "A(z) " + rendszamIn + "rendszámú autó nem található a nyilvántartásban."
        
        
#Bérlések listázása
    def berlesekLista(self) -> str:
        eredmeny = ""
        for aktBerles in self._berlesek:
            eredmeny += "Rendszám: " + aktBerles.rendszam + "\t Bérlés kezdete: " + str(aktBerles.kezdesDatum) + ", vége: " + str(aktBerles.vegDatum) + "\n"
        return eredmeny