seg1=float(input('Digite o primeiro segmento: '))
seg2=float(input('Digite o segundo segmento: '))
seg3=float(input('Digite o terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Um triângulo será formado')
    if seg1 == seg2 == seg3:
        print('Equilátero')
    elif seg1 != seg2 != seg3 != seg1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não será formado um triângulo')
