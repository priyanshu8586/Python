import random

names = {1: "Rock", 2: "Paper", 3: "Scissors"}

print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")
print("0 = Quit")

# Keep asking until the player enters 1, 2, 3 or 0 
while True:
    text = input("Enter a number : ")
    if text in ("0", "1", "2", "3"):
        player = int(text)
        break
    print("Wrong input! Numbers 0, 1, 2, or 3 only.")

if player == 0:
    print("Thanks for playing!")
    #break 

computer = random.randint(1, 3, )

print("You chose:", names[player])
print("Computer chose:", names[computer])

if player == computer:
    print("It's a tie!")
elif (player - computer) % 3 == 1:
    print("You win!")
else:
    print("You lose!")