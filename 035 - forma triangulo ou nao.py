print('=== Dá um triangulo ou não? ===')

l1 = float(input('Digite o comprimento da 1a reta: '))
l2 = float(input('Digite o comprimento da 2a reta: '))
l3 = float(input('Digite o comprimento da 3a reta: '))

# essa foi a minha solução: maiores = l1 + l2 + l3 - max(l1, l2, l3) dps ver um if maiores > max (l1, l2, l3)

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:  # teorema completo do triangulo.
    print('\nÉ possível formar um triângulo!')

#  aqui foi a adição do exercício 42
    if l1 == l2 == l3:
        print('E o triângulo em análise é equilátero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('E o triângulo em questão é isósceles!')
    else:
        print('E o triângulo em questão é escaleno!')


else:
    print('Não é possível formar um triângulo com essas retas.')
