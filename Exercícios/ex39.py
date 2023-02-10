import datetime
ano=int(input('Ano de nascimento: '))
atual=datetime.date.today().year - ano
anoalist= 18 - atual
print('Quem nasceu em {} tem {} ano hoje' .format(ano , atual))
if atual < 18:
    print('Ainda faltam {} anos para seu alistamento' .format(anoalist))
    print('Seu alistamento será em {}' .format(datetime.date.today().year + (18 - atual)) )
