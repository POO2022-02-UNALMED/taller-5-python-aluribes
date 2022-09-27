from gestion.zoologico import Zoologico

class Zona:
    def __init__(self, nombre, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self, animale): 
        self._animales.append(animale)
    
    def cantidadAnimales(self): 
        return len(self._animales)

    def setNombre(self, nombre): 
        self._nombre = nombre

    def getNombre(self): 
        return self._nombre

    def setUbicacion(self, ubicacion): 
        self._ubicacion = ubicacion

    def getUbicacion(self,): 
        return self._ubicacion

    def setZoologico(self, animales): 
        self._animales = animales

    def getZoologico(self): 
        return self._animales

    def setZoo(self, zoo): 
        self._zoo = zoo

    def getZoo(self): 
        return self._zoo