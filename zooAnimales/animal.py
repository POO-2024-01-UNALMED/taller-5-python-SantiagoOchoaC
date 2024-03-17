#from zooAnimales.mamifero import Mamifero
from zooAnimales import mamifero, ave, reptil, pez, anfibio

class Animal():
    _totalAnimales = 0
    def __init__(self,nombre, edad,habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    # Metodos
    
    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(self):
        return "Mamiferos: " + mamifero.Mamifero.cantidadMamiferos + "\nAves: " + ave.Ave.cantidadAves + "\nReptiles: " + reptil.Reptil.cantidadReptiles + "\nPeces: " + pez.Pez.cantidadPeces + "\nAnfibios: " + anfibio.Anfibio.cantidadAnfibios

    def toString(self):
        if (self._zona != None):
            return "Mi nombre es " + self.getNombre + ", tengo una edad de " + self.getEdad + ", habito en " + self.getHabitat + " y mi genero es " + self.getGenero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el " + self._zona.getZoo
        else:
            return "Mi nombre es " + self.getNombre + ", tengo una edad de " + self.getEdad + ", habito en " + self.getHabitat + " y mi genero es " + self.getGenero

    # Métodos get y set
    # Métodos get y set para _nombre
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    # Métodos get y set para _edad
    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    # Métodos get y set para _habitat
    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    # Métodos get y set para _genero
    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    # Métodos get y set para _zona
    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona