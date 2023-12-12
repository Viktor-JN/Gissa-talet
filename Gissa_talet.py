'''
Gissa_talet.PY: Gissa talet program

__author__  = "Viktor Johansson Nygren"
__version__ = "1.0.0"
__email__   = "viktor.johanssonnygren@elev.ga.ntig.se"
'''

import random as rand
from colors import bcolors
import os

guesses = 7
secret = rand.randint(1, 100)

os.system('cls')
print(bcolors.PURPLE + """
 _______  _______ _________ _______  _______  __________ _______  _        _______ _________
(  ____ \\__   __/(  ____ \(  ____ \(  ___  )  \__   __/(  ___  )( \      (  ____ \\__   __/
| (    \/   ) (   | (    \/| (    \/| (   ) |     ) (   | (   ) || (      | (    \/   ) (   
| |         | |   | (_____ | (_____ | (___) |     | |   | (___) || |      | (__       | |   
| | ____    | |   (_____  )(_____  )|  ___  |     | |   |  ___  || |      |  __)      | |   
| | \_  )   | |         ) |      ) || (   ) |     | |   | (   ) || |      | (         | |   
| (___) |___) (___/\____) |/\____) || )   ( |     | |   | )   ( || (____/\| (____/\   | |   
(_______)\_______/\_______)\_______)|/     \|     )_(   |/     \|(_______/(_______/   )_(   
                                                                                            """)
while True:
    while True:
        try:
            print(bcolors.PURPLE + "Du har", guesses, "gissningar kvar")
            guess=int(input(bcolors.PURPLE + "Gissa talet mellan 1 och 100\n")) #låter användare gissa och sparar gissningen i variabeln "guess"
            break
        except:
            print("Endast siffror")
    if guess == secret:
        guesses-=1 #tar bort gissningen man gjorde
        while True:
            print(bcolors.GREEN + "Du gissade rätt på", 7-guesses, "försök")
            print("Vill du spela igen?")
            again = input("Ja eller nej\n")
            if again.lower() == "ja":
                print("Vi kör igen")
                guesses = 7
                secret = rand.randint(1, 100) #skapar ett nytt tal man ska gissa
                break #börjar om spelet
            elif again.lower() == "nej":
                exit() #stänger av spelet
            else:
                continue

    if guesses == 1:
        while True:
            print(bcolors.RED + "Du hade fel, talet du skulle gissa var", secret, "\nVill du spela igen?") 
            again = input("Ja eller nej\n")
            if again.lower() == "ja":
                print("Vi kör igen")
                guesses = 7 #återställer gissningarna 
                secret = rand.randint(1, 100) #skapar ett nytt tal man ska gissa
                break #börjar om spelet
            elif again.lower() == "nej":
                exit() #stänger av spelet
            else:
                continue
    elif guess > secret:
        print(bcolors.BLUE + "Talet du ska gissa är mindre än talet du gissade")
        guesses-=1 #minskar antalet gissningar man har
    elif guess < secret:
        print(bcolors.BLUE + "Talet du ska gissa är större än talet du gissade")
        guesses-=1 #minskar antalet gissningar man har
