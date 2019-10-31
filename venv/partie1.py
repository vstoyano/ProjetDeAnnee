import os

def init_mat(m, n):
    matrice = [[" " for a in range(n)] for i in range(m)]
    return matrice
# l'initiation de la matrice
def afficher(M):
    ''''if(os.name=="posix"):
        os.system('clear')
    elif(os.name=="nt"):
        os.system('cls')'''''

    for i in range(len(M)):
        print(len(M)-i, end='')
        print(" ", end='')
        for j in range(len(M[i])):
            print(M[i][j], end='')
            print(" ", end='')
        print("")
    print('  A B C D')
    return None

def Mettre(M,pos,player):
    flag=False
    if (pos[0]=="A" or pos[0]=="B" or pos[0]=="C" or pos[0]=="D") and (pos[1]=="1" or pos[1]=="2" or pos[1]=="3" or pos[1]=="4") and len(pos)==2:
        if M[4 - int(pos[1])][ord(pos[0]) - 65]==player:
            print('cette case est déjà de votre couleur')
        elif M[4 - int(pos[1])][ord(pos[0]) - 65]=="_":
            M[4 - int(pos[1])][ord(pos[0]) - 65]=player
            flag=True
        else:
            print("ce coup vient d’être joué")
    else:
        print ('commande invalide')
    if not flag:
        if player == "X":
            print("joueur 1 > ")
        elif player == "O":
            print("joueur 2 > ")
        pos = input()
        Mettre(M, pos, player)

    return None

def HorizontalLine(M,player1,player2):
    for i in range(len(M)):
        if M[i][0]==player1 and M[i][1]==player1 and M[i][2]==player1 and M[i][3]==player1:
            return True, player1
        elif M[i][0]==player2 and M[i][1]==player2 and M[i][2]==player2 and M[i][3]==player2:
            return True, player2
        else:
            return False ,"none"

def VerticalLine(M,player1,player2):
    for i in range(len(M[0])):
        if M[0][i]==player1 and M[1][i]==player1 and M[2][i]==player1 and M[3][i]==player1:
            return True, player1
        elif M[0][i]==player2 and M[1][i]==player2 and M[2][i]==player2 and M[3][i]==player2:
            return True, player2
        else:
            return False, "none"

def TopLeftDiagonale(M,player1,player2):
    for i in range(len(M)):
        if M[i][i]==player1:
            return True, player1
        elif M[i][i]==player1:
            return True, player2
        else:
            return False, "none"

def TopRightDiagonale(M,player1,player2):
    for i in range(len(M)-1,-1,-1):
        if M[i][i]==player1:
            return True, player1
        elif M[i][i]==player1:
            return True, player2
        else:
            return False, "none"

def IsThereAnUnplayedSpace(M):
    flag=False
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]=="_":
                flag=True
    return flag
def WinningSituation(M,player1,player2):
    if HorizontalLine(M,player1,player2)[0] or VerticalLine(M,player1,player2)[0] or TopLeftDiagonale(M,player1,player2)[0] or TopRightDiagonale(M,player1,player2)[0]:
       return True
    else: return False


def boucle_jeu():
    board = init_mat(4,4)
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j]="_"
    afficher(board)
    player1="X"
    player2="O"
    while not WinningSituation(board,player1,player2):
        if IsThereAnUnplayedSpace(board):
            print("joueur 1 > ")
            Player1move=input()
            Mettre(board,Player1move,player1)
            afficher(board)
            if WinningSituation(board, player1, player2):
                if HorizontalLine(board, player1, player2)[1] == player1:
                    print("joueur 1 gagnant")
                    break
                if VerticalLine(board, player1, player2)[1] == player1:
                    print("joueur 1 gagnant")
                    break
                if TopRightDiagonale(board, player1, player2)[1] == player1:
                    print("joueur 1 gagnant")
                    break
                if TopLeftDiagonale(board, player1, player2)[1] == player1:
                    print("joueur 1 gagnant")
                    break

            print("joueur 2 > ")
            Player2move = input()
            Mettre(board, Player2move, player2)
            afficher(board)
            if WinningSituation(board, player1, player2):
                if HorizontalLine(board, player1, player2)[1] == player2:
                    print("joueur 2 gagnant")
                    break
                if VerticalLine(board, player1, player2)[1] == player2:
                    print("joueur 2 gagnant")
                    break
                if TopRightDiagonale(board, player1, player2)[1] == player2:
                    print("joueur 2 gagnant")
                    break
                if TopLeftDiagonale(board, player1, player2)[1] == player2:
                    print("joueur 2 gagnant")
                    break
        else:
            break
            print("Partie nulle")






    return None

if __name__ == '__main__':
    boucle_jeu()