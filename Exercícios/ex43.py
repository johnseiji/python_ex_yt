peso=float(input('Peso(KG): '))
altura=float(input('Altura(M): '))
imc=peso / (altura ** 2)
print('Seu IMC {:.1f}' .format(imc) )
if imc <= 18.5:
    print('Abaixo do peso ideal')
elif  imc >  18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif  imc > 30 and imc <= 40:
    print('Obeso')
else: 
    print('Obesidade Mórbida')