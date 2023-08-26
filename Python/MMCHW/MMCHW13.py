#Q1
class sq() :

    def __init__(self,max = 0) : 

        self.max = max
        self.number = 0

    def __iter__(self) :

        return self
    
    def __next__(self) :

        if (self.number < self.max) :

            answ = self.number ** 2

            self.number += 1

            return answ

        else :

            self.number = 0
            raise StopIteration   

sq = sq(6)

iterator = iter(sq)

for i in sq :

    print(i)

#-----------------------------------------------------------------------------------------------------------------------------------

def gFunc() :

    def isPrime(number) :

        i = 2

        while (i < number) :

            if (number % i == 0) :

                return False

            i += 1

        return True

    i = 2

    while True :

        if (isPrime(i)) :

            yield i 

        i += 1
        
print("**********************************************")

for i in gFunc() :

    if (i > 1000) :

        break
    
    else :

        print(i)


