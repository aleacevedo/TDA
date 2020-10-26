import heapq
import csv
import sys

from functools import reduce
from bovedas import Boveda
from obras import PrecioNegativoException
from obras import Obra


def imprimir_movimiento(boveda_a, boveda_b):
    precio_a = boveda_a.obtener_precio_acumulado()
    precio_b = boveda_b.obtener_precio_acumulado()
    movimiento = "{} -> {} : pago {}+{}={}".format(
        boveda_a, boveda_b, precio_a, precio_b, precio_a+precio_b)
    print(movimiento)


def imprimir_pagos(pagos):
    cadena = "Pago en total: "
    for pago in pagos:
        cadena += str(pago) + '+'
    cadena = cadena[:-1] + '=' + str(reduce(lambda a, b: a+b, pagos))
    print(cadena)


def reunir_obras(bovedas_init, cantidad_de_piezas):
    if len(bovedas_init) != cantidad_de_piezas:
        print("La cantidad de piezas especificada difiere con la cantidad de piezas en el archivo de valoraciones.")
    else:
        bovedas = bovedas_init
        pagos = []
        heapq.heapify(bovedas)
        for i in range(cantidad_de_piezas-1):
            boveda_a = heapq.heappop(bovedas)
            boveda_b = heapq.heappop(bovedas)
            imprimir_movimiento(boveda_a, boveda_b)
            boveda_b += boveda_a
            heapq.heappush(bovedas, boveda_b)
            pagos.append(boveda_b.obtener_precio_acumulado())
        imprimir_pagos(pagos)


def __main__():
    if len(sys.argv) < 3:
        print("Argumentos insuficientes.\nIndique la cantidad de piezas y el path al archivo de valoraciones.")
    else:
        path = sys.argv[2]
        try:
            with open(str(path)) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                row = next(csv_reader)

                bovedas = []
                for idx, valor in enumerate(row):
                    bovedas.append(
                        Boveda(chr(idx+65), Obra('P' + str(idx+1), int(valor))))

                reunir_obras(bovedas, int(sys.argv[1]))
        except FileNotFoundError:
            print("Archivo de valoraciones no encontrado.")
        except PrecioNegativoException:
            print("El archivo tiene un precio menor a 0")


__main__()
