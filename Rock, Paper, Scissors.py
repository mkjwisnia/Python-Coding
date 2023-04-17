############################## Paper, rock, scissors

import random


while True:

    choices = ["paper", "rock", "scissors"]
    computer = random.choice(choices)
    player = input(" Hey! Let's play. Choose - rock, paper or scissors: ")
    print()




    while player not in choices:
        print()
        player = input("There's no such option - paper, rock or scissors?: ").lower()
        



    
    
    while player == computer:
        print("It's a tie!. Try again!")
        computer = random.choice(choices)
        print()
        player = input("Paper, rock or scissors: ").lower()
        




    if player == "paper":
        if computer == "rock":
            print("You won! That was easy, right? ")
            print()
        elif computer =="scissors":
            print("You lose, but don't worry. You can try again! ")
            print()




    if player == "rock":
        if computer == "papier":
            print("Ehh not this time. You lose :( ) ")

        elif computer == "scissors":
            print("Great choice! You won!")
            print()



    if player == "scissors":
        if computer == "paper":
            print("Amazing! You won!")
            print()
        if computer == "rock":
            print("Well, not this time. You lose.")
            print()




    print()        
    print(f"Computer choice: {computer}")
    print()
    print(f"Your choice: {player}")
    

    print()
    another_game = input("Would You like to try again? (yes/no) :" )

    if another_game == "no":
        break

print("Alright. That was fun. See you!")
print("-------------")
        











