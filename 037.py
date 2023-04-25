print('Conversor de números')
print('-=' * 20)

binar = int(input('Digite um número inteiro: '))
esc = int(input('Bases de conversão:'
                '\n1 - binário\n2 - hexadecimal\n3 - octal\n'
                'Escolha: '))

if esc == 1:
    print(f'O número {esc} em sistema binário é igual a {str(bin(binar)).strip("-0b")}')

elif esc == 2:
    print(f'O número {esc} em sistema hexadecimal é igual a {str(hex(binar)).strip("-0x")}')

elif esc == 3:
    print(f'O número {esc} em sistema octal é igual a {str(oct(binar).strip("-0o"))}')
