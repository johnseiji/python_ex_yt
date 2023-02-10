soma = 0 #contador
for n in range (1 , 7):
    nu = int(input('Digite seis números: '))
    if nu % 2 != 0:
        print('Apenas valores pares válidos')
    else:
        soma +=  nu
print('A soma dos seis números digitados é {}' .format(soma))
