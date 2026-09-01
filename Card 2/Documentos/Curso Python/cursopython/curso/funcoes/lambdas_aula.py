# o reduce vem do functools
from functools import reduce

# uma lista de dicionários com os alunos
alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

# essas lambdas devolvem True ou False então elas servem de filtro
aluno_aprovado = lambda aluno: aluno['nota'] >= 7
aluno_honra = lambda aluno: aluno['nota'] >= 9

# o filter guarda só quem devolveu True
alunos_aprovados = filter(aluno_aprovado, alunos)

# essa lambda pega só a nota do aluno
obter_nota = lambda aluno: aluno['nota']

# essa lambda de soma vai ser usada pelo reduce
somar = lambda a, b: a + b

# o map aplica a função em cada item e o list mostra o resultado
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
# o reduce junta tudo num valor só começando do 0
total = reduce(somar, notas_alunos_aprovados, 0)

print(list(notas_alunos_aprovados))
print(total)

# a média dos aprovados
print(total / len(notas_alunos_aprovados))
