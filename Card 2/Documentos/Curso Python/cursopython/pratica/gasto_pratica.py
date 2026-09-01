# essa tupla ela que guarda as categorias válidas
# é a tupla porque é constante e a tupla não pode ser alterada depois
CATEGORIAS = ('alimentacao', 'transporte', 'moradia', 'lazer', 'outros')


class Gasto:
    # o __init__ é o construtor e roda sozinho quando o objeto ele é criado
    def __init__(self, descricao, valor, categoria):
        # esses dois são públicos então qualquer um pode mexer
        self.descricao = descricao
        # o __valor nasce zerado pra existir antes do setter
        self.__valor = 0
        # aqui não é atribuição direta e sim uma passada pelo setter
        self.valor = valor
        # se a categoria não estiver na tupla ele joga em outros
        self.categoria = categoria if categoria in CATEGORIAS else 'outros'

    # esse é o getter e deixa ler o gasto.valor como ele fosse um atributo
    @property
    def valor(self):
        return self.__valor

    # esse é o setter e deixa escrever o gasto.valor mas sempre conferindo antes
    @valor.setter
    def valor(self, novo_valor):
        # só aceita valor maior que zero então zero e negativo são totalmente ignorados
        if novo_valor > 0:
            self.__valor = novo_valor

    # essa property é calculada e monta o texto na hora sem guardar exatamente nada
    @property
    def resumo(self):
        # o dois f depois dos dois pontos deixa o número com duas casas, conhecemos como float
        return f'{self.descricao} - R$ {self.valor:.2f}'


# o GastoFixo herda tudo do Gasto e acaba ganhando o dia do vencimento
class GastoFixo(Gasto):
    def __init__(self, descricao, valor, categoria, dia_vencimento):
        # o super chama o construtor da mãe pra não repetir código
        super().__init__(descricao, valor, categoria)
        # esse atributo existe só no filho
        self.dia_vencimento = dia_vencimento

    # aqui nós vamos reescrever o resumo que veio da mãe
    @property
    def resumo(self):
        # o super devolve o resumo da mãe e a gente só emenda o vencimento
        return f'{super().resumo} vence dia {self.dia_vencimento}'
