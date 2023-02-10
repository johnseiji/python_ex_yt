''''n = 0
cont = 0
soma = 0'''''
n = int(input('Digite um número (999 para PARAR): '))
cont = soma = n = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número (999 para PARAR): '))
print('Você digitou {} números ' .format(cont))
print('O total dos valores é {}' .format(soma))
#REMOVER UM FLAG (n) -> COLOCA-LO NO FINAL DO WHILE E ANTES DO WHILE!!!
REVER