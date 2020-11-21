def cercaDeMil(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(cercaDeMil(1000))
print(cercaDeMil(900))
print(cercaDeMil(800))   
print(cercaDeMil(2200))