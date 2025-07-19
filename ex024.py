'''cid = str(input('Digite o nome de uma cidade: '))
cid = cid.upper()

if cid.startswith('Santo'):
    cid = cid.title()
    print('A cidade digitada começa com Santo.')
else:
    print('A cidade digitada não começa com Santo.')'''

cid = str(input('Digite o nome de uma cidade: ')).strip()

print(f'Começa com Santo: {cid[:5].upper() == 'SANTO'}')
