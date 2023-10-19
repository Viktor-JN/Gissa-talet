'''
Gissa_talet.PY: Beskrivning av fil/program

__author__  = "Viktor Johansson Nygren"
__version__ = "1.0.0"
__email__   = "viktor.johanssonnygren@elev.ga.ntig.se"
'''

import random as rand

guesses = 7
y = True
secret = rand.randint(1, 100)

while y == True:
    x = True
    try:
        guess=int(input("Gissa talet mellan 1 och 100\n"))
    except:
        print("Endast siffror")
        while x == True:
            print("Du gissade rätt")
            print("Vill du spela igen?")
            again = input("Ja eller nej\n")
            if again.lower() == "ja":
                print("Vi kör igen")
                secret = rand.randint(1, 100)
                guesses = 7
                x = False
            elif again.lower() == "nej":
                y = False
            else:
                print("Ja eller nej")

    if guesses == 1:
        print("Du hade fel, talet du skulle gissa var", secret, "\nVill du spela igen?") 
        while x == True:
            again = input("Ja eller nej\n")
            if again.lower() == "ja":
                print("Vi kör igen")
                guesses = 7
                x = False
                secret = rand.randint(1, 100)
            elif again.lower() == "nej":
                y = False
            else:
                print("Ja eller nej?")
    elif guess > secret:
        print("Talet du ska gissa är mindre än talet du gissade")
        guesses-=1
        print("Du har", guesses, "gissningar kvar")
    elif guess < secret:
        print("Talet du ska gissa är större än talet du gissade")
        guesses-=1
        print("Du har", guesses, "gissningar kvar")
