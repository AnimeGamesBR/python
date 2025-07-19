dados = {}
jogadores = []
gol = []
escolha = 0
count = 0
count2 = []

while True:
    nome = str(input('Digite o nome do jogador: ')).strip().capitalize()
    partidas = int(input('Quantas partidas ele jogou? '))

    for c in range(1, partidas + 1):
        gols = int(input(f'Quantos gols ele fez na {c}° partida? '))
        gol.append(gols)

    dados['nome'] = nome
    dados['gols'] = gol[:]
    dados['total'] = sum(gol)

    gol.clear()
    jogadores.append(dados.copy())
    dados.clear()

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('\033[1m-' * 60)
for c in range(0, len(jogadores)):
    count2.append(count)
    count += 1
    print(f'{c:3} {jogadores[c]['nome']:<10} {jogadores[c]['gols']} {jogadores[c]['total']:>10}')

print('-' * 60)
while escolha != 999:
    escolha = int(input('\033[mDeseja mostrar dados de qual jogador? [999 para parar] '))
    if escolha in count2:
        print(f'\033[1m-- Levantamento do jogador {jogadores[escolha]['nome']}:')
        for pos, g in enumerate(jogadores[escolha]['gols']):
            print(f'    No jogo {pos} fez {g} gols.')
        print('\033[m-' * 60)
    elif escolha not in count2 and escolha != 999:
        print(f'ERRO! Não existe jogador com código {escolha}! Tente novamente!')
        print('-' * 60)
