import simple_colors


p1=input("Player 1's name: ")
p2=input("Player 2's name: ")
one="1"
two="2"
three="3"
four="4"
five="5"
six="6"
seven="7"
eight="8"
nine="9"
while(True):
    print("\t ----------------------------------------------- ")
    print(f"\t|\t{one}\t|\t{two}\t|\t{three}\t|")
    print("\t| -------------\t| -------------\t| -------------\t|")
    print(f"\t|\t{four}\t|\t{five}\t|\t{six}\t|")
    print("\t| -------------\t| -------------\t| -------------\t|")
    print(f"\t|\t{seven}\t|\t{eight}\t|\t{nine}\t|")
    print("\t ----------------------------------------------- ")
    

    while(True):
        c5=input(f"\n{p1}'s move: ")
        if(c5=="1" and one!=simple_colors.green("O", "bold") and one!=simple_colors.red("X", "bold")):
            one=simple_colors.green("O", "bold")
            break
        elif(c5=="2" and two!=simple_colors.green("O", "bold") and two!=simple_colors.red("X", "bold")):
            two=simple_colors.green("O", "bold")
            break
        elif(c5=="3" and three!=simple_colors.green("O", "bold") and three!=simple_colors.red("X", "bold")):
            three=simple_colors.green("O", "bold")
            break
        elif(c5=="4" and four!=simple_colors.green("O", "bold") and four!=simple_colors.red("X", "bold")):
            four=simple_colors.green("O", "bold")
            break
        elif(c5=="5" and five!=simple_colors.green("O", "bold") and five!=simple_colors.red("X", "bold")):
            five=simple_colors.green("O", "bold")
            break
        elif(c5=="6" and six!=simple_colors.green("O", "bold") and six!=simple_colors.red("X", "bold")):
            six=simple_colors.green("O", "bold")
            break
        elif(c5=="7" and seven!=simple_colors.green("O", "bold") and seven!=simple_colors.red("X", "bold")):
            seven=simple_colors.green("O", "bold")
            break
        elif(c5=="8" and eight!=simple_colors.green("O", "bold") and eight!=simple_colors.red("X", "bold")):
            eight=simple_colors.green("O", "bold")
            break
        elif(c5=="9" and nine!=simple_colors.green("O", "bold") and nine!=simple_colors.red("X", "bold")):
            nine=simple_colors.green("O", "bold")
            break
        elif(c5!="1" and c5!="2" and c5!="3" and c5!="4" and c5!="5" and c5!="6" and c5!="7" and c5!="8" and c5!="9"):
            print("Plz enter a valid number")
        else:
            print("already over")
    print("\t ----------------------------------------------- ")
    print(f"\t|\t{one}\t|\t{two}\t|\t{three}\t|")
    print("\t| -------------\t| -------------\t| -------------\t|")
    print(f"\t|\t{four}\t|\t{five}\t|\t{six}\t|")
    print("\t| -------------\t| -------------\t| -------------\t|")
    print(f"\t|\t{seven}\t|\t{eight}\t|\t{nine}\t|")
    print("\t ----------------------------------------------- ")

    if(one==two==three==simple_colors.green("O", "bold") or one==four==seven==simple_colors.green("O", "bold") or one==five==nine==simple_colors.green("O", "bold") or two==five==eight==simple_colors.green("O", "bold") or three==six==nine==simple_colors.green("O", "bold") or three==five==seven==simple_colors.green("O", "bold") or four==five==six==simple_colors.green("O", "bold") or seven==eight==nine==simple_colors.green("O", "bold")):
        print(simple_colors.yellow(f"\"{p1}\" won", "bright"))
        print(simple_colors.yellow(f"Congratulations \"{p1}\"\n", "bright"))
        break
    elif(one==two==three==simple_colors.red("X", "bold") or one==four==seven==simple_colors.red("X", "bold") or one==five==nine==simple_colors.red("X", "bold") or two==five==eight==simple_colors.red("X", "bold") or three==six==nine==simple_colors.red("X", "bold") or three==five==seven==simple_colors.red("X", "bold") or four==five==six==simple_colors.red("X", "bold") or seven==eight==nine==simple_colors.red("X", "bold")):
        print(simple_colors.yellow(f"\"{p2}\" won", "bright"))
        print(simple_colors.yellow(f"Congratulations \"{p2}\"\n", "bright"))
        break
    elif((one==simple_colors.red("X", "bold") or one==simple_colors.green("O", "bold")) and (two==simple_colors.red("X", "bold") or two==simple_colors.green("O", "bold")) and (three==simple_colors.red("X", "bold") or three==simple_colors.green("O", "bold")) and (four==simple_colors.red("X", "bold") or four==simple_colors.green("O", "bold")) and (five==simple_colors.red("X", "bold") or five==simple_colors.green("O", "bold")) and (six==simple_colors.red("X", "bold") or six==simple_colors.green("O", "bold")) and (seven==simple_colors.red("X", "bold") or seven==simple_colors.green("O", "bold")) and (eight==simple_colors.red("X", "bold") or eight==simple_colors.green("O", "bold")) and (nine==simple_colors.red("X", "bold") or nine==simple_colors.green("O", "bold"))):
        print(simple_colors.yellow(f"It's a tie\n", "bright"))
        break
    else:
        pass




    while(True):
        c6=input(f"\n{p2}'s move: ")
        if(c6=="1" and one!=simple_colors.green("O", "bold") and one!=simple_colors.red("X", "bold")):
            one=simple_colors.red("X", "bold")
            break
        elif(c6=="2" and two!=simple_colors.green("O", "bold") and two!=simple_colors.red("X", "bold")):
            two=simple_colors.red("X", "bold")
            break
        elif(c6=="3" and three!=simple_colors.green("O", "bold") and three!=simple_colors.red("X", "bold")):
            three=simple_colors.red("X", "bold")
            break
        elif(c6=="4" and four!=simple_colors.green("O", "bold") and four!=simple_colors.red("X", "bold")):
            four=simple_colors.red("X", "bold")
            break
        elif(c6=="5" and five!=simple_colors.green("O", "bold") and five!=simple_colors.red("X", "bold")):
            five=simple_colors.red("X", "bold")
            break
        elif(c6=="6" and six!=simple_colors.green("O", "bold") and six!=simple_colors.red("X", "bold")):
            six=simple_colors.red("X", "bold")
            break
        elif(c6=="7" and seven!=simple_colors.green("O", "bold") and seven!=simple_colors.red("X", "bold")):
            seven=simple_colors.red("X", "bold")
            break
        elif(c6=="8" and eight!=simple_colors.green("O", "bold") and eight!=simple_colors.red("X", "bold")):
            eight=simple_colors.red("X", "bold")
            break
        elif(c6=="9" and nine!=simple_colors.green("O", "bold") and nine!=simple_colors.red("X", "bold")):
            nine=simple_colors.red("X", "bold")
            break
        elif(c6!="1" and c6!="2" and c6!="3" and c6!="4" and c6!="5" and c6!="6" and c6!="7" and c6!="8" and c6!="9"):
            print("Plz enter a valid number")
        else:
            print("already over")

    if(one==two==three==simple_colors.green("O", "bold") or one==four==seven==simple_colors.green("O", "bold") or one==five==nine==simple_colors.green("O", "bold") or two==five==eight==simple_colors.green("O", "bold") or three==six==nine==simple_colors.green("O", "bold") or three==five==seven==simple_colors.green("O", "bold") or four==five==six==simple_colors.green("O", "bold") or seven==eight==nine==simple_colors.green("O", "bold")):
        print(simple_colors.yellow(f"\"{p1}\" won", "bright"))
        print(simple_colors.yellow(f"Congratulations \"{p1}\"\n", "bright"))
        break
    elif(one==two==three==simple_colors.red("X", "bold") or one==four==seven==simple_colors.red("X", "bold") or one==five==nine==simple_colors.red("X", "bold") or two==five==eight==simple_colors.red("X", "bold") or three==six==nine==simple_colors.red("X", "bold") or three==five==seven==simple_colors.red("X", "bold") or four==five==six==simple_colors.red("X", "bold") or seven==eight==nine==simple_colors.red("X", "bold")):
        print(simple_colors.yellow(f"\"{p2}\" won", "bright"))
        print(simple_colors.yellow(f"Congratulations \"{p2}\"\n", "bright"))
        break
    elif((one==simple_colors.red("X", "bold") or one==simple_colors.green("O", "bold")) and (two==simple_colors.red("X", "bold") or two==simple_colors.green("O", "bold")) and (three==simple_colors.red("X", "bold") or three==simple_colors.green("O", "bold")) and (four==simple_colors.red("X", "bold") or four==simple_colors.green("O", "bold")) and (five==simple_colors.red("X", "bold") or five==simple_colors.green("O", "bold")) and (six==simple_colors.red("X", "bold") or six==simple_colors.green("O", "bold")) and (seven==simple_colors.red("X", "bold") or seven==simple_colors.green("O", "bold")) and (eight==simple_colors.red("X", "bold") or eight==simple_colors.green("O", "bold")) and (nine==simple_colors.red("X", "bold") or nine==simple_colors.green("O", "bold"))):
        print(simple_colors.yellow(f"It's a tie\n", "bright"))
        break
    else:
        pass
    
            