from random import randint
palpites = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
jogo = []
n = 0

print('{:=^35}'.format(f' SORTEANDO {palpites} JOGOS '))
for c in range(0, palpites):
    for q in range(0, 5):
        r = randint(0,80)
        while r in jogos[:]:
            r = randint(0, 80)
        jogos.append(r)
        n += 1
    n = 0
    jogo.append(jogos[:])
    jogos.clear()

for j in jogo:
    n += 1
    print(f'Jogo {n}: {sorted(j)}')
print('{:=^36}'.format(f' < BOA SORTE! > '))
