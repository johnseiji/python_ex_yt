lista = []
cont = 0
while True:
    cont += 1
    aluno = str(input('Nome: '))
    nota1 = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    lista.append([aluno, [nota1, nota2], media])
    if op == 'N':
        break
print('-'*29)
print(f'{"No.":<4} {"Nome":<8}   {"Média":>12}')
print('-'*29)
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<8}  {a[2]:>12.1f}')
print(lista)
print(len(lista))
while True:
    escolha = int(input('Mostrar nota de qual aluno? (999 INTERROMPE): '))
    if escolha == 999:
        print('Finalizando')
        break
    if escolha <= len(lista) -1:
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1]}')
        refazer