import random

print("\nHello, Welcome to \"Guess the Number\" game, Created by Mr. Vishwas Gandham")
print("\nHow to Play: You yourself will give me the range of numbers among which, I will select a number according to my wish, & then you will have to guess the number selected by me in \"n\" guesses challenged by me to you. Hope you understood.... :)")

while(True):
    l=int(input("\nGive me the least number to guess (ex: 0): "))
    u=int(input("Give me the highest number to guess (ex: 100): "))
    no_of_guesses=0
    
    r=int(random.randint(l, u))

    if((u-l)>0 and (u-l)<1000):
        k=int(random.randint(0, 10))
        
    elif((u-l)>=1000):
        k=int(random.randint(10, 15))

    print(f'\nI challenge you, Guess the number in {k} guesses')
    while(True):   
        no_of_guesses += 1
        guess=int(input("\nTry to guess it: "))
        if(guess<r):
            print("think big")
        elif(guess>r):
            print("come down")
        else:
            print(f'\nYaay, you got it buddy, the number is {r}')
            print("No. of guesses = " + str(no_of_guesses)+ " guesses")
            if(no_of_guesses<k):
                print(f'\nYou won, you guessed the number in {no_of_guesses} guesses which is less than {k} guesses.....Good')
            elif(no_of_guesses==k):
                print(f'\nYou won, you guessed the number in {no_of_guesses} guesses which is equal to {k} guesses.....Good')
            else:
                print(f'\nYou Lost, you guessed the number in {no_of_guesses} guesses which is greater than {k} guesses.....Better luck next time')
            break

    again=input("\n\nWanna play again: ")
    if(again.lower()=="yes"):
        no_of_guesses=0
    if(again.lower()!="yes"):
        break
    
