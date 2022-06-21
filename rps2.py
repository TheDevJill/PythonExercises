def rps(player1, player2):
    """
    input: player 1 and player2 -> 'rock', 'paper', 'scissors'
    output: "player 1 wins", "player 2 wins", "Its a tie"

    """

    # tie
    if player1 == player2:
      print("It's a tie!")
    # player 1 = rock
    elif player1 == 'rock':
          if player2 == 'paper':
            print("Player 2 wins!")
          elif player2 == 'scissors':
            print("Player 1 wins!")
    # player 1 = paper
    elif player1 == 'paper':
          if player2 == 'rock':
            print("Player 1 wins!")
          elif player2 == 'scissors':
            print("Player 2 wins!")
    # player 1 = scissors
    elif player1 == 'scissors':
          if player2 == 'rock':
            print("Player 2 wins!")
          elif player2 == 'paper':
            print("Player 1 wins!")


#paper
rps('paper', 'paper')
rps('paper', 'scissors')
rps('paper', 'rock' )
# rock
rps('rock', 'rock')
rps('rock', 'paper')
rps('rock', 'scissors')
#scissors
rps('scissors', 'scissors')
rps('scissors', 'rock')
rps('scissors', 'paper')
