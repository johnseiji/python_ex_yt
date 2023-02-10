times ='Palmeiras', 'Chapecoense','Vasco da Gama','Grêmio','Flamengo','Corinthians','Internacional','Cruzeiro','São Paulo','Atlético Mineiro','Botafogo','Fluminense','Coritiba','Bahia','Goiás','Guarani','Sport','Portuguesa','Atlético Paranaense','Vitória'
print(f'Lista de times {times}')
#ou for t in times:
        #print(t)
print(f'Os 5 primeiros colocados: {times[:5]}')
print(f'Os 4 últimos colocados: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'A Chapecoense está na posição {times.index("Chapecoense")+1}')



