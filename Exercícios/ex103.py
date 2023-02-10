def ficha (jog, gol): 
    print(f'O Jogador {jog} fez {gol} Gols')



# Programa Principal
nome = str(input('Digite o nome do jogador: '))
n_gols = str(input('Digite o número de GOLS: '))
if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0
if nome.strip() == '':
    nome = '<Jogador Desconhecido>'
else:
    nome = str(nome)
ficha(nome, n_gols)
