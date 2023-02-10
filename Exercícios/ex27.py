nome=str(input('Digite o seu nome completo: ')).strip()
nomedivi=nome.split()
print('O seu primeiro nome é {}'.format(nomedivi[0]))
print('O seu último nome é {}'.format(nomedivi[len(nomedivi) - 1]))
