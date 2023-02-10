sala=float(input('Qual o salário do funcionário? R$ '))
if sala > 1250:
    print('Com o aumento de 10 % o salário irá para {}' .format(sala * 110/100))
else:
    print('Com o aumento de 15 % o salário irá para {}' .format(sala * 115/100))