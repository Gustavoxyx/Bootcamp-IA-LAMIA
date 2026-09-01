# booleano é só True ou False
b1 = True
b2 = False
b3 = True

# o and só dá True se todos forem True
print(b1 and b2 and b3)

# o or dá True se pelo menos um for True
print(b1 or b2 or b3)

# o diferente funciona como ou exclusivo dá True só quando os valores diferem
print(b1 != b2)

# o not inverte o valor
print(not b1)
print(not b2)

# o not b2 vira True então tudo fica True
print(b1 and not b2 and b3)

x = 3
y = 4

# a comparação também vira True ou False então ela acaba entrando  no and
print(b1 and not b2 and x < y)
