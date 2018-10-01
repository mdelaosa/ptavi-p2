#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:26:55 2018
@author: mdelaosa
Calculadora con clase para documento
"""

import sys
fichero = './fichero'


class Calculadora:

    def plus(lineanumeros):
        suma = 0
        for i in lineanumeros:
            suma += i
        return suma

    def minus(lineanumeros):
        resta = 0
        for i in lineanumeros:
            resta -= i
        return resta


class CalculadoraHija(Calculadora):

    def mult(lineanumeros):
        multiplicacion = 1
        for i in lineanumeros:
            multiplicacion *= i
        return multiplicacion

    def div(lineanumeros):
        division = 1
        try:
            for i in lineanumeros:
                division /= i
            return division
        except ZeroDivisionError:
            return 'Division by zero is not allowed'


if __name__ == '__main__':
    with open(fichero, 'r') as fichero:
        for line in fichero:
                linea = line.split(', ')
                lineanumeros = list(map(int, linea[1:-1]))

                if 'suma' in linea:
                    resultado = CalculadoraHija.plus(lineanumeros)
                elif 'resta' in linea:
                    resultado = CalculadoraHija.minus(lineanumeros)
                elif 'multiplica' in linea:
                    resultado = CalculadoraHija.mult(lineanumeros)
                elif 'divide' in linea:
                    resultado = CalculadoraHija.div(lineanumeros)
                else:
                    sys.exit('Operation not valid')

                print(linea[0], resultado)

