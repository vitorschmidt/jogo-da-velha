import time
import os


maxPlays=9
player=1
plays=0
win="n"

board = [
    ["  ","  ","  "],
    ["  ","  ","  "],
    ["  ","  ","  "],
]

option = 0

def game():
        global board
        global plays
        os.system('cls')
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
    global maxPlays
    print(f"Jogador: {player}")
    try: 
        line=int(input("Linha: "))
        col=int(input("Coluna: "))
        if player==1 and plays<maxPlays:
            board[line][col]="X"
            player=2
            plays+=1
        elif player==2 and plays<maxPlays:
            board[line][col]="O"
            player=1
            plays+=1  
    except:
        print("Jogada inválida! linha ou coluna errada.")    
        os.system("pause")

def winCondition():
    global board
    win = "n"
    chacters= ["X", "O"]

    for res in chacters:
        win="n"
        indexL = 0
        indexC = 0
        while indexL < 3:
            sumNumbers = 0
            indexC = 0
            while indexC < 3:
                if(board[indexL][indexC] == res):
                    sumNumbers+=1
                indexC+=1
            if(sumNumbers==3):
                win = res
                break
            indexL+=1
        if(win!="n"):
            break
        while indexC < 3:
            sumNumbers = 0
            indexL = 0
            while indexL < 3:
                if(board[indexL][indexC] == res):
                    sumNumbers+=1
                indexL+=1
            
            if(sumNumbers==3):
                win = res
                break
            indexC+=1
        if(win!="n"):
            break

        sumNumbers=0
        indexDiag = 0
        while indexDiag < 3:
            if(board[indexDiag][indexDiag] == res):
                sumNumbers+=1
            indexDiag+=1
        if(sumNumbers==3):
            win = res
            break

        sumNumbers=0
        indexDiagL = 0
        indexDiagC = 2
        while indexDiagC >= 0:
            if(board[indexDiagL][indexDiagC] == res):
                    sumNumbers+=1
            indexDiagL+=1
            indexDiagC-=1
        if(sumNumbers==3):
            win = res
            break  
    return win                   


while option != 4:
    print('''    [ 1 ] Jogar
    [ 2 ] Como jogar?
    [ 3 ] Regras
    [ 4 ] Sair ''')
    option = int(input('Escolha uma opção: '))
    if option == 1:
        while True:
            game()
            startPlay()
            game()
            win=winCondition()
            if win!= "n" or plays >= maxPlays:
            
                if win=="X" or win=="O":
                    print("jogador "+ win + " ganhou!")
                break
    elif option == 2:
        print("C: 0      1     2")
        print("L: 0 ",  board[0][0] + " | ", board[0][1] + " | ", board[0][2])
        print("----------------------")
        print("L: 1 ",  board[1][0] + " | ", board[1][1] + " | ", board[1][2])
        print("----------------------")
        print("L: 2 ",  board[2][0] + " | ", board[2][1] + " | ", board[2][2])

        print("Você vai escolher a linha desejada e a coluna quando for fazer uma jogada, acima há uma representação de como funciona o tabuleiro do jogo")
    elif option == 3:
        print('''- O jogo ocorre em um tabuleiro 3x3;
- O jogo será para duas pessoas jogarem, alternadamente;
- O jogador 1, sempre será o X e sempre iniciará o jogo;
- O jogador 2, sempre será a O e sempre será o segundo a jogar;
- O jogo pode ter 3 resultados: vitória do jogador 1, vitória do jogador 2 ou empate;
- Ganha o jogador que primeiro formar uma reta na diagonal, vertical ou horizontal do tabuleiro;''') 
    elif option == 4:
        print("Saindo...") 
    else:
        print("Escolha uma opção valida!")   
    time.sleep(2)        
print("Fim de jogo")


 
