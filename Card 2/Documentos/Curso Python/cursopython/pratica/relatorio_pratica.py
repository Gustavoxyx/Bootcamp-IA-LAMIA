# o reduce mora no functools então precisa importar
from functools import reduce


# o total soma o valor de todos os gastos possiveis
def total(gastos):
    # se a lista estiver vazia ele devolve zero e nem cogita chamar o reduce
    if not gastos:
        return 0
    # o acumulado é o que já foi somado e o gasto é o item da vez
    return reduce(lambda acumulado, gasto: acumulado + gasto.valor, gastos, 0)


# a media divide o total pela quantidade
def media(gastos):
    # essa guarda evita o ZeroDivisionError com a lista vazia
    if not gastos:
        return 0
    # o len conta quantos gastos tem na lista
    return total(gastos) / len(gastos)


# o filter guarda só os gastos daquela categoria
def por_categoria(gastos, categoria):
    return list(filter(lambda gasto: gasto.categoria == categoria, gastos))


# essa list comprehension monta uma lista nova só com as descrições
def descricoes(gastos):
    return [gasto.descricao for gasto in gastos]


# aqui o retorno é um set porque o conjunto não guarda repetido
def categorias_usadas(gastos):
    return {gasto.categoria for gasto in gastos}


# o filter com lambda deixa passar só quem for maior que o limite
def acima_de(gastos, limite):
    return list(filter(lambda gasto: gasto.valor > limite, gastos))


# esse dicionário vai guardar a soma de cada categoria
def total_por_categoria(gastos):
    soma = {}
    for gasto in gastos:
        # o get devolve zero quando a categoria ainda não está no dicionário
        soma[gasto.categoria] = soma.get(gasto.categoria, 0) + gasto.valor
    return soma


# a estrela junta quantos gastos vierem numa tupla
def registrar_varios(lista, *valores):
    # percorre a tupla jogando cada gasto no fim da lista
    for gasto in valores:
        lista.append(gasto)
    return lista
