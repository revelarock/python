#Faca um programa que leia a largura e a altura de uma parede em metros
#calcule a sua area e a quantidade de tinta necessaria para pinta-la
#sabendo que 01 litro de tinta pinta 2m2.


l= float (input ('Qual a largura da parede : '))
a= float(input ('Qual a Altura da parede : '))
at = l * a
lt = at / 2
print ( ' A area total foi de {} Serao necessarios {} litros de tinta para pintar toda a parede'.format(at,lt))