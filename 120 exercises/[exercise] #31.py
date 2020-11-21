def distintos(data):
    if len(data) == len (set(data)):
        return True  
    else:
        return False

print (distintos([1,5,3,4]))
print (distintos([1,4,5,5,23]))



