import datetime
ano=int(input('Digite o ano que será analisado ou coloque 0 para analisar o ano atual '))
if ano == 0:
    ano = datetime.date.today().year
    print(ano)
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0 :
    print('Este ano é Bissexto')
else:
    print('Este ano não é Bissexto')

    #REVER
