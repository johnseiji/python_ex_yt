frase=str(input('Digite uma frase: ')).strip().upper()
palavras_separadas =  frase.split()
palavras_juntas = ''.join(palavras_separadas)
print('Voce digitou a frase {}' .format(frase))
fazer