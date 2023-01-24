import os
import time

max_plays = 9
player = 1
plays = 0
win = False

board = [
    ["  ", "  ", "  "],
    ["  ", "  ", "  "],
    ["  ", "  ", "  "],
]


option = 0


def game():
    global board
    global plays
    os.system("cls")
    print("   0    1    2")
    print("0 " + board[0][0] + " | ", board[0][1] + " | ", board[0][2])
    print("-----------------")
    print("1 " + board[1][0] + " | ", board[1][1] + " | ", board[1][2])
    print("-----------------")
    print("2 " + board[2][0] + " | ", board[2][1] + " | ", board[2][2])
    print("Total de jogadas: " + str(plays))


def startPlay():
    global plays
    global player
    global max_plays
    print(f"Jogador: {player}")
    if plays < max_plays:
        try:
            if player == 1:
                line = int(input("Linha: "))
                col = int(input("Coluna: "))
                if board[line][col] != "  ":
                    line = int(input("Linha: "))
                    col = int(input("Coluna: "))
                board[line][col] = "X"
                player = 2
                plays += 1

            elif player == 2:
                line = int(input("Linha: "))
                col = int(input("Coluna: "))
                if board[line][col] != "  ":
                    line = int(input("Linha: "))
                    col = int(input("Coluna: "))
                board[line][col] = "O"
                player = 1
                plays += 1
        except:
            print("Jogada inválida! linha ou coluna errada.")
            os.system("pause")


def win_condition():
    global board
    win = False
    characters = ["X", "O"]

    for res in characters:
        win = False
        index_l = 0
        index_c = 0
        while index_l < 3:
            sum_numbers = 0
            index_c = 0
            while index_c < 3:
                if board[index_l][index_c] == res:
                    sum_numbers += 1
                index_c += 1
            if sum_numbers == 3:
                win = res
                break
            index_l += 1
        if win != False:
            break
        index_l = 0
        index_c = 0
        while index_c < 3:
            sum_numbers = 0
            index_l = 0
            while index_l < 3:
                if board[index_l][index_c] == res:
                    sum_numbers += 1
                index_l += 1

            if sum_numbers == 3:
                win = res
                break
            index_c += 1
        if win != False:
            break

        sum_numbers = 0
        index_diag = 0
        while index_diag < 3:
            if board[index_diag][index_diag] == res:
                sum_numbers += 1
            index_diag += 1
        if sum_numbers == 3:
            win = res
            break

        sum_numbers = 0
        index_diagL = 0
        index_diagC = 2
        while index_diagC >= 0:
            if board[index_diagL][index_diagC] == res:
                sum_numbers += 1
            index_diagL += 1
            index_diagC -= 1
        if sum_numbers == 3:
            win = res
            break
    return win


while option != 4:
    print(
        """    [ 1 ] Jogar
    [ 2 ] Como jogar?
    [ 3 ] Regras
    [ 4 ] Sair """
    )
    option = int(input("Escolha uma opção: "))
    if option == 1:
        while True:
            game()
            startPlay()
            game()
            win = win_condition()
            if win != False or plays >= max_plays:

                if win == "X" or win == "O":
                    print("jogador " + win + " ganhou!")
                break
    elif option == 2:
        print("C: 0      1     2")
        print("L: 0 ", board[0][0] + " | ", board[0][1] + " | ", board[0][2])
        print("----------------------")
        print("L: 1 ", board[1][0] + " | ", board[1][1] + " | ", board[1][2])
        print("----------------------")
        print("L: 2 ", board[2][0] + " | ", board[2][1] + " | ", board[2][2])

        print(
            "Você vai escolher a linha desejada e a coluna quando for fazer uma jogada, acima há uma representação de como funciona o tabuleiro do jogo"
        )
    elif option == 3:
        print(
            """- O jogo ocorre em um tabuleiro 3x3;
- O jogo será para duas pessoas jogarem, alternadamente;
- O jogador 1, sempre será o X e sempre iniciará o jogo;
- O jogador 2, sempre será a O e sempre será o segundo a jogar;
- O jogo pode ter 3 resultados: vitória do jogador 1, vitória do jogador 2 ou empate;
- Ganha o jogador que primeiro formar uma reta na diagonal, vertical ou horizontal do tabuleiro;"""
        )
    elif option == 4:
        print("Saindo...")
    else:
        print("Escolha uma opção valida!")
    time.sleep(2)
print("Fim de jogo")
