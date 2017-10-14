# Faca um programa que leia o preco de um produto e mostre seu
# preco com 5% de desconto


preco = float (input ('Qual o valor do produto? '))

desc = preco * 5/100

final = preco - desc

print ( 'foi dado desconto de {} sendo o preco final de {} '.format (desc,final))