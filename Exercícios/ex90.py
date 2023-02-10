aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média do aluno {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}' )