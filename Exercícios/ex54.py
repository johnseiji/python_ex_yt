from datetime import date
total_maior = 0
total_menor = 0

for pess in range (7):
    nasc1=int(input('Digite o ano de nascimento da {} pessoa: '.format(pess + 1)))
    idade_atual1 = date.today().year - nasc1
    if  idade_atual1 >= 21:
        print('A primeira pessoa atingiu a maioridade, a sua idade é {} anos' .format(idade_atual1))
        total_maior += 1
    else:
        print('A primeira pessoa nao atingiu a maioridade, a sua idade é {} anos' .format(idade_atual1))
        total_menor += 1

print('{} pessoas sao maiores de idade'.format(total_maior))
print('{} pessoas sao menores de idade'.format(total_menor))