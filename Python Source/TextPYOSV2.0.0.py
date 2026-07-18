#Version
Version = 2.0
Subversion = 0.0

#Imports
import time

print("Use Y/N answers when prompted.")
print("TextPYOS Does not currently save any information.")
time.sleep(0.5)

#Setup

def DevMenu():
    #More coming soon.
    def TimeOverrideDevFunc():
        TimeOverride = input("Disable program pause/wait?: ").strip().lower()
        if TimeOverride == "y":
            def SleepTimeOverride(_=None):
                pass
            time.sleep = SleepTimeOverride
        else:
            pass

    DevMenuOps = {
        "timeoverride",
        "exit"
    }
    DevOpInput = input("").strip().lower()
    if DevOpInput in DevMenuOps:
        if DevOpInput == "timeoverride":
            TimeOverrideDevFunc()
        elif DevOpInput == "exit":
            DirectoryFUNC()

def UsernameCreation():
        global Username
        Username = input("Username: ")
        time.sleep(0.5)
        print(f"Username is: {Username}")
UsernameCreation()

def PasswordCreation():
        global Password
        Password = input("Password: ")
PasswordCreation()

#Greeting
time.sleep(1)
print(f"Welcome to TextPYOS! The current version is: {Version}, Subversion: {Subversion}")
time.sleep(1)
print("use a - symbol before executing a command. (e.x. -help)")

#Post-signin FUNCTIONS
def UsercodeApp():
    AppDirections = "Select an Input (Requires user to input string, number, ect) or Print (Prints what is typed)"
    DirectionsRequied = input("Would you like to see the instructions? Y/N: ").strip().lower()
    if DirectionsRequied == "y":
        time.sleep(0.5)
        print(AppDirections)
    elif DirectionsRequied == "n":
        pass
    else:
        print("Invalid Input. Y/N Required.")
        UsercodeApp()
    StatementType = input("[INPUT] or [PRINT] statement?: ").strip().lower()
    if StatementType == "input":
        InputStatement = input("Input Statement: ")
        InputStatementReply = input(f"{InputStatement}: ")
        print(InputStatementReply)
    elif StatementType == "print":
        PrintStatment = input("Print Statement: ")
        print(PrintStatment)
    else:
        print("Invalid. INPUT or PRINT required.")
    UCARedo = input("Try Again? Y/N: ")
    if UCARedo == "y":
        time.sleep(0.5)
        UsercodeApp()
    elif UCARedo == "n":
        DirectoryFUNC()

def HelpCenter():
    HelpList = ["Apps", "Version", "Other"]
    AppsHelpList = ["Usercode"]
    OtherHelpList = ["System Interaction", "Source Code"]
    print("Welcome to the TextPYOS Helpcenter. Current options include:" + str(HelpList))
    HelpOption = input("Choice: ").strip().lower()
    if HelpOption == "version":
        print(f"Version: {Version}, Subversion: {Subversion}")
    elif HelpOption == "apps":
        print(AppsHelpList)
        AppHelp = input("App: ").strip().lower()
        if AppHelp == "usercode":
            print("Usercode allows you to make [input] or [print] statements.")
            print("Input statements require a user to type, and with usercode, it will print what is typed.")
            print("Print statements are a statement that is typed and printed, no input required.")
        else:
            print("Invalid Input.")
            HelpCenter()
    elif HelpOption == "other":
        print(OtherHelpList)
        OtherHelp = input("Choice: ").strip().lower()
        if OtherHelp == "system interaction":
            print("System interaction is done via a set of Y/N (yes/no) interactions.")
            print("System app calling is done via -[app name]")
        elif OtherHelp == "source code":
            print("Source Code can be found via the '-github' app.")
            print("Or at: https://github.com/The-TextPYOS-Foundation/TextPYOS")
        else:
            print("Invalid Input.")
            DirectoryFUNC()
    else:
        print("Invalid Input")
        HelpCenter()
    DoAgain = input("Ask Another Question? Y/N: ").strip().lower()
    if DoAgain == "y":
        HelpCenter()
    else:
        DirectoryFUNC()

def UsernameReset():
    global Username
    print(f"Your current Username is: {Username}")
    time.sleep(0.5)
    Username = input("Set new Username: ").strip().lower()
    time.sleep(0.5)
    print(f"Your new username is: {Username}")
    time.sleep(0.5)
    DirectoryFUNC()

def PasswordReset():
    global Password
    print(f"Your current Password is: {Password}")
    time.sleep(0.5)
    Password = input("Set new Password: ").strip().lower()
    time.sleep(0.5)
    print(f"Your new password is: {Password}")
    time.sleep(0.5)
    DirectoryFUNC()

def CalculatorApp():
    Operators = ["+", "-", "/", "*"]
    print(Operators)
    try:
        NumOne = float(input("First Digit: ").strip())
        NumTwo = float(input("Second Digit: ").strip())
        OperatorChoice = input("Choose Operator: ").strip()
        if OperatorChoice == "+":
            Equals = NumOne + NumTwo
            print(Equals)
        elif OperatorChoice == "-":
            Equals = NumOne - NumTwo
            print(Equals)
        elif OperatorChoice == "/":
            Equals = NumOne / NumTwo
            print(Equals)
        elif OperatorChoice == "*":
            Equals = NumOne * NumTwo
            print(Equals)
        else:
            print("Invalid Input. Use Operator.")
            CalculatorApp()
    except(ValueError):
        print("Invalid Input.")
        CalculatorApp()
    except(ZeroDivisionError):
        print("Zero Error.")
        CalculatorApp()
    CalcRedo = input("Try Again? Y/N: ").strip().lower()
    if CalcRedo == "y":
        CalculatorApp()
    else:
        DirectoryFUNC()

def GithubLink():
    print("https://github.com/The-TextPYOS-Foundation/TextPYOS")
    time.sleep(1.5)
    DirectoryFUNC()

#Use DirectoryFUNC() to send back to directory.

def DirectoryFUNC():
    uinput = input("")
    if uinput == "-ucd":
        UsercodeApp()
    elif uinput == "-hlpc":
        HelpCenter()
    elif uinput == "-user-reset":
        UsernameReset()
    elif uinput == "-pass-reset":
        PasswordReset()
    elif uinput == "-calc":
        CalculatorApp()
    elif uinput == "-ghb":
        GithubLink()
    elif uinput == "-DMenu":
        DevMenu()
    elif uinput == "-exit":
        exit()
    else:
        print("Invalid Input. Try again.")
DirectoryFUNC()