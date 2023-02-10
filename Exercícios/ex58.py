import random
cont = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = random.choice(lista)
jogador = int(input('Digite um valor de 0 á 10: '))
print('escolha do computador {}'.format(computador))
while jogador != computador:
    if jogador < computador:
        print('Mais...')
    elif jogador > computador:
        print('Menos...')
    jogador=int(input('Você errou! \nTente novamente: '))
    cont += 1 
print('Parabéns você acertou! a sua escolha foi {} e a do computador {}'.format(jogador,computador))
print('Você precisou de {} tentativas para acertar'.format(cont + 1))
#perguntar pro thiago true or false
Lo