import random
player1_win=0
player2_win=0
player1=0
player2=0  # type: int
player1_moves =  []
player2_moves =  []
i=0

print("1-rock")
print("2-paper")
print("3-scissors")

player1 = input("PLAYER 1: ")
player2= random.randint(1, 3);
print "PLAYER 2 MOVE: ", player2

if player2 == player1:
    print("DRAW");
else:
    if player1 == 1:
        if player2 == 2:
            print("PLAYER 2 WIN")
            player2_win = player2_win + 1;
        if player2 == 3:
            print("PLAYER 1 WIN")
            player1_win = player1_win + 1;
    if player1 == 2:
        if player2 == 1:
            print("PLAYER 1 WIN")
            player1_win = player1_win + 1;
        if player2 == 3:
            print("PLAYER 2 WIN")
            player2_win = player2_win + 1;
    if player1 == 3:
        if player2 == 1:
            print("PLAYER 1 WIN")
            player1_win = player1_win + 1;
        if player2 == 2:
            print("PLAYER 2 WIN")
            player2_win = player2_win + 1;

player1_moves.append(player1)
player2_moves.append(player2)

while(player1!=4):
    print("1-rock")
    print("2-paper")
    print("3-scissors")
    print("4-finish")
    player1 = input("PLAYER 1: ")
    if player1 != 4:
        if  player1_moves[i]==1 and player2_moves[i]==3 :
            player2= 2;
            print "PLAYER 2 MOVE: ", player2
        elif player1_moves[i]==2 and player2_moves[i]==1 :
            player2= 3;
            print "PLAYER 2 MOVE: ", player2
        elif player1_moves[i]==3 and player2_moves[i]==2 :
            player2= 1;
            print "PLAYER 2 MOVE: ", player2
        else:
            player2= random.randint(1, 3);
            print "PLAYER 2 MOVE: ", player2;

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
                print("PLAYER 2 WIN")
                player2_win=player2_win+1;
            if player2 == 2:
                print("PLAYER 1 WIN")
                player1_win=player1_win+1;

    player1_moves.append(player1)
    player2_moves.append(player2)
    i=i+1;

print "PLAYER 1 SCORE: ", player1_win
print "PLAYER 2 SCORE: ", player2_win
print(player1_moves)
print(player2_moves)

