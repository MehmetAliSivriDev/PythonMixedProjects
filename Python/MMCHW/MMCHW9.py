from functools import reduce


def aCalculation(tuple) :

    return tuple[0] * tuple[1]

def isTriangle(tuple) :

    if(abs(tuple[0]+tuple[1]) > tuple[2] and abs(tuple[0]+tuple[2]) > tuple[1] and abs(tuple[1]+tuple[2]) > tuple[0]) :

        return True
    
    return False

#Q1
def q1() :

    nList = [(3,4),(10,3),(5,6),(1,9)]

    print(list(map(aCalculation,nList)))
    
#Q2
def q2() :

    nList =  [(3,4,5),(6,8,10),(3,10,7)]

    print(list(filter(isTriangle,nList)))

#Q3 
def q3() :

    nList = [1,2,3,4,5,6,7,8,9,10]

    fEvNumber = (list(filter(lambda x : x % 2 == 0,nList)))
    print(reduce(lambda x,y : x + y,fEvNumber))

#Q4
def q4() :

    fName = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
    lName = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

    for i,j in zip(fName,lName) :

        print(i,j)