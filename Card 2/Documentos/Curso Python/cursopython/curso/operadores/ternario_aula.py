lockdown = False
grana = 130

# o ternário é um if com else numa linha só
# no ternário a ordem acaba sendo invertida primeiro o valor se der True, depois a condição, depois o valor se der False
# uso ele quando só quero escolher um valor porque o if normal gastaria 4 linhas pra isso
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print(status)

# o f na frente troca as chaves pelo valor da variável
print(f'O status é: {status}')
