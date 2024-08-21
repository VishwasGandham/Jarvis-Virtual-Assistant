import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import keyboard
import time
import webbrowser
import cv2
import os
import random
import pyjokes
import pywhatkit 
import pyautogui
import simple_colors
import subprocess

chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"

engine=pyttsx3.init()
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishm():
    hour=int(datetime.datetime.now().hour)
    d=datetime.datetime.now().strftime("%d\t%m\t%Y\t")
    t=datetime.datetime.now().strftime("%I:\t%M\t%p")

    if hour>=0 and hour<12:
        print("\nGood Morning Sir!")
        speak(f"Good Morning Sir")

    elif(hour>=12 and hour<16):
        print("\nGood Afternoon Sir!")
        speak(f"Good Afternoon Sir")

    else:
        print("\nGood Evening Sir!")
        speak(f"Good Evening Sir")


def wishf():
    hour=int(datetime.datetime.now().hour)
    d=datetime.datetime.now().strftime("%d\t%m\t%Y\t")
    t=datetime.datetime.now().strftime("%I:\t%M\t%p")

    if hour>=0 and hour<12:
        print("\nGood Morning Mam!")
        speak(f"Good Morning Mam")

    elif(hour>=12 and hour<16):
        print("\nGood Afternoon Mam!")
        speak(f"Good Afternoon Mam")

    else:
        print("\nGood Evening Mam!")
        speak(f"Good Evening Mam")


def talk():
    speak("Type it here: ")
    talk=input("Type here: ")
    speak(talk)


def url(input):
    webbrowser.get(chrome_path).open(input)


def dt():
    hour=int(datetime.datetime.now().hour)
    d=datetime.datetime.now().strftime("%d,\t%B,\t%Y\t")
    t=datetime.datetime.now().strftime("%I:,\t%M\t%p")
    dp=datetime.datetime.now().strftime("%d %B %Y")
    tp=datetime.datetime.now().strftime("%I:%M %p")
    ad=datetime.datetime.now().strftime("%A")
    print(f"\nToday's Date is: {dp}")
    speak(f"Today's Date is, {d}")
    print(f"It's {ad} today.")
    speak(f"It's {ad} today.")
    print(f"The Time at this moment is: {tp}\n")
    speak(f"& the time at this moment is, {t}")


def listen(attempt=1, max_attempts=5):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening.... ")
        r.pause_threshold=0.5
        r.energy_threshold=100
        audio=r.listen(source, 86400, 5)
    try:
        print("Trying to recognize....")
        query=r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again please...\n")
        if(attempt<max_attempts):
            return listen(attempt=attempt+1, max_attempts=max_attempts)
        else:
            print("Sorry, I am unable to get you, Please try later")
            return "None"
    return query

