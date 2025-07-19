'''nome = str(input('Digite um nome completo: '))

if 'SILVA' in nome.upper():
    print('Este nome tem Silva.')
else:
    print('Este nome não tem Silva.')'''

nome = str(input('Digite um nome completo: '))

print(f'Tem Silva? {'SILVA' in nome.upper()}')
