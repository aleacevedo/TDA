class Obra:

    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def obtener_nombre(self):
        return self._nombre

    def obtener_precio(self):
        return self._precio

    def __str__(self):
        return self._nombre
