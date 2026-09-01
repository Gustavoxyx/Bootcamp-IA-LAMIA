from functools import reduce

notas = [6.4, 7.2, 5.8, 8.4]

# essa função soma um e meio na nota
def mais_um_meio(nota):
    return nota + 1.5

# o map aplica a função item por item
# ele é preguiçoso só calcula quando a gente percorre
notas_finais = map(mais_um_meio, notas)

# isso é closure, agora o quanto somar é escolhido na hora
def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar

notas = [6.4, 7.2, 5.4, 8.4]
# o somar_nota ele devolve uma função e o map usa ela em cada nota
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)

# o list força o map a rodar
print(list(notas_finais_1))

print(list(notas_finais_2))

# o (a) é o que já foi somado e o (b) é o item da vez
def somar(a, b):
    return a + b

# o reduce transforma tudo num número só e o 0 é o começo
total = reduce(somar, notas, 0)
print(total)
