vel = float(input('Qual a velocidade que o carro passou? '))

if vel > 80.99:
    print('Se lascou, você está acima da velocidade permitida de 80km/h\n'
          f'Vai pagar uma multa de R${7*(vel-80):.2f}')
else:
    print('Parabéns pelo mínimo! Você está andando sob o limite.')
