
letras = {'a', 'e', 'i', 'o', 'u'}
print(f' O tamanho do conjunto letras é: {len(letras)}')
letras.add('b')
print('A vogal "i" está presente no conjunto letras?', 'i' in letras)
letras.remove('b')

consoantes = {'b', 'd', 'f'}
print('O conjunto "consoantes" está contido no conjunto "letras"?', consoantes.issubset(letras))

letcon = letras.union(consoantes)
print(f' A união dos conjuntos "letras" e "consoantes" é {letcon}')