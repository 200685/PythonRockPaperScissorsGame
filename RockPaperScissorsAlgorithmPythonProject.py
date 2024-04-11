import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def predict_player_move(history):
    if not history:
        return random.choice(["rock", "paper", "scissors"])
    most_common = max(set(history), key=history.count)
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else: # most_common == "scissors"
        return "rock"

def play_game(rounds):
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    player_history = []
    
    for round in range(1, rounds + 1):
        print(f"\nRound {round} of {rounds}")
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        while player_choice not in choices:
            print("Invalid choice. Please choose again.")
            player_choice = input("Choose rock, paper, or scissors: ").lower()
        
        player_history.append(player_choice)
        computer_choice = predict_player_move(player_history)
        print(f"Computer chose {computer_choice}")
        
        winner = determine_winner(player_choice, computer_choice)
        if winner == "player":
            print("You win this round!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Current Score - Player: {player_score}, Computer: {computer_score}")
    
    if player_score > computer_score:
        print("\nCongratulations! You've won the game!")
    elif player_score < computer_score:
        print("\nSorry, the computer has won the game.")
    else:
        print("\nThe game ended in a tie.")

num_rounds = int(input("How many rounds would you like to play? "))
play_game(num_rounds)
