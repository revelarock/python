#O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos
#alunos. faca um programa que leia o nome dos quatro alunos e mostr a ordem sorteada.import

import random

aluno1 = input(' Digite o nome do Aluno 1 : ')
aluno2 = input(' Digite o nome do aluno 2 : ')
aluno3 = input(' Digite o nome do aluno 3 : ')
aluno4 = input(' Digite o nome do aluno 4 : ')

ordem = random.choices ([aluno1,aluno2,aluno3,aluno4], k=5)

print(ordem)