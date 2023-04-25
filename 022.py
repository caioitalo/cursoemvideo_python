print('====== EXERCÍCIO 22 ======\nInformações do nome\n')

n = str(input('Digite seu nome completo: ')).strip()

#  n = n.strip() eu tinha feito isso aqui antes de ver a resolução, fazer acima fica mais fácil.

print(f'{n.upper()}\n{n.lower()}\n{n.title}\n{n.capitalize()}')
print(f'O seu primeiro nome tem {len(n.split()[0])} letras')

n = n.split()
print(f'O total de letras é: {len("".join(n))}')

#  atenção aos métodos de split, strip e join. interessante. demorei bastante
