while True:
    player1 = input('Player1: rock/paper/scissors: ').lower()
    player2 = input('Player2: rock/paper/scissors: ').lower()

    if player1 == player2:
        print('Its a Tie')

    elif (player1 == 'rock' and player2 == 'paper') or (player1 == 'paper' and player2 == 'scissors') \
        or (player1 == 'scissors' and player2 == 'rock'):
            print('Player 2 wins. If u want stop type stop: ')
            another_game = input()
            if another_game != 'stop':
                continue;
            else:
                break

    elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') \
        or (player1 == 'scissors' and player2 == 'paper'):
            print('Player 1 wins. If u want stop type stop: ')
            another_game = input()
            if another_game != 'stop':
                continue;
            else:
                break
