pn = float(input('Digite o preço normal do produto: '))
print('Formas de pagamento'
      '\n1 - Dinheiro/Cheque'
      '\n2 - 1x no cartão'
      '\n3 - 2x no cartão'
      '\n4 - 3x ou mais no cartão\n')
met = int(input('Digite o código do método: '))

if met == 1:
      print(f'\nFoi concedido 10% de desconto e o novo preço será de R$ {0.9 * pn:.2f}')
elif met == 2:
      print(f'\nFoi concedido 5% de desconto será de R$ {0.95 * pn:.2f}')
elif met == 3:
      print(f'''\nNessa condição não houve desconto R$ {pn:.2f}
      As parcelas serão de R$ {pn / 2}''')
elif met == 4:
      parc = int(input('Em quantas vezes será o pagamento? '))

      print('Nessa condição há 20% de juros'
            f'\nO preço final será de R${(pn * 1.2):.2f} e a prestação será de R${(pn * 1.2 / parc):.2f}')
