preco = int(input('Qual a distância da viagem em km? '))

if preco <= 200:
    passagem = preco * 0.5
else:
    passagem = preco * 0.45

print(f'O preço da passagem é de R${passagem}')  # pode colocar o print fora, code cleaning.
