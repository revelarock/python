# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dolares ela pode comprar
# considere U$S 1,00 = R$ 3,27

d = float( input ('Quantos reais eu tenho na carteira: '))
dl = d / 3.27

print ('Eu consigo comprar US$ {} com estes R$ {}'.format(dl,d))