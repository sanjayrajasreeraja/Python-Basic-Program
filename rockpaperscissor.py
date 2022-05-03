import random

command=["R","P","S"]

while True:
    print("\nRock Paper Scissors")
    play=input("Choose [R]ock [P]aper [S]cissors or [E]xit:")
    cplay=random.randint(0,2)
    cplay=command[cplay]
    if play.upper() not in ["R","P","S","E"]:
        print("Invalid Command")

    elif play.upper()=="E":
        break

    if play.upper() == cplay:
        print("Tie")

    elif play.upper()=="R" and cplay=="S":
        print("You win")

    elif play.upper()=="P" and cplay=="R":
        print("You win")
    
    elif play.upper()=="S" and cplay=="P":
        print("You win")

    elif play.upper()=="S" and cplay=="R":
        print("You lose")

    elif play.upper()=="R" and cplay=="P":
        print("You lose")
    
    elif play.upper()=="P" and cplay=="S":
        print("You lose")
