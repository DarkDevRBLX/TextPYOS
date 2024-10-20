# Current Ver: TextPY OS V1.0

#Pre-Variables
Version = 1.0

#Imports
import time


#Starting stages
Username = input ("What would you like your username to be?: ")

if Username == "Guest" or  Username == "guest":
    Guestproceed = input ("Are you sure you want to proceed as guest? This is an in-development feature: ")
    if Guestproceed == "Yes" or Guestproceed == "yes":
        print ("Okay! We will proceed.")
    if Guestproceed == "No" or Guestproceed == "no":
        print ("This window will now close.")
        time.sleep(2) ;quit()

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
if inputusername != Username:   print ("Incorrect, The program will now close.")
if inputusername != Username:   time.sleep(2) ;quit()

inputpassword = input ("Please input your PASSWORD: ")
if inputpassword == Password:   print ("Correct")
if inputpassword != Password:   print ("Incorrect, The program will now close.")
if inputpassword != Password:   time.sleep(2) ;quit()

#Software
time.sleep(1)
print ("Hello! Welcome to TextPY OS! The current version is: ", Version, " This software is a work in progress and will be built upon in further updates.")
time.sleep(1)
print ("The directory is a feature that allowes the user to navigate through the program. To see a list of all current commands say '-Commands' ")

#Directory should be cleared at the end of every process. (Enter Directory value to () to clear directory and create a new Directly = input ("") to send back to directory.)

#Software Variables
Commands = ["NAN"]

Directory = input ("")

if Directory == "-Commands" or Directory == "-commands":
    print (Commands)