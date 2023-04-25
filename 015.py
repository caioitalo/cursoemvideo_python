print('====== EXERCÍCIO 15 ======')

d = int(input("Por quantos dias o carro foi alugado? "))
km = float(input('Quantos km foram rodados? '))

pre = d * 60 + 0.15 * km

print(f'O preço total a pagar será de R$ {pre:.2f}')

