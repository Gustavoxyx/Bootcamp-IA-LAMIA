# o range 10 gera os números de 0 até 9, o 10 não entra
for i in range(10):
    # o end com espaço faz o print continuar na mesma linha
    print(i, end=' ')

# esse print vazio serve só pra pular linha
print('')

# aqui o range recebe início e fim, então começa no 1 e para antes do 11
for i in range(1, 11):
    print(i, end=' ')

print('')

# o terceiro número é o passo, então ele pula de 7 em 7
for i in range(1, 100, 7):
    print(i, end=' ')

print('')

# com passo negativo a contagem vai de trás pra frente
for i in range(20, 0, -3):
    print(i, end=' ')

print('')

# uma lista de números
nums = [2, 4, 6, 8]
# aqui o for pega um item da lista por vez
for n in nums:
    print(n, end=' ')

print('')

texto = 'Python é muito massa!'
# aqui da pra percorrer o texto letra por letra
for letra in texto:
    print(letra, end=' ')

print('')

# o conjunto não guarda valor repetido, então o 4 so vai aparecer uma vez só
for n in {1, 2, 3, 4, 4, 4} :
    print(n, end=' ')

print('')

# um dicionário guarda chave e valor
produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

# aqui o dicionário vem direto, então vem somente as chaves
for atrib in produto:
    # usando a chave pra pegar o valor
    print(atrib, '==>', produto[atrib], end=' ')

print('')

# com o items vem a chave e o valor juntos
for atrib, valor in produto.items():
    print(atrib, '==>', valor, end=' ')

print('')

# com o values vêm somente os valores
for valor in produto.values():
    print(valor, end=' ')

print('')

# com o keys vêm somente as chaves
for atrib in produto.keys():
    print(atrib, end=' ')

print('')
