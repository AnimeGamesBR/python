tupla = ('forno', 'carro', 'jaguar', 'logica', 'doidera', 'seloco')
vogais = 'aeiou'

print('[ Contando Vogais ]')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
