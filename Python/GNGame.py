import random as r

print(""" 
Please Guess a Number Between (1,40)
""")

number = r.randint(1,40)

gRight = 7

while True :
    pGuess = int(input("Please Enter Your Guess :"))

    if (pGuess < number) :
        print("You need to think higher!")

        gRight -= 1

        print("Remaining Guess Rights :",gRight)
    elif (pGuess > number) :
        print("You need to think lower!")
        
        gRight -= 1

        print("Remaining Guess Rights :",gRight)
    else :
        print("Congratulations! The Number was :",number)
        break

    if(gRight == 0) :

        print("You've run out of guesses.")
        break
