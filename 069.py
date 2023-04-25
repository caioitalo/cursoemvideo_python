op = ''
sexo = []
idade = []
cont = mde18 = homem = mmde20 = 0

while True:
    print('=' * 30)
    idade.append(int(input('Digite a idade da pessoa: ')))
    sexo.append(str(input('Digite o sexo da pessoa[M/F]: ').strip()[0].upper()))
    while sexo[cont] != 'M' and sexo[cont] != 'F':
        sexo.append(str(input('Por favor, insira uma opção válida[M/F]: ').strip()[0].upper()))

    if idade[cont] > 18:
        mde18 += 1
    if sexo[cont] == 'M':
        homem += 1
    if idade[cont] < 20 and sexo[cont] == 'F':
        mmde20 += 1
    cont += 1

    op = str(input('Você deseja continuar a inserir dados[S/N]? ')).strip().upper()
    while op != 'S' and op != 'N':
        op = str(input('Por favor, insira uma opção válida [S/N]: ')).strip().upper()
    if op == 'N':
        break

print(f'''\nO número de mulheres abaixo de 20 anos é de {mmde20}.
A quantidade de pessoas maiores de idade é {mde18}.
{homem} homens foram cadastrados.''')

