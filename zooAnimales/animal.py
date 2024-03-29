import zooAnimales

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

    @staticmethod
    def totalPorTipo():
        return "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces : " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    
    def toString(self):
        if (self._zona != None):
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el zoo " + self._zona.getZoo().getNombre()
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero

    # Métodos get y set 
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, valor):
        cls._totalAnimales = valor

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