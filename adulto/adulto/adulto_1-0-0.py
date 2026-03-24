"""
Programa adulto
Descrição: Este programa pergunta a idade de uma pessoa. Se a idade for menor de 13 anos, imprima na tela "Oi! Você é uma criança.".
Se a idade for de 13 a 17, imprima "Oi! Você é um adolescente". Se for maior de 18, imprima "Oi! Você é um adulto.". 
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
    
elif idade > 13 and idade <= 17:
    texto = "Oi! Você é um adolescente."

else:
    texto = "Oi! Você é uma criança."

# Saída de dados 

print(texto)