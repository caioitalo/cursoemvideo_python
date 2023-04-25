sal = float(input('Digite o salário do funcionário: '))

if sal > 1250:
    print(f'O aumento é de 10% e será de R$ {(sal * 1.1):.2f}')

else:
    print(f'O aumento é de 15% e será de R$ {(sal * 1.15):.2f}')
