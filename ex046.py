from time import sleep
n = int(input('Digite um número: '))

for c in range(n, -1, -1):
    print(c)
    sleep(1)
print('\033[31mBOOOMMMMMM!!!')
