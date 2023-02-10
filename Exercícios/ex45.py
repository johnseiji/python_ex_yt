''''import random
jogador=int((input('Escolha entre \n 1 - [Pedra] \n 2 - [Papel] \n 3 - [Tesoura] \n ')))
lista=[1, 2, 3]
computador=int(random.choice(lista))
if jogador == 1:
    print('Você escolheu PEDRA')
elif jogador == 2:
    print('Você escolheu PAPEL')
elif jogador == 3:
    print('Você escolheu TESOURA')
if computador == 1:
    print ('O computador escolheu PEDRA')
elif computador == 2:
    print('O computador escolheu PAPEL')
elif computador == 3:
    print('O computador escolheu TESOURA')
if jogador == computador:
    print('EMPATE!')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR VENCEU!')
elif jogador == 1 and computador == 3:
    print('JOGADOR VENCEU!')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCEU!')
elif jogador == 2 and computador == 3:
    print('COMPUTADOR VENCEU')
elif jogador == 3 and computador == 1:
    print('COMPUTADOR VENCEU')
elif jogador == 3 and computador == 2:
    print('JOGADOR VENCEU') '''
# OU
import random
lista=['Pedra','Papel' ,'Tesoura']
computador= int(random.randint(0,2))
print('Suas Opçoes: \n [Pedra] - 1 \n [Papel] - 2 \n [Tesoura] - 3 ')
jogador=int((input('Faça a sua escolha: ')))
if jogador != 1 and jogador != 2 and jogador != 3:
    print('JOGADA INVÁLIDA')
print('Voce escolheu {}' .format(lista[jogador - 1]))
print('O Computador escolheu {}!' .format(lista[computador]))
if computador == 0: # computador escolheu PEDRA
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    elif jogador == 3:
        print('JOGADOR VENCEU')
elif computador == 1: # computador escolheu papel
    if jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('JOGADOR VENCEU')
elif computador == 2:
    if jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    elif jogador == 3:
        print('EMPATE')                

