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
print (colorama.Fore.MAGENTA + "Starting quantum stablizers...")
time.sleep(1)
print (colorama.Fore.BLUE + "Doing things...")
time.sleep(0.5)
print (colorama.Fore.GREEN + "ENTERING..." + colorama.Style.RESET_ALL)
time.sleep(2)

#Login
def UsernameInput():
    UsernameAttempts = 0
    while UsernameAttempts <= 2:
        InputUsername = input("Please input your username: ")
        if InputUsername == Username:
            print ("Correct")
            break
        else:
            print ("Incorrect")
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
            print ("Correct")
            break
        else:
            print ("Incorrect")
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
    

#Software Variables
Commands = ["-Commands, -Usercode"]

Directory = input("").lower()

if Directory == "-commands":
    print(Commands)
    Directory = input("").lower()

if Directory == "-usercode":
    Usercode()
else:
    print ("Error, invaid input detected. Please try again.")
    Directory = input("").lower()