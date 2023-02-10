soma = 0 # Acumulador
cont = 0 #Contador
for n in range(1 , 501 , 2 ):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n 
print('A soma de todos os {} impares e divisiveis por 3 é {}'.format(cont , soma))

