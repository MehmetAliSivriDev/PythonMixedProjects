#Q1 
from ast import Break


def q1(number) :

    sum = 0

    for i in range(1,number + 1) :

        if(number % i == 0 and number != i) :

            sum += i

    return sum == number;        

#Q2
def q2() :

    gcd = 1

    n1 = int(input("Please Enter your First Number :"))
    n2 = int(input("Please Enter your Second Number :"))

    i = 1

    while(i <= n1 and i <= n2) :

        if(n1 % i == 0 and n2 % i == 0) :
            gcd = i
        i+=1
    
    print("GCD of the These Numbers is : " ,gcd)

#Q3
def q3() :

    lcm = 1

    n1 = int(input("Please Enter your First Number :"))
    n2 = int(input("Please Enter your Second Number :"))

    i = 2

    while True :

        if (n1 % i == 0 and n2 % i == 0) :

            lcm *= i

            n1 //= i
            n2 //= i
        elif(n1 % i == 0 and n2 % i != 0) :

            lcm *= i
            n1 //= i 
        elif(n1 % i != 0 and n2 % i == 0) :

            lcm *= i
            n2 //= i
        else :
            i+=1

            if(n1 == 1 and n2 == 1) :

                break
    print("LCM of the These Numbers is :",lcm)

#Q4 
def q4() :
    birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

    number = int(input("Lütfen 2 basamaklı bir sayı giriniz :"))

    birlerB = number % 10
    onlarB = number // 10

    print("Girmiş oldugunuz sayı ",onlar[onlarB],birler[birlerB])
    
#Q5
def q5() :

    for fEdge in range(1,101) :

        for sEdge in range(1,101) :

            hypo = (fEdge ** 2 + sEdge ** 2) ** 0.5

            if(hypo == int(hypo)) :

                print(fEdge,sEdge,hypo," Triangle")

while True :
    print("WARNING : if yoy want to exit press 6")
    choice = int(input("Enter the Question which You Want to Try (1-5) : "))

    if choice == 1 :
        for i in range(1,1001) :

            if (q1(i)) :
        
                print(i," is a perfect number!")
    elif choice  == 2 :
        q2()
    elif choice == 3 :
        q3()
    elif choice == 4 :
        q4()
    elif choice == 5 :
        q5()
    elif choice == 6 :
        break