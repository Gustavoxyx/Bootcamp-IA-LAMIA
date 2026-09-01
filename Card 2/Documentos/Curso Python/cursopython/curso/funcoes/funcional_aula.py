def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

# a função é um valor então somar aponta pra mesma função
# vai sem parênteses senão a gente estaria chamando ela
somar = soma
print(somar(3, 4))

# essa função recebe outra função no lugar do fn
def operacao_aritmetica(fn, op1, op2):
    # aqui ele chama a função que chegou
    return fn(op1, op2)

# passando a soma como argumento
resultado = operacao_aritmetica(soma, 13, 48)
print(resultado)

# agora passando a sub sem mudar nada na função de cima
resultado = operacao_aritmetica(sub, 13, 48)
print(resultado)

# isso é closure a função de dentro lembra do a
def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    # aqui ele devolve a função e não o resultado
    return concluir_soma

# o fn agora é a concluir_soma com o (a) valendo 10
fn = soma_parcial(10)

resultado_final = fn(12)
print(resultado_final)

# o primeiro parênteses devolve a função e o segundo executa ela
resultado_final = soma_parcial(10)(12)
print(resultado_final)

# aqui o (a) fica travado em 1 então dá pra reusar várias vezes
soma_1 = soma_parcial(1)
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)
print(resultado_final, r1, r2, r3)
