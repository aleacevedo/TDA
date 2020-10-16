import heapq
import csv

from pathlib import Path
from functools import reduce
from bovedas import Boveda
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


def reunir_obras(bovedas_init):
    bovedas = bovedas_init
    pagos = []
    heapq.heapify(bovedas)
    while(len(bovedas) > 1):
        boveda_a = heapq.heappop(bovedas)
        boveda_b = heapq.heappop(bovedas)
        imprimir_movimiento(boveda_a, boveda_b)
        boveda_b += boveda_a
        heapq.heappush(bovedas, boveda_b)
        pagos.append(boveda_b.obtener_precio_acumulado())
    imprimir_pagos(pagos)


def __main__():
    base_path = Path(__file__).parent
    with open(str(base_path) + '/valor_obras.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row = next(csv_reader)

        bovedas = []
        for idx, valor in enumerate(row):
            bovedas.append(Boveda(chr(idx+65), Obra('P' + str(idx+1), int(valor))))

        reunir_obras(bovedas)


__main__()
