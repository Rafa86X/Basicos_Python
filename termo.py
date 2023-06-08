import random
import json

f = open("termoJSON.json", encoding="utf8")
frases = json.load(f)

fraseSorteada = random.choice(list(frases.keys()))
print(fraseSorteada)

dica = frases[fraseSorteada]
tamanhoDica = len(fraseSorteada)
tentativa = 1
vitoria = False

print(f'\n  Com {tamanhoDica} letras, {dica}  \n')

avaliacao = []

def testaTamanhoDigitado(fraseDesavio):
    controle = False
    
    while controle == False:
        digitadoUsusario = input("Digite sua resposta: ")
        if len(digitadoUsusario) != len(fraseDesavio):
            print(f"\n A palavra tem exatamente {tamanhoDica} letras! \n")
        else:
            controle = True
            return digitadoUsusario
            


def testaDigitado(palavraUsuario, fraseDesavio):
    pontos = 0
    avaliacao = []
    for p in range(0, len(palavraUsuario)):
        if palavraUsuario[p] == fraseDesavio[p]:
            avaliacao.append("✅")
            pontos=pontos+1
        else:
            avaliacao.append("💢")
    print(f"\n\n------------< TENTATIVA {tentativa} de 5 >------------")
    print("\n")
    print(" | ".join(palavraUsuario))
    print(" |".join(avaliacao))
    print("######################################\n\n")

    return pontos


def f_vitoria():
    print(f"\n    PARABÉNS! a palavar era {fraseSorteada}\n\n")
    input()
    quit()
 
while tentativa < 6:

    inputAPROVADO = testaTamanhoDigitado(fraseSorteada)
    pontos = testaDigitado(inputAPROVADO,fraseSorteada)
    if(pontos == len(fraseSorteada)):
        f_vitoria()
    tentativa = tentativa+1


print(f"\n    VC PERDEU! a palavar era {fraseSorteada}\n\n")

input()



