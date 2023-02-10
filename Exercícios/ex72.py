cont = 'Zero','Um', 'Dois','Três', 'Quatro', 'Cinco', 'Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte'
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente')

print(f'Você Digitou {cont[numero]}')
