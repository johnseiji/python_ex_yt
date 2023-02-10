lar=float(input('Qual a largura da sua parede em metros? '))
alt=float(input('Qual a altura da sua parede em metros? '))
print('A área da sua parede tem a dimensão de {} x {} e área de {}m²' .format(lar , alt , lar * alt))
print('Para pintar a parede será necessário {} litros de tinta' .format((lar * alt)/2))
# 1 l de tinta a cada 2 m²
