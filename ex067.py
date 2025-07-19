n = ''
cont = 0
m = 1

while True:
    n = input('Digite um número e veja sua tabuada (digite fim para parar): ')
    if n.strip().upper() == 'FIM':
        break
    print('=-=' * 25)
    for c in range(0, 11):
        print(f'{n} x {cont} = {int(n)*cont}')
        cont += 1
    print('=-=' * 25)
    cont = 0
print('=-=' * 25)
print('FIM DO PROGRAMA')
