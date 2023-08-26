
def calculate(number1,number2,operator) :

    if (operator == "+") :
        print("The Answer is :",(number1 + number2))
    elif(operator == "-") :
        print("The Answer is :",(number1 - number2))  
    elif(operator == "*") :
        print("The Answer is :",(number1 * number2))
    elif(operator == "/") :
        print("The Answer is :",(number1 / number2))

print("Do Just Simple Math! (+,-,*,/)")
print("Enter Your Process : ")
number1 = int(input())
operator = input()
number2 = int(input())

if(operator == "+") :
    calculate(number1,number2,"+")
elif(operator == "-") :
    calculate(number1,number2,"-")
elif(operator == "*") :
    calculate(number1,number2,"*")
elif(operator == "/") :
    calculate(number1,number2,"/")

    

