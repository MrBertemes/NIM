def usuario_escolhe_jogada(n, m):
    if n<=0:
        pass
    else:
        aux = True  # Varialvel para criar um laco
        while aux: # Laco
            escolha = int(input("Quantas peças você vai tirar? "))
            if (escolha <= m)and (escolha>0): # Validando a entrada do usuario
                aux = False #Quebrando o laco
                if escolha == 1:
                    print("Você tirou uma peça") # Printando se tirou 1
                else:
                    print("Você tirou %i peças" %escolha) #Printando se tirou mais que 1
                return escolha # Retorna quanto o usuario tirou
            else:
                print("\nOops! Jogada inválida! Tente de novo\n") # Resposta invalida
    pass

def computador_escolhe_jogada(n, m):
    escolha = 1 # Define a escolha minima da maquina
    while((n-escolha) % (m+1) !=0 )and(escolha<m)and(escolha>0): # Entra em um laco
        escolha = escolha + 1 # Ao comprir cumprir com os requisitos sai do laco

    if escolha == 1:
        print("O computador tirou uma peça") # Printando se tirou 1
    else:
        print("O computador tirou %i peças" %escolha) # Printando se tirou mais que 1
    return escolha # Retorna a escolha da maquina
    pass

def atualiza_tabuleiro(n):# Resolvi criar essa função facilitar minha vida na funcão partida()
    if n<=0:
        pass
    else:
        if n == 1:
            print("Agora resta uma peça no tabuleiro\n")
        else:
            print("Agora restam %i peças no tabuleiro\n" %n)
        return n

def partida():
    escolha = 0
    n = int(input("Quantas peças? "))  # Quandtidade de peças em jogo
    m = int(input("Limite de peças? ")) # Limite de peças a serem tiradas por rodada
    if n % (m + 1)==0 : # Verificando a condicao de vitoria, assim vendo quem começa (VOCE)
        print("\nVoce começa!\n")
        while n > 0: # Um laco para realizar uma repeticao
            escolha = usuario_escolhe_jogada(n, m) # Coloca a escolha em uma variavel e roda a funcao usuario_escolhe_jogada(n, m)
            if n<=0:
                pass
            else:
                n = n - escolha # Tira a quandtidade escolhida pela usuario do valor inicial
            atualiza_tabuleiro(n) # Funcao que printa a altual quantidade de peças
            escolha = computador_escolhe_jogada(n, m) # Ocorre os mesmo da variavel escolha acima, so que com o a funcao computador_escolhe_jogada(n, m)
            if n<=0:
                pass
            else:
                n = n - escolha # Tira a quantidade escolhida pelo computador da restante de peças
            atualiza_tabuleiro(n)# Atualiza a quantidade de peças
        print("Fim de jogo! O computador ganhou!\n")
    else: # (COMPUTADOR) - Tudo igual ao do VOCE so invertendeo a ordem
        print("\nComputador começa!\n")
        while n > 0 :
            escolha = computador_escolhe_jogada(n, m)
            if n<=0:
                pass
            else:
                n = n - escolha
            atualiza_tabuleiro(n)
            escolha = usuario_escolhe_jogada(n, m)
            if n<=0:
                pass
            else:
                n = n - escolha
            atualiza_tabuleiro(n)
        print("Fim de jogo! O computador ganhou!\n")

def campionato():
    print("**** Rodada 1 ****\n")
    partida() # Chama funcao partida
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("**** Final de campionato! ****\n")
    print("Placar: Você 0 X 3 Computador")

def main():
        print("Bem-vindo ao jogo do NIM! Escolha:\n")
        x = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campionato "))
        if x == 1:
            print("Voce escolheu uma partida isolada!\n")
            partida()
        else:
            print("\nVoce escolheu um campionato!\n")
            campionato()

main()
