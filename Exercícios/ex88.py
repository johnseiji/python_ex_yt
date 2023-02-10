import random
cont = 0
lista = []
a = 'MEGA SENA'
print('-'*30)
print(f'{a:^30}')
print('-'*30)
jogos = int(input('Quantos jogos você quer que sejam sorteados? '))
while True:
    cont += 1
    num = random.randint(1,60)
    if num not in lista:
        lista.append(num)
    if cont > 6:
        break
lista.sort()
print(f'Os números sorteados foram {lista}')
fazer