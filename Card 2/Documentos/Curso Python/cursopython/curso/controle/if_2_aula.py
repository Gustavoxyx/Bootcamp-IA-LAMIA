# texto com conteúdo é verdadeiro, então o not vira False
print (not 'valor')

# aplicando o not duas vezes a gente volta pro valor original
print(not not 'valor')

# daqui pra baixo a ideia é ver o que o Python considera de verdadeiro ou falso
a = 'valor'
# texto com conteúdo é verdadeiro
if a:
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')

a = 0
# o zero é falso
if a:
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')

a = -0.00001
# qualquer número diferente de zero é verdadeiro mesmo sendo negativo
if a:
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')

a = ''
# texto vazio é falso
if a:
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')

a = ' '
# esse texto tem um espaço, então não está vazio então é verdadeiro
if a:
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')

a = []
# lista vazia é falsa
if a:
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')

a = {}
# dicionário vazio também é falso
if a:
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')
