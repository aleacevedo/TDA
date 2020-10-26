class PrecioNegativoException(Exception):
    def __init__(self, mensaje="El precio es menor a 0"):
        self.message = mensaje
        super().__init__(self.message)


class Obra:

    def __init__(self, nombre, precio):
        if(precio < 0):
            raise PrecioNegativoException
        self._nombre = nombre
        self._precio = precio

    def obtener_nombre(self):
        return self._nombre

    def obtener_precio(self):
        return self._precio

    def __str__(self):
        return self._nombre
