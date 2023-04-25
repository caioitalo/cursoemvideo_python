cad_pessoas = []
pessoa = {}
soma = 0

while True:
    op = ''
    pessoa['Nome'] = input('NOME: ')
    pessoa['Sexo'] = str(input('SEXO[M/F]: ').strip().upper())
    while pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
        pessoa['Sexo'] = str(input('VALOR INVÁLIDO. SEXO[M/F]: ').strip().upper())
    pessoa['Idade'] = int(input('IDADE: '))
    cad_pessoas.append(pessoa.copy())
    pessoa.clear()
    while op != 'N' and op != 'S':
        op = str(input('Deseja adicionar outra pessoa[S/N]? ').strip().upper())
    if op == 'N':
        break

for c in range(0, len(cad_pessoas)):
    soma += cad_pessoas[c]['Idade']
med = soma / len(cad_pessoas)

print(f'O número de pessoas cadastradas foi de {len(cad_pessoas)}.')
print(f'A média de  idade das pessoas foi de {med:.1f} anos.')

print('As mulheres cadastradas foram: ', end='')
for i in range(0, len(cad_pessoas)):
    if cad_pessoas[i]['Sexo'] == 'F':
        print(cad_pessoas[i]['Nome'], end=' ')

print()
print('As pessoas acima da média foram: ', end='')
for c in range(0, len(cad_pessoas)):
    if cad_pessoas[c]['Idade'] > med:
        print(cad_pessoas[c]['Nome'])
