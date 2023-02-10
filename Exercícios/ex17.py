''' co=float(input('Qual o comprimento do cateto oposto? '))
ca=float(input('Qual o comprimento do cateto adjacente? '))
print('A hipotenusa é {:.2f}' .format((co ** 2 + ca ** 2) ** (1/2))) '''
 # OU
import math
co=float(input('Qual o comprimento do cateto oposto? '))
ca=float(input('Qual o comprimento do cateto adjacente? '))
print('A hipotenusa é {:.2f}' .format(math.hypot(co,ca)))