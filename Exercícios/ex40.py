a=float(input('Digite a primeira nota: '))
b=float(input('Digite a segunda nota: '))
media=(a + b)/2
print('Tirando {} e {}, a média do aluno será {}' .format(a , b , media))
if media < 5:
    print('Reprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
elif media >= 7:
    print('Aprovado')