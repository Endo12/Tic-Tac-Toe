play_again = True
while play_again:
    winner = 0
    current_player1 = True
    p1_letter = input('Would Player 1 like to be X or O? ')
    p2_letter = 'placeholder' #will later be assigned to player 2's letter
    if p1_letter.lower() == 'x':
        p2_letter = 'o'
    else:
        p2_letter = 'x'
    moves = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '} #dict that represents the 9 spots on the board
    def print_board(plays): #prints board, will use the moves dict
        print('   |   |   ')
        print(f' {plays[7]} | {plays[8]} | {plays[9]} ')
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(f' {plays[4]} | {plays[5]} | {plays[6]} ')
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(f' {plays[1]} | {plays[2]} | {plays[3]} ')
        print('   |   |   ')
    def keep_playing(plays): #figures out if anyone won, given by the winner variable
        xindexes = []
        oindexes = []
        global winner #this will need to be referenced outside the method def
        for loc, letter in plays.items(): #appends the location of all the letters to the respective list
            if letter == 'x':
                xindexes.append(loc)
            elif letter == 'o':
                oindexes.append(loc)
        #the following code defines a list of all possible winning index combnations
        winning_indexes = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        for a, b, c in winning_indexes:
            if a in xindexes and b in xindexes and c in xindexes: #checks if the 3 indexes are in xindexes
                #the player using x is assigned winner
                if p1_letter == 'x':
                    winner = 1
                else:
                    winner = 2
            elif a in oindexes and b in oindexes and c in oindexes: #checks if the 3 indexes are in oindexes
                #the player using o is assigned winner
                if p1_letter == 'o':
                    winner = 1
                else:
                    winner = 2
        return winner == 0
    moves_made = 0
    while keep_playing(moves): #this loop contains the actual game
        if moves_made == 9:
            winner = 3 #draw situation
            break
        print('\n'*100) #clears board
        print_board(moves)
        if current_player1:
            keep_going = True #this variable keeps track of whose turn it is
            while keep_going:
                player_loc = int(input('Player 1 pick a location (1-9) '))
                if moves[player_loc] == ' ': #makes sure no one took the desired spot
                    moves[player_loc] = p1_letter
                    keep_going = False
                    current_player1 = False
                    moves_made += 1
                else:
                    print('That spot is already taken, please pick a spot that is not taken')
        else:
            keep_going2 = True
            while keep_going2:
                player_loc2 = int(input('Player 2 pick a location (1-9) '))
                if moves[player_loc2] == ' ':
                    moves[player_loc2] = p2_letter
                    keep_going2 = False
                    current_player1 = True
                    moves_made += 1
                else:
                    print('That spot is already taken, please pick a spot that is not taken')
    print('\n' * 100)
    print_board(moves)
    if winner == 1 or winner == 2:
        print(f'Player {winner} won!')
    else:
        print('Draw!')
    if input('Play again? (Y or N) ') == 'N':
        play_again = False
