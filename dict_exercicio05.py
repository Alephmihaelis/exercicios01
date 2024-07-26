'''
Meu códio original:

agenda = dict(Nome_0 = 'João', Telefone_0 = '21 99999-9999', Email_0 = 'emaildojoao@joao')

# Adicionamento dos três amigos
agenda_compl = dict(Nome_1 = 'Maria', Telefone_1 = '21 98888-8888', Email_1 = 'emaildamaria@maria')
agenda_compl2 = dict(Nome_2 = 'Tiago', Telefone_2 = '21 97777-7777', Email_2 = 'emaildotiago@tiago')
agenda_compl3 = dict(Nome_3 = 'José', Telefone_3 = '21 96666-6666', Email_3 = 'emaildojose@jose')

#Junção dos dicionários
agenda_full = {**agenda, **agenda_compl, **agenda_compl2, **agenda_compl3}

# Exibição na tela o telefone do primeiro amigo da agenda.
print(agenda_full['Telefone_0'])
print('='*30)

# Modificação do email do segundo amigo para um novo endereço.
agenda_full['Email_1'] = 'emaildamaria@mariaemailnovo'

# Adicionamento da chave 'cidade' ao dicionário de informações do terceiro amigo, com o valor correspondente à sua cidade natal.
agenda_compl2['Cidade'] = 'Rio de Janeiro'

# Exibição na tela de todas as chaves e valores do dicionário do terceiro amigo.
print(agenda_compl2)
'''

agenda = {}
agenda['João'] = {
    'Telefone': '(21) 1234-5678',
    'Email': 'emaildojoao@joao'
}
agenda['Pedro'] = {
    'Telefone': '(21) 2345-6789',
    'Email': 'emaildopedro@pedro'
}
agenda['Maria'] = {
    'Telefone': '(21) 3456-7890',
    'Email': 'emaildamaria@maria'
}

primeiro_amigo = list(agenda.keys())[0]
print(f'O telefone do primeiro amigo, que é {primeiro_amigo}, é {agenda["João"]["Telefone"]}') # Notei que para acessar a chave do dicionário tive obrigatoriamente de usar aspas duplas em vez de aspas simples.
# Ou: print(f'O telefone do primeiro amigo, que é {primeiro_amigo}, é {agenda[primeiro_amigo]["Telefone"]}')

agenda['Pedro']['Email'] = 'emailpedro2@pedro'
agenda['Maria']['Cidade'] = 'Roma'

for chave, valor in agenda['Maria'].items():
    print(f'{chave}: {valor}')