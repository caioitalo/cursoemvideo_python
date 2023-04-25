tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

c = int(input('Digite um número entre 0 e 10: '))
while not 0 < c < 11:
      c = int(input('Tente novamente. Digite um número entre 0 e 10: '))
print(f'Você digitou o número {tupla[c]}')
