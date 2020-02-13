import random
player1_win=0
player2_win=0
counter_rock=0
counter_paper=0
counter_scissors=0
player1=0
player2=0  # type: int
player1_moves =  []
player2_moves =  []
while(player1!=4):
    print("1-rock")
    print("2-paper")
    print("3-scissors")
    print("4-finish")
    player1 = input("PLAYER 1: ")
    if player1 != 4:
        if counter_rock>=counter_paper and counter_rock>=counter_scissors:
            player2=2
            print "PLAYER 2 MOVE: ", player2
        elif counter_paper>counter_rock and counter_paper>=counter_scissors:
            player2=3
            print "PLAYER 2 MOVE: ", player2
        elif counter_scissors > counter_rock and counter_scissors > counter_paper:
            player2 = 1
            print "PLAYER 2 MOVE: ", player2
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
    if player1 == 1:
        counter_rock=counter_rock+1
    elif player1 == 2:
        counter_paper=counter_paper+1
    elif player1 == 3:
        counter_scissors=counter_scissors+1

print "PLAYER 1 SCORE: ", player1_win
print "PLAYER 2 SCORE: ", player2_win
print(player1_moves)
print(player2_moves)
