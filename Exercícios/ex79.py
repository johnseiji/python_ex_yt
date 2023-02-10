lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor digitado com sucesso...')
    else :
        print('Número duplicado, não é possível adicioná-lo')
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if escolha == 'n':
        break
print(f'Valores digitados {lista}')
lista.sort()
print(f'Os valores em ordem crescente são {lista}')

