lista = []
mai = 0
men = 0
for val in range (0, 5):
    lista.append(input(f'Digite um valor para a posição {val} para ser inserido na LISTA: '))
    if val == 0:
        mai = men = lista[val]
    else:
        if lista[val] > mai:
            mai = lista[val]
        if lista[val] < men:
            men = lista[val]
print(f'Você digitou os seguintes valores: {lista}')
print(f'O maior valor digitado foi {mai} na posição ' , end = '')
for pos , v in enumerate(lista):
    if v == mai:
        print(f'{pos}', end = '... ')
print(' \n')
print(f'O menor valor digitado foi {men} na posição ', end = '')
for pos, val in enumerate(lista):
    if val == men:
        print(f'{pos}', end = '... ')

   REVER E PERGUNTAR O PQ DO 10 NAO FUNCIONAR

    