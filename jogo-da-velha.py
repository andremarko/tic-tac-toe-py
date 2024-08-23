import functions

tab = functions.criaTabuleiro()
player = 'X'
while functions.temEspaco(tab) and not functions.haGanhador(tab):
    functions.imprime(tab)
    print("Vez do jogador: ", jogador)
    lin = int(input("Linha:"))
    col = int(input("Coluna:"))
    resp = functions.joga(tab, lin, col, player)
    if resp == True:
        player = functions.trocaJogador(player)
    else:
        print("Jogada inválida, tente novamente")
     