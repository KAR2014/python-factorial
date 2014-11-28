# -*- coding: utf-8 -*-
""" Factorial """
import time
import sys

FACTORIAL = 0
RESPUETA = 0
def factorial(NUMERO):
    CONTADOR = 1
    while NUMERO > 0:
        CONTADOR = CONTADOR*(NUMERO)
        NUMERO = NUMERO-1
    print "Factorial:"
    return CONTADOR
print u"                 ¡Bienvenido a nuestro programa!"
print u"La función del mismo es calcular el Factorial de un número\n"
while True:
    FACTORIAL = raw_input("Ingrese Número: ")
    try:
        FACTORIAL = int(FACTORIAL)
        if FACTORIAL > 0:
            break
        else:
            print u"Debe ingresar un número entero positivo\n"
    except(RuntimeError, TypeError, NameError, ValueError):
        print u"Debe ingresar un número entero positivo\n"
        RESPUESTA = True

RESPUESTA = factorial(FACTORIAL)
print RESPUESTA

if RESPUESTA > 0:
    time.sleep(2)
    print
    print u"                    **** Caja Registradora Full Pro 2.0 © ****"
    print u"                              ***** Cognits *****"
    print u"                         Third Generation Grupo: KAR-FER :\n"
    print u"                                  Fernando López"
    print u"                                   Kevin Herrera\n"
    print u"                          KAR_KO,INDUSTRIS Copyright ®"
    time.sleep(3)
    sys.exit(2)
