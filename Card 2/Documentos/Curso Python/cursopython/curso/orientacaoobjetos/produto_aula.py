class Produto:
    # construtor com valor padrão pro preco e pro desc
    def __init__(self, nome, preco = 1.99, desc = 0):
        # esse atributo é público então qualquer um mexe
        self.nome = nome
        # o __preco é privado então só a classe mexe nele
        self.__preco = preco
        self.desc = desc

    # esse é o getter ele deixa ler o p1.preco
    @property
    def preco(self):
        return self.__preco

    # esse é o setter ele deixa escrever o p1.preco mas conferindo antes
    @preco.setter
    def preco(self, novo_preco):
        # só aceita preço positivo então o negativo ele é ignorado
        if novo_preco > 0:
            self.__preco = novo_preco

    # essa property é calculada ela não guarda nada e acaba fazendo a conta na hora
    @property
    def preco_final(self):
        # aqui ele aplica o desconto sobre o preço
        return (1 - self.desc) * self.__preco

# criando dois objetos
p1 = Produto('Caneta', 10, 0.1)
p2 = Produto('Caderno', 14, 0.5)

# o setter barra o negativo então o preço não muda
p1.preco = -70
p2.preco = -1.99

# agora sim os valores são aceitos
p1.preco = 70.89
p2.preco = 17.99

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)
