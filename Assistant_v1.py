import pyttsx3
import os
import subprocess
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 35)

r = sr.Recognizer()

pyttsx3.speak("Welcome to Varun's Personal Assistant and How may i help you")
print(" ")
print("                                Welcome to my Small PersonalAssistant                                                         ")
print("How could help you?")

# r = sr.Recognizer()
# def voice():
#     with sr.Microphone() as source:
#         print("Speak Anything :")
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio)
#             print("You said : {}".format(text))
#             return text
#         except:
#             print("Sorry could not recognize what you said")
        
while(True):
    print("Enter Here: ", end='')
    p = input()
    # print(text)
    #pyttsx3.speak("What should i do more?")
    # print(p)
    if(("run" in p) or ("open" in p) or ("start" in p)) and (("chrome" in p) or ("google chrome" in p)):
        pyttsx3.speak("Okay would you like to open Google Chrome in Incognito mode?.")
        q = input("Incognito? ")
        if q == "no":
            pyttsx3.speak("Okay tell me which website would you like to surf?")
            website = input("Website: ")
            w = website + ".com"
            pyttsx3.speak("Opening {} for you".format(website))
            os.system("chrome.exe {}".format(w))

        if q == 'yes':
            pyttsx3.speak("Okay tell me which website would you like to surf?")
            website = input("Website: ")
            w = website + ".com"
            pyttsx3.speak("Opening {} for you in private mode".format(website))
            os.system("chrome.exe {} -incognito".format(w))
            # cmd="chrome -incognito"
            # subprocess.call(cmd, shell=True)
    
    elif(("can"in p) and ("you" in p) and ("do" in p)):
        pyttsx3.speak("I can do multiple tasks like opening browsers, setting alarms, open text or code editors for you and much more even lock your screen for privacy!")
        
    elif(("set alarm" in p) or ("alarm" in p) or ("wake" in p)):
        pyttsx3.speak("Okayy opening alarms for you ")
        pyttsx3.speak("Just set your alarm I'll wake you up!")
        cmd = "explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App"
        subprocess.call(cmd, shell=True)
    # explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App

    elif(("run" in p) or ("open" in p) or ("start" in p)) and (("mozilla" in p) or ("mozilla firefox" in p) or ("firefox" in p)):
        pyttsx3.speak("Okay opening Mozilla Firefox.")
        os.system("firefox")

    elif(("run" in p) or ("open" in p) or ("start" in p)) and (("vs code" in p) or ("code editor" in p) or ("visual studio" in p)):
        pyttsx3.speak("Okay opening Visual Studio Code for you!")
        os.system("code")

    # elif(("run" in p) or ("open" in p)) and (("incognito mode" in p) or ("private" in p)):
    #     pyttsx3.speak("Okay opening Google Chrome in incognito mode.")
    #     cmd="chrome -incognito"
    #     subprocess.call(cmd, shell=True)

    elif(("photos" in p) or ("images" in p) or ("gallery" in p)):
        os.system("chrome.exe https://photos.google.com/")

    elif (("open" in p) or ("run" in p)) and (("notepad" in p)):
        pyttsx3.speak("Okay opening Notepad.")
        os.system("notepad")
    
    elif(("lock" in p) and ("screen" in p)):
        pyttsx3.speak("Okay Locking your screen! Are you sure?")
        perm = input("Yes/No: ")
        if perm=="Yes" or perm=="yes" or perm=='y' or perm=="Y" :
            cmd = "rundll32.exe user32.dll,LockWorkStation"
            subprocess.call(cmd, shell=True)
        else:
            pass
    
    elif (p=="exit" or p=="quit" or p=="thank you" or ("bye" in p)):
        pyttsx3.speak("Thank you see you again Varun!")
        cmd="exit"
        subprocess.call(cmd,shell=True)
        break
    
    else:
        print("I'am sorry am still under development mode can't understand you please retry")
        pyttsx3.speak("I'am sorry am still under development mode can't understand you please retry!")
        pass

    # elif int(p) == 2:
    #     pyttsx3.speak("Okay opening Notepad.")
    # #     os.system("notepad")

    # else:
    #     print("There is an ambiguity!")

    #     except:
    #         print("Sorry could not recognize what you said")
    #         break









