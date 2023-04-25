n = int(input('Digite um número inteiro de 0 a 9999: '))
n = 10000 + n
n = str(n)

print('Analisando seu número, temos:')
print(f'Unidade: {n[4]}\nDezena: {n[3]}')
print(f'Centena: {n[2]}\nMilhar: {n[1]}')

#  errei e tive dificuldade