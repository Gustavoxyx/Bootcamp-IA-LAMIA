class Contador:
    # esse atributo é da classe então ele é compartilhado com tods
    contador = 10

    # esse é um metodo normal ele recebe o self
    def inc_maluco(self):
        # tem que ter cuidado porque isso cria um atributo só desse objeto com o mesmo nome
        self.contador = self.contador + 1
        return self.contador

    def inst(self):
        return 'Estou bem!'

    # o classmethod recebe a classe cls no lugar do objeto
    @classmethod
    def inc(cls):
        # aqui ele mexe no contador da classe então vale pra todos
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    # o staticmethod não recebe self nem cls então é uma função solta dentro da classe
    @staticmethod
    def mais_um(n):
       return n + 1

# criando um objeto
c1 = Contador()
# o metodo de classe também pode ser chamado pelo objeto
print(c1.inc())
print(c1.inc())
print(c1.inc())
print(c1.dec())
print(c1.dec())
print(c1.dec())

# chamando direto pela classe sem criar objeto
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())

c1 = Contador()
print(c1.inst())

# aqui o contador desgruda da classe e passa a ser só desse objeto
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())
# o contador da classe continua com o valor dele
print(Contador.inc())
print(Contador.inc())

# o metodo estático ele é usado como uma função qualquer
print(Contador.mais_um(99))
