#Crie um programa que leia um numero Real qualquer pelo tecaldo e mostrar na tela a sua porcao inteira
#EX.. Digite o mumero : 6.127
#o numero 6.127 tem a partre inteira 6



import math

n = float (input('Digite um numero ex: .127: '))

print ('o numero digitado foi  {} e o numero inteiro e {}'.format(n, math.ceil(n-1)))