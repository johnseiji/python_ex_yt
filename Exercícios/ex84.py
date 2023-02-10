cont  = 0
temp = []
definitiva= []
mai = men = 0
pme = pma = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(definitiva) == 0:
        mai = men = temp [1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    op =str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    definitiva.append(temp[:])
    print(temp)
    print(definitiva)
    temp.clear()
    if op == 'N':
        break        
print(definitiva)
print(temp)
for p in definitiva:
    if p[1] == mai:
        print(f'A pessoa mais pesada {p[0]}')
for p in definitiva:
    if p[1] == men:
        print(f'A pessoa mais leve {p[0]}')

print(f'Foram cadastradas {len(definitiva)} pessoas')
print(f'O maior peso foi {mai}')
print(f'O menor peso foi {men}')
rever