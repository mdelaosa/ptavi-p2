#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:20:29 2018

@author: mdelaosa
"""

import sys
import csv
import calcoohija


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as fichero:
        linea = list(csv.reader(fichero, delimiter=','))
        micalc = calcoohija.CalculadoraHija()

        operaciones = {"suma": micalc.plus,
                       "resta": micalc.minus,
                       "multiplica": micalc.mult,
                       "divide": micalc.div}

        for line in linea:
            try:
                numeros = list(map(int, line[1:]))
            except ValueError:
                sys.exit('Error: Non numerical parameters')
            op1 = numeros[0]
            for op2 in numeros[1:]:
                if op2 == 0 and line[0] == "divide":
                    print('Division by zero is not allowed')
                else:
                    op1 = operaciones[line[0]](op1, op2)
            print(op1)
