x = 0
# o while repete enquanto a condição for verdade então só para quando digitar -1
while x != -1:
    x = float(input('Informe o número ou -1 para sair: ' ))

print('Fim!')

# essas variáveis acumulam a soma e a quantidade de notas
total = 0
qtde = 0
nota = 0
while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    # o -1 é só o aviso de parada então não entra na conta
    if nota != -1:
        qtde += 1
        total += nota

x = 10
# enquanto x não for zero o laço continua porque zero é falso
while x:
    print(x)
    # sem esse decremento o laço nunca termina
    x -= 1

print('Fim!')
