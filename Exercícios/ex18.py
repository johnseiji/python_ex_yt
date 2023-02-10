import math
ang=float(input('Digite o angulo que você deseja: '))
print('O angulo de {:.2f}\nSENO: {:.2f}\nCOS: {:.2f}\nTANGENTE: {:.2f}' .format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))