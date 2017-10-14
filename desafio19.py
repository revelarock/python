# Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
# faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido


import random
aluno1 = input ('Digite aluno 1:')
aluno2 = input('Digite o aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digigte o nome do aluno 4')

aluno = random.choice([aluno1,aluno2,aluno3,aluno4])

print('o Aluno escolhido foi : ',aluno)