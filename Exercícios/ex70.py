total_gasto = total_1000 = 0
barato = ''
menor = 0
maior = 0
cadastros = 0
print('-' * 30)
print('     LOJA SUPER BARATÃO')
print('-' * 30)
while True:
    nome = str(input('Nome do Produto: '))
    preco = int(input('R$'))
    op = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print('-' * 30)
    total_gasto += preco
    if preco > 1000:
        total_1000 += 1
    cadastros += 1
    if cadastros == 1:
        menor = preco
        barato = cadastros
    else:
        if preco < menor:
            menor = preco
            barato = cadastros
    if op  == 'N':
        break
print('Sessão Finalizada')
print(f'O total gasto na compra R${total_gasto}')
print(f'O total de produtos acima de R$1000 é {total_1000}')
print(f'O produto mais barato é o de valor R${menor} {barato}')
refazer não entendi
