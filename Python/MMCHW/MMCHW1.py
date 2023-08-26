#Q1
def q1() :
    fNumber = int(input("Enter the First Number : "))
    sNumber = int(input("Enter the Second Number : "))
    tNumber = int(input("Enter the Third Number : "))
    print("Result : {}".format((fNumber * sNumber * tNumber)))

#Q2
def q2() :
    weight = float(input("Enter Your Weight (kg) : "))
    height = float(input("Enter Your Height (m) : "))
    print("Your Body Mass Index is : {}".format(( + weight / (height * height))))

#Q3
def q3() :
    gasoline = float(input("How many liters of gasoline does your car burn per kilometer? : "))
    km = float(input("How many kilometers did you travel? : "))
    print("You Need to Pay : {}".format((gasoline * km)) + " Dolar") 

#Q4
def q4() :
    fName = input("Enter Your First Name : ")
    lName = input("Enter Yout Last Name : ")
    pNumber = int(input("Enter Your Phone Number : "))
    print("Informantions :\n{}\n{}\n{}".format(fName,lName,pNumber))

#Q5
def q5() :
    fNumber = int(input("First Number : "))
    sNumber = int(input("Second Numer : "))
    print("Before :\nFirst Number : {}\nSecond Number : {}\n".format(fNumber,sNumber))

    #temp = fNumber
    #fNumber = sNumber
    #sNumber = temp

    fNumber,sNumber = sNumber,fNumber
 
    print("After :\nFirst Number : {}\nSecond Number : {}\n".format(fNumber,sNumber))

#Q6
def q6() :
    fEdge = float(input("Enter the Value of First Edge : "))
    sEdge = float(input("Enter the Value of Second Edge : "))

    print("Hypotenuse is : {}".format((fEdge ** 2 + sEdge ** 2) ** 0.5))

while True :
    print("WARNING : if yoy want to exit press 7")
    choice = int(input("Enter the Question which You Want to Try (1-6) : "))

    if choice == 1 :
        q1()
    elif choice  == 2 :
        q2()
    elif choice == 3 :
        q3()
    elif choice == 4 :
        q4()
    elif choice == 5 :
        q5()
    elif choice == 6 :
        q6()
    elif choice == 7 :
        break
