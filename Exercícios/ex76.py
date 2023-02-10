print('-' * 30)
print('       LISTA DE PREÇOS')
print('-' * 30)
listagem =  ('Lápis', 1.75, 
             'Borracha', 2.00, 
             'Caderno', 15.90, 
             'Estojo', 25, 
             'Tranferidor', 4.90, 
             'Compasso', 9.99, 
             'Mochila', 120.32, 
             'Canetas', 22.30, 
             'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'Produto: {listagem[pos]:.<40}', end=' ')
    if pos % 2 != 0:
        print(f'R$ {listagem[pos]:.2f}')