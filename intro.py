import os
from random import randint
from modulos.biblioteca import z

#x = 5
#print(f"O valor de x é{x}")

#for _ in range(5):
 #   y = randint(5,12)
  #  print(y)

#x = y + z
#print(f"aa:{x}")


texto = "Isabelly Hartmann Lopes Gonçalves"
num_vogais = 0

for letra in texto:
    if letra.upper() in "AEIOU":
        num_vogais += 1
print(num_vogais)