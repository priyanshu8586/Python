import random

# Dictionary: number -> choice
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

# Dictionary: what each choice beats
beats = {1: 3, 2: 1, 3: 2}  # Rock beats Scissors, Paper beats Rock, Scissors beats Paper

WIN_SCORE = int(input("Enter the winig score :"))  # first to reach this score ends the game

player_score = 0
computer_score = 0

print("=== Rock Paper Scissors ===")
print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")
print("0 = Quit")

while True:
    try:
        player = int(input("\nEnter your number: "))
    except ValueError:
        print("Please enter a number only.")
        continue

    if player == 0:
        print("Thanks for playing!")
        break

    if player not in choices:
        print("Invalid number. Use 1, 2, 3 or 0 to quit.")
        continue

    computer = random.randint(1, 3)
    print(f"You chose: {choices[player]}")
    print(f"Computer chose: {choices[computer]}")

    if player == computer:
        print("It's a tie!")
    elif beats[player] == computer:
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> Player: {player_score} | Computer: {computer_score}")

    if player_score == WIN_SCORE or computer_score == WIN_SCORE:
        print(f"\nSomeone reached {WIN_SCORE} points. Game over!")
        break

print("\n=== Final Score ===")
print(f"Player: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("You are the overall winner!")
elif computer_score > player_score:
    print("Computer is the overall winner!")
else:
    print("Overall result: Tie!")
