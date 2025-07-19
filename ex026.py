frase = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')

print(f'Esta frase tem {frase.count('A')} letras A.')
print(f'A primeira posição de letras A nesta frase é {frase.find('A') + 1}.')
print(f'A ultima posição de letras A nesta frase é {frase.rfind('A') + 1}.')