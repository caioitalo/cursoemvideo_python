aluno_notas = []

while True:
    op = ''
    aluno = [[], []]
    aluno[0].append(str(input('NOME: ')).strip().capitalize())
    aluno[1].append(float(input('NOTA 1:')))
    aluno[1].append(float(input('NOTA 2:')))
    aluno_notas.append(aluno)
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar[S/N]? ')).strip().upper()
    if op == 'N':
        break

print('=' * 30)
print(f'=== BOLETIM DO ALUNOS ===')
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')  # atenção como fazer textos alinhados. até aqui eu não sabia.
for i, c in enumerate(aluno_notas):

    print(f'{i}'
          f'\t{c[0]}'
          f'\t\t{(sum(c[1]) / 2)}')

while op != 999:
    print('=' * 30)
    op = int(input('Digite o No do aluno para ver as notas (999 para interromper): '))
    print(f'As notas do aluno {aluno_notas[op][0]} são {aluno_notas[op][1]}')