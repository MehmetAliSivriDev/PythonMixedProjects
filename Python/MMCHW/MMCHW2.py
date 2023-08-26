#Q1
from tkinter.tix import MAX


def Q1() :
    weight = float(input("Enter Your Weight (kg) : "))
    height = float(input("Enter Your Height (m) : "))
    print("Your Body Mass Index is : {}".format(( + weight / (height * height))))

    bmi = weight / (height * height)
    
    if (bmi >= 30) :
        print("Result : Obese")
    elif(bmi >= 25 and bmi < 30) :
        print ("Result : Overweight")
    elif(bmi >= 18.5 and bmi < 25) :
        print("Result : Normal")
    elif(bmi < 18.5) :
        print("Result : Weak")

#Q2
def Q2() :
    fNumber = int(input("Enter the First Number : "))
    sNumber = int(input("Enter the Second Number : "))
    tNumber = int(input("Enter the Third Number : "))

    print("The Heighest Number is : ",max(fNumber,sNumber,tNumber))

#Q3
def Q3() :

    mExam = float(input("Enter Your Midterm Exam Grade : "))
    fExam = float(input("Enter Your Final Exam Grade : "))

    result = (mExam * 40) / 100 + (fExam * 60) / 100

    if(result >= 90) :
        print("Your Letter Grade is : AA")
    elif(result >= 85) :
        print("Your Letter Grade is : BA")
    elif(result >= 80) :
        print("Your Letter Grade is : BB")    
    elif(result >= 75) :
        print("Your Letter Grade is : CB")
    elif(result >= 70) :
        print("Your Letter Grade is : CC")
    elif(result >= 65) :
        print("Your Letter Grade is : DC")
    elif(result >= 60) :
        print("Your Letter Grade is : DD")
    elif(result >= 55) :
        print("Your Letter Grade is : FD")
    elif(result < 55) :
        print("Your Letter Grade is : FF")    

#Q4
def Q4() :

    shape = input("Which One Do You Want to Learn the Type Of Shape? :")

    if(shape == "rectangle") :

        print("Please Enter the Edges Carrefully and in Order!")

        e1 = int(input("Enter the Value Of Edge 1 : "))
        e2 = int(input("Enter the Value Of Edge 2 : "))
        e3 = int(input("Enter the Value Of Edge 3 : "))
        e4 = int(input("Enter the Value Of Edge 4 : "))

        if(e1 == e2 == e3 == e4) :
            print("It's a Square!")
        elif(e1 == e3 and e2 == e4) :
            print("It's a Rectangle!")
        else :
            print("Its' a Quadrilateral!")
    elif(shape == "triangle") :
        
        print("Please Enter the Edges Carrefully and in Order!")

        e1 = int(input("Enter the Value Of Edge 1 : "))
        e2 = int(input("Enter the Value Of Edge 2 : "))
        e3 = int(input("Enter the Value Of Edge 3 : "))

        if(abs(e1+e2) > e3 and abs(e1+e3) > e2 and abs(e2+e3) > e1) :

            if(e1 == e2 == e3) :
                print("It's an Equilateral Triangle!")
            elif((e1 == e2) and (e1 != e3) or (e1 == e3) and (e1 != e2) or (e2 == e3) and (e2 != e1)) :
                print("It's an Isosceles Triangle!")
            else :
                print("It's a Scalene Triangle!")
        else :
            print("It's not a Triangle!")

while True :
    print("WARNING : if yoy want to exit press 5")
    choice = int(input("Enter the Question which You Want to Try (1-4) : "))

    if choice == 1 :
        Q1()
    elif choice  == 2 :
        Q2()
    elif choice == 3 :
        Q3()
    elif choice == 4 :
        Q4()
    elif choice == 5 :
        break