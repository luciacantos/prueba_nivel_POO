from subclases.bicicleta import bicicleta
from subclases.coche import coche
from subsubclases.motocicleta import motocicleta
from subsubclases.camioneta import camioneta

def lanzador():
    vehiculos = []  # lista de vehiculos

    vehiculo_1 = bicicleta("blanca", "2", "deportiva")
    vehiculos.append(vehiculo_1)
    print(vehiculo_1)

    vehiculo_2 = coche("negro", "4", "200", "500")
    vehiculos.append(vehiculo_2)
    print(vehiculo_2)

    vehiculo_3 = motocicleta("verde", "2", "deportiva", "300", "600")
    vehiculos.append(vehiculo_3)
    print(vehiculo_3)

    vehiculo_4 = camioneta("negro", "4", "200", "600", "1000")
    vehiculos.append(vehiculo_4)
    print(vehiculo_4)

    def catalogar(vehiculos, ruedas=None):
        if ruedas is not None:
            vehiculos = [v for v in vehiculos if v.ruedas == ruedas]

        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vars(vehiculo)}")


    catalogar(vehiculos)
    catalogar(vehiculos, 0)
    catalogar(vehiculos, 2)
    catalogar(vehiculos, 4)
