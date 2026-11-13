import random

choices = ["rock", "paper", "scissors"]
wins = losses = 0

while True:
    player = input("Choose rock, paper, or scissors (or 'quit'): ").lower()

    if player == "quit":
        print(f"Final score - You: {wins}, Computer: {losses}")
        break

    if player not in choices:
        print("Invalid choice. Try again.")
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