from superclase.vehiculo import vehiculo

class coche(vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

