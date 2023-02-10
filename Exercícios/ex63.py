print('-' * 23)
print('Sequencia de Fibonacci')
print('-' * 23)
cont = 3
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}' .format(t1, t2), end = ' ')
while cont <= termos:
    cont += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('-> {}' .format(t3), end = ' ')
print('FIM')
rever