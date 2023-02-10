jogador = dict()
partidas = list()
jogador['Nome'] = nome = str(input('Nome do Jogador: '))
jogos = int(input(f'Partidas jogadas por {nome}: '))
for c in range(jogos):
    partidas.append(int(input(f"GOL's na partida {c + 1}: ")))
jogador["Gols"] = partidas
jogador["Total de Gols's"] = total = sum(partidas)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas')
for c in range(jogos):
    print(f'=> Na partida {c+1}, fez {jogador["Gols"][c]} Gols')
