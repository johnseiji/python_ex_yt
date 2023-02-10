while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()
    while len(sexo) > 1 or sexo not in 'MF':
        print('Por favor, digite apenas "M" OU "F" ')
        sexo = str(input('Sexo[M/F]: ')).upper().strip()
    idade = int(input('Idade: '))
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while len(op) > 1 or op not in 'SN':
        print('Por favor, digite apenas "S" ou "N" ')
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()