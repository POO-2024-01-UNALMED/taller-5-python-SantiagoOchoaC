class Zoologico():

    # Constructor
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
        

    # Métodos 

    def agregarZonas (self, zona):
        self._zonas.append(zona)
        

    def cantidadTotalAnimales(self):
        cantidadTotalAnimales = 0
        for zona in self._zonas:
            cantidadTotalAnimales += zona.cantidadAnimales()
        return cantidadTotalAnimales


    # Metodos get y set

    # Métodos get y set para _nombre
    def getNombre (self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre

    # Métodos get y set para _ubicacion
    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    # Métodos get y set  para _zonas
    def getZona(self):
        return self._zonas

    def setZona(self, zonas):
        self._zonas = zonas