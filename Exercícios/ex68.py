import random
print('-' * 21)
print('Jogo de PAR ou ÍMPAR')
print('-' * 21)
while True:
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    comp_escolha = random.randint(0,10)
    soma = comp_escolha + valor
    print(f'Você jogou {valor} e o computador jogou {comp_escolha}. O total deu {soma}')
    if soma % 2 == 0:
        print('O total deu um número PAR')
        cho = 'P'
        if escolha == cho:
            print('Parabéns você venceu!')
        elif escolha != cho:
            print('Você Perdeu! GAME OVER')
            break
    else:
        print('O total deu um número Ímpar')
        cho = 'I'
        if escolha == cho:
            print('Parabéns você venceu!')
        elif escolha != cho:
            print('Você Perdeu! GAME OVER')
            break
        rever video do exercico