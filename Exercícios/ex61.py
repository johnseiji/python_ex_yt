p1= int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
termo = p1
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end =' ')
    termo += razao
    cont += 1 
print('Fim')
REFAZER