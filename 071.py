from time import sleep

n = cont50 = cont20 = cont10 = cont5 = cont1 = 0
print(f'== BANCAIO ==')
val = int(input('Digite um valor a ser sacado R$ '))
while val < 0:
    val = int(input('Valor inválido! Digite um valor a ser sacado R$ '))

while 50 > val:
    cont50 += 1
    val -= 50

while 20 > val:
    cont20 += 1
    val -= 20

while 10 > val:
    cont10 += 1
    val = val - 10

while 5 > val:
    cont5 += 1
    val = val - 5

while 1 > val:
    cont1 += 1
    val = val - 1

print('Calculando...')
sleep(1.25)
if cont50 > 0:
    print(f'FORAM UTILIZADAS {cont50} NOTAS DE 50')
if cont20 > 0:
    print(f'FORAM UTILIZADAS {cont20} NOTAS DE 20')
if cont10 > 0:
    print(f'FORAM UTILIZADAS {cont10} NOTAS DE 10')
if cont5 > 0:
    print(f'FORAM UTILIZADAS {cont5} NOTAS DE 5')
if cont1 > 0:
    print(f'FORAM UTILIZADAS {cont1} NOTAS DE 1')

print('Fim da operação. Obrigado por utilizar o BANCAIO')