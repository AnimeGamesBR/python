n = float(input('Digite um valor para ver sua tabuada: '))

if n.is_integer():
    n = int(n)
    print(f'\033[35m{'-'*16}\033[m \n\033[1;31m{n:.0f} x  0 = {n*0} \n{n:.0f} x  1 = {n*1} \n{n:.0f} x  2 = {n*2} \n{n:.0f} x  3 = {n*3} \n{n:.0f} x  4 = {n*4} \n{n:.0f} x  5 = {n*5} \n{n:.0f} x  6 = {n*6} \n{n:.0f} x  7 = {n*7} \n{n:.0f} x  8 = {n*8} \n{n:.0f} x  9 = {n*9} \n{n:.0f} x 10 = {n*10}\033[m \n\033[35m{'-'*16}')
else:
    print(f'\033[31m{'-'*22} \n\033[1;35m{n} x  0 = {n * 0:.2f} \n{n} x  1 = {n * 1:.2f} \n{n} x  2 = {n * 2:.2f} \n{n} x  3 = {n * 3:.2f} \n{n} x  4 = {n * 4:.2f} \n{n} x  5 = {n * 5:.2f} \n{n} x  6 = {n * 6:.2f} \n{n} x  7 = {n * 7:.2f} \n{n} x  8 = {n * 8:.2f} \n{n} x  9 = {n * 9:.2f} \n{n} x 10 = {n * 10:.2f}\033[m \n\033[31m{'-'*22}')
