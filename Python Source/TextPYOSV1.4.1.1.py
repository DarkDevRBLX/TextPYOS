#Pre-Variables
Version = 1.4

#Imports
import time
import colorama

def ColoramaIsEnabledInput():
    global ColoramaEnabled
    ColoramaEnabled = input("Do you want to enable colorama? Y/N: ").strip().lower()
    global ColoramaEnabledNum
    if ColoramaEnabled == "y" or ColoramaEnabled == "yes":
        colorama.init()
        ColoramaEnabledNum = 1
        time.sleep(0.5)
        print("Colorama is now enabled!")
    elif ColoramaEnabled == "n" or ColoramaEnabled == "no":
        time.sleep(0.5)
        print ("Colorama will not be enabled.")
        ColoramaEnabledNum = 0
    else:
        print("Error, invalid input detected! Please try again.")
        ColoramaIsEnabledInput()
ColoramaIsEnabledInput()

def UsernameCreation():
    global Username
    Username = input("What would you like your username to be?: ")
    if ColoramaEnabledNum == 1:
        time.sleep(0.5)
        print (colorama.Fore.GREEN + "Your username is: " + colorama.Style.RESET_ALL + Username)
    elif ColoramaEnabledNum == 0:
        time.sleep(0.5)
        print ("Your username is: " + Username)
UsernameCreation()

def PasswordCreation():
    global Password
    Password = input("What would you like your password to be?: ")
    if ColoramaEnabledNum == 1:
        time.sleep(0.5)
        print (colorama.Fore.GREEN + "Your password is: " + colorama.Style.RESET_ALL + Password)
    elif ColoramaEnabledNum == 0:
        time.sleep(0.5)
        print ("Your username is: " + Password)
PasswordCreation()

#Software
time.sleep(1)
print ("Hello! Welcome to TextPY OS! The current version is: ", Version, " This software is a work in progress and will be built upon in further updates.")
time.sleep(1)
print ("The directory is a feature that allowes the user to navigate through the program. To see a reminder of commands, say '-commands'")

#Post-signin FUNCTIONS
def UCDoAgain():
    Usercode()

def Usercode():
    UCType = input("What kind of command would you like to make: [INPUT] or [PRINT]?: ").lower().strip()
    if UCType == "print":
        print ("Please type your print statement: ")
        UCPrintStatement = input("")
        print ("print = " + "'" + UCPrintStatement + "'")
        DoAgain = input("Would you like to try again?: ").lower().strip()
        if DoAgain == "yes":
            UCDoAgain()
        else:
            print ("Redirecting to Directory...")
            time.sleep(1)
            DirectoryFUNC()
    
    if UCType == "input":
        print ("Please type your input statement: ")
        UCInputStatement = input("")
        UCInputStatementResponse = input("Question = " + UCInputStatement + ": ")
        print ("answer: " + "'" + UCInputStatementResponse + "'")
        DoAgain = input("Would you like to try again?: ").lower().strip()
        if DoAgain == "yes":
            UCDoAgain()
        else:
            print ("Redirecting to Directory...")
            DirectoryFUNC()

def helpcommand():
    def HCDoAgain():
        helpcommand()
    HelpOptions = ["Apps" , "Version"]
    print ("Welcome to the TextPYOS helpcenter! Here, you can check what commands do, and how to use them!")
    time.sleep(0.5)
    print(HelpOptions)
    HCType = input ("What do you need help with today?: ").strip().lower()
    
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
            DirectoryFUNC()
    
    if HCType == "version":
        print ("You are currently running on version: ")
        print (Version)
        if input ("Anything else you need help with?: ").strip().lower() == "Yes":
            helpcommand()
        else:
            print ("Okay, you will be sent back to the directory.")
            DirectoryFUNC()

    else:
        print ("Unknown input detected")
        helpcommand()


def UsernameReset():
    global Username
    if ColoramaEnabledNum == 1:
        Username = input (colorama.Fore.GREEN + "What would you like your new username to be?: " + colorama.Style.RESET_ALL).strip().lower()
        time.sleep(0.5)
        print (colorama.Fore.GREEN + "Your new username is: " + colorama.Style.RESET_ALL + Username)
        time.sleep(0.5)
        DirectoryFUNC()
    elif ColoramaEnabledNum == 0:
        Username = input ("What would you like your new username to be?: ").strip().lower()
        time.sleep(0.5)
        print ("Your new username is" + Username)
        time.sleep(0.5)
        DirectoryFUNC()
    else:
        print ("Unknown input detected, please try again.")
        UsernameReset()

