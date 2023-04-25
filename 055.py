# menor = 1000. essa é a maneira da gambiarra, mas é melhor do jeito abaixo. mais programático

for i in range(0, 5):
    peso = float((input('Digite o peso da pessoa: ')))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
        if peso <= 0 or peso > 600:
            print('Você não digitou um peso válido. Tente novamente!')
            exit()

print(f'O maior peso dentre os 5 foi {maior:.2f} kg')
print(f'O menor peso dentre os 5 foi {menor:.2f} kg')
