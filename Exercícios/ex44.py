preço=float(input('Digite o valor do produto: '))
print('[1] - À vista (Dinheiro / Cheque) / 10% Desconto')
print('[2] - À vista no  cartão / 5% Desconto')
print('[3] - 2x no cartão / Preço normal')
print('[4] - 3x ou MAIS no cartão / 20 % de Juros')
op=int(input('Digite a forma de pagamento '))
if op == 1:
    print('[1] O valor final do produto será R${}' .format(preço * (90/100)))
elif op == 2:
    print('[2] O valor final do produto será R${}' .format(preço * (95/100)))
elif op == 3:
    print('[3] O valor final do produto será R${} em 2x' .format(preço/2))
elif op == 4:
    parcelas = int(input('Digite o número de parcelas: '))
    print('[4] Sua compra será parcelada em {}x de R${:.2f} ' .format(parcelas , (preço/parcelas)*(120/100)))
    print('O preço final da sua compra será R${}' .format(preço  * (120/100)) )   



