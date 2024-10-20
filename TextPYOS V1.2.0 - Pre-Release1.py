# Current Ver: TextPY OS V1.0

#Pre-Variables
Version = 1.2

#Imports
import time

#Starting stages
Username = input ("What would you like your username to be?: ")

Password = input ("What would you like your password to be?: ")

time.sleep(2)

print ("Starting...")
time.sleep(1)
print ("Starting quantum stablizers...")
time.sleep(1)
print ("Doing things...")
time.sleep(0.5)
print ("ENTERING...")

time.sleep(2)

#Login

inputusername = input ("Please input your USERNAME: ")
if inputusername == Username:   print ("Correct")
else:
    print ("Incorrect. The program will now close.")
    time.sleep(2)
    quit()

inputpassword = input ("Please input your PASSWORD: ")
if inputpassword == Password:   print ("Correct")
else:
    print ("Incorrect, The program will now close.")
    time.sleep(2)
    quit()

#Software
time.sleep(1)
print ("Hello! Welcome to TextPY OS! The current version is: ", Version, " This software is a work in progress and will be built upon in further updates.")
time.sleep(1)
print ("The directory is a feature that allowes the user to navigate through the program. To see a list of all current commands say '-Commands' ")

#Directory should be cleared at the end of every process. (Enter Directory value to () to clear directory and create a new Directly = input ("") to send back to directory.)

#Post-signin FUNCTIONS

def chatbot():
    print ("Chatbot is currently a WIP feature, and is limited.")
    time.sleep(0.5)
    CBotUsername = input("Hello! I am chatbot. Whats your name?: ")
    print ("Very nice to meet you,", CBotUsername)
    CBotChatOptions = ["favorite things"]
    print ("The current things I can talk about are:", CBotChatOptions)
    CBotChat = input("What would you like to talk about today?: ").lower()
    time.sleep(0.1)
    
    if CBotChat == "favorite things":
        print ("Alright! What are some of your favorite things?: ")
        CBotFavorite = input("").lower()
        print ("Thats cool! I also like", CBotFavorite)
    else:
        print ("Error, unknown input detected. Please try again.")


#Software Variables
Commands = ["-chatbot"]

Directory = input ("")

if Directory.lower() == "-commands":
    print (Commands)
    Directory = input("")
if Directory.lower() == "-chatbot":
    chatbot()