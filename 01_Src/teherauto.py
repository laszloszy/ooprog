'''
[Készítő: Szy László Csongor (UATE6K)
Objektum-orientált programozás, A feladat]
- **Teherauto:** A teherautók specifikus attribútumait tartalmazó osztály.
'''

import auto
#TODO: osztályattribútumok megvalósítása
#Teherautó osztály
class Teherauto(auto.Auto):
    
    #Konstruktor
    def __init__(self, rendszamIn, tipusIn, berletiDijIn):
        self.rendszam = rendszamIn
        self.tipus = tipusIn
        self.berletiDij = berletiDijIn
 

#----------Property-k----------
               
   #Rendszám
    @property
    def rendszam(self):
        return self._rendszam
    
    @rendszam.setter
    def rendszam(self, rendszamIn):
        self._rendszam = rendszamIn
    
    #Típus
    @property
    def tipus(self):
        return self._tipus
    
    @tipus.setter
    def tipus(self, tipusIn):
        self._tipus = tipusIn
    
    #Bérleti díj 
    @property
    def berletiDij(self):
        return self._berletiDij
    
    @berletiDij.setter
    def berletiDij(self, berletiDijIn):
        self._berletiDij = berletiDijIn
    
    