dados = {}
gol = []
nome = str(input('Digite o nome do jogador: ')).strip().capitalize()
partidas = int(input('Quantas partidas ele jogou? '))
count = 1

for c in range(1, partidas + 1):
    gols = int(input(f'Quantos gols ele fez na {c}° partida? '))
    gol.append(gols)

dados['nome'] = nome
dados['gols'] = gol
dados['total'] = sum(gol)


print(f'Em {partidas} partidas {dados['nome']} marcou um total de {dados['total']} gols durante o campeonato.' if partidas != 1 else f'Em {partidas} partida {dados['nome']} marcou um total de {dados['total']} gols durante o campeonato.')
print('-=' * 20)
print(f'O jogador {dados['nome']} jogou {partidas} partidas.' if partidas != 1 else f'O jogador {dados['nome']} jogou {partidas} partida.')
for d in dados:
    if count <= partidas:
        print(f'    => Na {count}° partida, fez {gol[count - 1]} gols.')
        count += 1
    if count > partidas:
        break
print(f'Foi um total de {dados['total']} gols.')
