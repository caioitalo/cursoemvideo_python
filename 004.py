variav = input('Digite algo: ')
print('foi digitado algo?', bool(variav))
print('O tipo primitivo do digitado é:', type(variav))
print('O que foi digitado é número? ', variav.isnumeric())
print('o que foi digitado é palavra? ', variav.isalpha())
print('o que foi digitado é alfanúmerico? ', variav.isalnum())
print(f'o que foi digitado tá tudo maiusculo? {variav.isupper()} ') #forma nova de formatar a variável dentro do print
print(f'o que foi digitado é só espaço? {variav.isspace()}')
print(f'o que foi digitado está capitalizada? {variav.istitle()}') # 1a letra maiuscula


# esses exemplos parecem interessantes no momento de análises de senhas
# ou para ver checar se algum campo ficou em branco