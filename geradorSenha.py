import random
import string

def geradorSenha(tamanhoSenha =8):
    caracteres = string.ascii_letters #pega todas as letras, maiusculas e minusculas
    numeros = string.digits #pega todas os digitos(numeros)
    pontuacao = string.punctuation #pega todos os caracteres especiais
    baseSenha = pontuacao+numeros+caracteres

    senha = ""
    
    for i in range(0, tamanhoSenha):
        digito = random.choice(baseSenha)
        senha = senha+digito
    
    return senha

tamanoSenha = int(input("   Digite o tamanho da senha: "))

print(f"\n\n   Sua nova senha é: {geradorSenha(tamanoSenha)}\n")

input()