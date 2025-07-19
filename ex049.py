v = int(input('Digite um número: '))

print('-' * 20)
print('[ \033[1;4;35mTABUADA\033[m ]')
for c in range(0, 11):
    n = 0 + c
    print(f'\033[31m{v} x {c:2} = {v * c}\033[m')
print('-' * 20)
