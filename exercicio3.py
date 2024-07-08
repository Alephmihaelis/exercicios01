temp_c = float(input('Diga uma temperatura em ºC: '))
# temp_f = temp_c*9/5 + 32
# Em Python, a linha 2 é desnecessária: é possível fazer a conta diretamente na função PRINT.
print(f'A conversão de {temp_c:.2f}ºC em Fahrenheit é {temp_c * 9 / 5 + 32:.2f}°F.')