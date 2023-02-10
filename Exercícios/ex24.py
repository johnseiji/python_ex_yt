cidade=str(input('Digite o nome da sua cidade: ')).strip()
cidadem=cidade.lower()
print('Sua cidade começa com Santo {}'.format(cidadem[:5] == 'santo'))