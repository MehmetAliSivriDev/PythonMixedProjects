import math 

print("""

1-Sum
2-Subtract
3-Divide
4-Multiply
5-Take the Logarithm
6-Take the Square root
7-Take the Exponential Numbers
8-Quit

""")

while True :

    choose = int(input("Enter Your Operation : "))

    if (choose == 1) :

        fNumber = float(input("Enter Your First Number :"))
        sNumber = float(input("Enter Your Second Number :"))

        print("Answer is :",(fNumber + sNumber))
    elif (choose == 2) :
        fNumber = float(input("Enter Your First Number :"))
        sNumber = float(input("Enter Your Second Number :"))

        print("Answer is :",(fNumber - sNumber))
    elif (choose == 3) :
        fNumber = float(input("Enter Your First Number :"))
        sNumber = float(input("Enter Your Second Number :"))

        print("Answer is :",(fNumber / sNumber))
    elif (choose == 4) :
        fNumber = float(input("Enter Your First Number :"))
        sNumber = float(input("Enter Your Second Number :"))

        print("Answer is :",(fNumber * sNumber))
    elif (choose == 5) : 
        number = float(input("Enter a number which you want to take log10 :"))

        print("Answer is :",math.log10(number))
    elif (choose == 6) :
        number = float(input("Enter a number which you want to take square root :"))

        print("Answer is :",math.sqrt(number))
    elif (choose == 7) : 
        fNumber = float(input("Enter the floor number of the exponential number :"))
        cNumber = float(input("Enter the celil number of the exponential number :"))

        print ("Answer is :",math.pow(fNumber,cNumber))
    elif (choose == 8) :
        print("System is shutting down!")
        break
