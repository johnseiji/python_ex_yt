all_val = [[] , []]
for val in range(0 , 7):
    valores = int(input(f'Digite o {val + 1} valor: '))
    if valores % 2 == 0:
        all_val[0].append(valores)
    if valores % 2 != 0:
        all_val[1].append(valores)
all_val[0].sort()
all_val[1].sort()
print(f'Os valores pares digitados: {all_val[0]}')
print(f'Ós valores ímpares digitados: {all_val[1]}')
