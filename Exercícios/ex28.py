import random
numero=int(input('Escolha um número de 0 a 5: '))
lista=[0, 1, 2, 3, 4, 5 ]
computador=random.choice(lista)
print('Você escolheu {} o Computador escolheu {}'.format(numero , computador))
if numero == computador:
    print('Parabéns !!! Você adivinhou o número que o Computador escoheu! ')
else:
    print('Que pena, você errou')

