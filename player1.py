player1_win=0
player2_win=0
player1=0
player2=0
player1_moves =  []
player2_moves =  []
while(player1!=4):
    print("1-rock")
    print("2-paper")
    print("3-scissors")
    print("4-finish")
    player1 = input("PLAYER 1: ")
    if player1 != 4:
        player2 = input("PLAYER 2: ")
    else:
        break

    if player2 == player1:
        print("DRAW");
    else:
        if player1==1:
            if player2==2:
                print("PLAYER 2 WIN")
                player2_win=player2_win+1;
            if player2==3:
                print("PLAYER 1 WIN")
                player1_win=player1_win+1;
        if player1 == 2:
            if player2 == 1:
                print("PLAYER 1 WIN")
                player1_win=player1_win+1;
            if player2 == 3:
                print("PLAYER 2 WIN")
                player2_win=player2_win+1;
        if player1 == 3:
            if player2 == 1:
                print("PLAYER 1 WIN")
                player1_win=player1_win+1;
            if player2 == 2:
                print("PLAYER 2 WIN")
                player2_win=player2_win+1;

    player1_moves.append(player1)
    player2_moves.append(player2)

print "PLAYER 1 SCORE: ", player1_win
print "PLAYER 2 SCORE: ", player2_win
print(player1_moves)
print(player2_moves)
