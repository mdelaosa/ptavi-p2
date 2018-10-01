#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:26:55 2018
@author: mdelaosa
Calculadora con clase para documento
"""

import sys
import calcoohija
fichero = './fichero'


if __name__ == '__main__':

    fichero = open('fichero', encoding='utf-8', mode='r')
    try:
        micalc = calcoohija.CalculadoraHija()

    except ValueError:
        sys.exit('Error: Non numerical parameters')

    for line in fichero:
        linea = line.split(', ')
        numeros = list(map(int, linea[1:]))

        if 'suma' in linea:
            op1 = 0
            for op2 in numeros:
                op1 = micalc.plus(op1, op2)

        elif 'resta' in linea:
            op1 = numeros[0]
            for op2 in numeros[1:]:
                op1 = micalc.minus(op1, op2)

        elif 'multiplica' in linea:
            op1 = 1
            for op2 in numeros:
                op1 = micalc.mult(op1, op2)

        elif 'divide' in linea:
            op1 = numeros[0]
            try:
                for op2 in numeros[1:]:
                    op1 = micalc.div(op1, op2)

            except ZeroDivisionError:
                print('Division by zero is not allowed')

        else:
            sys.exit('Operation not valid')

        print(op1)
    fichero.close()
