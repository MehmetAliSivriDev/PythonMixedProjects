def perfNumber(func) :

    def wrapper () :

        

        print("Perfect Numbers :")

        for num in range(1,1000) :

            sum = 0
            i = 1

            while (i < num) :


                if(num % i == 0 and num != i) :

                    sum += i 

                i += 1    

            if(num == sum) :
                print(num)
        
        func()

    return wrapper
        

@perfNumber
def pNumber() :

    print("Prime Numbers :")

    for num in range(2,1000) :

        i = 2 
        count = 0
        
        while (i < num) :

            if (num % i == 0) :

                count += 1

            i += 1

        if (count == 0) :

            print(num)
        
pNumber()



