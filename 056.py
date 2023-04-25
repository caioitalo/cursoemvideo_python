nome = []
idade = []
sexo = []
ade20 = 0

for i in range(0, 4):
    print(f'\n--- {i+1}ª PESSOA ---')
    nome.append(str(input('Digite um nome: ')).strip().title())
    idade.append(int(input('Digite a idade: ')))
    sexo.append(str(input('Digite o Sexo (M/F): ')).strip().upper())

    if idade[i] < 20 and sexo[i] == 'F':
        ade20 = ade20 + 1

maisv = nome[idade.index(max(idade))]
med = sum(idade)/4
print(f'''A média de idade é de {med}.
O homem mais velho é o {maisv} e tem {idade.index(max(idade))}.
Há {ade20} mulheres abaixo de 20 anos.''')