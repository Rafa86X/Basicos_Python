import random

def iniciaGame():
    print("\n\n-----------------------> <><><><><><><><><><> <-----------------------")
    print("\n\n            Bem vindo ao PEDRA, PAPEL e TESSOURA\n\n")
    print("----------------------> <><><><><><><><><><> <-----------------------")
    if input("\n\nPrescione S para começar!, ou qualquer letra para encerrar.\n\n") == 's':
        print("\n\n###############################################################")
        pedraPapelTessoura()
    else:
        encerraGame()

def encerraGame():
        print("\n\nAté a proxima!\n\n")
        input()
        exit()

def juiz(pontosConsole,pontosPlayer):
     print("\n\n-----------------------> Resultado <-----------------------\n\n")
     if pontosConsole>pontosPlayer:
           print("--------> Você Perdeu Pra Mim! - kkkkkkkkkkk <---------")
     elif pontosConsole<pontosPlayer:
           print("--------> Você me derrotouuu Aaaaaaaaaaaaaaaaaaaaa <---------")
     else:
         print("--------> Empatamos! <---------")
     print(" \n\n -----------> O total de pontos do Console: ", str(pontosConsole))
     print(" \n\n -----------> O total de pontos do Payer: ", str(pontosPlayer))
     print("\n\n###############################################################")
     encerraGame()
      

def jogo():
     pontosConsole = 0
     pontosPlayer = 0
     rodada = 0
     jogada_console = {0:"p",1:"k",2:"t"}
     jogada_empate = {0:"Pedra x Pedra",1:"Papel x Papel",2:"Tessoura x Tessoura"}

     while rodada < 5:
        sorteiajogada = random.randint(0,2)
        jogada_Player = input("\nBatalha, P - Pedra, k - Papel ou T para Tessoura... ")

        if(jogada_Player  == jogada_console[sorteiajogada]):
                print(f'\nEmpate em {jogada_empate[sorteiajogada]}\n\n')

        elif(jogada_Player == 'p' and jogada_console[sorteiajogada]=='k'):
                print("\nVitória do Console Pedra X Papel\n\n")
                pontosConsole = pontosConsole +1

        elif(jogada_Player == 'p' and jogada_console[sorteiajogada]=='t'):
                print("\nVitória do Player Pedra X Tessoura\n\n")
                pontosPlayer = pontosPlayer + 1

        elif(jogada_Player == 'k' and jogada_console[sorteiajogada]=='p'):
                print("\nVitória do Player Papel X Pedra\n\n")
                pontosPlayer = pontosPlayer + 1

        elif(jogada_Player == 'k' and jogada_console[sorteiajogada]=='t'):
                print("\nVitória do Console Papel X Tessoura\n\n")
                pontosConsole = pontosConsole +1

        elif(jogada_Player == 't' and jogada_console[sorteiajogada]=='p'):
                print("\nVitória do Console Tessoura X Pedra\n\n")
                ppontosConsole = pontosConsole +1

        elif(jogada_Player == 't' and jogada_console[sorteiajogada]=='k'):
                print("\nVitória do Player Tessoura x Papel\n\n")
                pontosPlayer = pontosPlayer + 1
        rodada = rodada + 1
     juiz(pontosConsole,pontosPlayer)
          
          

def pedraPapelTessoura():
     print("\n\nQuero ver você me ganhar no Pedra Papel e Tessoura!\n\n        VALENDOOO!!   \n\n")
     print("Digite:\n\nP - Pedra,\n\nK - Papel\n\nT - Tessoura\n\nQualquer outra letra para Sair.\n")         
     jogo()
     

iniciaGame()