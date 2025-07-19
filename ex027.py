nome = str(input('Digite um nome completo: ')).title().strip().split()

print(f'Muito prazer em te conhecer {nome[0]}!')
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome) - 1]}')
