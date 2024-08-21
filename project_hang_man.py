import random
import keyboard
import simple_colors


def check(yo):
    for i in range(len(cor)):
        if(yo==cor[i]):
            ans[i]=ans[i].replace("_", yo)

    for i in ans:
        print(i, end=" ")

    if(yo not in cor):
        global num
        num+=1
        if(num==1):
            print("\n1st Miss, [remaining misses = 4]")
            print(simple_colors.yellow("  \t O"))
            print(simple_colors.red("\t/", "bright")+("|")+simple_colors.yellow("\\"))
            print(simple_colors.yellow("\t/")+simple_colors.yellow(" \\"))
        elif(num==2):
            print("\n2nd Miss, [remaining misses = 3]")
            print(simple_colors.yellow("  \t O"))
            print(simple_colors.red("\t/", "bright")+("|")+simple_colors.red("\\", "bright"))
            print(simple_colors.yellow("\t/")+simple_colors.yellow(" \\"))
        elif(num==3):
            print("\n3rd Miss, [remaining misses = 2]")
            print(simple_colors.yellow("  \t O"))
            print(simple_colors.red("\t/", "bright")+("|")+simple_colors.red("\\", "bright"))
            print(simple_colors.red("\t/", "bright")+simple_colors.yellow(" \\"))
        elif(num==4):
            print("\n4th Miss, [remaining misses = 1]")
            print(simple_colors.yellow("  \t O"))
            print(simple_colors.red("\t/", "bright")+("|")+simple_colors.red("\\", "bright"))
            print(simple_colors.red("\t/", "bright")+simple_colors.red(" \\", "bright"))
        elif(num==5):
            print("\n5th Miss, [remaining misses = 0]")
            print(simple_colors.red("  \t O", "bright"))
            print(simple_colors.red("\t/", "bright")+("|")+simple_colors.red("\\", "bright"))
            print(simple_colors.red("\t/", "bright")+simple_colors.red(" \\", "bright"))
            print("\nGame Over, You lost")
            print("\nCorrect answer: ")
            for i in cor:
                print(i, end=" ")
        
    

if __name__=="__main__":
    while(True):
        k=int(random.randint(1, 5))
        print("\n\nSelect your preferred area:")
        print("1) General Knowledge\n2) Politics\n3) Movies\n")
        choice=input("Enter your choice: ").lower()
        if "1" in choice or "general knowledge" in choice or "gk" in choice:
            if(k==1):
                print("\nWho named the Pacific Ocean?")
                ans=["_","_","_","_","_","_","_","_","_"," ","_","_","_","_","_","_","_","_"]
                cor=["f","e","r","d","i","n","a","n","d"," ","m","a","g","e","l","l","a","n"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==2):
                print("\nWhat is the physical phase of life called?")
                ans=["_","_","_","_","_","_","_","_","_","_"]
                cor=["p","r","o","t","o","p","l","a","s","m"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==3):
                print("\nIn which of the following sects was Bindusara interested?")
                ans=["_","_","_","_","_","_","_","_"]
                cor=["a","j","i","v","a","k","a","s"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==4):
                print("\nWho painted the Sistine Chapel ceiling?")
                ans=["_","_","_","_","_","_","_","_","_","_","_","_"]
                cor=["m","i","c","h","e","l","a","n","g","e","l","o"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==5):
                print("\nWho wrote \"Alice's Adventures in Wonderland\"?")
                ans=["_","_","_","_","_"," ","_","_","_","_","_","_","_"]
                cor=["l","e","w","i","s"," ","c","a","r","r","o","l","l"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            else:
                break




        elif "2" in choice or "politics" in choice:
            if(k==1):
                print("In which house the no-confidence motion is brought?")
                ans=["_","_","_"," ","_","_","_","_","_"]
                cor=["l","o","k"," ","s","a","b","h","a"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==2):
                print("In which case the Supreme Court of India propounded the theory of basic structure of the Constitution?")
                ans=["_","_","_","_","_","_","_","_","_","_"," ","_","_","_","_","_","_","_"]
                cor=["k","e","s","h","v","a","n","a","n","d"," ","b","h","a","r","a","t","i"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==3):
                print("Who is the first Woman Chief Minister in India?")
                ans=["_","_","_","_","_","_","_"," ","_","_","_","_","_","_","_","_"]
                cor=["s","u","c","h","e","t","a"," ","k","r","i","p","l","a","n","i"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==4):
                print("If there is a deadlock between Rajya Sabha and Lok Sabha over an ordinary bill, it will be resolved by whom?")
                ans=["_","_","_"," ","_","_","_","_","_"," ","_","_","_","_","_","_","_"," ","_","_"," ","_","_","_","_","_","_","_","_","_"]
                cor=["t","h","e"," ","j","o","i","n","t"," ","s","e","s","s","i","o","n"," ","o","f"," ","p","a","r","l","i","m","e","n","t"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==5):
                print("Preamble to the constitution of India consists what?")
                ans=["_","_","_","_","_","_","_","_","_","_"," ","_","_","_","_","_","_","_","_","_","_"," ","_","_","_","_","_","_","_","_"," ","_","_","_","_","_","_","_","_","_","_"," ","_","_","_","_","_","_","_","_"]
                cor=["s","o","v","e","r","e","i","g","n",","," ","s","o","c","i","a","l","i","s","t",","," ","s","e","c","u","l","a","r",","," ","d","e","m","o","c","r","a","t","i","c"," ","r","e","p","u","b","l","i","c"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            else:
                break




        elif "3" in choice or "movies" in choice:
            if(k==1):
                print("Guess the Movie name, Hint: It's an OLD movie")
                ans=["_","_","_","_","_","_","_"]
                cor=["t","r","i","s","h","u","l"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==2):
                print("Guess the Movie name, Hint: It's niether old nor new, It's a medium aged movie")
                ans=["_","_","_","_","_","_","_"]
                cor=["a","a","g","h","a","a","z"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==3):
                print("Guess the Movie name, Hint: It's niether old nor new, It's a medium aged movie")
                ans=["_","_","_","_","_","_"]
                cor=["f","u","k","r","e","y"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==4):
                print("Guess the Movie name, Hint: It's a new movie")
                ans=["_","_","_","_","_","_","_"]
                cor=["d","h","a","a","k","a","d"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            elif(k==5):
                print("Guess the Movie name, Hint: It's niether old nor new, It's a medium aged movie")
                ans=["_","_","_","_","_","_"]
                cor=["f","r","e","d","d","y"]
                num=0
                for i in ans:
                    print(i, end=" ")
                while(True):
                    yo=input("\n\nAns: ").lower()
                    check(yo)
                    if(num==5):
                        break
                    if(ans==cor):
                        print("\nYeah, Correct")
                        break

            else:
                break