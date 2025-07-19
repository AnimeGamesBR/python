lista = []
poscoluna = 0
poslinha = 0
for n in range(0, 9):
    lista.append(int(input(f'Digite um número para a posição [{poscoluna}, {poslinha}]: ')))
    poslinha += 1
    if poslinha >= 3:
        poslinha = 0
        poscoluna += 1
print('-=' * 40)
print(f'[ {lista[0]:^5} ] [ {lista[1]:^5} ] [ {lista[2]:^5} ]')
print(f'[ {lista[3]:^5} ] [ {lista[4]:^5} ] [ {lista[5]:^5} ]')
print(f'[ {lista[6]:^5} ] [ {lista[7]:^5} ] [ {lista[8]:^5} ]')
