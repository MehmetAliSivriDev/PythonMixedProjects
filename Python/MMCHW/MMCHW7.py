#Q1

def q1() :

    list = ["345","sadas","324a","14","kemal"]

    for i in list :

        try :

            i = int(i)

            print(i)


        except ValueError :

            pass
        
#Q2

def q2() :

    nList = [12,11,89,23,32,24,19,17,66,55]

    for i in nList :

        try :

            if (i % 2 == 0) :

                print(i)
            else :

                raise ValueError("Just Even Numbers can be written.")
        
        except ValueError :

            pass

print("---")
q1()
print("---")
q2()