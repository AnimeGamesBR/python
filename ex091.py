from random import randint
dados = {}
count = 1

for c in range(1, 5):
    dados[f'jogador{c}'] = randint(1, 7)

print('Valores sorteados: ')
for d in dados.items():
    print(f'   O {d[0]} tirou {d[1]}')

dados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=True))
print('Ranking dos jogadores: ')
for d in dados.items():
    print(f'   {count}° lugar: {d[0]} com {d[1]}')
