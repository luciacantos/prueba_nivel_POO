from subclases.bicicleta import bicicleta

class motocicleta(bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindarda):
        super().__init__(color, ruedas, tipo)
        self.veocidad = velocidad
        self.cilindrada = cilindarda

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
