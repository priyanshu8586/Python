import random

names = {1: "Rock", 2: "Paper", 3: "Scissors"}

print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")

# Keep asking until the player enters 1, 2, or 3
while True:
    text = input("Enter a number (1, 2, or 3): ")
    if text in ("1", "2", "3"):
        player = int(text)
        break
    print("Wrong input! Numbers 1, 2, or 3 only.")
    

computer = random.randint(1, 3)

print("You chose:", names[player])
print("Computer chose:", names[computer])

if player == computer:
    print("It's a tie!")
elif (player - computer) % 3 == 1:
    print("You win!")
else:
    print("You lose!")