nome = str(input('Digite seu nome completo: '))

nome = nome.strip()
nome = nome.title().split()  # combinação entre manipulação de textos

print(f'O seu primeiro nome é: {nome[0]}')
print(f'O seu último nome é: {nome[len(nome)-1]}')

# linha 7 foi uma gambiarra, pois o len vai mostrar o número de palavras depois do split. Guanabara fez do msm jeito
# exemplo: caio italo alves, o len disso mostra a contagem de [caio], [italo], [alves], ou seja, 3