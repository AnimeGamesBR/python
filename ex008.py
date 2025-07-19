n = float(input('\033[36mDigite um valor em metros:\033[m '))

print(f'A medida de \033[1;32m{n:.2f}m\033[m corresponde a: \n\033[1;31m{n/1000}km\033[m \n\033[1;33m{n/100}hm\033[m \n\033[1;34m{n/10}dam\033[m \n\033[1;35m{n*10}dm\033[m \n\033[1;36m{n*100}cm\033[m \n\033[1;37m{n*1000}mm\033[m')
