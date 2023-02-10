n1=int(input('Digite um valor: '))
n2=int(input('Digite um segundo valor: '))
n3=int(input('Digite um terceiro valor: '))
n4=int(input('Digite um quarto valor: '))
numeros = n1 , n2 , n3 , n4
print(f'Você digitou {numeros}')
print(f'O número 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print('Os valores pares digitados foram', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
