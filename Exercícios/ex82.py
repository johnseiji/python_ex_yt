lista = []
lista_par = []
lista_impar = [] 
while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista_par.append(n)
    if n % 2 != 0:
        lista_impar.append(n)
    escolha = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    lista.append(n)
    if escolha == 'N':
        break
print(f'A sua lista {lista}')
print(f'A sua lista de números pares {lista_par}')
print(f'A sua lista de números ímpares {lista_impar}')
ver video exercico