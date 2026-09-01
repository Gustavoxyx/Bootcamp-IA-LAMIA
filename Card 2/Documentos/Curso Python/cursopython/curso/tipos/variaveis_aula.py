# esse é int
a = 3

# esse é float
b = 4.4

# int mais float dá float
print(a + b)

texto = 'Sua idade é...'
idade = 23

# o f na frente troca as chaves pelo valor da variável
print(f'{texto}')

# dentro das chaves dá pra fazer conta
print(f'{texto} {12 + 13}')

print(f'{texto} {idade}')

# texto vezes número repete o texto
print(3 * 'bom dia ')

saudacao = 'bom dia '
print(3 * saudacao)

# constante em maiúsculo é só um combinado,e a linguagem no caso seria o python acaba deixando trocar mesmo assim
PI = 3.14
PI = 3.1415

# o input vem como texto então o float converte
raio = float(input('Informe o raio da circ? '))

# conferindo que agora o tipo é float
print(type(raio))

# o pow eleva o raio ao quadrado
area = PI * pow(raio, 2)
print(area)
print(f'A área da circ é {area} m2.')
