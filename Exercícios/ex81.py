contador = 0
lista = []
while True:
    valor = int(input('Digite um valor: '))
    escolha = str(input('Você deseja continuar? [S/N]: ')).strip().lower()[0]
    lista.append(valor)
    contador += 1 
    if escolha == 'n':
        break
print(f'Você digitou {contador} elementos')
print(f'A sua lista: {lista}')
lista.sort(reverse = True)
print(f'A sua lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na sua lista!')
else:
    print('O valor 5 não foi encontrado na sua lista')
ver video exercicio