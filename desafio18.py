#faca um programa que leia um angulo qualquer e mostra na tela o valor do seno
# cosseno e tangente desse angulo.

#to. Para qualquer triângulo com catetos a, b e c e ângulos A, B e C, a Lei dos Senos afirma que a / sen A = b / sen B = c / sen C.
#A Lei dos Senos pode ser usada na resolução de qualquer triângulo, mas somente um triângulo retângulo terá uma hipotenusa.


import math

grau = float(input('digite o angulo: '))

seno = math.sin(grau)

print ('o seno e {}'.format(seno))
