import random
import string

def gerador_senhas(tamanho_senha):

    letras = string.ascii_letters  #Todas as letras minúsculas e maiúsculas
    numeros = string.digits  #Números de 0 a 9
    pontuacoes = string.punctuation  #Simbolos especiais

    caracteres_possiveis = letras + numeros + pontuacoes

    senha = ""

    for i in range(0, tamanho_senha):

        digito = random.choice(caracteres_possiveis)

        senha = senha + digito  #Incrementa um dígito até chegar no tamanho solicitado

    return senha