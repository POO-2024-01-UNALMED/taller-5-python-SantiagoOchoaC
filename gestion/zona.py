class Zona():
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    # Metodos
        
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        animal.setZona(self)
        

    def cantidadAnimales(self):
        return len(self._animales)

    # Métodos get y set

    # Métodos get y set para _nombre
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    # Métodos get y set para _zoo
    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo

    # Métodos get y set para _animales
    def getAnimales(self):
        return self._animales

    def setAnimales(self, animales):
        self._animales = animales