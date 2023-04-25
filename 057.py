sexo = str(input('Digite o sexo da pessoa (M/F): ')).strip().upper()[0]  # se a pessoa digitar masculino pega só o 1o dígito
while sexo != 'M' and sexo != 'F':  # outra forma: while sexo not in 'MmFf':
    sexo = str(input('Por Favor, insira um valor válido: ')).strip().upper()
