frase = str(input('Digite uma frase: ')).upper().strip()

frase = frase.replace(' ', '')
invfrase = []  # outra forma de inverter seria invfrase = frase[::-1]. precisava nem de for
for i in range(len(frase), 0, -1):
    invfrase.append(frase[i-1:i])  # funciona como o for, as partições não contam o ultimo elemento, mas até anterior.
invfrase = ''.join(invfrase)


if invfrase == frase:
    print('UAU! A frase é um PALÍNDROMO')
else:
    print('Nada demais, essa frase não é um palindromo.')


