# Primeiro método de fazer o cálculo da média

print('Vamos calcular a média de três números!')
print('Você pode usar números com vírgula, como 7,3 -- mas lembre-se: para assinalar a casa decimal, use . e não ,!')
# A linha 4 padece do mesmo problema da linha 2 do exercício 5.
num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite outro número: '))
num_3 = float(input('Digite mais um número: '))
print(f'A média de {num_1}, {num_2} e {num_3} é {(num_1 + num_2 + num_3) / 3:.2f}.')

# Segundo método de fazer o cálculo da média

print('Vamos calcular a média de três números!')
valor_1 = float(input('Digite um número: '))
valor_2 = float(input('Digite outro número: '))
valor_3 = float(input('Digite mais um número: '))
s = valor_1 + valor_2 + valor_3
print(f'A média de {s} é {s/3:.2f}')

''' Professor, achei que o segundo método é mais fácil e que ficou mais limpo visualmente.
As strings muito longas deixam o código um pouco feio -- eu o acho.
Sei que a variável "s" usará de mais memória, mas não sei se esse acŕescimo vale a
legibilidade do código. Gostaria da opinião do senhor quanto a isso.
'''