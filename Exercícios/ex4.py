v1=input('Digite algo: ')
print('O tipo primitivo desse número é {}'.format(type(v1)))
print('O que foi digitado só tem espaços? ', v1.isspace())
print('O que foi digitado é um número? ' , v1.isdigit())
print('O que foi digitado possuí apenas letras maiúsculas?' , v1.isupper())
print('O que foi digitado possuí apenas letras minúscular?' , v1.islower())
print('A primeira letra é maiúscula (Capitalizada) ? ' ,  v1.istitle())