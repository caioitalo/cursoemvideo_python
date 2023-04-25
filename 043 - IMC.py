print('-=' * 21)
print('CÁLCULO DE IMC')
print('-=' * 21)

peso = float(input('Digite o peso do paciente (em kg): '))
alt = float(input('Digite a altura do paciente (em m): '))
imc = peso / pow(alt, 2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} estando na categoria ABAIXO DO PESO.')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f} estando na categoria PESO IDEAL.')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f} estando na categoria SOBREPESO.')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f} estando na categoria OBESIDADE.')
else:
    print(f'Seu IMC é de {imc:.2f} estando na categoria OBESIDADE MÓRBIDA.')
