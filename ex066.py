n = ''
s = cont = 0

while True:
    n = input('Digite um número (fim para parar): ')
    if n.upper().strip() == 'FIM':
        break
    s += int(n)
    cont += 1
print(f'{cont} número foi digitado e seu valor é {s}' if cont == 1 else f'{cont} valores foram digitados e a soma deles é {s}' )
