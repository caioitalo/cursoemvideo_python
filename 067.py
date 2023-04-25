while True:
    a = int(input('\nDeseja ver a tabuada de outro número? '))
    if a < 0:
        break

    print(f'\n---Contemple a tabuada de {a}---')
    for i in range(1, 11):
        print(f'{a} x {i} = {i * a}')

print('Fim da execução do Programa Tabuada. Muito obrigado.')
