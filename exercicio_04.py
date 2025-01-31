### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

import re

idade = int(input("Digite sua idade: "))
email = input("Digite o seu e-mail: ")

padrao = r'\^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z|A-Z]{2,7}\$'

if re.match(padrao,email) and idade >= 18 and idade <= 65:
    print("Dados corretos!")
else:
    print("Dados incorretos!")