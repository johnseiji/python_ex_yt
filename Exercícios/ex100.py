import random
from time import sleep
def sorteia(lista):
    print(f'Sorteando 5 valores para a lista...', flush = True)
    sleep(0.5)
    for c in range(5):
        n = random.randint(0,10)
        lista.append(n)
        print(f'{n}', end = '  ', flush = True)
        sleep(0.5)
    print('\nPronto')
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma de todos os valores pares é igual a {soma}')


# Programa Principal
números = []
sorteia(números)
somapar(números)