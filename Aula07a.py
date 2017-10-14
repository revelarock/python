n1 = int(input ('Um Valor:'))
n2 = int(input ('Outro Valor:'))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1 // n2
e= n1 ** n2

print ('A Soma vale {}, \n o produto vale {} \n divisao vale {:3f} \n'.format(s,m,d), end=' ')
print ('Divisao inteira {} \n e potencia {:2f} '.format(di,e))

