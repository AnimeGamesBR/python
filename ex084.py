q = 0
dados = []
todos = []
peso = []
npesadas = []
nleves = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    q += 1

    for c in range(q):
        todos.append(dados[:])
        dados.clear()
        q -= 1
    for t in todos:
        peso.append(t[1])
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break

for t in todos:
    if t[1] == max(peso):
        npesadas.append(t[0])
    if t[1] == min(peso):
        nleves.append(t[0])

print('-=' * 20)
print(f'A quantidade total de pessoas cadastradas foi {len(todos)}!')
print(f'O maior peso foi {max(peso):.1f}Kg. Peso de {npesadas}')
print(f'O menor peso foi {min(peso):.1f}Kg. Peso de {nleves}')
