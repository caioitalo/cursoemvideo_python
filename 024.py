cid = str(input('Digite o nome da sua cidade: '))
cid = cid.title()  # caso a pessoa digite minúsculo ou com caps
cid = cid.split()  # cortou os espaços e dividiu as palavras
print('A cidade que você mora inicia com Santo?', 'Santo' == cid[0])
