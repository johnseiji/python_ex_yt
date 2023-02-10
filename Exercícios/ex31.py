'''dist=float(input('Digite a distância que será percorrida em KM: '))
if dist <= 200:
    print('O valor da passagem será R${} Está no limite de 200 KM' .format(0.50 * dist))
else:
    print('O valor da passagem será  R${} Excedeu o limite de 200 KM ' .format( 0.45 * dist))'''
     #OU
dist=float(input('Digite a distância que será percorrida em KM: '))
preço= 0.50 * dist if dist <= 200 else dist * 0.45
print('O preço da passaggem será R${:.2F}'.format(preço))