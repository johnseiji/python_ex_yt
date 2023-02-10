import random
import time
import operator
dic = dict()
jogada1 = dic['JOGADOR 1'] = random.randint(1,6)
jogada2 = dic['JOGADOR 2'] = random.randint(1,6)
jogada3 = dic['JOGADOR 3'] = random.randint(1,6)
jogada4 = dic['JOGADOR 4'] = random.randint(1,6)
print('Jogadas Realizadas')
for k, v in dic.items():
    print(f'O {k} tirou {v}')
    time.sleep(1)
ranking = list()
ranking = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)
print('-=' * 30)
print('RANKING DOS JOGADORES')
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i + 1} LUGAR: {v[0]} com {v[1]}')
    time.sleep(1)
print('-=' * 30)
rever