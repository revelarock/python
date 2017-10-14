# Faca um programa que leia o comprimento do cateto adjacente de um triangulo
# calcule o mostre o comprimento da hipotenusa
#a2 + b2 = c2.

import math

a = float (input('Digite o numero de lado a :'))
b = float (input('Digite o numero do lado b: '))
c = (a*a) + (b*b)
d = math.sqrt(c)

print ('a hypotenusa e {}'.format(d))

