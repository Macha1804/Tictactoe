from affichage_tictactoe import display_board


def init_board():
    list_principale = [[" "," "," "],
                       [" "," "," "],
                       [" "," "," "]]
    return list_principale



def switch_player(player):
    if player == "X":
        return "O"
    if player == "O":
        return "X"

def play_move(board, player, position):
    # position =(0,0)
    # j'ecris un exemple de valeur qui peuvent prendre
    #[[" ","X"," "],[" "," "," "],[" "," "," "]]
    #2,2 utilisateur => valeur python 1,1
    # player = switch_player
    # board[1][0]
    # position(board[1],board[1][0])
    # position = input_user()
    # X = position[0]
    # Y = position[1]
    #je sais à quelle joueur je me retrouve
    # player = switch_player()
    #je récupère ma position
    # position = input_user()
    X = position[0]
    Y = position[1]
    #j'indique à l'ordinateur où le coup du joueur doit être positionner
    board[Y][X]= player


def valider_position(position,board):
    coordonnees_valides = ["1","2","3"]
    position = position.split(",")
    #je vérifie que les valeurs dans ma position corresponde à des entiers
    for valeur in position:
        if valeur not in coordonnees_valides:
            return False
    X = int(position[0]) - 1
    Y = int(position[1]) - 1
    if board[Y][X] != " ":
        return False
    else:
        return True


def input_user(board):
    position = input("Entrez votre position: ")
    while valider_position(position,board)== False:
        position = input("Entrez votre position: ")
    #"2,2"
    position = position.split(",")
    X,Y = position #X vaut le premeier élément de position mais cela ne va pas changer position
    # X = position[0]
    # Y = position[1]
    X = int(X)
    Y = int(Y)
    X = X-1
    Y = Y-1
    return [X,Y]

    #position_a_jouer.append(position)




def check_rows(board, player):
    for rows in board:
        if rows[0] == player and rows[1] == player and rows[2] == player :
            return True
    return False


def check_columns(board, player):
    for i in range(0,3,1):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False

def check_diagonales(board, player):
    return ((board[0][0] == player and board[1][1] == player and board[2][2] == player) or
            (board[0][2] == player and board[1][1] == player and board[2][0] == player))
#Ici, je demande est ce que je t'ai mis entre parenthèses c'est vrai ou faux

def check_winner(board, player):
    return check_rows(board, player) or check_columns(board, player) or check_diagonales(board, player)

def check_draw(board, player):
    for row in board:
        for case in row:
            if case == " ":
                return False
    return check_winner(board, player) == False


def playgame():
    board = init_board()
    player = "X"
    end = False
    display_board(board)
    while end == False:
        position = input_user(board)
        play_move(board, player, position)
        display_board(board)
        if check_winner(board, player) == True:
            end = True
            print(f"{player} a gagné")
        if check_draw(board, player) == True:
            end = True
            print("Il n'y a pas de gagnant")
        player = switch_player(player)


playgame()
