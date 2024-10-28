# Current Ver: TextPY OS V1.0

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

inputusername = input ("Please input your USERNAME: ")
if inputusername == Username:   print ("Correct")
else:
    print (colorama.Style.BRIGHT)
    print (colorama.Fore.RED + "Incorrect. The program will now close." + colorama.Style.RESET_ALL)
    time.sleep(2)
    quit()

inputpassword = input ("Please input your PASSWORD: ")
if inputpassword == Password:   print ("Correct")
else:
    print (colorama.Style.BRIGHT)
    print (colorama.Fore.RED + "Incorrect, The program will now close." + colorama.Style.RESET_ALL)
    time.sleep(2)
    quit()

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
        UCTypePrintStatement = input("")
        print (UCTypePrintStatement)
        DoAgain = input("Would you like to try again?: ").lower().strip()
        if DoAgain == "yes":
            UCDoAgain()
        else:
            print ("Program will close shortly...")
            time.sleep(1.5)
            quit()
    
    if UCType == "input":
        print ("WORK IN PROGRESS")
        UCDoAgain()
    

#Software Variables
Commands = ["-Commands, -Usercode"]

Directory = input("").lower()

if Directory == "-commands":
    print(Commands)
    Directory = input("").lower()
if Directory == "-usercode":
    Usercode()