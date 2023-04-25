aluno = {}

aluno['nome'] = str(input('NOME: ')).strip()
aluno['média'] = float(input('MÉDIA: '))
print('-' * 30)

for i, c in aluno.items():
    print(f'O(A) {i} do aluno é {c}')

if aluno['média'] < 7:
    print('O aluno está reprovado')
else:
    print('O aluno está aprovado')