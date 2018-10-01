#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:20:17 2018
@author: mdelaosa
Calculadora con clase suma y resta.
"""

import sys


class Calculadora:

    def plus(self, op1, op2):
        return op1 + op2

    def minus(self, op1, op2):
        return op1 - op2


if __name__ == '__main__':

    micalc = Calculadora()
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
        Suma = micalc.plus(op1, op2)
        Resta = micalc.minus(op1, op2)

    except ValueError:
        sys.exit('Error: Non numerical parameters')

    if sys.argv[2] == "suma":
        resultado = Suma
    elif sys.argv[2] == "resta":
        resultado = Resta
    else:
        sys.exit('Operación sólo puede ser sumar o restar')

    print(resultado)
