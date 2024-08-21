import random
import time
import simple_colors

while(True):
    p=input("\n\nName of the Player: ")
    print(f"Hello \"{p}\", The coin is being tossed, Please wait")
    time.sleep(2)
    toss=["Batting", "Balling"]
    k=int(random.randint(0, 1))
    p_s=0
    c_s=0
    toss_result=toss[k]
    print("\nToss results declared")
    print(f"You will be \"{toss_result}\" first")

    if(toss_result=="Batting"):  
        while(True):
            print("\nEnter the runs: ")
            p_bat=int(input())
            print(f"\nYour runs: {p_bat}")
            r=int(random.randint(0, 6))
            c_ball=r
            print(f"Computer's throw: {c_ball}")
            if(p_bat!=c_ball):
                p_s= p_bat+p_s
            elif(p_bat==c_ball):
                print("\nIt's a wicket, You are Out")
                print(f"Your Total Score: {p_s}")
                print()
                break
            
        print(f"\nGet ready {p}, It's balling time")
        while(True):
            print("\nEnter your throw: ")
            p_ball=int(input())
            r=int(random.randint(0, 6))
            c_bat=r
            print(f"\nComputer's runs: {c_bat}")
            print(f"Your throw: {p_ball}")
            if(p_ball!=c_bat):
                c_s=c_s+c_bat
                if(c_s>p_s):
                    print("Game Over")
                    print(f"Computer's Total Score: {c_s}")
                    break
            elif(p_ball==c_bat):
                print("\nCongratulations, It's a wicket, Computer got Out")
                print(f"Computer's Total Score: {c_s}")
                break



    elif(toss_result=="Balling"):
        while(True):
            print("\nEnter your throw: ")
            p_ball=int(input())
            r=int(random.randint(0, 6))
            c_bat=r
            print(f"\nComputer's runs: {c_bat}")
            print(f"Your throw: {p_ball}")
            if(p_ball!=c_bat):
                c_s=c_s+c_bat
            elif(p_ball==c_bat):
                print("\nCongratulations, It's a wicket, Computer got Out")
                print(f"Computer's Total Score: {c_s}")
                break
        
        print(f"\nGet ready {p}, It's batting time")
        while(True):
            print("\nEnter the runs: ")
            p_bat=int(input())
            print(f"\nYour runs: {p_bat}")
            r=int(random.randint(0, 6))
            c_ball=r
            print(f"Computer's throw: {c_ball}")
            if(p_bat!=c_ball):
                p_s= p_bat+p_s
                if(p_s>c_s):
                    print("Game Over")
                    print(f"Your Total Score: {p_s}")
                    break
            elif(p_bat==c_ball):
                print("\nIt's a wicket, You are Out")
                print(f"Your Total Score: {p_s}")
                break
            

    print(simple_colors.yellow("\nResults Time :)", "bright"))
    if(p_s>c_s):
        print(simple_colors.yellow(f"Congratulations {p}, You won!", "bright"))
    elif(p_s<c_s):
        print(simple_colors.yellow(f"Computer Won, Better luck next time", "bright"))
    else:
        print(simple_colors.yellow("It's a tie", "bright"))
    
    again=input("\nWanna play again: ").lower()
    if(again=="yes" or again=="y"):
        continue
    else:
        break
            









