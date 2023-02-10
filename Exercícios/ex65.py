cont = 0
soma = 0
maior = menor = 0
op = 'Ss'
while op in 'Ss':
    n = int(input('Digite um número: '))
    op = str(input('Você deseja continuar? \n[S/N]: ' )).upper().strip()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números' .format(cont))
print('A média desses números é {}' .format(soma/cont))
print('MAIOR valor digitado -> {} \nMENOR valor digitado -> {}'.format(maior, menor))
REVER
