"""
Programa adulto
Descrição: Este programa pergunta a idade de uma pessoa. Se a pessoa for maior do que 18 anos, o programa imprime 
na tela "Oi! Você é uma adulto.". Caso contrário, imprima "Oi! Você é menor de idade.".
Autor: Mariana Meller Jost
Data: 24/03/2026
Versão: 0.1.0

"""


# Alocação de memória 

idade = 0

texto = ""


# Entrada de dados

idade = int(input("\nQual é a sua idade?"))


# Processamento de dados 

if idade >= 18:
    texto = "Oi! Você é um adulto."

else:
    texto = "Oi! Você é menor de idade."

# Saída de dados 

print(texto)