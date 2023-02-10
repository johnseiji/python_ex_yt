
a=float(input('Primeiro lado: '))
b=float(input('Segundo lado: '))
c=float(input('Terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('Irá formar um triângulo!')
else:
    print('Não irá formar um triângulo')