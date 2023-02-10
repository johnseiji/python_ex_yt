from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Nascimento'] = int(input('Ano de nascimento: '))
dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho [0 não possuí]: '))
dados['Idade'] = idade = date.today().year - dados['Nascimento'] 
if dados['Carteira de Trabalho'] == 0:
    print('-=' * 30)
    for k, v in dados.items():
        print(f'- {k} é igual a {v}')
else:
    dados['Ano de Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário R$: '))
    dados['Idade Aposentadoria'] = dados['Idade'] + (dados['Ano de Contratação'] + 35) - date.today().year
    print('-=' * 30)
    for k, v in dados.items():
        print(f'- {k} tem o valor igual a {v}')