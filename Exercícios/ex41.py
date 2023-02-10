import datetime
ano=int(input('Digite o ano de nascimento do atleta: '))
idade=int(datetime.date.today().year - ano)
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Atleta MIRIM')
elif idade > 9 and ano <= 14:
    print('Atleta INFANTIL')
elif idade > 14 and ano <= 19:
    print('Atleta JUNIOR')
elif idade > 19 and ano <= 25:
    print('Atleta SENIOR')
elif idade > 25:
    print('Atleta MASTER')