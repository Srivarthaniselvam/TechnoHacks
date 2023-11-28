# rock paper scissors game
import random


print("Welcome to Rock-Paper-Scissors Game!")

def play_game():
    # scores
    user_score = 0
    computer_score = 0

    # Play the rounds
    for round in range(1, 6):
        # Get user input
        user_choice = input("Choose Rock, Paper, or Scissors: ")

        # choice for computer choice
        computer_choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(computer_choices)

        # Determine winner
        if user_choice == computer_choice:
            result = "Tie"
        elif user_choice == "rock" and computer_choice == "scissors":
            result = "You win!"
            user_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            result = "You win!"
            user_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            result = "You win!"
            user_score += 1
        else:
            result = "You lose"
            computer_score += 1

        # results
        print("Round:", round)
        print("You choose:", user_choice)
        print("Computer choose:", computer_choice)
        print("Result:", result)

        # score
        print("Your score:", user_score)
        print("Computer score:", computer_score)

    # overall winner
    if user_score > computer_score:
        print("Congratulation You win the game!")
    elif user_score < computer_score:
        print("Computer win the game"
              "\n you are lose")
    else:
        print("The game is a tie!")

# Play again?
while True:
   play_game()
   play_again = input("Play again? (yes/no): ")
   if play_again != "yes":
        break
print("Thanks for playing the Rock_Paper_Scissors game!")
