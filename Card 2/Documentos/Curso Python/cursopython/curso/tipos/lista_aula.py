# a lista usa colchetes e isso pode mudar depois
nums = [1, 2 , 3]
print(type(nums))

# o append põe o item no final
nums.append(3)
# a lista aceita repetido diferente do conjunto
nums.append(4)
nums.append(500)
# o len conta os itens
print(len(nums))

# o in pergunta se o valor existe na lista
print(2 in nums)

# a contagem começa no 0 então esse é o quarto item
nums[3] = 100
# o insert põe na posição e empurra o resto
nums.insert(0, -200)

# pegando o item da posição 6
print(nums[6])

# número negativo conta de trás pra frente então o -1 e será o último
print(nums[-1])

# o -2 é o penúltimo
print(nums[-2])

# mostrando a lista toda pra conferir
print(nums)
