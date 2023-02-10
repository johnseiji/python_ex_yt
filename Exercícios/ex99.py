from time import sleep
def maior(* núm):
    cont = maior = 0
    print('Análisando os valores fornecidos... ')
    for valor in núm:
        print(f'{valor} ',end = ' ', flush = True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam infromados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


# Programa Principal
maior(2, 9, 8, 3, 5)
maior(20, 5, 4, 12)
# maior(1, 7, 3, 10)
rever