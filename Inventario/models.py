class Mapa:
    def __init__(self, nombre, tipo, año, ubicación, notas):
        self.nombre = nombre
        self.tipo = tipo
        self.año = año
        self.ubicacion = ubicación
        self.notas = notas

    def __repr__(self):
        return f"{self.nombre} ({self.tipo}, {self.año})"




