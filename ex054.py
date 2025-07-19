from datetime import date
qm = 0
qn = 0

for c in range(1, 8):
    an = int(input(f'Ano de nascimento da {c}° pessoa: '))
    i = date.today().year - an
    if i >= 18:
        qm += 1
    else:
        qn += 1

if qm > 1 and qn > 1:
    print(f'{qm} pessoas são maiores de idade e {qn} pessoas são menores de idade.')
elif qm == 1 and qn == 1:
    print(f'{qm} pessoa é maior de idade e {qn} pessoa é menor de idade.')
elif qm == 1 and qn > 1:
    print(f'{qm} pessoa é maior de idade e {qn} pessoas são menores de idade.')
else:
    print(f'{qm} pessoas são maiores de idade e {qn} pessoa é menor de idade.')
