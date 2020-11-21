def suma(x,y,z):
    sum = x + y + z
    
    if x == y == z:
        sum = sum * 3
        return sum 

print(suma(1,5,7))
print(suma(7,7,7))