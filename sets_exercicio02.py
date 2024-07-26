
numeros1 = {2, 4, 6, 8, 10}
numeros2 = {1, 3, 5, 7, 9}
print(f' A união dos conjuntos "numeros1" e "numeros2" é {numeros1.union(numeros2)}')
print(f' A intersecção dos conjuntos "numeros1" e "numeros2" é {numeros1.intersection(numeros2)}')
print(f' A diferença desses dois conjuntos é {numeros1.difference(numeros2)}')
print('Os conjuntos "numeros1" e "numeros2" são iguais?', numeros1 == numeros2)
primos = {2, 3, 5, 7}
print(f'O conjunto "primos" é um subproduto de "numeros1"? {primos.issubset(numeros1)}')

#print(numeros1 & numeros2) -> Segundo método para fazer a intersecção
#print(numeros1 - numeros2) -> Segundo método para exibir a diferença dos conjuntos
#print(primos <= numeros1) -> Segundo métdo para saber se um conjunto é subproduto do outro