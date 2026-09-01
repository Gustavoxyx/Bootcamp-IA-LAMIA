# importando as entidades do outro arquivo
from gasto_pratica import CATEGORIAS, Gasto, GastoFixo
# importando as funções do relatório
from relatorio_pratica import total, media, descricoes, categorias_usadas
from relatorio_pratica import acima_de, total_por_categoria, registrar_varios


# essa função protege o programa de quebrar quando digitarem letra
def ler_valor():
    # o try tenta converter e o except segura o erro se der ruim
    try:
        return float(input('Valor do gasto R$ '))
    except ValueError:
        print('Isso não é número')
        return 0


def cadastrar(gastos, fixo):
    descricao = input('Descrição do gasto ')
    valor = ler_valor()
    # eu paro ele aqui antes de criar o objeto senão o setter deixaria o gasto com valor zero;
    if valor <= 0:
        print('Valor inválido então o gasto não foi salvo')
        return
    print(f'Categorias válidas {CATEGORIAS}')
    categoria = input('Categoria ')
    # o fixo decide qual das duas classes será usada
    if fixo:
        dia = input('Dia do vencimento ')
        registrar_varios(gastos, GastoFixo(descricao, valor, categoria, dia))
    else:
        registrar_varios(gastos, Gasto(descricao, valor, categoria))
    print('Gasto salvo')


def mostrar_relatorio(gastos):
    # lista vazia é falsa então esse not avisa antes de tentar calcular alguma coisa
    if not gastos:
        print('A lista está vazia e ainda não tem gasto pra mostrar')
        return
    # o for percorre a lista mostrando um gasto por vez
    for gasto in gastos:
        print(gasto.resumo)
    print(f'Total R$ {total(gastos):.2f}')
    print(f'Média R$ {media(gastos):.2f}')
    print(f'Categorias usadas {categorias_usadas(gastos)}')
    print(f'Descrições {descricoes(gastos)}')
    # o items devolve a chave e o valor juntos do dicionário
    for categoria, soma in total_por_categoria(gastos).items():
        print(f'{categoria} R$ {soma:.2f}')
    # aqui acaba mostrando só os gastos acima de cem
    for gasto in acima_de(gastos, 100):
        print(f'Passou de cem {gasto.resumo}')


def main():
    # a lista começa vazia e vai guardando os objetos
    gastos = []
    # o while True roda pra sempre e só para no break
    while True:
        print('\n1 novo gasto')
        print('2 novo gasto fixo')
        print('3 relatório')
        print('4 sair')
        opcao = input('Escolha ')

        if opcao == '1':
            cadastrar(gastos, False)
        elif opcao == '2':
            cadastrar(gastos, True)
        elif opcao == '3':
            mostrar_relatorio(gastos)
        elif opcao == '4':
            # o break encerra o while na hora
            break
        # o else ele pega qualquer coisa que não seja de um a quatro
        else:
            print('Opção inválida')

    print('Até mais')


# esse if só é verdade quando o arquivo roda direto e não quando é importado
if __name__ == '__main__':
    main()
