
def calcula_media(notas):
    soma = sum(notas.values())
    media = soma / len(notas)
    return media

alunos = {
    'Aluno_1': {'Matemática': 10, 'Português': 3, 'História': 2},
    'Aluno_2': {'Matemática': 0, 'Português': 8, 'História': 7},
    'Aluno_3': {'Matemática': 3, 'Português': 2, 'História': 3}
}

for aluno, notas in alunos.items():
    media_alunos = calcula_media(notas)
    print(f'O aluno {aluno} obteve média {media_alunos:.2f}')