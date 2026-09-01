# a tupla usa parênteses e não pode mudar depois
nomes = ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')

print(type(nomes))
print(nomes)

# o in liga pra maiúscula então o bia minúsculo não é achado
print('bia' in nomes)
print('Bia' in nomes)

# o acesso é por posição começando do 0
print(nomes[0])

# aqui é o fatiamento então vem o início e o fim e o fim não entra
print(nomes[1:2])
print(nomes[1:3])
# com negativo no fim ele vai até o penúltimo
print(nomes[1:-1])
# sem o fim ele vai até o final
print(nomes[2:])
# sem o começo ele vai do início e os dois últimos ficam de fora
print(nomes[:-2])

# essa é a pegadinha parênteses sem vírgula não é tupla é só texto
x = ('Bia')
print(type(x))
# com a vírgula no final aí sim ela é uma tupla de um item
x = ('Bia', )
print(type(x))

# o len conta os itens e o repetido conta também
print(len(nomes))
