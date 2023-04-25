from random import randint
tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
for c in tupla:  # FORMA DE INVOCAR MOSTRAR TODOS OS ELEMENTOS DA TUPLA, ACHO MAIS VISTOSO ASSIM.
    print(f'{c}', end=' ')
print(f'\nO maior valor é {max(tupla)} e o menor é {min(tupla)}')