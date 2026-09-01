# a estrela junta todos os argumentos numa tupla, então soma 1 2 3 vira uma tupla com os três
def soma(*nums):
    total = 0
    # aqui ele percorre a tupla somando tudo
    for n in nums:
        total += n
    return total

# as duas estrelas juntam os argumentos com nome num dicionário
def resultado_final(**kwargs):
    # o ternário escolhe o status pela nota
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    # aqui vão aspas duplas pra não brigar com as simples de fora
    return f'{kwargs["nome"]} foi {status}'
