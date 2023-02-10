soma = 0
maioridadehomem = 0
nomevelho = 0
for c in range (1 , 5):
    print('----- {} Pessoa -----' .format( c ))
    nome = str(input('Nome: ')) 
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:'))
    soma += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho == nome
    if
media_idade = soma / 4
print('A média de idade do grupo {}'.format(media_idade))
print('O homem mais velho do grupe é {}'.format())