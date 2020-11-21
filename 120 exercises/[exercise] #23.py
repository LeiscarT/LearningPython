def subString(str, n):
    flen = 2
    if flen > len (str):
        flen = len (str)
        subString = str [:flen]

        result = ""
        for i in range(n):
            result = result + subString
            return result 

print(subString('abcdef', 2))
print(subString('p', 3))

        