def PasswordReset():
    global Password
    if ColoramaEnabledNum == 1:
        Password = input (colorama.Fore.GREEN + "What would you like your new password to be?: " + colorama.Style.RESET_ALL).strip().lower()
        time.sleep(0.5)
        print (colorama.Fore.GREEN + "Your new password is: " + colorama.Style.RESET_ALL + Password)
        time.sleep(0.5)
        DirectoryFUNC()
    elif ColoramaEnabledNum == 0:
        Password = input ("What would you like your new username to be?: ").strip().lower()
        time.sleep(0.5)
        print ("Your new password is" + Password)
        time.sleep(0.5)
        DirectoryFUNC()
    else:
        print ("Unknown input detected, please try again.")
        PasswordReset()

def AccountSettings():
    print ("Welcome to the account settings menu.")
    time.sleep(0.3)
    AccSetInput = input ("What would you like to change? Username or password?: ").strip().lower()
    if AccSetInput == "password":
        PasswordReset()
    elif AccSetInput == "username":
        UsernameReset()
    else:
        print ("Error, unrecognized input detected, please try again.")
        AccountSettings()

def CalculatorApp():
    CalcAppAllowedFuncs = ["Addition", "Subtraction", "Division", "Multiplication"]
    print (CalcAppAllowedFuncs)
    CalcAppType = input ("What mode would you like?: ").strip().lower()
    if CalcAppType == "addition":
        try:
            CalcAdditionValA = float(input ("What would you like your first addition number to be?: ").strip())
            CalcAdditionValB = float(input ("What would you like your second addition number to be?: ").strip())
            CalcAdditionValTotal = (CalcAdditionValA + CalcAdditionValB)
            print (CalcAdditionValTotal)
            CalculatorAppDoAgain = input ("Would you like to perform another calculation?: ").strip().lower()
            if CalculatorAppDoAgain == "yes":
                CalculatorApp()
            else:
                print ("Redirecting to directory...")
                DirectoryFUNC()
        except ValueError:
            print ("Error, please enter a number.")
            CalculatorApp()
    elif CalcAppType == "subtraction":
        try:
            CalcSubtractionValA = float(input ("What would you like your first subtraction number to be?: ").strip())
            CalcSubtractionValB = float(input ("What would you like your second subtraction number to be?: ").strip())
            CalcSubtractionValTotal = (CalcSubtractionValA - CalcSubtractionValB)
            print (CalcSubtractionValTotal)
            CalculatorAppDoAgain = input ("Would you like to perform another calculation?: ").strip().lower()
            if CalculatorAppDoAgain == "yes":
                CalculatorApp()
            else:
                print ("Redirecting to directory...")
                DirectoryFUNC()
        except ValueError:
            print ("Error, please enter a number.")
            CalculatorApp()
    elif CalcAppType == "division":
        try:
            CalcDivisionValA = float(input ("What would you like your first division number to be?: ").strip())
            CalcDivisionValB = float(input ("What would you like your second division number to be?: ").strip())
            CalcDivisionValTotal = (CalcDivisionValA / CalcDivisionValB)
            print (CalcDivisionValTotal)
            CalculatorAppDoAgain = input ("Would you like to perform another calculation?: ").strip().lower()
            if CalculatorAppDoAgain == "yes":
                CalculatorApp()
            else:
                print ("Redirecting to directory...")
                DirectoryFUNC()
        except ValueError:
            print ("Error, please enter a number.")
            CalculatorApp()
    elif CalcAppType == "multiplication":
        try:
            CalcMultiplicationValA = float(input ("What would you like your first multiplication number to be?: ").strip())
            CalcMultiplicationValB = float(input ("What would you like your second multiplication number to be?: ").strip())
            CalcMultiplicationTotal = (CalcMultiplicationValA * CalcMultiplicationValB)
            print (CalcMultiplicationTotal)
            CalculatorAppDoAgain = input ("Would you like to perform another calculation?: ").strip().lower()
            if CalculatorAppDoAgain == "yes":
                CalculatorApp()
            else:
                print ("Redirecting to directory...")
                DirectoryFUNC()
        except ValueError:
            print ("Error, please enter a number.")
            CalculatorApp()
    else:
        print ("Error, unknown input detected.")
        CalculatorApp()



#Use DirectoryFUNC() to send back to or to execute the directory.
#Software Variables
def DirectoryFUNC():
    Commands = ["-usercode", "-help", "commands", "-calculator", "-AccountSettings", "-exit"]
    print ("The currently supported commands are: ")
    print (Commands)
    Directory = input("").strip().lower()

    if Directory == "-commands":
        print (Commands)
        DirectoryFUNC()
    elif Directory == "-help":
        helpcommand()
    elif Directory == "-usercode":
        Usercode()
    elif Directory == "-accountsettings":
        AccountSettings()
    elif Directory == "-calculator":
        CalculatorApp()
    elif Directory == "-exit":
        quit()
    else:
        print ("Error, unrecognized input detected. Please try again.")
        DirectoryFUNC()
DirectoryFUNC()