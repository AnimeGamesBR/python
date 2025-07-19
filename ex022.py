nome = str(input('Digite seu nome completo: '))
maiusculas = nome.upper()
minusculas = nome.lower()
letrastotais = len(nome.replace(' ', ''))
letraspn = len(nome.split()[0])

print(f'Seu nome em letras maiúsculas fica: {maiusculas}. \nSeu nome em letras minúsculas fica: {minusculas}. \nSeu nome tem um total de {letrastotais} letras. \nSeu primeiro nome tem um total de {letraspn} letras.')
