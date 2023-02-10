print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
total_18 = quant_m = mulher_20 = 0
while True:
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = str(input('Digite o sexo dessa pessoa [M/F]: ')).upper().strip()[0]
    print('-' * 40)
    op = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
    if idade >= 18:
        total_18 += 1
    if  sexo == 'M':
        quant_m += 1
    if sexo == 'F':
        if idade < 20:
            mulher_20 += 1
    if op== 'N':
        break
print('Cadastros Finalizados')
print(f'Foram cadastradas {total_18} pessoas maiores de idade')
print(f'Foram cadastrados {quant_m} homens')
print(f'Foram cadastradas {mulher_20} mulheres com menos de 20 anos')
rever video aula