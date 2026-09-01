# se não passar nada ele usa Pessoa e 20
def saudacao(nome = 'Pessoa', idade = 20):
    # a barra n quebra a linha
    print(f'Bom dia {nome}! \nVc nem parece ter {idade} anos!')

# o return devolve o valor e a multiplicação acontece antes da soma
def soma_e_multi(a, b, x):
    return a + b * x

# esse if só é verdade quando o arquivo roda direto e não quando ele é importado
if __name__ == '__main__':
    # o Ana vai por posição e a idade vai por nome
    saudacao('Ana', idade=30)
