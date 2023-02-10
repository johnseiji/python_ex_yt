
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: ' ))
op = 0 
while op != 5:
    print('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos Números \n[5]Sair do programa')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        print('A SOMA dos valores {} e {} é igual {} ' .format(v1,v2, v1+v2))
    if op == 2:
        print('A MULTIPLICAÇÃO dos valores {} e {} é igual a {}' .format(v1,v2, v1*v2))
    if op == 3:
        if v1 > v2:
            print('O PRIMEIRO VALOR é MAIOR')
        elif v1 < v2:
            print('O SEGUNDO VALOR É MAIOR')
        else:
            print('Os VALORES são IGUAIS')
    if op == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: ' ))
    if op > 5:
        print('Digite uma opção válida')
print('Você saiu do proggrama!')