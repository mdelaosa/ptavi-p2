#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:43:41 2018
@author: mdelaosa
Calculadora con clase suma, resta, mult, div.
"""
import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def mult(self, op1, op2):
        return op1*op2

    def div(self, op1, op2):
        try:
            return op1/op2
        except ZeroDivisionError:
            return 'Division by zero is not allowed'


if __name__ == '__main__':

    micalc = CalculadoraHija()
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
        Suma = micalc.plus(op1, op2)
        Resta = micalc.minus(op1, op2)
        Multiplicacion = micalc.mult(op1, op2)
        Division = micalc.div(op1, op2)

    except ValueError:
        sys.exit('Error: Non numerical parameters')

    if sys.argv[2] == "suma":
        resultado = Suma
    elif sys.argv[2] == "resta":
        resultado = Resta
    elif sys.argv[2] == "multiplica":
        resultado = Multiplicacion
    elif sys.argv[2] == "divide":
        resultado = Division
    else:
        sys.exit('Operation not valid')

    print(resultado)
