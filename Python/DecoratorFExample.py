def eAvarege (func) :

    def wrapper(numbers) :

        oddNumber = 0
        evenNumber = 0

        sumOdd = 0
        sumEven = 0

        for i in numbers :

            if (i % 2 == 0) :

                evenNumber += 1
                sumEven += i            

            else :

                oddNumber += 1
                sumOdd += i
                
        print("Even Number Average is :",(sumEven / evenNumber))
        print("Odd Number Average is :",(sumOdd / oddNumber))

        func(numbers)

    return wrapper

@eAvarege    
def fGAverage(numbers) :

    sum = 0

    for i in numbers :

        sum += i 

    print("General Average is :",(sum/len(numbers)))    

fGAverage([10,20,32,42,11,23,44,55,13,25])