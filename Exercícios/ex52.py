n = int(input('Digite um número: '))
tot = 0 #numero de divisiveis
for c in range ( 1 , n + 1 ):
    if n % c == 0:
        tot += 1 
        print('\033[31m')
    else:
        print('\033[m')
    print('{}' . format(c), end = ' ')
print('\n\033[mO número {} foi divisível {} vezes' .format(n , tot))
if tot == 2 or tot == 1:
    print('Este número é primo')
else:
    print('Este número nao é primo')
REFAZER