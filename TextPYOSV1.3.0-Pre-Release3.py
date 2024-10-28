#Pre-Variables
Version = 1.3
Directory = input("").lower()

#Imports
import time
import colorama
colorama.init()

#Starting stages
Username = input ("What would you like your username to be?: ")

Password = input ("What would you like your password to be?: ")

time.sleep(2)

print (colorama.Fore.GREEN + "Starting...")
time.sleep(1)
print (colorama.Style.BRIGHT + colorama.Fore.MAGENTA + "Starting quantum stablizers...")
time.sleep(1)
print (colorama.Fore.CYAN + "Doing things...")
time.sleep(1)
print (colorama.Fore.GREEN + "ENTERING..." + colorama.Style.RESET_ALL)
time.sleep(2)

#Login
def UsernameInput():
    UsernameAttempts = 0
    while UsernameAttempts <= 2:
        InputUsername = input("Please input your username: ")
        if InputUsername == Username:
            print (colorama.Style.BRIGHT + colorama.Fore.GREEN + "Correct" + colorama.Style.RESET_ALL)
            break
        else:
            print (colorama.Style.BRIGHT + colorama.Fore.RED + "Incorrect" + colorama.Style.RESET_ALL)
            UsernameAttempts += 1
        if UsernameAttempts > 2:
            print ("You have incorrectly entered your username too many times, the program will now close.")
            time.sleep(1)
            quit()

def PasswordInput():
    PasswordAttempts = 0
    while PasswordAttempts <= 2:
        InputPassword = input("Please input your password: ")
        if InputPassword == Password:
            print (colorama.Style.BRIGHT + colorama.Fore.GREEN + "Correct" + colorama.Style.RESET_ALL)
            break
        else:
            print (colorama.Style.BRIGHT + colorama.Fore.RED + "Incorrect" + colorama.Style.RESET_ALL)
            PasswordAttempts += 1
        if PasswordAttempts > 2:
            print ("You have incorrectly entered your password too many times, the program will now close.")
            time.sleep(1)
            quit()

UsernameInput()
PasswordInput()

#Software
time.sleep(1)
print ("Hello! Welcome to TextPY OS! The current version is: ", Version, " This software is a work in progress and will be built upon in further updates.")
time.sleep(1)
print ("The directory is a feature that allowes the user to navigate through the program. To see a list of all current commands say '-Commands' ")

#Directory should be cleared at the end of every process. (Enter Directory value to () to clear directory and create a new Directly = input ("") to send back to directory.)

#Post-signin FUNCTIONS
def UCDoAgain():
    Usercode()

def DirectorySendback():
    Directory == input("").lower()

def Usercode():
    UCType = input("What kind of command would you like to make: [INPUT] or [PRINT]?: ").lower().strip()
    if UCType == "print":
        print ("Please type your print statement: ")
        UCPrintStatement = input("")
        print (UCPrintStatement)
        DoAgain = input("Would you like to try again?: ").lower().strip()
        if DoAgain == "yes":
            UCDoAgain()
        else:
            print ("Program will close shortly...")
            time.sleep(1.5)
            quit()
    
    if UCType == "input":
        print ("Please type your input statement: ")
        UCInputStatement = input("")
        UCInputStatementResponse = input("Question = " + UCInputStatement + ": ")
        print (UCInputStatementResponse)
        DoAgain = input("Would you like to try again?: ").lower().strip()
        if DoAgain == "yes":
            UCDoAgain()
        else:
            print ("Program will close shortly...")
            time.sleep(1.5)
            quit()

def helpcommand():
    def HCDoAgain():
        helpcommand()
    HelpOptions = ["Commands" , "Apps" , "Version"]
    print ("Welcome to the TextPYOS helpcenter! Here, you can check what commands do, and how to use them!")
    time.sleep(0.5)
    print(HelpOptions)
    HCType = input ("What do you need help with today?: ").strip().lower()
    
    if HCType == "commands":
        print("WIP")
    
    if HCType == "apps":
            def helpcommandAPP():
                if HCType == "apps":
                    HCTApp = input ("What app do you need help with?: ").strip().lower()
                    if HCTApp == "usercode":
                        print ("To use usercode, you must first decide if you want to make an input, or print statement.")
                        time.sleep(0.5)
                        print ("A print statment will print (repeat) what you prompted it to say. [e.x: 'hello world'], it will respond with 'hello world'")
                        time.sleep(1)
                        print ("An input statement however, will prompt the user with your input. [e.x: ['favorite snack'] and the user will be prompted to respond to 'favorite snack'")
                    else:
                        print ("Error, invalid input detected.")
                        helpcommandAPP()
    
    if HCType == "apps":
        helpcommandAPP()
        HCTypeAPPSDoAgain = input ("Do you want to ask another question?: ").strip().lower()
        if HCTypeAPPSDoAgain == "yes":
            HCDoAgain()
        else:
            print ("Sending back to directory...")
            DirectorySendback()


    if HCType == "version":
        print ("You are currently running on version: " + Version)
        if input ("Anything else you need help with?: ").strip().lower() == "Yes":
            helpcommand()
        else:
            print ("Okay, you will be sent back to the directory.")
            DirectorySendback()


#Software Variables
Commands = ["-Commands, -Usercode, -Help"]

Directory = input("").lower()

if Directory == "-commands":
    print(Commands)
    Directory = input("").lower()

if Directory == "-usercode":
    Usercode()

if Directory == "-help":
    helpcommand()

else:
    print ("Error, invaid input detected. Please try again.")
    Directory = input("").lower()