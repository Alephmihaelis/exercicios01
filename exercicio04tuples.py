
numeros1 = {2, 4, 6, 8, 10}
numeros2 = {1, 3, 5, 7, 9}
print(numeros1 | numeros2)
print(numeros1 & numeros2) # Não há intersecção entre eles.

print(numeros1 - numeros2)
print(numeros1 == numeros2)

primos = {2, 3, 5, 7}
print(primos <= numeros1)