# essa é a classe mãe a base das outras
class Carro:
    # o __init__ é o construtor ele roda sozinho quando o objeto é criado
    def __init__(self):
        # os dois underscores na frente deixam o atributo privado
        self.__velocidade = 0

    # o property deixa ler o metodo como se fosse um atributo

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self):
        # aumenta a velocidade de 5 em 5
        self.__velocidade += 5
        return self.__velocidade

    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade

# a Uno herda tudo do Carro
class Uno(Carro):
    # o pass não acrescenta nada ela usa o que veio da mãe
    pass

# a Ferrari também herda mas vai mudar o acelerar
class Ferrari(Carro):
    pass

    # aqui a gente reescreve um o metodo que veio da mãe
    def acelerar(self):
        # o super chama a versão da mãe e chamando duas vezes o carro anda 10
        super().acelerar()
        return super().acelerar()

# criando um objeto da classe Uno
c1 = Uno()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())

# agora com a Ferrari, pra comparar
c1 = Ferrari()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
# o frear continua sendo o da mãe, então tira 5
print(c1.frear())
print(c1.frear())
print(c1.frear())
