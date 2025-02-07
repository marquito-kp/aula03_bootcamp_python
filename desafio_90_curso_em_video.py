# Desafio 90
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final mostre o conteúdo da estrutura na tela.

alunos ={}

alunos['Nome'] = str(input("Nome do aluno: "))
alunos['Média'] = float(input(f"Média de {alunos['Nome']}: "))

if alunos['Média'] < 6:
    alunos['Situaçao'] = "Reprovado"
else:
    alunos['Situaçao'] = "Aprovado"

for k, v in alunos.items():
    print(f'{k} é igual a {v}')


