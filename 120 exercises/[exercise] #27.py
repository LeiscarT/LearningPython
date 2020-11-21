def concatenar (list):
    result = ''
    for element in list:
        result += str(element)
    return result

print(concatenar([1,5,3,56,6,2,4]))