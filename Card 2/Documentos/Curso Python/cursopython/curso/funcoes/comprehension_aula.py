# o reduce mora no functools ele não é nativo como o map e o filter
from functools import reduce

# uma lista de dicionários cada aluno tem nome e nota
alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

# essa é a list comprehension ela monta uma lista nova em uma linha
# lê assim, pega cada aluno se a nota for 7 ou mais
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7 ]
print(alunos_aprovados)

# a lambda é uma função curta sem nome
somar = lambda a, b: a + b

# outra comprehension agora só pra tirar as notas
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
# o reduce vai somando dois a dois e o 0 é onde ele começa
total = reduce(somar, notas_alunos_aprovados, 0)

print(list(notas_alunos_aprovados))
print(total)

# a média é a soma dividida pela quantidade e o len conta os itens
print(total / len(notas_alunos_aprovados))
