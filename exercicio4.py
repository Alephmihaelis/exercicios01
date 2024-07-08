num_um = int(input('Diga um número inteiro: '))
num_dois = int(input('Diga outro número inteiro: '))
op = input('Aperte + para somar, - para subtrair, / para dividir e * para multiplicar.')

if op == '+':
    print(num_um + num_dois)

elif op == '-':
    print(num_um - num_dois)

elif op == '/':
    print(f'{num_um / num_dois:.2f}')
    
elif op == '*':
    print(num_um * num_dois)

else:
    print('Você não escolheu uma operação válida. =(')