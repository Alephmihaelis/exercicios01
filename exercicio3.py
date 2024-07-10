temp_c = float(input('Diga uma temperatura em ºC: '))
# temp_f = temp_c*9/5 + 32
# Em Python, a variável temp_f é desnecessária: é possível fazer a conta diretamente na função print.
print(f'A conversão de {temp_c:.2f}ºC em Fahrenheit é {temp_c * 9 / 5 + 32:.2f}°F.')