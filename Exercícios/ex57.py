sexo = str(input('Digite se o sexo é [M] ou [F]: ')).upper().strip()[0]
print(sexo)
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor, informe seu sexo ')).upper().strip()[0]
if sexo == 'M':
  sexo = 'Masculino'
elif sexo == 'F':
  sexo = 'Feminino'
    
print('Sexo {} registrado com sucesso'.format(sexo))
