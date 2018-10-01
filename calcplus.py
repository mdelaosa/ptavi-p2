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
        op1 = numeros[0]
        for op2 in numeros[1:]:
            if 'suma' in line:
                op1 = micalc.plus(op1, op2)

            elif 'resta' in line:
                op1 = micalc.minus(op1, op2)

            elif 'multiplica' in line:
                op1 = micalc.mult(op1, op2)

            elif 'divide' in line:
                    if op1 == 0 or op2 == 0:
                        print('Division by zero is not allowed')
                    else:
                        op1 = micalc.div(op1, op2)

            else:
                sys.exit('Operation not valid')

        print(op1)
    fichero.close()
