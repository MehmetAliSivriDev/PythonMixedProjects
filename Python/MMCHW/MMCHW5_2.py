import BasicMathModul as math

print("""

1-Sum
2-Subtract
3-Divide
4-Multiply
5-Take the Square root
6-Take the Exponential Numbers
7-Quit

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
        number = float(input("Enter a number which you want to take square root :"))

        print("Answer is :",math.sqrt(number))
    elif (choose == 6) : 
        fNumber = float(input("Enter the floor number of the exponential number :"))
        cNumber = float(input("Enter the celil number of the exponential number :"))

        print ("Answer is :",math.epn(fNumber,cNumber))
    elif (choose == 7) :
        print("System is shutting down!")
        break
