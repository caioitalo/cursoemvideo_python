cid = str(input('Digite seu nome completo: '))
cid = cid.strip()
cid = cid.title()  # caso a pessoa digite minúsculo ou com caps

print('O nome digitado tem Silva no sobrenome?', 'Silva' in cid.split())

