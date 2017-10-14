#faca um programa que leia um numero inteiro qualquer e mostre
# na tela a sua tabuada.\


t =  int (input ('Digite a tabuada desejada:\n' ))

 # Variavel de multiplicacao
m1 = t * 1
m2 = t * 2
m3 = t * 3
m4 = t * 4
m5 = t * 5
m6 = t * 6
m7 = t * 7
m8 = t * 8
m9 = t * 9
m10 = t * 10
     # variavel de Divisao
d1 = t / 1
d2 = t / 2
d3 = t / 3
d4 = t / 4
d5 = t / 5
d6 = t / 6
d7 = t / 7
d8 = t / 8
d9 = t / 9
d10 = t / 10

print (' A tabuada escolhida foi ', t ,'\n')

print (' Veja a Tabuada completa\n' )

print  (  '',t,'x 1 = ', m1, '\n' ,t, 'x 2 = ', m2, '\n',  t, 'x 3 = ',m3, '\n', t, 'x 4 = ', m4, '\n',t, 'x 5 = ', m5, '\n', end='')
print  (  '', t,'x 6 = ', m6, '\n', t, 'x 7 = ', m7, '\n',  t, 'x 8 = ', m8, '\n', t, 'x 9 = ', m9,'\n',t,'x 10 =', m10,'\n' , '\n')

print ('agora veja a tabuada de divisao  de ', t , '\n')

print ('', t, ': 1 = ', d1, '\n', t, ': 2 =', d2, '\n', t,': 3 =', d3,'\n',t,': 4 = ', d4,'\n',t,': 5 =',d5,'\n')
print ('', t, ': 6 =',  d6, '\n', t, ': 7 =', d7, '\n', t,': 8 =', d8,'\n',t,': 9 = ', d9,'\n',t,':10 =',d10,'\n' )