if __name__=="__main__":
    
    # while(True):
    #     # speak("Please type your Gender, is it male or female?")
    #     gender=input("\nPlease type your Gender (Male/Female): ")
    #     if(gender.lower()=="male"):
    #         wishm()
    #         break

    #     elif(gender.lower()=="female"):
    #         wishf()
    #         break

    #     else:
    #         print("Please type either \"Male\" or \"Female\"")
    #         continue
    wishm()
    speak("This is Jarvis, Your personal AI Assistant!")
    # dt()
    
    mode=input("Will you type or speak: ").lower()

    while(True):
        
        k=int(random.randint(0, 12))
        if "type" in mode:
            query=input("\n\nHow can I help you? ").lower()
        elif "speak" in mode:
            print("\n\nHow can i help you?")
            query=listen().lower()


        if ("in wikipedia" in query) and ("jarvis" in query):
            speak("\nSearching in Wikipedia. Got it")
            if "in wikipedia" in query:
                query=query.replace("in wikipedia", "")
            else:
                query=query.replace("wikipedia", "")
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            result=wikipedia.summary(query)
            speak("According to wikipedia")
            print("\n", result)


        elif ("search in google" in query or "search something in google" in query) and ("jarvis" in query):
            ser=input("What do you want to search: ")
            if "search for" in ser:
                ser=ser.replace("search for", "")
            elif "search" in ser:
                ser=ser.replace("search", "")
            else:
                pass
            if "in google" in ser:
                ser=ser.replace("in google", "")
            else:
                pass
            if "jarvis" in ser:
                ser=ser.replace("jarvis", "")
            else:
                pass
            speak("Searching in Google. Got it")
            webbrowser.get(chrome_path).open(f"https://www.google.com.tr/search?q={ser}")


        elif ("search" in query or "search for" in query or "search about" in query) and ("jarvis" in query):
            if "search for" in query:
                query=query.replace("search for", "")
            elif "search about" in query:
                query=query.replace("search about", "")
            else:
                pass
            if "search" in query:
                query=query.replace("search", "")
            else:
                pass
            if "in google" in query:
                query=query.replace("in google", "")
            else:
                pass
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak("Searching in Google. Got it")
            webbrowser.get(chrome_path).open(f"https://www.google.com.tr/search?q={query}")


        elif ("open" in query or "open about" in query) and ("google" in query) and ("jarvis" in query):
            if "open about" in query:
                query=query.replace("open about", "")
            else:
                pass
            if "open" in query:
                query=query.replace("open", "")
            else:
                pass
            if "in google" in query:
                query=query.replace("in google", "")
            else:
                pass
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak("Searching in Google. Got it")
            webbrowser.get(chrome_path).open(f"https://www.google.com.tr/search?q={query}")


        elif ("watch in youtube" in query or "watch something in youtube" in query) and ("jarvis" in query):
            wat=input("What do you want to watch: ")
            if "open" in wat:
                wat=wat.replace("open", "")
            else:
                pass
            if "in youtube" in wat:
                wat=wat.replace("in youtube", "")
            else:
                pass
            if "jarvis" in wat:
                wat=wat.replace("jarvis", "")
            else:
                pass
            speak("Opening youtube....")
            webbrowser.get(chrome_path).open(f"https://www.youtube.com/search?q={wat}")


        elif ("play" in query) and ("local music" in query) and ("jarvis" in query):
            music_folder="D:/Personal/Songs"
            songs=os.listdir(music_folder)
            # print(songs)
            try:
                selected=songs[k]
                print(f"Playing \"{selected}\" song:")
                os.startfile(os.path.join(music_folder, selected))
            except Exception as e:
                speak("I'm Sorry, some error occured, Can u plz try it again?")
                print("Plz try it again after some time.")


        elif ("play" in query) and ("in youtube" in query) and ("jarvis" in query):
            if "play" in query:
                query=query.replace("play", "")
            else:
                pass 
            if "in youtube" in query:
                query=query.replace("in youtube", "")
            else:
                pass
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak(f"playing {query}")
            pywhatkit.playonyt(query)


        elif ("play" in query) and ("in spotify" in query) and ("jarvis" in query):
            if "play" in query:
                query=query.replace("play", "")
            else:
                pass 
            if "song" in query:
                query=query.replace("song", "")
            else:
                pass
            if "in spotify" in query:
                query=query.replace("in spotify", "")
            else:
                pass
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak(f"playing {query}")
            os.system("spotify")
            time.sleep(20)
            pyautogui.keyDown("ctrl")
            pyautogui.press("l")
            pyautogui.keyUp("ctrl")
            time.sleep(3)
            pyautogui.write(query)
            time.sleep(5)
            pyautogui.press("enter")
            pyautogui.press("pagedown")
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.press("shift")
            pyautogui.press("enter")


        elif ("in youtube" in query) and ("jarvis" in query):
            if "open" in query:
                query=query.replace("open", "")
            else:
                pass 
            if "in youtube" in query:
                query=query.replace("in youtube", "")
            else:
                pass
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak("Opening youtube....")
            webbrowser.get(chrome_path).open(f"https://www.youtube.com/search?q={query}")


        elif ("play" in query) and ("jarvis" in query):
            if "play" in query:
                query=query.replace("play", "")
            else:
                pass 
            if "in youtube" in query:
                query=query.replace("in youtube", "")
            else:
                pass
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak(f"playing {query}")
            print(query)
            pywhatkit.playonyt(query)


        elif ("youtube" in query) and ("jarvis" in query):
            webbrowser.get(chrome_path).open("youtube.com")


        elif ("google" in query) and ("jarvis" in query):
            webbrowser.get(chrome_path).open("google.com")


        elif ("facebook" in query or "fb" in query) and ("jarvis" in query):
            webbrowser.get(chrome_path).open("facebook.com")


        elif ("chrome" in query) and ("jarvis" in query):
            pyautogui.keyDown("win")
            pyautogui.press("2")
            pyautogui.keyUp("win")


        elif ("new chrome" in query) and ("jarvis" in query):
            ch_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
            os.startfile(ch_path)


        elif ("chatgpt" in query) and ("jarvis" in query):
            webbrowser.get(chrome_path).open("chat.openai.com")


        elif ("wikipedia" in query) and ("jarvis" in query):
            webbrowser.get(chrome_path).open("wikipedia.com")


        elif ("amazon" in query) and ("jarvis" in query):
            webbrowser.get(chrome_path).open("amazon.com")


        elif ("flipkart" in query) and ("jarvis" in query):
            webbrowser.get(chrome_path).open("flipkart.com")


        elif ("vs code" in query) and ("jarvis" in query):
            code_path="C:/Users/hp/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(code_path)


        elif ("file manager" in query or "this pc" in query) and ("jarvis" in query):
            pyautogui.keyDown("win")
            pyautogui.press("1")
            pyautogui.keyUp("win")


        elif ("new file manager" in query or "new this pc" in query) and ("jarvis" in query):
            fm_path="D:/"
            os.startfile(fm_path)


        elif ("what can you do" in query) and ("jarvis" in query):
            speak("because i am a small and simple AI program, I may not be able to help you out in big works or majority of the things, but i can try to help you by doing some of your minor works, please allow me to try and help you a little bit.")
                  

        elif ("message" in query or "mssge" in query) and ("jarvis" in query):
            num=input("Enter the phone number: ")
            mssge=input("Enter the message: ")
            hr=int(input("Enter the time in hours: "))
            mins=int(input("Enter the time in mins: "))
            pywhatkit.sendwhatmsg(num, mssge, hr, mins)
            pyautogui.click(1050, 950)
            keyboard.press_and_release("enter")


        elif ("whatsapp" in query) and ("jarvis" in query):
            pyautogui.keyDown("win")
            pyautogui.press("3")
            pyautogui.keyUp("win")


        elif ("new whatsapp" in query) and ("jarvis" in query):
            whats="C:/Users/hp/AppData/Local/WhatsApp/WhatsApp.exe"
            os.startfile(whats)


        elif ("joke" in query or "jokes" in query) and ("jarvis" in query):
            jo=pyjokes.get_joke()
            print(jo)
            speak(jo)


        elif ("news" in query) and ("jarvis" in query):
            webbrowser.get(chrome_path).open("timesofindia.indiatimes.com")


        elif ("who are you" in query or "what are you" in query) and ("jarvis" in query):
            print("This is Jarvis, Sir")
            speak("This is Jarvis Sir")
            print("I am an AI program, created to assist you")
            speak("I am an AI program, created to assist you")  


        elif ("your name" in query) and ("jarvis" in query):
            print("I am \"Jarvis\" sir")
            speak("I am \"Jarvis\" sir")               

               
        elif ("spotify" in query) and ("jarvis" in query):
            os.system("spotify")


        elif ("instagram" in query or "insta" in query) and ("jarvis" in query):
            insts="C:/Users/hp/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/Instagram"
            os.startfile(insts)


        elif ("greet" in query) and ("jarvis" in query):
            query=query.replace("greet", "")
            if "me" in query:
                speak("Hello Vishwas")
            else:
                speak(f"Hello {query}")
            speak("How are you doing?")
            reply=input("How are you doing? ")
            if "fine" in reply or "good" in reply:
                speak("Nice, happy to hear that!")
            else:
                speak("ohhhh!, hoping for you to be better soon.")   


        elif ("calculator" in query or "calci" in query or "calculate" in query) and ("jarvis" in query):
            cal="C:/Windows/System32/calc.exe"
            os.startfile(cal)


        elif ("date" in query) and ("jarvis" in query):
            d=datetime.datetime.now().strftime("%d,\t%B,\t%Y\t")
            dp=datetime.datetime.now().strftime("%d %B %Y")
            ad=datetime.datetime.now().strftime("%A")
            print(f"Today's Date is: {dp}")
            speak(f"Today's Date is, {d}")
            print(f"It's {ad} today.")
            speak(f"& It's {ad} today.")


        elif ("day" in query) and ("jarvis" in query):
            ad=datetime.datetime.now().strftime("%A")
            print(f"It's {ad} today.")
            speak(f"It's {ad} today.")
            

        elif ("time" in query) and ("jarvis" in query):
            tp=datetime.datetime.now().strftime("%I:%M %p")
            t=datetime.datetime.now().strftime("%I:,\t%M\t%p")
            print(f"The Time at this moment is: {tp}\n")
            speak(f"The time at this moment is, {t}")


        elif ("set an alarm" in query or "alarm" in query) and ("jarvis" in query):
            music_folder="D:/Personal/Songs"
            songs=os.listdir(music_folder)
            tp=datetime.datetime.now().strftime("%I:%M %p")
            td=datetime.datetime.now().strftime("%I:%M")
            print(f"Current time: {tp}")
            alarm=input("Enter the time for alarm: ")
            while(True):
                now=datetime.datetime.now()
                ch=now.strftime("%I")
                cm=now.strftime("%M")
                tm=ch+":"+cm
                if(alarm==tm):
                    os.startfile(os.path.join(music_folder, "Arjan Vailly.mp3"))
                    break
                else:
                    pass


        elif ("good" in query or "amazing" in query or "excellent" in query or "superb" in query) and ("jarvis" in query):
            speak("I am very much thankful for your compliment, I am happy that you found me useful and worthy.  Thank you very much")


        elif ("virtual desktop" in query or "vd" in query or "v d" in query) and ("jarvis" in query):
            pyautogui.keyDown("ctrl")
            pyautogui.keyDown("win")
            pyautogui.press("d")
            pyautogui.keyUp("win")
            pyautogui.keyUp("ctrl")


        elif ("open" in query) and ("jarvis" in query):
            link=query.replace("open", "")
            webbrowser.get(chrome_path).open(link)


        elif ("hi " in query or "hello " in query or "hey " in query) and ("how are you" in query or "how are you doing" in query) and ("jarvis" in query):
            speak("Hello sir")
            speak("I am fine, Thank you!")
            speak("How are you Sir")
            reply=input("How are you Sir? ")
            if "fine" in reply or "good" in reply:
                speak("Nice, happy to hear that!")
            else:
                speak("ohhhh!, hoping for you to be better soon.")


        elif ("how are you" in query) and ("jarvis" in query):
            print("I am fine, Thank you!")
            speak("I am fine, Thank you!")
            speak("How are you Sir")
            reply=input("How are you Sir? ")
            if "fine" in reply or "good" in reply:
                speak("Nice, happy to hear that!")
            else:
                speak("ohhhh!, hoping for you to be better soon.")


        elif ("game" in query or "games" in query) and ("jarvis" in query):
            speak("Fine, please check out the available games list and select the game you want to play")
            print("Games Available:")
            print("1) Guess the number\n2) Hand Cricket\n3) Hang Man\n4) Rock Paper Scissors\n5) Tic Tac Toe")
            play=int(input("Which game would you like to play: "))
            if(play==1):
                subprocess.run(["python", "D:\Educational\Python\project_guess_the_number.py"])
            elif(play==2):
                subprocess.run(["python", "D:\Educational\Python\project_hand_cricket.py"])
            elif(play==3):
                subprocess.run(["python", "D:\Educational\Python\project_hang_man.py"])
            elif(play==4):
                subprocess.run(["python","D:\Educational\Python\project_rock_paper_scissors.py"])
            elif(play==5):
                subprocess.run(["python", "D:\Educational\Python\project_tic_tac_toe.py"])
            elif(play>5):
                print("There are only 5 games available for now")
            else:
                print("Please type the serial number of the game you want to play ")


        elif ("hi" in query or "hello" in query or "hey" in query) and ("jarvis" in query):
            speak("Hello Sir, How are you doing?")
            reply=input("How are you doing? ")
            if "fine" in reply or "good" in reply:
                speak("Nice, happy to hear that!")
            else:
                speak("ohhhh!, hoping for you to be better soon.")


        elif ("what" in query) and ("jarvis" in query):
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak("Searching in Google. Got it")
            webbrowser.get(chrome_path).open(f"https://www.google.com.tr/search?q={query}")


        elif ("which" in query) and ("jarvis" in query):
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak("Searching in Google. Got it")
            webbrowser.get(chrome_path).open(f"https://www.google.com.tr/search?q={query}")


        elif ("who" in query) and ("jarvis" in query):
            if "jarvis" in query:
                query=query.replace("jarvis", "")
            else:
                pass
            if "," in query:
                query=query.replace(",", "")
            else:
                pass
            speak("Searching in Google. Got it")
            webbrowser.get(chrome_path).open(f"https://www.google.com.tr/search?q={query}")


        elif "jarvis" in query or "hey jarvis" in query:
            print("Jarvis 1 point O, in your service Sir")
            speak("Jarvis 1 point O, in your service Sir")


        elif "quit" in query or "exit" in query or "quit jarvis" in query or "jarvis quit" in query or "exit jarvis" in query or "jarvis exit" in query:
            break


        elif "jarvis" not in query:
            if "type" in mode:
                print("\"JARVIS\" was not identified in the sentence")
            elif "speak" in mode:
                print("\"JARVIS\" was not identified in the sentence")
                listen().lower()
            




        else:
            break

    print("\nThis is Jarvis, Signing off!")
    speak("This is Jarvis, Signing off")
    print("Good Bye...\n")
    speak("Good Bye")
    
    
            