import random

print('====== EXERCÍCIO 19 ======\nEscolhendo um aluno aleatório')

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

print(f'O aluno sorteado é: {random.choice ([a1, a2, a3, a4])}')

#  ensinou a saber procurar no site as funções
#  de longe o que mais demorei até agora