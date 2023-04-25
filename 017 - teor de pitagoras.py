from math import sqrt, pow  # forma de chamar só algumas funções da biblioteca

print('====== EXERCÍCIO 17 ======\nCalculando a hipotenusa')

ca = float(input('\nDigite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))

h = sqrt(pow(co, 2) + pow(ca, 2))  # no caso de puxar a função específica lá em cima, declara aqui sem o math. antes

print(f'A hipotenusa do triângulo é de: {h:.2f}')
