from time import sleep
print('-=' * 30)
print(f'De 0 a 10 pulando de 1 em 1')
print('-=' * 30)
for x in range(0, 11, 1):
    sleep(0.2)
    print(f'{x}', end =' ')
print(' ')
print('-=' * 30)
print(f'De 10 a 0 pulando de 2 em 2')
print('-=' * 30)
for y in range(10, -1, -2):
    sleep(0.2)
    print(f'{y}', end = ' ')
print(' ')
print('-=' * 30)
print('Agora é as sua vez!')
def contador(a, b, c):
    for c in range(a, b+1, c):
        sleep(0.5)
        print(f'{c}', end=' ')


# Programa Principal
a = int(input('Digite o ínicio: '))
b = int(input('Digite o fim: '))
c = int(input('Digite o passo: '))    
contador(a,b,c)
ver video