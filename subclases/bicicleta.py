from superclase.vehiculo import vehiculo

class bicicleta(vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)
