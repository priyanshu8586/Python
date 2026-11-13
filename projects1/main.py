import random

choices = ["rock", "paper", "scissors"]
wins = losses = 0

while True:
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("0. Quit")

    try:
        player = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a number only.")
        continue

    if player == 0:
        print(f"Final score - You: {wins}, Computer: {losses}")
        break

    if player not in choices:
        print("Invalid number. Enter 1, 2, or 3.")
        continue

      
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("Tie! Choose again.")
        continue

    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

    print(f"Score - You: {wins}, Computer: {losses}")