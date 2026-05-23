'''
[Készítő: Szy László Csongor (UATE6K)
Objektum-orientált programozás, A feladat]
- **Berles:** Az autóbérléshez szükséges osztály, amely egy autó bérlését egy napra tárolja.
'''

from datetime import date, timedelta
from typing import Final

class Berles(object):
    BERLES_HOSSZ: Final = 1 #Az alapértelmezett bérléshossz (nap)
    
    #Konstruktor
    def  __init__(self, bereltAutoRendszam="", kezdesDatum="N/A", vegDatum="N/A"):
        if len(bereltAutoRendszam) > 0:
            self._rendszam = bereltAutoRendszam
            
            if (kezdesDatum == "N/A"):
                self._kezdesDatum = date.today()
            else:
                self._kezdesDatum = kezdesDatum

            if (vegDatum != "N/A"):
                self._vegDatum = vegDatum
            else:
                self._vegDatum = self._kezdesDatum + timedelta(days=Berles.BERLES_HOSSZ)
        else:
            raise ValueError("Hiányzik a bérlendő autó rendszáma")                        


#----------Property-k----------
        
    #Bérelt autó rendszáma
    @property
    def rendszam(self) -> str:
        return self._rendszam
    
    @rendszam.setter
    def rendszam(self, rendszamIn):
        self._rendszam = rendszamIn
        #TODO: a rendszám ellenőrzése a kölcsönző listájában
        
    #Bérlés dátumai
    @property
    def kezdesDatum(self) -> date:
        return self._kezdesDatum
    
    @kezdesDatum.setter
    def kezdesDatum(self, kezdesIn):
        self._kezdesDatum = kezdesIn
    
    @property
    def vegDatum(self) -> date:
        return self._kezdesDatum
    
    @vegDatum.setter
    def vegDatum(self, vegIn):
        self._vegDatum = vegIn
        
        
#----------Metódusok----------        
        
    def lejartE(self) -> bool:
        return self._vegDatum < date.today()