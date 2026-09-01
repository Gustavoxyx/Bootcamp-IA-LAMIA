# duas listas pra combinar
pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']
# aqui é um for dentro de outro então cada pessoa recebe cada adjetivo
for p in pessoas:
    for a in adjs:
        # o f na frente do texto deixa usar variável dentro das chaves
        print(f'{p} é {a}!')

for i in [1, 2, 3]:
    # o pass não faz nada serve só pra não deixar o bloco vazio
    pass

for i in range(1, 11):
    # resto 1 na divisão por 2 quer dizer que o número é ímpar
    if i % 2  == 1:
        # o continue pula pra próxima volta então saem só os pares
        continue
    print(i)

for i in range(1, 11):
    if i == 5:
        # o break para o laço na hora
        break
    print(i)

print('Fim')
