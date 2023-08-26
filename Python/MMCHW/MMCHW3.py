#Q1
from ast import While


def q1() :
    sum = 0

    number = int(input("Enter a Number : "))

    for i in range(1,number + 1) :

        if(number % i == 0 and number != i) :

            sum += i 
    if(number == sum) :
        print("It's a perfect number!")
    else :
        print("It's not a perfect number!")

#Q2
def q2() :

    number = input("Enter a Number : ")

    stepCount = len(number)
    step = 0
    sum = 0

    number = int(number)

    tempN = number

    while (tempN > 0) :

        step = tempN % 10
        sum += step ** stepCount
        tempN //= 10

    if (number == sum) :
        print("It's a Armstrong number!")
    else :
        print("It's not an Armstrong number!")
    
#Q3
def q3() :

    for i in range(1,11) :

        for j in range(1,11) :

            print(i ,"*",j," = ",i*j)
     
#Q4
def q4() :

    sum = 0

    while True :

        print("If you want to end the process please enter 'q'!")

        number = input("Please Enter the Number :") 

        if(number == "q") :

            break
        
        number = int(number)
        sum += number
        print("Current sum is : ",sum)

#Q5
def q5() :

    for i in range(1,100) :

        if (i % 3 != 0) :
            continue
        print(i)

#Q6
def q6() :

    list1 = [i for i in range(1,101) if (i % 2 == 0)]
    print(list1)

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

