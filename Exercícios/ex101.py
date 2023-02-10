
def voto(nascimento):
    import datetime
    idade_atual = datetime.date.today().year - nascimento
    if idade_atual < 16:
        return (f'Com {idade_atual} anos\nNão Vota')
    elif  16 <= idade_atual < 18 or idade_atual > 65:
        return (f'Com {idade_atual} anos\nVoto Opcional')
    else:
        return (f'Com {idade_atual} anos\nVoto Obrigatório')



# Programa principa
ano = int(input('Ano de nascimento: '))
a = voto(ano)
print(a)