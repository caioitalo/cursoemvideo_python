cad = []
pessoa_pesada = []
maior_peso = menor_peso = 0
pessoa_leve = []

while True:
    op = ''
    pessoa = []
    print('-' * 30)
    pessoa.append(str(input('NOME: ')).strip().capitalize())
    pessoa.append(int(input('PESO: ')))

    cad.append(pessoa[:])

    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar [S/N/]? ')).strip().upper()
    if op == 'N':
        break

print('-' * 30)
print(f'Ao todo, você cadastrou {len(cad)} pessoas.')

for i, c in enumerate(cad):
    if i == 0:
        pessoa_pesada.append(c[0])
        maior_peso = c[1]
        menor_peso = c[1]
        pessoa_leve.append(c[0])
    elif i > 0 and c[1] == maior_peso:
        pessoa_pesada.append(c[0])
    elif i > 0 and c[1] > maior_peso:
        pessoa_pesada.clear()
        pessoa_pesada.append(c[0])
        maior_peso = c[1]
    elif i > 0 and c[1] == menor_peso:
        pessoa_leve.append(c[0])
    elif i > 0 and c[1] < menor_peso:
        pessoa_leve.clear()
        pessoa_leve.append(c[0])
        menor_peso = c[1]

print(f'As pessoas mais pesadas pesam {maior_peso} kg')
print(f'As pessoas pesadas são: ', end='')
for c in pessoa_pesada:
    print(c, end=', ')
print('\n')

print(f'As pessoas menos pesadas pesam {menor_peso} kg')
print(f'As pessoas menos pesadas são: ', end='')
for c in pessoa_leve:
    print(c, end=', ')
