minha_tupla = ('Vermelho', 'Laranja', 'Amarelo', 'Verde', 'Azul', 'Anil', 'Violeta')
print(minha_tupla[3])

# minha_tupla[4] = "Marrom" ----- Este código gera um erro, porque as tuplas são imutáveis.

cores_invertidas = tuple(reversed(minha_tupla))
print(cores_invertidas)

# Método alternativo para inverter a tupla -> cores_invertidas = minha_tupla[::-1]
