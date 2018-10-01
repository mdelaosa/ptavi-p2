#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:20:29 2018

@author: mdelaosa
"""

import sys
import csv
import calcoohija
fichero = './fichero'


if __name__ == '__main__':

    with open('fichero', 'r') as fichero:
        linea = list(csv.reader(fichero, delimiter=','))

        try:
            micalc = calcoohija.CalculadoraHija()

        except ValueError:
            sys.exit('Error: Non numerical parameters')

        for line in linea:
            numeros = list(map(int, line[1:]))

            if 'suma' in line:
                op1 = 0
                for op2 in numeros:
                    op1 = micalc.plus(op1, op2)

            elif 'resta' in line:
                op1 = numeros[0]
                for op2 in numeros[1:]:
                    op1 = micalc.minus(op1, op2)

            elif 'multiplica' in line:
                op1 = 1
                for op2 in numeros:
                    op1 = micalc.mult(op1, op2)

            elif 'divide' in line:
                op1 = numeros[0]
                try:
                    for op2 in numeros[1:]:
                        op1 = micalc.div(op1, op2)

                except ZeroDivisionError:
                    print('Division by zero is not allowed')

            else:
                sys.exit('Operation not valid')

            print(op1)
