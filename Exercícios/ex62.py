p1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
cont = 1
termo = p1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ->'.format(termo), end = ' ')
        cont += 1
        termo += razao 
    print('PAUSA')
    mais = int(input('Quantos termos você quer adicionar a mais? '))
print('FIM')
rever