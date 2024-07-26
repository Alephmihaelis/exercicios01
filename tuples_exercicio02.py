
frutas = ('Banana', 'Maçã', 'Laranja')
lgms = ('Tomate', 'Cenoura', 'Batata')
mercado = frutas + lgms

if 'Laranja' in mercado:
    print('Sim, "Laranja" está na lista.')
else:
    print('Não, "Laranja" não está na lista.')

if 'Alface' in mercado:
    print('Sim, "Alface" está na lista.')
else:
    print('Não, "Alface" não está na lista.')

print(f' O último item da lista é {mercado[-1]}.')