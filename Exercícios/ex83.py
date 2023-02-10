pilha_ab = []
pilha_fe = []
exp = str(input('Digite a função: '))
for parenteses in exp:
    if parenteses == '(':
        pilha_ab.append('(')
    elif parenteses == ')':
        pilha_fe.append(')')
cont_ab = len(pilha_ab) 
cont_fe = len(pilha_fe)
if cont_ab == cont_fe:
    print('A sua função está correta!')
else:
    print('A sua função está incorreta!')
ver video exer