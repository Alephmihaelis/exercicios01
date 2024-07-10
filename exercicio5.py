info_1 = int(input('Digite um número inteiro: '))
info_2 = float(input('Digite um número com vírgula, MAS SUBSTITUA A VÍRGULA POR PONTO!: '))
'''
Na linha 2, achei bom pôr aquele aviso, porque o Python não aceita vírgulas.
Não é tão intuitivo para o usuário brasileiro -- mas também não é impossível
de se realizar.
'''
info_3 = str(input('Digite uma palavra: '))

print(f'O tipo de "{info_1}" é {type(info_1)}')
print(f'O tipo de "{info_2}" é {type(info_2)}')
print(f'O tipo de "{info_3}" é {type(info_3)}')