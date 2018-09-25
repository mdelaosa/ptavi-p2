#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:26:55 2018
@author: mdelaosa
Calculadora con clase para documento
"""

import sys

class CalculadoraHija:
    
    def plus(self, op1, op2):
        return op1 + op2
    
    def minus(self, op1, op2):
        return op1 - op2
    
    def mult(self, op1, op2):
        return op1 * op2
    
    def div(self, op1, op2):
        try:
            return op1 / op2
        except ZeroDivisionError:
            return 'Division by zero is not allowed'
  
if __name__ == '__main__':
    micalcplus = CalculadoraHija()
   
    try:
        n = len(sys.argv)
        resultadosu = 0
        
        """ op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
        Suma = micalcplus.plus(op1, op2)
        Resta = micalcplus.minus(op1, op2)
        Multiplicacion = micalcplus.mult(op1, op2)
        Division = micalcplus.div(op1, op2)"""
        
    except ValueError:
        sys.exit('Error: Non numerical parameters')
        
        for op in (1, n):
            suma = micalcplus.plus(resultadosu, sys.argv[op])
            resultadosu = suma
            op = op + 1
            
        print(suma)