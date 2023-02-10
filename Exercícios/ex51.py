p_termo = int(input('Digite o termo em que a P.A irá iniciar: '))
razao = int(input('Digite a razao da P.A: '))
decimo = p_termo + (10 - 1) * razao
print('Os 10 primeiros termos sao:')
for p_termo in range (p_termo , decimo + 1 , razao):
    print('{}' .format(p_termo), end=' -> ' )
print('ACABOU')
REFAZER