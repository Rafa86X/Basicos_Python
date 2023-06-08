import random

Questao_1 = ['Na fase de levantamento de dados para sistemas de informação, a técnica que é executada emgrupo com o objetivo de gerar o maior número possível de ideias denomina-se:',
             'brainstorming.',
             'prototipagem.',
             'questionário.',
             'Delphi.',
             'entrevista.'
             ]
Questao_2 = ['Assinale a afirmação verdadeira.',
             'Cascata, incremental, espiral e evolutivo são alguns dos modelos de ciclos de vida adotados no desenvolvimento de um software.',
             'As técnicas modernas de engenharia de software são completamente incompatíveis com a filosofia ágil e/ou com equipes auto-gerenciáveis.',
             'Arquitetura de software define as técnicas de desenvolvimento para um hardware específico, por exemplo, se o processador é RISC ou CISC, 32 ou 64 bits, quais são os limites de memória (primária e secundária) etc.',
             'Do ponto de vista da engenharia de software, um bom ambiente de desenvolvimento de software é fisicamente ergonômico, com flexibilidade de turnos/horário de trabalho, e naturalmente gera criatividade através de um grande apelo lúdico para que as melhores soluções sejam encontradas pela equipe.',
             'Uma efetiva gerência de software consiste em um organograma com vários níveis hierárquicos muito bem definidos, composto por diretores, gerentes, chefes, desenvolvedores, analistas e administradores (de banco de dados, de rede, de servidores de aplicação etc).'
             ]

Questao_3 = ['Existem dois tipos de padrões de engenharia de software que podem ser definidos e usados no gerenciamento de qualidade de software. São eles:',
             'Padrões de produto e Padrões de processo.',
             'Padrão de Imagem e Padrão de Vídeo.',
             'Padrão de documentação e Padrão de uso.',
             'Padrão de tela e Padrão de Interface.',
             'Padrão de reutilização de código e Padrão de análise de código.',
             ]
Questao_4 = ['Scrum, Extreme Programming e Lean, são exemplos de:',
             'metodologias ágeis.',
             'projeto estruturado.',
             'programação estruturada.',
             'business intelligence.',
             'projeto conceitual.',
             ]
Questao_5 = ['Em um modelo DevOps existe um método para entregar aplicações com frequência aos clientes, visando integração, entrega e implantação contínuas. Chamamos esse método de:',
             'CI/CD',
             'git',
             'pipeline',
             'flowchar',
             'reentrante',
             ]

def embaralha_respostas_das_Questoes(pergunta = []):
    respCorreta=pergunta[1]
    print("\n",pergunta[0], "\n")
    pergunta.pop(0)
    random.shuffle(pergunta)
    random.shuffle(pergunta)
    print("A - ",pergunta[0])
    print("B - ",pergunta[1])
    print("C - ",pergunta[2])
    print("D - ",pergunta[3])
    print("E - ",pergunta[4])
    print('\n')
    i=0
    for p in pergunta:
        if p==respCorreta:
            return i
        else:
            i=i+1

def questionador():
   Questoes=[Questao_1,Questao_2,Questao_3,Questao_4,Questao_5]
   random.shuffle(Questoes)
   random.shuffle(Questoes)
   i=0
   nota = 0
   while i < 5:       
        respCorreta =  embaralha_respostas_das_Questoes(Questoes[i])
        dicionarioDeResposta = {0:'a',1:'b',2:'c',3:'d',4:'e'}
        RespostaDoUsuario = input()
        if(RespostaDoUsuario==dicionarioDeResposta[respCorreta]):
            print("Parabens, resposta certa!")
            nota = nota+1
        else:
            print("Errouuuu!, otário kkkkkkk!!")
        i = i + 1    

   print('\n')   
   print(f'Fim de Jogo !! Voçe acertou {(nota/5)*100}% das questões.')
   print('\n')
   input()

def iniciaGame():
    print("\n\n\nBem vindo ao Quiz\n\n")
    if input("Prescione S para começar!, ou qualquer letra para encerrar.\n\n") == 's':
        questionador()
    else:
        print("\n\nAté a proxima!\n\n")
        input()

iniciaGame()
