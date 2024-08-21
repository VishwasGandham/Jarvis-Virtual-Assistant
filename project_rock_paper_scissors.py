import random

user_wins=0
computer_wins=0

print("\nHello, Welcome to \"Rock, Paper & Scissors\" game, Created by Mr. Vishwas Gandham")
print("\nHow to Play: You have to type either \"Rock\", \"Paper\" or \"Scissors\" as your pick. Hope you understood.... :)")

while(True):
    options=["rock", "paper", "scissors"]
    random_number=random.randint(0, 2)
    
    user_input=input("\n\n\nYour pick (Type \"q\" to end the game and get final scores): ")
    
    if(user_input=="q"):
        print("\nFinal Scores:")
        print(f'Computer\'s Score: {computer_wins}')
        print(f'Your Score: {user_wins}')
        if(user_wins>computer_wins):
            print("\nYou Won\nGood Bye\n\n")
        elif(user_wins==computer_wins):
            print("\nIt\'s a Tie\nGood Bye\n\n")
        else:
            print("\nComputer Won\nGood Bye\n\n")
        break

    if(user_input.lower() not in options):
        print("You have to type EITHER \"rock\", \"paper\", \"scissors\" to PLAY the game OR \"q\" to QUIT the game.")
        continue

    else:
        computer_pick=options[random_number]
        print("Computer's pick =", computer_pick)

        if(user_input=="rock" and computer_pick=="scissors"):
            user_wins+=1
        elif(user_input=="rock" and computer_pick=="paper"):
            computer_wins+=1
        elif(user_input=="rock" and computer_pick=="rock"):
            print("Tie")

        if(user_input=="paper" and computer_pick=="scissors"):
            computer_wins+=1
        elif(user_input=="paper" and computer_pick=="paper"):
            print("Tie")
        elif(user_input=="paper" and computer_pick=="rock"):
            user_wins+=1

        if(user_input=="scissors" and computer_pick=="scissors"):
            print("Tie")
        elif(user_input=="scissors" and computer_pick=="paper"):
            user_wins+=1
        elif(user_input=="scissors" and computer_pick=="rock"):
            computer_wins+=1

    
    # if(user_wins>computer_wins):
    #     print("\nWow, you won")
    # elif(user_wins<computer_wins):
    #     print("\nComputer won")
    # else:
    #     print("\nIt was a tie")
    print("\nYour Score:",user_wins)
    print("Computer's Score:",computer_wins)
    


