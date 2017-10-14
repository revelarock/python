#Escreva uma programa que leia um valor em Metros
# e exiba convertido em centimentros e milimetros
#
#
m = int (input ('Digite o valor em Metros: '))
c = m * 100
mi = m  * 1000
print (' O valor de  metros foi {} \n O Valo em centimetros e {:03} \n e o valor em Milimetros e {:03}' .format(m,c,mi))