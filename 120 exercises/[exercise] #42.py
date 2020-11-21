def permutaciones(nums):
    resultado = [[]]
    for n in nums :
        nPermutaciones = []
        for perm in resultado:
            for i in range(len(perm)+1):
                nPermutaciones.append(perm[:i] + [n] + perm[i:])
                resultado = nPermutaciones
            return resultado


my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))