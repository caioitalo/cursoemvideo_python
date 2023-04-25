    #exp = str(input('Digite uma expressão: '))

    #if exp.count('(') == exp.count(')'):
    #    print('A expressão é válida!')
    #else:
    #    print('A expressão não é válida!')
    # esse método contém um erro pois não considera expressões bizonhas. )a+b(*3

exp = str(input('Digite uma expressão: '))
an = []

for c in exp:
    if c == '(':
        an.append('(')
    elif c == ')':
        if len(an) > 0:
            an.pop()  # aqui ele retira um elemento relativo ao outro, par.
        else:
            an.append('0')
            break

if len(an) == 0:
    print('expressão válida')
else:
    print('expressão inválida')