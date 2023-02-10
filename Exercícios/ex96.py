def area (l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é {a}')


# Programa principal (2x linhas de distância)
print('Controle de terrenos')
print('-' * 20)
l = float(input('Largura(M): '))
c = float(input('Comprimento(M): '))
area(l,c)