print('=== Analisador de anos ===')

ano = int(input('Digite um ano a ser analisado: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
# eu havia colocado só a primeira, não sabia que dava pa colocar 2 condições. ainda tem o operador 'or'
# há essa outra condição para anos bissextos

    print(f'O ano de {ano} é bissexto')

else:
    print(f'O ano de {ano} não é bissexto')