'''
[Készítő: Szy László Csongor (UATE6K)
Objektum-orientált programozás, A feladat]
- **Auto (absztrakt osztály):** Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).
'''

from abc import ABC, abstractmethod

#Auto absztrakt osztály
class Auto(ABC):    
    
    #Rendszám
    @property
    @abstractmethod
    def rendszam(self):
        ...
    
    @rendszam.setter
    @abstractmethod
    def rendszam(self, rendszamIn):
        ...
    
    #Típus
    @property
    @abstractmethod
    def tipus(self):
        ...
    
    @tipus.setter
    @abstractmethod
    def tipus(self, tipusIn):
        ...
    
    #Bérleti díj 
    @property
    @abstractmethod
    def berletiDij(self):
        ...
    
    @berletiDij.setter
    @abstractmethod
    def berletiDij(self, berletiDijIn):
        ...    