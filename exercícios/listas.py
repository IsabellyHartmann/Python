nums = [2,5,8,11,7,9,13]

# imprimir a lista
print(nums) #[2,5,8,11,7,9,13]

#imprimir um elemento da lista
print(nums[2]) #8

# inserir novo elemento no final da lista
nums.append(17) #[2,5,8,11,7,9,13,17]

# inserir vários elementos no final da lista
nums.extend([12,16]) #[2,5,8,11,7,9,13,17,12,16]

# inserir em posição específica
nums.insert(3,29)#[2,5,8,29,11,7,9,13,17,12,16]

#remover elemento no final da lista
nums.pop() #[2,5,8,29,11,7,9,13,17,12]

# remover elemento de uma posição específica da lista pelo índice
nums.pop(2) #[2,5,8,29,11,7,9,13,17,12]

# remover elemento de uma posição específica da lista pelo valor
nums.remove(17) #[2,5,8,29,11,7,9,13,12]

#nº de elementos da lista
total = len(nums)#8

for n in nums: # para cada elemento da minha linha
    if n<= 10:
        print(n, end=" ")


for indice in range(len(nums)):
    if nums[indice] <= 10:
        print(nums[indice], end=" ")
        