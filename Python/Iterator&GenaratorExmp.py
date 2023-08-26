class force3() :

    def __init__(self,max = 0) :

        self.max = max
        self.force = 0
        

    def __iter__ (self) :

        return self

    def __next__ (self) :

        if(self.force <= self.max) :

            answ = 3 ** self.force

            self.force += 1

            return answ

        else :

            self.force = 0
            raise StopIteration

def fibonacci() :

    a = 1
    b = 1

    yield a
    yield b

    while True :

        a,b = b,a+b

        yield b

force = force3(5)

iterator = iter(force)

for i in force :

    print(i)

print("-------------------------")

for i in fibonacci() :

    if (i > 100000) :

        break
    print(i)

