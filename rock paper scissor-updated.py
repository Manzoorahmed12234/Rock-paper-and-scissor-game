import random                       #library imported

player1_wins = 0
player2_wins = 0

options = ["rock", "paper", "scissors"]         #made a list of choices

while True:                                     #asking for a choice
    player1_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player1_input == "q":
        break

    if player1_input not in options:
        continue

    random_number = random.randint(0, 2)      #random selection of choice
    # rock: 0, paper: 1, scissors: 2
    player2_pick = options[random_number]
    print("Computer picked", player2_pick + ".")

    if player1_input == "rock" and player2_pick == "scissors":    #conditions for rock,paper scissor
        print("You won!")
        player1_wins += 1

    elif player1_input == "paper" and player2_pick == "rock":
        print("You won!")
        player1_wins += 1

    elif player1_input == "scissors" and player2_pick == "paper":
        print("You won!")
        player1_wins += 1

    elif player1_input == "scissors" and player2_pick == "scissors":
        print("It's a draw!")

    elif player1_input == "paper" and player2_pick == "paper":
        print("It's a draw!")

    elif player1_input == "rock" and player2_pick == "rock":
        print("It's a draw!")

    else:
        print("You lost!")
        player2_wins += 1

print("You won", player1_wins, "times.")                      #output of the results
print("The computer won", player2_wins, "times.")
print("Goodbye! Play again next time")