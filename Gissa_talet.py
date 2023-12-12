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
y = True
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
            guess=int(input(bcolors.PURPLE + "Gissa talet mellan 1 och 100\n"))
            break
        except:
            print("Endast siffror")
    if guess == secret:
        guesses-=1
        print(bcolors.GREEN + "Du gissade rätt på", 7-guesses, "försök")
        while True:
            print("Vill du spela igen?")
            again = input("Ja eller nej\n")
            if again.lower() == "ja":
                print("Vi kör igen")
                secret = rand.randint(1, 100)
                guesses = 7
                break
            elif again.lower() == "nej":
                exit()
            else:
                print("Ja eller nej")

    if guesses == 1:
        print(bcolors.RED + "Du hade fel, talet du skulle gissa var", secret, "\nVill du spela igen?") 
        while True:
            again = input("Ja eller nej\n")
            if again.lower() == "ja":
                print("Vi kör igen")
                guesses = 7
                secret = rand.randint(1, 100)
                break
            elif again.lower() == "nej":
                exit()
            else:
                print("Ja eller nej?")
    elif guess > secret:
        print(bcolors.BLUE + "Talet du ska gissa är mindre än talet du gissade")
        guesses-=1
        print(bcolors.BLUE + "Du har", guesses, "gissningar kvar")
    elif guess < secret:
        print(bcolors.BLUE + "Talet du ska gissa är större än talet du gissade")
        guesses-=1
        print(bcolors.BLUE + "Du har", guesses, "gissningar kvar")
