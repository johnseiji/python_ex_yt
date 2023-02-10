velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade, o valor da multa será de R${} ' .format((velocidade-80)*7))
else:
    print('Você está dentro do limite de velocidade')
