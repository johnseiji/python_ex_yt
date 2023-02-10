matriz = [[0,0,0],[0,0,0],[0,0,0]]
print(matriz)
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a Matriz({l} , {c}): '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end = '')
    print()
    refazer