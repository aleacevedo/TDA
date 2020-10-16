class Boveda:

    def __init__(self, nombre, obra):
        self._nombre = nombre
        self._obras = [obra]
        self._precio_acumulado = obra.obtener_precio()

    def agregar_obras(self, obras, precio):
        self._obras += obras
        self._precio_acumulado += precio

    def vaciar(self):
        obras_aux = self._obras
        precio_aux = self._precio_acumulado
        self._obras = []
        self._precio = 0
        return obras_aux, precio_aux

    def obtener_precio_acumulado(self):
        return self._precio_acumulado

    def obtener_obras(self):
        return self._obras

    def obtener_nombre(self):
        return self._nombre

    def __str__(self):
        cadena = self._nombre + " ("
        for obra in self._obras:
            cadena += str(obra) + ' '
        cadena = cadena[:-1] + ')'
        return cadena

    def __iadd__(self, other):
        self.agregar_obras(other._obras,
                           other._precio_acumulado)
        return self

    def __equal__(self, other):
        return self._precio_acumulado == other._precio_acumulado

    def __ge__(self, other):
        return self._precio_acumulado >= other._precio_acumulado

    def __gt__(self, other):
        return self._precio_acumulado > other._precio_acumulado

    def __le__(self, other):
        return self._precio_acumulado <= other._precio_acumulado

    def __lt__(self, other):
        return self._precio_acumulado < other._precio_acumulado
