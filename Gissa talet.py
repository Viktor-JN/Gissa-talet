import random as rand

tal = rand.randint(1, 100)
gissningar = 5

while gissningar > 0:
    try:
        gissning=int(input("Gissaa talet mellan 1 och 100\n"))
    except:
        print("Endast siffror")
    if gissning > tal:
        print("Talet du ska gissa är mindre än talet du gissade")
        gissningar-=1
        print("Du har", gissningar, "gissningar kvar")
    elif gissning < tal:
        print("Talet du ska gissa är större än talet du gissade")
        gissningar-=1
        print("Du har", gissningar, "gissningar kvar")
    else:
        print("Du gissade rätt")
print("""Du suger dase, du fick inte rätt
Det var""", tal)