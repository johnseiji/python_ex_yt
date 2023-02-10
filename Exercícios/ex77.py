palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'
for p in palavras:
    print(f'\nNa palavra {p} existem as vogais: ', end = '')
    for letra in p:
        if letra in 'aAeEIiOoUu':
            print(letra.lower(), end = ' ')
            rever
