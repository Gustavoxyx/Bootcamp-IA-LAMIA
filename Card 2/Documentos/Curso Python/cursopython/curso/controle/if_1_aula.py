# o input vem como texto, então o float el converte para número
nota = float(input('Informe a nota do aluno: '));

# esse é o ternário, se digitou s vira True senão vira False
comportado = True if input('Comportado (s/n): ') == 's' else False

# o and exige que as duas condições sejam verdade
if nota >= 9 and comportado:
    print('Duas palavras: para bens! :P')
    print('Quadro de Honra')
# o elif só é testado se o de cima der falso
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperação')
elif nota >= 3.5:
    print('Recuperação + Trabalho')
# o else é quando nada acima bateu
else :
    print('Reprovado')
print(nota)
